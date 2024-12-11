from fastapi import APIRouter, HTTPException
from ..db import Session
from ..db.models import VacancyRequest
from ..schemas.vacancy import VacandyRequestData

router = APIRouter(prefix="/vacancy-request", tags=["vacancy-request"])


@router.get("/list")
def list_vacancy():
    with Session() as session:
        return session.query(VacancyRequest).all()


@router.get("/get")
def get_vacancy_request(request_id: int):
    with Session() as session:
        vacancy_request = session.query(VacancyRequest).filter(VacancyRequest.id == request_id).first()

        if not vacancy_request:
            raise HTTPException(status_code=404, detail="Vacancy request is not found")

        return vacancy_request


@router.patch("/flip-status")
def flip_vacancy_request_status(request_id: int):
    with Session() as session:
        vacancy_request = session.query(VacancyRequest).filter(VacancyRequest.id == request_id).first()

        if not vacancy_request:
            raise HTTPException(status_code=404, detail="Vacancy request is not found")

        vacancy_request.checked = not vacancy_request.checked

        session.add(vacancy_request)
        session.commit()
        session.refresh(vacancy_request)

        return {"message": "Success!"}


@router.delete("/delete")
def delete_vacancy_request(request_id: int):
    with Session() as session:
        vacancy_request = session.query(VacancyRequest).filter(VacancyRequest.id == request_id).first()

        if not vacancy_request:
            raise HTTPException(status_code=404, detail="Vacancy request is not found")

        session.delete(vacancy_request)
        session.commit()

        return {"message": f"{vacancy_request} was deleted successfully"}


@router.post("/create")
def create_vacancy_request(vacancy_request_data: VacandyRequestData):
    with Session() as session:
        vacancy_request = VacancyRequest(
            vacancy_id=vacancy_request_data.vacancy_id,
            name=vacancy_request_data.name,
            phone_number=vacancy_request_data.phone_number
        )

        session.add(vacancy_request)
        session.commit()
        session.refresh(vacancy_request)

        return vacancy_request
