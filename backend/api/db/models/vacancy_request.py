from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import Base


class VacancyRequest(Base):
    id: Mapped[int] = mapped_column(primary_key=True)

    vacancy_id: Mapped[int] = mapped_column(ForeignKey("vacancys.id"))
    vacancy: Mapped["Vacancy"] = relationship(back_populates="requests")

    name: Mapped[str] = mapped_column(nullable=False)
    phone_number: Mapped[str] = mapped_column(nullable=False)

    archieved: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return (
            f"VacancyRequest(id={self.id}, "
            f"vacancy_id={self.vacancy_id!r}, "
            f"name={self.name!r}, "
            f"phone_number={self.phone_number!r})"
        )