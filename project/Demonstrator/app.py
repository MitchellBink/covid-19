# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 17:10:15 2020

@author: Mitchell Bink, Max Kleinman en Sandro Offermans"""

from flask import Flask, render_template, request, Markup
import pandas as pd
import numpy as np
from scipy.integrate import odeint
from scipy import interpolate
import markdown2
import dateutil
import datetime
from os import environ



app = Flask(__name__)

def getValuesCountry(countryName):
    print(countryName)
    numberOfRow = 283
    data = pd.read_excel('data_countries_all_with_relatives_xls.xls', sheet_name = None)
    RegularData = pd.read_excel('regular_data_countries_xls.xls')
    listCumuCases = list(data[countryName]["Cumulative cases"].iloc[0:numberOfRow])
    listCumuDeaths = list(data[countryName]["Cumulative deaths"].iloc[0:numberOfRow])
    populationNumber = int(RegularData.loc[RegularData["ISO-3166"] == countryName]["Total population"])
    # densityNumber = int(RegularData.loc[RegularData["ISO-3166"] == countryName]["population density"])
    CasesPerTenThousand = list([round(number / (populationNumber / 10000),2) for number in listCumuCases])
    DeathsPerTenThousand = list([round(number / (populationNumber / 10000),2) for number in listCumuDeaths])

    listNewCases = list(data[countryName]["New Cases"].iloc[0:numberOfRow])
    listChangeCases = list(data[countryName]["Change of Cases"].iloc[0:numberOfRow])
    listNewDeaths = list(data[countryName]["New Deaths"].iloc[0:numberOfRow])
    listChangeDeaths = list(data[countryName]["Change of Deaths"].iloc[0:numberOfRow])
    listStringency = list(data[countryName]["Stringency"].iloc[0:numberOfRow])
    
    deathratio = []
    for i in range(len(listCumuCases)):
        if listCumuCases[i] != 0:
            dratio = (listCumuDeaths[i] /listCumuCases[i] * 100 )
            dratio = round(dratio, 2)
        else:
            dratio = 0
        deathratio.append(dratio)
    return ([list(listCumuCases), 
             list(listCumuDeaths), 
             list(CasesPerTenThousand), 
             list(DeathsPerTenThousand), 
             list(deathratio), 
             list(listNewCases), 
             list(listChangeCases),
             list(listNewDeaths),
             list(listChangeDeaths),
             list(listStringency)])

numbersNL = getValuesCountry('NLD')
numbersBE = getValuesCountry('BEL')
numbersALB = getValuesCountry('ALB')
numbersAND = getValuesCountry('AND')
numbersBLR = getValuesCountry('BLR')
numbersAUT = getValuesCountry('AUT')
numbersBIH  = getValuesCountry('BIH')
numbersBGR  = getValuesCountry('BGR')
numbersHRV  = getValuesCountry('HRV')
numbersGBR  = getValuesCountry('GBR')
numbersUKR  = getValuesCountry('UKR')
numbersCHE  = getValuesCountry('CHE')
numbersSWE  = getValuesCountry('SWE')
numbersESP  = getValuesCountry('ESP')
numbersSVN  = getValuesCountry('SVN')
numbersSVK  = getValuesCountry('SVK')
numbersSRB  = getValuesCountry('SRB')
numbersRUS  = getValuesCountry('RUS')
numbersROU  = getValuesCountry('ROU')
numbersPRT  = getValuesCountry('PRT')
numbersPOL  = getValuesCountry('POL')
numbersNOR  = getValuesCountry('NOR')
numbersMDA  = getValuesCountry('MDA')
numbersLUX  = getValuesCountry('LUX')
numbersLTU  = getValuesCountry('LTU')
numbersLVA  = getValuesCountry('LVA')
numbersITA  = getValuesCountry('ITA')
numbersIRL  = getValuesCountry('IRL')
numbersISL  = getValuesCountry('ISL')
numbersHUN  = getValuesCountry('HUN')
numbersGRC  = getValuesCountry('GRC')
numbersDEU  = getValuesCountry('DEU')
numbersFRA  = getValuesCountry('FRA')
numbersFIN  = getValuesCountry('FIN')
numbersEST  = getValuesCountry('EST')
numbersDNK  = getValuesCountry('DNK')
numbersCZE  = getValuesCountry('CZE')

@app.route('/', methods = ['GET'])
def index():
     return render_template(
         'index.html',
         meta_title = 'Dashboard covid-19 - Zuyd Hogeschool',
         meta_description = 'Compare the numbers of the countries',
         rel_canonical = '/',
         icon = 'https://dataintelligence.zuyd.nl/wp-content/uploads/2020/09/cropped-Penrose-driehoek-192x192.png',
         numbersNL = numbersNL,
         numbersBE = numbersBE,
         numbersALB = numbersALB,
         numbersAND = numbersAND,
         numbersBLR = numbersBLR,
         numbersAUT = numbersAUT,
         numbersBIH = numbersBIH,
         numbersBGR = numbersBGR,
         numbersHRV = numbersHRV,
         numbersGBR = numbersGBR,
         numbersUKR = numbersUKR,
         numbersCHE = numbersCHE,
         numbersSWE = numbersSWE,
         numbersESP = numbersESP,
         numbersSVN = numbersSVN,
         numbersSVK = numbersSVK,
         numbersSRB = numbersSRB,
         numbersRUS = numbersRUS,
         numbersROU = numbersROU, 
         numbersPRT = numbersPRT,
         numbersPOL = numbersPOL,
         numbersNOR = numbersNOR,
         numbersMDA = numbersMDA,
         numbersLUX = numbersLUX,
         numbersLTU = numbersLTU,
         numbersLVA = numbersLVA,
         numbersITA = numbersITA,
         numbersIRL = numbersIRL,
         numbersISL = numbersISL,
         numbersHUN = numbersHUN,
         numbersGRC = numbersGRC,
         numbersDEU = numbersDEU,
         numbersFRA = numbersFRA,
         numbersFIN = numbersFIN,
         numbersEST = numbersEST,
         numbersDNK = numbersDNK,
         numbersCZE = numbersCZE)
    


@app.route('/info', methods = ['GET'])
def info():
    return render_template('info.html',
           meta_title = 'Info - Zuyd Hogeschool',
           meta_description = 'Algemene informatie over het Lectoraat Data Intelligence',
           rel_canonical = '/info')

@app.route('/project/doelstelling-project', methods = ['GET'])
def aanleiding():
    return render_template('doelstelling-project.html',
           meta_title = 'Doelstelling - Zuyd Hogeschool',
           meta_description = 'Doelstelling van het project',
           rel_canonical = '/project/doelstelling-project')

@app.route('/onderzoek/ontwikkeling-in-nederland', methods = ['GET'])
def Ontwikkeling_in_Nederland():
    marked_text = ''
    with open("README.md", encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read(),extras=['fenced-code-blocks'])
    return render_template('Ontwikkeling-in-Nederland.html', 
                           meta_title = "Ontwikkeling in Nederland", 
                           meta_description = "Hoe heeft covid-19 zich ontwikkeld in Nederland ten opzichte van andere Europese landen?",
                           rel_canonical = "/onderzoek/ontwikkeling-in-nederland", md=Markup(marked_text))

@app.route('/project/lectoraat-data-intelligence', methods = ['GET'])
def lectoraat():
    return render_template('Lectoraat.html',
           meta_title = 'Lectoraat Data Intelligence - Zuyd Hogeschool',
           meta_description = 'Algemene informatie over het Lectoraat Data Intelligence',
           rel_canonical = '/project/lectoraat-data-intelligence')

@app.route('/project/achtergrond-project', methods = ['GET'])
def opzet():
    return render_template('achtergrond-project.html',
           meta_title = 'Achtergrond - Zuyd Hogeschool',
           meta_description = 'De achtergrond over het project',
           rel_canonical = '/project/achtergrond-project')

@app.route('/overig/contact', methods = ['GET'])
def referenties():
    return render_template('Contact.html',
           meta_title = 'Contact - Zuyd Hogeschool',
           meta_description = 'Contacteer het Lectoraat Data Intelligence',
           rel_canonical = '/overig/contact')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



def deriv(y, t, r0_y_interpolated, gamma, sigma, N, p_I_to_C, p_C_to_D, Beds):
    S, E, I, C, R, D = y

    def betaa(t):
        return I / (I + C) * (12 * p_I_to_C + 1/gamma * (1 - p_I_to_C)) + C / (I + C) * (
            min(Beds(t), C) / (min(Beds(t), C) + max(0, C-Beds(t))) * (p_C_to_D * 7.5 + (1 - p_C_to_D) * 6.5) +
            max(0, C-Beds(t)) / (min(Beds(t), C) + max(0, C-Beds(t))) * 1 * 1
        )

    def beta(t):
        try:
            return r0_y_interpolated[int(t)] / betaa(t) if not np.isnan(betaa(t)) else 0
        except:
            return r0_y_interpolated[-1] / betaa(t)
            
    dSdt = -beta(t) * I * S / N
    dEdt = beta(t) * I * S / N - sigma * E
    dIdt = sigma * E - 1/12.0 * p_I_to_C * I - gamma * (1 - p_I_to_C) * I
    dCdt = 1/12.0 * p_I_to_C * I - 1/7.5 * p_C_to_D * \
        min(Beds(t), C) - max(0, C-Beds(t)) - \
        (1 - p_C_to_D) * 1/6.5 * min(Beds(t), C)
    dRdt = gamma * (1 - p_I_to_C) * I + (1 - p_C_to_D) * \
        1/6.5 * min(Beds(t), C)
    dDdt = 1/7.5 * p_C_to_D * min(Beds(t), C) + max(0, C-Beds(t))
    return dSdt, dEdt, dIdt, dCdt, dRdt, dDdt

gamma = 1.0/9.0
sigma = 1.0/3.0

def logistic_R_0(t, R_0_start, k, x0, R_0_end):
    return (R_0_start-R_0_end) / (1 + np.exp(-k*(-t+x0))) + R_0_end

def Model(initial_cases, initial_date, N, beds_per_100k, R_0_start, k, x0, R_0_end, p_I_to_C, p_C_to_D, s, end_date, total_days, r0_y_interpolated=None):
    days = total_days
    def beta(t):
        return logistic_R_0(t, R_0_start, k, x0, R_0_end) * gamma
    
    def Beds(t):
        beds_0 = beds_per_100k / 100_000 * N
        return beds_0 + s*beds_0*t  # 0.003


    diff = int((np.datetime64("2020-01-01") - np.datetime64(initial_date)) / np.timedelta64(1, "D"))
    if diff > 0:
        r0_y_interpolated = [r0_y_interpolated[0] for _ in range(diff-1)] + r0_y_interpolated
    elif diff < 0:
        r0_y_interpolated = r0_y_interpolated[(-diff):]

    last_date = np.datetime64(initial_date) + np.timedelta64(days-1, "D")
    missing_days_r0 = int((last_date - np.datetime64(end_date)) / np.timedelta64(1, "D"))
    r0_y_interpolated += [r0_y_interpolated[-1] for _ in range(missing_days_r0+1)]

    y0 = N-initial_cases, initial_cases, 0.0, 0.0, 0.0, 0.0
    t = np.linspace(0, days, days)
    ret = odeint(deriv, y0, t, args=(r0_y_interpolated,
                                        gamma, sigma, N, p_I_to_C, p_C_to_D, Beds))
    S, E, I, C, R, D = ret.T
    R_0_over_time = r0_y_interpolated
    total_CFR = [0] + [100 * D[i] / sum(sigma*E[:i]) if sum(
        sigma*E[:i]) > 0 else 0 for i in range(1, len(t))]
    daily_CFR = [0] + [100 * ((D[i]-D[i-1]) / ((R[i]-R[i-1]) + (D[i]-D[i-1]))) if max(
        (R[i]-R[i-1]), (D[i]-D[i-1])) > 10 else 0 for i in range(1, len(t))]



    dates = []
    ax = pd.DataFrame(index=pd.date_range(start=(initial_date), periods=days))

    for item in ax.index:
        item = str(item)
        item = item.replace(' 00:00:00','').replace('-',', ')
        dates.append(item) 
        
    return dates, list([round(s,3) for s in S]), list([round(e,3) for e in E]), list([round(i,3) for i in I]), list([round(c,3) for c in C]), list([round(r,3) for r in R]), list([round(d,3) for d in D]), R_0_over_time, list([round(total_cfr,3) for total_cfr in total_CFR]), list([round(daily_cfr,3) for daily_cfr in daily_CFR]), [Beds(i) for i in range(len(t))], end_date, total_days


def update_graph(initial_cases, initial_date, population, icu_beds, p_I_to_C, p_C_to_D, r0_data, r0_columns, range_x, end_date, total_days):
    
    last_initial_date, last_population, last_icu_beds, last_p_I_to_C, last_p_C_to_D = "2020-01-15", 1_000_000, 5.0, 5.0, 50.0
    if not (initial_date and population and icu_beds and p_I_to_C and p_C_to_D):
        initial_date, population, icu_beds, p_I_to_C, p_C_to_D = last_initial_date, last_population, last_icu_beds, last_p_I_to_C, last_p_C_to_D


    r0_data_y = [datapoint["R value"] if ((not np.isnan(datapoint["R value"])) and (datapoint["R value"] >= 0)) else 0 for datapoint in r0_data]
    f = interpolate.interp1d(range_x, r0_data_y, kind='linear')
    r0_x_dates = pd.date_range(start=np.datetime64(initial_date), end=np.datetime64(end_date), freq="D")
    r0_y_interpolated = f(np.linspace(0, len(range_x)-1, num=len(r0_x_dates))).tolist()

    dates, S, E, I, C, R, D, R_0_over_time, total_CFR, daily_CFR, B, date_end, days_total = Model(initial_cases, initial_date, population, icu_beds, 3.0, 0.01, 50, 2.3, float(p_I_to_C)/100, float(p_C_to_D)/100, 0.001,  end_date, total_days, r0_y_interpolated)

    return  (dates, S, E, I, C, R, D, R_0_over_time, total_CFR, daily_CFR, B, list([0] + [round(D[i]-D[i-1],3) for i in range(1, len(dates))]), list([0] + [max(0, round(C[i-1]-B[i-1],3)) for i in range(1, len(dates))]))

@app.route('/onderzoek/epidemic-calculator', methods =['POST','GET'])
def calc():
    if request.method == 'POST':
        form_population_range = request.form.get('population_range')
        form_ICU_beds_range = request.form.get('ICU_beds_range')
        form_Initial_cases_range = request.form.get('Initial_cases_range')
        form_p_symptoms_range = request.form.get('p_symptoms_range')
        form_p_dying_range = request.form.get('p_dying_range')
        form_start_date = request.form.get('start_date_picker')
        form_months = request.form.get('countofMonths')
        form_end_date = request.form.get('end_date_picker')
        form_days = request.form.get('valueOfDays')
        
        if (type(form_population_range) == type(None)):
            form_population_range = 17800000
        if (type(form_ICU_beds_range) == type(None)):
            form_ICU_beds_range = 10
        if (type(form_Initial_cases_range) == type(None)):
            form_Initial_cases_range = 1
        if (type(form_p_symptoms_range) == type(None)):
            form_p_symptoms_range = 5.0
        if (type(form_p_dying_range) == type(None)):
            form_p_dying_range = 5.0
        if (type(form_start_date) == type(None)):
            form_start_date = "2020-01-01"
        if (type(form_end_date) == type(None)):
            form_end_date = "2020-09-01"
        if (type(form_months) == type(None)):
            form_months = 9
        else:
            form_months = int(form_months)
            
        listOfRdata = []
        listOfRcolumns = []
        list_r_values = []
        a_month = dateutil.relativedelta.relativedelta(months=int(1))  
        a_date = datetime.datetime.strptime(form_start_date, "%Y-%m-%d")
        for vals in range(form_months):
            tem_date = str(a_date)
            temp_r = 'r_value_' + str(vals)
            r_value = request.form.get(temp_r)
            listOfRdata.append({"Date": str(tem_date[0:10]), "R value": float(r_value)})
            listOfRcolumns.append({"Date": str(tem_date[0:10]), "R value": float(r_value)})
            list_r_values.append(r_value)
            a_date += a_month

        def getnums(s, e,i):
           return list(range(s, e,i))
        
        # Driver Code
        start, end, intval = 0, form_months,1
        x_range = getnums(start, end,intval) 
            
        ax = update_graph(int(form_Initial_cases_range), str(form_start_date), int(form_population_range), int(form_ICU_beds_range), float(form_p_symptoms_range), float(form_p_dying_range), listOfRdata, listOfRcolumns, x_range, form_end_date, int(form_days))
        return render_template("Epidemic-calculator.html", 
               results = list(ax),
               default_values = [str(form_start_date), int(form_population_range), int(form_Initial_cases_range), int(form_ICU_beds_range), float(form_p_symptoms_range), float(form_p_dying_range), str(form_end_date), int(form_days), list_r_values],

        meta_title = 'Epidemic calculator - Zuyd Hogeschool',
        meta_description = 'Epidemic calculator',
        rel_canonical = '/onderzoek/epidemic-calculator')
    
    if request.method == 'GET':
        def getnums(s, e,i):
           return list(range(s, e,i))
        
        # Driver Code
        start, end, intval = 0, 9,1
        x_range = getnums(start, end,intval) 
        ax = update_graph(1,"2020-01-01",17700000,10,5.0,5.0,[ {"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-02-01", "R value" : 2.9},{"Date" : "2020-03-01", "R value" : 2.5},{"Date" : "2020-04-01", "R value" : 0.8},{"Date" : "2020-05-01", "R value" : 1.1},{"Date" : "2020-06-01", "R value" : 2},{"Date" : "2020-07-01", "R value" : 2.1},{"Date" : "2020-08-01", "R value" : 2.2},{"Date" : "2020-09-01", "R value" : 2.3}],    [ {"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-01-01", "R value" : 3.2}     ],x_range, "2020-09-01", 360)
        return render_template("Epidemic-calculator.html", 
               results = list(ax),
               default_values = ["2020-01-01", 17800000, 1, 10, 5.0, 5.0, "2020-09-01", 360, [3.2, 2.9,2.5,0.8,1.1,2,2.1,2.2,2.3]],
           meta_title = 'Epidemic calculator - Zuyd Hogeschool',
           meta_description = 'Epidemic calculator',
           rel_canonical = '/onderzoek/epidemic-calculator')
    
    
if __name__ == "__main__":
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT)