FROM python:3.8

WORKDIR /flsite
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["flsite.py"]
