# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 17:10:15 2020

@author: Mitchell Bink, Max Kleinman en Sandro Offermans"""

from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from scipy.integrate import odeint
from scipy import interpolate



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

@app.route('/')
def index():
     return render_template(
         'index.html',
         meta_title = 'Dashboard covid-19 - Zuyd Hogeschool',
         meta_description = 'Compare the numbers of the countries',
         rel_canonical = '/test',
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
    


@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/project/aanleiding-project')
def aanleiding():
    return render_template('Aanleiding-project.html')

@app.route('/overig/biasses')
def biasses():
    return render_template('Biasses.html')

@app.route('/onderzoek/deelvragen')
def deelvragen():
    return render_template('Deelvragen.html')

@app.route('/onderzoek/hoofdvraag')
def hoofdvraag():
    return render_template('Hoofdvraag.html')

@app.route('/project/lectoraat-data-intelligence')
def lectoraat():
    return render_template('Lectoraat.html')

@app.route('/project/opzet')
def opzet():
    return render_template('Opzet.html')

@app.route('/overig/referenties')
def referenties():
    return render_template('Referenties.html')

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

def Model(initial_cases, initial_date, N, beds_per_100k, R_0_start, k, x0, R_0_end, p_I_to_C, p_C_to_D, s, r0_y_interpolated=None):
    days = 360
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
    missing_days_r0 = int((last_date - np.datetime64("2020-09-01")) / np.timedelta64(1, "D"))
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



    # dates = pd.date_range(start=np.datetime64(initial_date), periods=days, freq="D")
    dates = []
    ax = pd.DataFrame(index=pd.date_range(start=(initial_date), periods=days))

    for item in ax.index:
        item = str(item)
        item = item.replace(' 00:00:00','').replace('-',', ')
        dates.append(item) 
        
    return dates, list([round(s,3) for s in S]), list([round(e,3) for e in E]), list([round(i,3) for i in I]), list([round(c,3) for c in C]), list([round(r,3) for r in R]), list([round(d,3) for d in D]), R_0_over_time, list([round(total_cfr,3) for total_cfr in total_CFR]), list([round(daily_cfr,3) for daily_cfr in daily_CFR]), [Beds(i) for i in range(len(t))]


def update_graph(initial_cases, initial_date, population, icu_beds, p_I_to_C, p_C_to_D, r0_data, r0_columns):
    
    last_initial_date, last_population, last_icu_beds, last_p_I_to_C, last_p_C_to_D = "2020-01-15", 1_000_000, 5.0, 5.0, 50.0
    if not (initial_date and population and icu_beds and p_I_to_C and p_C_to_D):
        initial_date, population, icu_beds, p_I_to_C, p_C_to_D = last_initial_date, last_population, last_icu_beds, last_p_I_to_C, last_p_C_to_D


    r0_data_y = [datapoint["R value"] if ((not np.isnan(datapoint["R value"])) and (datapoint["R value"] >= 0)) else 0 for datapoint in r0_data]
    f = interpolate.interp1d([0, 1, 2, 3, 4, 5, 6, 7, 8], r0_data_y, kind='linear')
    r0_x_dates = pd.date_range(start=np.datetime64("2020-01-01"), end=np.datetime64("2020-09-01"), freq="D")
    r0_y_interpolated = f(np.linspace(0, 8, num=len(r0_x_dates))).tolist()

    dates, S, E, I, C, R, D, R_0_over_time, total_CFR, daily_CFR, B = Model(initial_cases, initial_date, population, icu_beds, 3.0, 0.01, 50, 2.3, float(p_I_to_C)/100, float(p_C_to_D)/100, 0.001, r0_y_interpolated)

    return  (dates, S, E, I, C, R, D, R_0_over_time, total_CFR, daily_CFR, B, list([0] + [round(D[i]-D[i-1],3) for i in range(1, len(dates))]), list([0] + [max(0, round(C[i-1]-B[i-1],3)) for i in range(1, len(dates))]))

@app.route('/epidemic-calculator', methods =['POST','GET'])
def calc():
    if request.method == 'POST':
        results = request.form
        return render_template("Epidemic-calculator.html", result = results)
    if request.method == 'GET':
        ax = update_graph(1,"2020-01-01",17700000,10,5.0,5.0,[ {"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-02-01", "R value" : 2.9},{"Date" : "2020-03-01", "R value" : 2.5},{"Date" : "2020-04-01", "R value" : 0.8},{"Date" : "2020-05-01", "R value" : 1.1},{"Date" : "2020-06-01", "R value" : 2},{"Date" : "2020-07-01", "R value" : 2.1},{"Date" : "2020-08-01", "R value" : 2.2},{"Date" : "2020-09-01", "R value" : 2.3}],    [ {"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-01-01", "R value" : 3.2},{"Date" : "2020-01-01", "R value" : 3.2}     ])
        return render_template("Epidemic-calculator.html", results = list(ax))
    
    
if __name__ == "__main__":
    app.run(debug=False)