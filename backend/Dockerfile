FROM python:3.8.1-slim-buster
WORKDIR /usr/src/app/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/backend/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/backend
CMD ["uvicorn", "--host", "0.0.0.0", "main:app", "--reload"]