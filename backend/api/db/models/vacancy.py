from typing import List
from sqlalchemy import JSON, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import Base


class Vacancy(Base):
    id: Mapped[int] = mapped_column(primary_key=True)

    # Назва вакансії
    title: Mapped[str] = mapped_column(nullable=False)  # Українська
    title_ru: Mapped[str] = mapped_column(nullable=False)  # Російська

    # Основне зображення
    main_image_path: Mapped[str] = mapped_column(nullable=False)

    # Додаткові зображення
    images_path: Mapped[List[str]] = mapped_column(JSON, nullable=False, default=list)

    # Відео
    video_path: Mapped[str] = mapped_column(nullable=False)

    # Зарплата
    salary: Mapped[str] = mapped_column(nullable=False)  # Українська
    salary_ru: Mapped[str] = mapped_column(nullable=False)  # Російська

    # Графік
    schedule: Mapped[str] = mapped_column(nullable=False)  # Українська
    schedule_ru: Mapped[str] = mapped_column(nullable=False)  # Російська

    # Проживання
    accommodation: Mapped[str] = mapped_column(nullable=False)  # Українська
    accommodation_ru: Mapped[str] = mapped_column(nullable=False)  # Російська

    # Місце роботи
    work_location: Mapped[str] = mapped_column(nullable=False)  # Українська
    work_location_ru: Mapped[str] = mapped_column(nullable=False)  # Російська

    # Детальний опис
    description: Mapped[str] = mapped_column(Text, nullable=False)  # Українська
    description_ru: Mapped[str] = mapped_column(Text, nullable=False)  # Російська

    # Відношення до заявок
    requests: Mapped[List["VacancyRequest"]] = relationship(back_populates="vacancy", cascade="all, delete")

    def __repr__(self):
        return (
            f"Vacancy(id={self.id}, "
            f"title={self.title!r}, title_ru={self.title_ru!r}, "
            f"main_image_path={self.main_image_path!r}, "
            f"images_path={len(self.images_path)} item(s), "
            f"video_path={self.video_path!r}, "
            f"salary={self.salary!r}, salary_ru={self.salary_ru!r}, "
            f"schedule={self.schedule!r}, schedule_ru={self.schedule_ru!r}, "
            f"accommodation={self.accommodation!r}, accommodation_ru={self.accommodation_ru!r}, "
            f"work_location={self.work_location!r}, work_location_ru={self.work_location_ru!r}, "
            f"description={self.description[:30]!r}, description_ru={self.description_ru[:30]!r})"
        )
