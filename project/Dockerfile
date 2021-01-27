FROM python:3.7-stretch
WORKDIR /Covid19
ENV FLASK_APP=Demonstrator/app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
