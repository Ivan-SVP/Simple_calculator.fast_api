from pydantic import BaseModel, conint

calc_field = conint(strict=True, ge=0)  # неотрицательные целые числа со строгой "типизацией"


class CalcInput(BaseModel):
    """Модель данных, которые принимает калькулятор."""
    number1: calc_field
    number2: calc_field

    class Config:
        schema_extra = {
            'example': {
                'number1': 3,
                'number2': 2,
            },
        }


class CalcOutput(BaseModel):
    """Результат вычисления."""
    result: calc_field
