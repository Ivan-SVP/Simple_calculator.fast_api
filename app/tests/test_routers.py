import pytest

from app.tests import parametrization_data


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "number1, number2, expected_result, expected_code",
    parametrization_data.test_calc
)
async def test_calc(client, number1, number2, expected_result, expected_code):
    data = {'number1':  number1, 'number2':  number2}

    response = await client.post('calc/', json=data)
    result = response.json().get('result')

    assert response.status_code == expected_code
    assert result == expected_result
