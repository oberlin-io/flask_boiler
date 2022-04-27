FROM python:3

WORKDIR /home/john/flask_boiler

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY /app .

ENTRYPOINT ["python"]
CMD ["app.py"]
