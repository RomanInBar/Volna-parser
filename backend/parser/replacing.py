from database.manager import DBManager, objT
from database.models import Replacement


class Replace:
    """
    Replace the value of word from URL on users value.
    """

    db = DBManager(Replacement)

    def _prepare_data_from_database(self) -> dict:
        """Check if word in database and return object if found."""
        data = {obj.current_value: obj.replace for obj in self.db.get_all()}
        return data

    def replacing(self, data: list[list[str]]):
        db_data = self._prepare_data_from_database()
        for index in range(len(data)):
            string = data[index][0].split()
            data[index][0] = " ".join([db_data.get(word) or word for word in string])
        return data
