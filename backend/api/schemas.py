from typing import List
from pydantic import BaseModel, Field

from typing import List
from pydantic import BaseModel


class VacancyData(BaseModel):
    title: str
    title_ru: str
    main_image_path: str
    images_path: List[str]
    video_path: str
    salary: str
    salary_ru: str
    schedule: str
    schedule_ru: str
    accommodation: str
    accommodation_ru: str
    work_location: str
    work_location_ru: str
    description: str
    description_ru: str

    class Config:
        from_attributes = True



class VacandyRequestData(BaseModel):
    vacancy_id: int
    name: str
    phone_number: str

    class Config:
        from_attributes = True


class AdminCredentials(BaseModel):
    username: str
    password: str