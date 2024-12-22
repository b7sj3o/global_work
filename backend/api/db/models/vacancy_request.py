from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone

from .. import Base


class VacancyRequest(Base):
    id: Mapped[int] = mapped_column(primary_key=True)

    vacancy_id: Mapped[int] = mapped_column(ForeignKey("vacancys.id"))
    vacancy: Mapped["Vacancy"] = relationship(back_populates="requests")

    name: Mapped[str] = mapped_column(nullable=False)
    phone_number: Mapped[str] = mapped_column(nullable=False)

    archieved: Mapped[bool] = mapped_column(default=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return (
            f"VacancyRequest(id={self.id}, "
            f"vacancy_id={self.vacancy_id!r}, "
            f"name={self.name!r}, "
            f"phone_number={self.phone_number!r})"
        )