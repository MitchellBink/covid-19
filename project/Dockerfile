FROM python:3.7-stretch
WORKDIR /Covid19
ENV FLASK_APP=Demonstrator/app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
COPY data_countries_all_with_relatives_xls.xls data_countries_all_with_relatives_xls.xls
COPY regular_data_countries_xls.xls regular_data_countries_xls.xls
RUN pip install -r requirements.txt
RUN pip install xlrd
COPY . .
CMD ["flask", "run"]
