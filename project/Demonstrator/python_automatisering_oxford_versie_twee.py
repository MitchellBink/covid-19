# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 17:45:52 2020

@author: Mitchell
"""

import requests as rq
import datetime
import json
from datetime import timedelta, date
import xlsxwriter
import time


#default data
start_date = datetime.date.today()
end_date = datetime.date.today()
row = 0
col = 0
#commented countries have no information provides, thus have been left out of the request. Country code bases on ISO 3166
country_dictionary = {
    "Albania":"ALB", 
    "Andorra":"AND", 
    "Austria":"AUT", 
    "Belarus":"BLR",
    "Belgium":"BEL",
    "Bosnia and Herzegovina":"BIH",
    "Bulgaria":"BGR",
    "Croatia":"HRV",
  #  "Vatican city":"VAT",
    "United Kingdom":"GBR",
    "Ukraine":"UKR",
    "Switzerland":"CHE",
    "Sweden":"SWE",
    "Spain":"ESP",
    "Slovenia":"SVN",
    "Slovakia":"SVK",
    "Serbia":"SRB",
  #  "San Marino":"RSM",
    "Russia":"RUS",
    "Romania":"ROU",
    "Portugal":"PRT",
    "Poland":"POL",
    "Norway":"NOR",
    "Netherlands":"NLD",
  #  "Montenegro":"MNE",
  #  "Monaco":"MCO",
    "Moldova":"MDA",
  #  "Malta":"MLT",
    "Luxembourg":"LUX",
    "Lithuania":"LTU",
  # "Liechtenstein":"LIE",
    "Latvia":"LVA",
 #   "Kosovo":"UNK",
    "Italy":"ITA",
    "Ireland":"IRL",
    "Iceland":"ISL",
    "Hungary":"HUN",
    "Greece":"GRC",
    "Germany":"DEU",
    "France":"FRA",
    "Finland":"FIN",
    "Estonia":"EST",
    "Denmark":"DNK",
    "Czechia":"CZE"
    }



def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


#make variable in frontend

start_date = date(2020, 1, 21)
end_date = date(2020, 12, 6)
'''
#controle data
response_country = rq.get("https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/actions/NLD/2021-1-12")
json_str = json.dumps(response_country.json())
resp = json.loads(json_str)
print(resp)
'''
# get data and write to xlsx
workbook = xlsxwriter.Workbook('data_countries_all_with_relatives.xlsx')
fnames = ['Date', 'New Cases', 'Change of Cases', 'Cumulative cases','New Deaths', 'Change of Deaths', 'Cumulative deaths','Stringency','C1' ,'C2' ,'C3' ,'C4' ,'C5' ,'C6' ,'C7' ,'C8' ,'E1','E2' ,'E3' ,'E4' ,'H1' ,'H2' ,'H3','H4' ,'H5' ,'H6', 'H7']

for key in country_dictionary:
    #makes sheet per country
    worksheet = workbook.add_worksheet(country_dictionary[key])
    #prints header row
    for col_no, item in enumerate(fnames):
        worksheet.write(0, col_no, item)
        
    row_num = 1
    prev_cases = 0
    prev_deaths = 0
    change_cases = 0
    change_deaths = 0
    last_day_cases= 0
    last_day_deaths =0 
    #gets data
    for single_date in daterange(start_date, end_date):
        col_num=0
        r = ""
        try:
            r = rq.get("https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/actions/"+ country_dictionary[key] +"/" + single_date.strftime("%Y-%m-%d"), timeout=5)
        except rq.exceptions.ConnectionError as e:
            continue

        response_country = r
        json_str = json.dumps(response_country.json())
        resp = json.loads(json_str)
        try:
            daily_cases = int(resp["stringencyData"]["confirmed"])-prev_cases
            daily_deaths = int(resp["stringencyData"]["deaths"])-prev_deaths
            my_data = [str(resp["stringencyData"]["date_value"]), 
                       (daily_cases), 
                       (daily_cases-last_day_cases),
                       int(resp["stringencyData"]["confirmed"]), 
                       (daily_deaths), 
                       (daily_deaths-last_day_deaths), 
                       int(resp["stringencyData"]["deaths"]), 
                       resp['stringencyData']['stringency']]
            last_day_cases = daily_cases
            last_day_deaths = daily_deaths
            prev_cases = int(resp["stringencyData"]["confirmed"])
            prev_deaths = int(resp["stringencyData"]["deaths"])
            for x in range(len(resp["policyActions"])):
                my_data += [str(resp["policyActions"][x]["flagged"])]
            for data in my_data:            
                worksheet.write(row_num, col_num, data)
                col_num +=1
            row_num +=1
        except:
            print(key + " rip" + single_date.strftime("%Y-%m-%d"))
            
        time.sleep(0.5)


     
workbook.close()




"""
prob not needed if there is a list with all countries
response_total = rq.get("https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/2020-06-02/2020-06-03")
"""


    
"""
###general information about the json data retrieved from the get requests

{
  policyActions: {
    0...n: {  //Numerical key
      policy_type_code: String, //Policy type 2 or 3 digit code - letter/number - or NONE if no data available
      policy_type_display: String, //String describing policy value,
      policyvalue: Integer, //Represents policy status
      is_general: Boolean, //If this is a general policy,
      flagged: Boolean, //Replaces isgneral from 28 April 2020,
      policy_value_display_field: String, //Describes the level of stringency of the policy or type of policy
      notes: String, //Notes entered by contributors
    }
  },
  stringencyData: {
    date_value: String, //YYYY-MM-DD date of record
    country_code: String, //ALPHA-3 country code
    confirmed: Integer, //Recorded confirmed cases,
    deaths: Integer, //Recorded deaths,
    stringency_actual: Integer, //Calculated stringency
    stringency: Integer, //Display stringency - Will be actual value if available. For previous 7 days will take last available value. Otherwise null.
  }
}


"""