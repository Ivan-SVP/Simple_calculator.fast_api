FROM python:3.6 as base

RUN mkdir -p /application
WORKDIR /application
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv && pipenv install --ignore-pipfile --system --deploy --dev
COPY . .

EXPOSE 8001
CMD ["uvicorn", "app.main:app.server", "--host", "0.0.0.0", "--port", "8001", "--reload"]
