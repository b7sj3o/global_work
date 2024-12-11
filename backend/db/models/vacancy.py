from typing import List
from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import Base


class Vacancy(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    main_image_path: Mapped[str] = mapped_column(nullable=False)
    images_path: Mapped[List[str]] = mapped_column(JSON, nullable=False, default=list)
    video_path: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)

    requests: Mapped[List["VacancyRequest"]] = relationship(back_populates="vacancy")

    def __repr__(self):
        return (
            f"Vacancy(id={self.id}, "
            f"title={self.title!r}, "
            f"main_image_path={self.main_image_path!r}, "
            f"images_path={len(self.images_path)} item(s), "
            f"video_path={self.video_path!r}, "
            f"description={self.description[:30]!r})"
        )