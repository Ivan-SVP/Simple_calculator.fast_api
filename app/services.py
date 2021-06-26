import logging

from fastapi import HTTPException

from app.schemas import CalcInput, CalcOutput

logger = logging.getLogger(__name__)


async def calculate(data: CalcInput) -> CalcOutput:
    try:
        sum_ = data.number1 + data.number2
    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=400, detail='Calculating error')
    return CalcOutput(result=sum_)
