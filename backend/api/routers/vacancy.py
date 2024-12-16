from fastapi import APIRouter, HTTPException, status
from ..db import Session
from ..db.models import Vacancy
from ..schemas.vacancy import VacandyData

router = APIRouter(prefix="/vacancy", tags=["vacancy"])


@router.get("/list")
def list_vacancy():
    with Session() as session:
        return session.query(Vacancy).all()


@router.get("/{vacancy_id}")
def get_vacancy(vacancy_id: int):
    with Session() as session:
        vacancy = session.query(Vacancy).filter_by(id=vacancy_id).first()

        if not vacancy:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vacancy is not found")

        return vacancy

@router.post("/create")
def create_vacancy(vacancy_data: VacandyData):
    with Session() as session:
        vacancy = Vacancy(
            title=vacancy_data.title,
            short_description=vacancy_data.short_description,
            description=vacancy_data.description,
            main_image_path=vacancy_data.main_image_path,
            images_path=vacancy_data.images_path,
            video_path=vacancy_data.video_path,
        )

        session.add(vacancy)
        session.commit()
        session.refresh(vacancy)

        return vacancy


@router.put("/update/{vacancy_id}")
def update_vacancy(vacancy_id: int, vacancy_data: VacandyData):
    with Session() as session:
        vacancy = session.query(Vacancy).filter_by(id=vacancy_id).first()

        if not vacancy:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vacancy is not found")

        data_to_update = vacancy_data.model_dump(exclude_unset=True)
        for k, v in data_to_update.items():
            setattr(vacancy, k, v)

        session.add(vacancy)
        session.commit()
        session.refresh(vacancy)

        return vacancy


@router.delete("/delete/{vacancy_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vacancy(vacancy_id: int):
    print(vacancy_id)
    with Session() as session:
        vacancy = session.query(Vacancy).filter_by(id=vacancy_id).first()
        if not vacancy:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vacancy is not found")
    
        session.delete(vacancy)
        session.commit()

        return {"message": f"Vacancy was deleted successfully"}
