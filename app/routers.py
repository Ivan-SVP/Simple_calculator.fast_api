from fastapi import APIRouter

from app.services import calculate
from app.schemas import CalcInput, CalcOutput

router = APIRouter(prefix='')


@router.post("/calc", response_model=CalcOutput, description="Add two positive numbers", tags=['Calculator'])
async def calc(input_: CalcInput):
    return await calculate(input_)
