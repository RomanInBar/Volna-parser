from sqlalchemy.orm import Mapped, mapped_column

from database.engine import Base


class Replacement(Base):
    __tablename__ = "replacements"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    current_value: Mapped[str] = mapped_column(unique=True, nullable=False)
    replace: Mapped[str] = mapped_column(nullable=False)


class URLs(Base):
    __tablename__ = "urls"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(unique=True, nullable=False)
