FROM python:3.13.7-alpine

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]