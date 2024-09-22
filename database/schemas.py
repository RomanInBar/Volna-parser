class BaseModel:

    @classmethod
    def values(cls, obj):
        try:
            return [
                obj.__dict__[annotation] for annotation in cls.__annotations__.keys()
            ]
        except KeyError as error:
            raise ValueError(f"Ошибка валидации: {error}")


class ReplaceSchema(BaseModel):
    current_value: str
    replace: str
