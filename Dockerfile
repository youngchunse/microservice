FROM python:3.6-alpine

COPY . /backend

WORKDIR /backend

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["main.py"]
