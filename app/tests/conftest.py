from typing import AsyncIterator

import pytest
from httpx import AsyncClient

from app.main import app


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    async with AsyncClient(
        app=app.server,
        base_url="http://test",
        headers={"Content-Type": "application/json"}
    ) as client:
        yield client
