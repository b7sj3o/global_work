from typing import List
from pydantic import BaseModel, Field

class VacandyData(BaseModel):
    title: str
    main_image_path: str
    images_path: List[str]
    video_path: str
    description: str

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "title": "Python Developer",
    #             "main_image_path": "/uploads/images/main.jpg",
    #             "images_path": ["/uploads/images/img1.jpg", "/uploads/images/img2.jpg"],
    #             "video_path": "/uploads/videos/intro.mp4",
    #             "description": "We are looking for an experienced Python developer to join our team.",
    #         }
    #     }


class VacandyRequestData(BaseModel):
    vacancy_id: int
    name: str
    phone_number: str = Field(pattern=r"^\+?[1-9]\d{1,14}$") # check for valid phone number
