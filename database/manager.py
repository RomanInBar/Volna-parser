import logging
from typing import TypeVar

from sqlalchemy import delete, insert, select
from sqlalchemy.exc import NoResultFound

from database.engine import session

objT = TypeVar("objT")


class DBManager:
    def __init__(self, model) -> None:
        self.model = model

    def get_all(self) -> list:
        query = select(self.model)
        with session() as s:
            result = s.execute(query)
            logging.info(
                f"Выгрузка данных из модели {self.model.__tablename__} завершена"
            )
            return result.scalars().all()

    def get(self, **kwargs) -> objT:
        query = select(self.model).filter_by(**kwargs)
        with session() as s:
            try:
                result = s.execute(query)
            except NoResultFound:
                return
        return result.scalar()

    def create(self, **kwargs) -> None:
        query = insert(self.model).values(**kwargs)
        with session() as s:
            s.execute(query)
            s.commit()
        logging.info(f'Данные "{kwargs}" добавлены в базу данных')

    def remove(self, **kwargs) -> None:
        query = delete(self.model).filter_by(**kwargs)
        with session() as s:
            s.execute(query)
            s.commit()
        logging.info(f'Данные "{kwargs}" удалены из базы данных')
