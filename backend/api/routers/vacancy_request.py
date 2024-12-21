from fastapi import APIRouter, HTTPException, status
from ..db import Session
from ..db.models import VacancyRequest
from ..schemas import VacandyRequestData

router = APIRouter(prefix="/vacancy-request", tags=["vacancy-request"])


@router.get("/list")
def list_vacancy(show_archieved: bool = False):
    with Session() as session:
        if show_archieved:
            return session.query(VacancyRequest).all()
        else:
            return session.query(VacancyRequest).filter_by(archieved=False).all()


@router.get("/get/{request_id}")
def get_vacancy_request(request_id: int):
    with Session() as session:
        vacancy_request = session.query(VacancyRequest).filter_by(id=request_id).first()

        if not vacancy_request:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vacancy request is not found")

        return vacancy_request


@router.patch("/archieve/{request_id}")
def archieve_vacancy_request(request_id: int):
    with Session() as session:
        vacancy_request = session.query(VacancyRequest).filter_by(id=request_id).first()

        if not vacancy_request:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vacancy request is not found")

        vacancy_request.archieved = not vacancy_request.archieved

        session.add(vacancy_request)
        session.commit()
        session.refresh(vacancy_request)

        return {"message": "Success!"}


@router.delete("/delete/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vacancy_request(request_id: int):
    with Session() as session:
        vacancy_request = session.query(VacancyRequest).filter_by(id=request_id).first()

        if not vacancy_request:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vacancy request is not found")

        session.delete(vacancy_request)
        session.commit()

        return {"message": f"{vacancy_request} was deleted successfully"}


@router.post("/create")
def create_vacancy_request(vacancy_request_data: VacandyRequestData):
    with Session() as session:
        vacancy_request = session.query(VacancyRequest).filter_by(
            vacancy_id=vacancy_request_data.vacancy_id,
            name=vacancy_request_data.name,
            phone_number=vacancy_request_data.phone_number,
        ).first()

        if vacancy_request:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Ви вже залишили заявку до цієї вакансії!")

        vacancy_request = VacancyRequest(
            vacancy_id=vacancy_request_data.vacancy_id,
            name=vacancy_request_data.name,
            phone_number=vacancy_request_data.phone_number,
        )

        session.add(vacancy_request)
        session.commit()
        session.refresh(vacancy_request)

        return vacancy_request
