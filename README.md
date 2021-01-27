# Hoe heeft covid-19 zich ontwikkeld in Nederland?

*Door:*
Mitchell Bink, Sandro Offermans & Max Kleinman

In het onderzoek naar de ontwikkeling van covid-19 in Nederland zijn een aantal deelonderwerpen onderzocht.  Voor de gedane onderzoeken zijn zoveel mogelijk wetenschappelijke artikelen en bronnen gebruikt om mogelijke aannames te voorkomen. 
Dit project is uitgevoerd in opdracht van het **Lectoraat Data Intelligence** van **Zuyd Hogeschool** te **Heerlen** als onderdeel van de minor **Data Science**.



## Inhoud

- Hebben temperaturen en klimaten invloed op de verspreiding van corona?
- Zit er een verschil in de verspreiding op een eiland en op het vasteland?
- Leidt een hogere bevolkingsdichtheid tot een hogere verspreiding?
- Wat is het 'Reproductie getal' en de 'strengheid' van een land?
- Is er een afwijking in de R-coëfficient in landen met vergelijkbare kenmerken (o.a. populatie) als Nederland en welke maatregelen zijn overeenkomend dan wel verschillend?
- Aannames 
- Referenties


## Hebben temperaturen en klimaten invloed op de verspreiding van corona?

Om over dit onderwerp inzicht te krijgen zijn alle landen gelabled met het “Köppen-Geiger climate classification scheme”. Hierbij wordt vooral gekeken naar Cfb (oceanic climate) en Dfb (warm summer continental), deze zijn het meest voorkomend in europa.

Het onderzoek wordt uitgevoerd door de data van 5 Cfb landen  en 5 Dfb landen met elkaar te vergelijken, om dit te doen is er een percentage genomen. Namelijk hoeveel procent van de samenleven geïnfecteerd is geweest. Dit is genomen zodat ieder land op een “gelijk” vlak valt. Het is natuurlijk niet helemaal gelijk, ieder land heeft namelijk een andere bevolkingsdichtheid. De bevolkingsdichtheid kan al groot invloed hebben op de verspreidingsgraad in de landen. De koudere landen (Dfb) hebben een lagere bevolkingsdichtheid dat de Cfb landen.

De 5 gekozen Cfb landen zijn: Groot Brittannië, Nederland, Denemarken, Hongarije en Ierland.
De 5 gekozen Dfb landen zijn: Belarus, Estonia, Tsjechië, Roemenië en Oostenrijk.
Hierbij is de volgende data gebruikt.


| Country               |Total population                          |Population density                         |Climate                         |Total cases per 6-12-2020                         |
|----------------|-------------------------------|-----------------------------|-----------------------------|-----------------------------|
|United Kingdom|67320323            |270.87            |Cfb            |1723242            |
|Netherlands|17842387            |419.51            |Cfb            |557224            |
|Denmark|5946336            |137.65            |Cfb            |90603            |
|Hungary|9769526            |105            |Cfb            |250278            |
|Ireland|6572728            |77.8            |Cfb            |74246            |
||            |            |            |            |
|Belarus|94084000            |45.32            |Dfb            |147157            |
|Estonia|1328976            |28            |Dfb            |14978            |
|Czech Republic|10699142            |135.66            |Dfb            |546833            |
|Romania|19317984            |84            |Dfb            |513576            |
|Austria|8935112            |106.52            |Dfb            |303430            |

### Conclusie
Uit het onderzoek blijft dat Dfb landen een hogere besmettingsgraad hebben. Het verschilt met 0.6% tot de Cfb landen.
![results_image_1](https://github.com/MitchellBink/covid-19/blob/main/lfs/results_climate.png)

De Dfb landen zijn kouder ten opzichte van de Cfb landen. Het zijn in een kouder land kan betekenen dan personen vaker binnen zitten, en omdat het zo koud is zal ventilatie minder zijn om de warmte binnen te houden. Hiernaast hebben de landen van Dfb een lagere bevolkingsdichtheid maar een hogere procentueel aantal cases. Dit gaat tegen logica in, met een hogere bevolkingsdichtheid (zoals de Cfb landen) zou je de aannamen kunnen maken dat er meer cases zijn als mensen dichter bij elkaar zijn. Logisch zou dit ook zo zijn, maar het kan beïnvloed worden door de hoeveelheid testen die door de overheid uitgevoerd worden.

Een antwoord op deze deelvraag kan niet volledig zijn, dit komt omdat Covid-19 verspreidingen veel factoren hebben. In het uitgevoerde onderzoek wordt alleen op basis cijfers gerekend, andere factoren zoals maatregelen, hoeveelheid testen en kracht van de overheid wordt hier niet in kaart gebracht. Het antwoord daar dit onderzoek op komt is dat Covid-19 zich sneller verspreid in koude landen, maar dit kan vanwege de vele factoren niet als waarheid genomen worden.

Het onderzoek _COVID-19 in the environment_. (2021, January 1) van ScienceDirect wordt aangegeven dat andere onderzoeken aangeven dat er een kans is dat het weer invloed heeft op covid-19 infecties, maar de onderzoeken konden dit niet volledige concluderen.



## Zit er een verschil in de verspreiding op een eiland en op het vasteland?
Voor deze deelvraag is er een kort onderzoek gedaan waarbij er gekeken is naar 3 landen die als eiland geclassificeerd zijn en 3 landen die als vasteland gecategoriseerd zijn. Hierbij wordt naar Groot-Brittannië, Ierland en IJsland  gekeken als eilanden en er wordt naar Romania, Oostenrijk en Noorwegen gekeken als vasteland landen.

Groot Brittannië en Ierland bevinden zich samen op 2 land massa’s, IJsland bevind zich op een enkele landmassa. Logisch geredeneerd zouden de eilanden minder verspreiding moeten hebben, omdat reizen naar deze landen via minder makkelijke manier gedaan moet worden door bijvoorbeeld gebruik van boot of vliegtuig.

Hierbij is de volgende data gebruikt.
![results_image_2](https://github.com/MitchellBink/covid-19/blob/main/lfs/results_islands.png)
### Conclusie
Volgens het door ons uitgevoerde onderzoek is de verspreidingsgraad hoger op eilanden dat het is op het vaste land. Dit gaat tegen logica in, maar dit geeft ook weer aan zoals in de klimaat vraag dat er veel meer factoren meespelen bij het verspreiden van COVID-19. Dit kan te maken hebben met de verschillende maatregelen de landen opleggen, maar ook door de verschillende mutaties van COVID-19.

Net als de andere deelvraag kan hier geen concrete en volledige conclusie uit getrokken worden omdat het hele totaal plaatje van COVID-19 met vele factoren werkt.  Daarnaast is het ook mogelijk dat deze landen een beperkt aantal covid testen tot hun beschikking hadden of een beperkt testbeleid, waardoor het daadwerkelijke total cases anders is dan de nu gemelde aantal cases.

## Leidt een hogere bevolkingsdichtheid tot een hogere verspreiding?

Hierbij is gekeken naar 5 landen met een population density boven de 100, en 5 landen met een population density onder de 100.
De landen boven de 100 zijn: Nederland, Luxembourg, Italië. Groot Brittannië en België.
De landen onder de 100 zijn: Bosnië, Bulgarije, Kroatië, Belarus en Roemenië.

Het logische antwoord op deze vraag zou zijn dat verspreiding hoger ligt in de landen met een hogere population density. Dit komt omdat hoe hoger het nummer, hoe dichter bij de mensen bij elkaar wonen. Hoe dichterbij mensen zijn, hoe makkelijker het is om iemand te infecteren.

Hierbij is de volgende data gebruikt:
![results_image_3](https://github.com/MitchellBink/covid-19/blob/main/lfs/results_density.png)

### Conclusie
Volgens het door ons uitgevoerde onderzoek heeft de population density een groot invloed op het verspreiden van covid-19. De landen met een population density hoger dan 100 hebben gemiddeld 19,54% van hun inwoners geïnfecteerd gehad, waarbij dit maar op 12,98% ligt bij de landen onder de 100.

De populatie in de landen met een population density onder de 100 woont verder van elkaar, hierdoor is het contact met andere mensen minder waardoor infecties zich minder snel verspreiden. Hiernaast is het mogelijk dat andere factoren zoals het klimaat en de maatregelen van de overheid hier groot invloed op kan hebben.

## Wat is het 'Reproductie getal' en de 'strengheid' van een land?

Het basisreproductiegetal wordt in een ideale situatie gemeten volgens het individual leveling model (ILM). Hierbij wordt gekeken naar een geïnfecteerd persoon en vervolgens het gemiddelde aantal personen dat deze geïnfecteerde persoon ook besmet met het virus (dus effectief het virus overdraagt naar een andere drager). Dit is in het geval van pandemieën zeer moeilijk te controleren en te indexeren daar er veel personen zijn die geïnfecteerd raken en niet iedereen bijhoudt waar hij/zij is geweest of zoals in Nederland het geval is geweest, dat mensen pseudonamen en/ of telefoonnummers opgeven om anoniem te blijven. Hierdoor is ILM haast onmogelijk om dit juist toe te passen.

Naast het ILM model, kan er een soortgelijk model worden toegepast. Dit is het population leveling model. Hierbij wordt gekeken naar de cijfers van de populatie in plaats van een individu. Onder de cijfers wordt hier verstaan, de geïnfecteerde personen van vandaag ten opzichte van de geïnfecteerde personen van gisteren.

Voor het R-getal dat ons gepresenteerd wordt in de media, geldt als volgt: Het basisreproductiegetal ($R_0$) is een minder accurate term. Omdat we ver voorbij de secundaire infectie reeks zijn (namelijk, het virus is al geruime tijd onder ons) is het beter om te spreken van de term “het effectieve reproductiegetal” ($R_e$). Omdat men allicht verwarring kan krijgen door verschillend gebruik van de termen, wordt ons het algemene R getal gepresenteerd, zonder nadere specifieke toevoeging.

Ondanks dat men verwacht dat Re rond de 3 ligt (Gallagher, 2020), kan en zal het virus uiteindelijk stoppen met zijn exponentiële groei. Immers, dieren kunnen zonder voedsel geraken, mensen kunnen overbevolken  waardoor er te weinig plaats (woonruimte) is en zo ook kunnen virussen te weinig gastheren krijgen waar zij zich kunnen voortplanten. Zo zal elk virus, dat de mogelijkheid heeft zich exponentieel voort te planten, zich in het begin ook extreem snel voortplanten, maar na een tijd zal deze versnelling afzwakken en zichzelf uiteindelijk stabiliseren.

Voor zo’n virus, en dus ook voor het reproductiegetal, zijn een aantal factoren belangrijk:

1. Het gemiddelde aantal personen dat een willekeurig persoon tegenkomt op een dag;
2. De kans dat een blootstelling een uiteindelijke infectie wordt;
3. De duur van de uiteindelijke infectie;
4. De populatiegrootte;
5. De populatiedichtheid;
6. De mate van herstel dan wel dood door het virus.

Een ander misbegrip over het reproductiegetal, is dat het door veel landen als een landelijk getal wordt gepresenteerd. Echter, dit is niet de realiteit van het reproductiegetal. Doordat de ene stad, gemeente, provincie hoger ‘scoort’ dan een andere, bevinden beide steden zich onder hetzelfde getal. Hierdoor zou het bijvoorbeeld beter zijn wanneer er een (confidence)interval zou worden gegeven of een standaarddeviatie. Op deze manier wordt het meer transparant over de werkelijke waarde van het getal. Daarnaast kan het/ een virus zich ook anders verspreiden bij verschillende leeftijden, bevolkingsgroepen of klimaten.

Om het virus werkelijk onder controle te krijgen (dat betekent het reproductiegetal maximaal rond de waarde 1 krijgen), zijn er maatregelen benodigd.

De meeste maatregelen die genomen worden door een land zijn bedoeld om het virus te bedwingen (of in ieder geval in poging tot), maar andere maatregelen zijn bedoeld om de getroffen personen dankzij andere maatregelen te ondersteunen (denk aan een extra uitkering/schadevergoeding).  
Om te bepalen of maatregelen nodig zijn, en in welke mate, is het belangrijk dat het duidelijk is hoe groot de schade kan worden. Hier zijn 3 maatstaven voor:

1. Het reproductiegetal
2. De dodelijkheid/ziektebeelden
3. Het aantal gevallen

Wanneer het om een hoog reproductiegetal gaat, is het belangrijk dat de mensen zo min mogelijk socialiseren face-to-face zodat het virus zich niet kan voortplanten zoals het wilt voortplanten.

Bij ziektebeelden of een extreem laag dodelijkheidsgeval zijn de maatregelen minder streng en ingrijpend omdat bijvoorbeeld de zorg ook minder belastend is voor diegene die het krijgen. Echter, bij een hoog sterfgeval of zeer ingrijpende zorg die benodigd is om de mensen in leven te houden, maken een virus belangrijk en dus worden er ook strengere maatregelen genomen.

Het laatste punt is voornamelijk belangrijk voor “wanneer” grijp je in als overheid met maatregelen. En wat wordt de mate / strengheid van een dergelijke maatregel, immers bij een hoog aantal gevallen en geen/milde maatregelen zal het aantal ook hoog blijven.

De maatregelen die de meeste landen (hetzij landelijk, hetzij regionaal) genomen hebben die (effectief) bijdragen aan het verminderen van de verspreiding van Covid-19 (tussen haakjes is de schaal aangegeven van de maatregel):

1. (C1) Het sluiten van scholen (0,1,2,3);
2. (C2) Het sluiten van werkplaatsen (thuiswerken indien mogelijk) (0,1,2,3);
3. (C3) Annuleren van publieke evenementen (0,1,2);
4. (C4) Limieten plaatsen op bijeenkomsten (begrafenissen/bruiloften bijvoorbeeld maximaal  30 personen) (0,1,2,3, 4);
5. (C5) Openbaar vervoer limiteren/sluiten (0,1,2);
6. (C6) Het verplichten tot thuisblijven (lockdown) (0,1,2,3);
7. (C7) Limieten leggen aan nationale verplaatsingen(0,1,2);
8. (C8) Het sluiten van grenzen voor niet-woonachtigen van het eigen land (0,1,2,3,4);
9. (H1) Publieke belangstelling creëren door informatieve reclame te geven (0,1,2).

Deze maatregelen kunnen alleen maar effectief zijn als ze landelijk geregeld worden. In een ideale situatie zou dit zelfs continentaal geregeld worden, omdat de meeste continenten een verdrag hebben tussen de landen per continent.

De strengheid van de maatregelen kan gedefinieerd worden met de volgende formule (Oxford University, 2020):
$$I =\frac{1}{9} \sum_{j=1}^9 I_j$$

Hierbij geldt het volgende:

I = de strengheid van een land tussen 0 en 100, waarbij 100 alle maatregelen op maximale strengheid worden toegediend;
j = nummer van de maatregel

Omdat niet elke maatregel dezelfde schaal heeft qua beoordelen, omdat in sommige gevallen meer nuance aangebracht kan worden, is er een formule die de weging van de maatregelen berekent ten opzichte van de ordinale schaal die deze indicatoren hebben:
$$ w =\frac{1}{8} \sum_{j=1}^8 \frac{1}{N_j + 1} \approx 0,2854 $$

Waarbij geldt dat:

$N_j$ = de maximum in de ordinale schaal  $\to$ (0,1,2), Nj = 2

Deze formule geldt voor de weging van alle maatregelen, behalve voor het controleren dan wel sluiten van grenzen. Dit omdat deze altijd landelijk worden geregeld, zal deze een andere formule krijgen uiteindelijk.

Voor de berekening van een individuele indicator die al dan niet landelijk geregeld kan worden, en wat de strengheid van die indicator dus is, geldt het volgende:

$$I_j =100 \left(C_j \frac{1-w}{N_j}+w \cdot G_j \right)$$

$w \approx 0.2854$
$G_j = $ 1 indien het landelijk is, anders 0
$C_j = $ de waarde van de indicator (0,1,2,..)

Voor de 8ste indicator geldt de volgende, omdat die alleen landelijk geregeld kan zijn:
$$I_j =100 \left( \frac{C_8}{N_8} \right)$$

Echter, de strengheid van een land hoeft geen correlatie te hebben met het aantal besmettingen, sterfgevallen, of andere cijfers, maar kunnen door een land te pas en te onpas opgelegd worden aan de bevolking. Er schijnt wel een overeenkomst te zijn als wanneer er pieken zijn, dat de strengheid van een land qua maatregelen ook hoger wordt, maar wanneer de aantallen afnemen nemen niet persé ook de maatregelen af qua strengheid.

### Conclusie

Ondanks dat een virus dodelijk kan zijn, hoog aantal infecties heeft en ook een hoog reproductiegetal heeft, is het mogelijk om dit virus in bedwang te krijgen. Door onder andere vaccins en maatregelen kunnen we ervoor zorgen dat er groepsimmuniteit bereikt wordt.

Op het moment is het voornamelijk belangrijk dat het reproductiegetal laag blijft dan al niet lager wordt. Dit kan gedaan worden door passende (en effectieve) maatregelen te treffen, en men dient zich daar aan te houden. Wanneer het reproductie getal onder de 2 kan blijven, is een groepsimmuniteit van 50 % afdoende en dus zal het virus (bij 50 % of meer immuniteit) langzaam afzwakken en verdwijnen. (Pandit, 2020)

## Is er een afwijking in de R-coëfficient in landen met vergelijkbare kenmerken (o.a. populatie) als Nederland en welke maatregelen zijn overeenkomend dan wel verschillend?
Er is gekeken naar 5 verschillende landen, namelijk: Groot Brittannië, Zweden, Spanje, Nederland en Frankrijk. Deze landen zijn gekozen omdat de afstand tussen de landen niet al te groot is, en de getallen van populatiegrootte en dichtheid redelijk dicht bij elkaar liggen.

Om te kijken of maatregelen invloed hebben gehad op de R-coëfficiënt wordt naar data gekeken 2 weken na het ingaan van de maatregel. Dit is gedaan omdat covid-19 zich niet altijd toont, en de isolatie tijd 10-14 dagen is.

C1, C2, C3, C4, C6 en H1 zijn in Nederland op 2020-03-16 ingevoerd, $R_e$ = 1. 588571
C1, C2, C3, C4, C5, C6, C7, E1 en H1 zijn in Frankrijk op 2020-03-18 ingevoerd, $R_e$ = 1.366405
C1, C2, C3, C5, C6, C7 en H1 zijn in Spanje op 2020-03-16 ingevoerd, $R_e$ = 1.524893314
C1, C2, C3, C4, C6 en H1 zijn in Zweden op 2020-03-25 ingevoerd, $R_e$ = 1.371179039
C1, C2, C3, C5, C6, C7 en H1 zijn in Groot Brittannië op 2020-03-23 ingevoerd, $R_e$ = 1.698181818

Na 2 weken zijn de R-coëfficiënten van de landen:

Nederland: R = 0.801451, dus 1.588571 – 0.801451 = 0.78712  
Frankrijk: R = 0.633594, dus 1.366405 – 0.633594 = 0.732811  
Spanje: R = 1.141402386, dus 1.524893314 – 1.141402386 = 0.383490928  
Zweden: R = 0.704968944, dus 1.371179039 – 0.704968944 = 0.666210095  
Groot Brittannië: R = 1.46813248, dus 1.698181818 – 1.46813248 = 0.230049338  
  
Alle landen hebben hun R-coëfficiënten naar beneden gehaald, 3 landen scoren hier redelijk hoog, 2 landen redelijk laag.

### Conclusie

Volgens het door ons uitgevoerde onderzoek kijkt naar de verschil van het R-coëfficiënt bij het begin van het invoeren van de maatregelen en twee weken na het voor het eerst invoeren van de maatregelen. Het verwachte beeld is dat het r-coëfficiënt flink afneemt, aangezien de verandering in de samenleving er voor moeten zorgen dat contact en verspreidingsgevaar verminderd wordt. In veel landen is dit een advies geweest en was er geen mogelijkheid op controle en handhaving.  
  
3 van de 5 landen hebben een vermindering van ongeveer 0.7, dit zorgt bij hun dat het R-coëfficiënt onder 0 valt. Dit betekend dat het virus zich op dat moment meer mensen genezen van het virus dat geïnfecteerd raken.  
  
Het is bij ieder land omlaag gegaan waardoor je kan zeggen dat alle maatregelen een positief effect hebben op de verspreiden van covid-19, maar omdat maatregelen in groepen komen, is het niet mogelijk om aan te gegeven welke maatregel het beste is om covid-19 infecties te voorkomen. Als het om maatregelen gaat helpt ieder klein beetje.  
  
Landen die vergelijkbaar zijn zoals Groot Brittannië en Nederland hebben een groot verschil in hun R-coëfficiënt. Redenen hiervoor kunnen zijn dat inwoners de maatregelen in Engeland minder serieus namen, waardoor ze geen effect hebben. Al wordt in dit onderzoek wel gevonden dat iedere maatregel een effect heeft.

## Aannames 
1. In de bestrijding tegen covid-19 zijn maatregelen opzich zelf niet alleen de oorzaak van meer of minder besmettingen.
2. Genomen maatregelen maken deel uit van een totaalpakket. Een totaalpakket kan voor een shift in de getallen zorgen.
3. Niet elk land heeft op hetzelfde moment de eerste besmetting, eerste golf en eerste piek gehad waardoor sommige landen meer voorbereidingstijd hadden en dus in theorie ook beter konden preventeren. Hierdoor zijn vergelijkingen moeilijk te maken, laat staan concrete conclusies te maken. 
4. Dit onderzoek is gebaseerd op de beschikbare data en informatie op de dag van schrijven. Op moment van lezen kunnen inmiddels nieuwe bevindingen gedaan zijn.
5. Voor zover mogelijk is de data vergeleken en gecontroleerd maar niet alle landen hebben data beschikbaar gesteld of data op de juiste manier gedeeld. Om deze reden kunnen gedane conclusies afwijken van de realiteit.  
6. Volgens een contactpersoon van de overheid van Luxemburg zijn de dalingen te wijten aan een shift in de manier van rapportage van de cijfers. De melding van een negatief getal schijnt zo te zijn dat het van alle meldingen naar meldingen van inwoners van Luxemburg is gegaan.
7. Data van COVID-19 ligt 1 à 2 weken achter op schema. Mogelijke effecten en conclusies zijn hierdoor ook 1 à 2 weken achterhaald.
8. Niet in elk land kan iedereen getest worden en/ of wilt iedereen zich laten testen. Hierdoor ontstaat een onnauwkeurigheid in de cijfers die gepresenteerd worden. 
9. Landen hebben een eigen definitie van de cijfers die ze melden. (Bijvoorbeeld; land 1 meldt het aantal positieve testen, terwijl land 2 het aantal positieve (unieke) mensen meldt)
10. Economische en zorgmaatregelen zijn niet allemaal op een ordinale schaal. Hierdoor is het niet mogelijk dit te vergelijken tussen de landen, terwijl dit wel effect kan hebben op de cijfers van covid-19.
11. De strengheid van maatregelen hoeft niet in verhouding te staan aan het aantal gemelde gevallen van covid-19. 
12. Het virus kan in (delen van) landen een verschillend mutageen hebben. Hierdoor kan het virus zich anders gedragen dan de verwachting.
13. Bloedgroeppen van mensen zijn niet meegenomen in de verspreiding.
14. Het aantal mensen dat de grens passeert kan ook van invloed zijn op een extra verspreiding. Grensverkeer is niet meegenomen in het onderzoek en is er uitgegaan van geïsoleerde landen.
15. Het project is uitgevoerd door onderzoekers met een computer-technische achtergrond. De kennis en kunde is gebasseerd op de reeds gepubliceerde artikelen. 



## Referenties

Highsoft. (z.d.). Interactive JavaScript charts for your webpage | Highcharts. Highcharts. Geraadpleegd op 25 november 2020, van [https://www.highcharts.com/](https://www.highcharts.com/)

European Centre for Disease Prevention and Control. (z.d.). All resources on COVID-19. Geraadpleegd op 25 november 2020, van [https://www.ecdc.europa.eu/en/covid-19/all-reports-covid-19](https://www.ecdc.europa.eu/en/covid-19/all-reports-covid-19)

European Respiratory Society. (z.d.). COVID-19: Guidelines and recommendations directory | European Respiratory Society. covid 19 guidelines and recommendations directory. Geraadpleegd op 25 november 2020, van [https://www.ersnet.org/covid-19-guidelines-and-recommendations-directory](https://www.ersnet.org/covid-19-guidelines-and-recommendations-directory)

Rijksinstituut voor volksgezondheid en milieu. (z.d.). Databronnen COVID-19. Databronnen COVID-19. Geraadpleegd op 25 november 2020, van [https://www.databronnencovid19.nl/](https://www.databronnencovid19.nl/)

European Centre for Disease Prevention and Control. (z.d.-b). COVID-19 | European Centre for Disease Prevention and Control. Geraadpleegd op 25 november 2020, van [https://qap.ecdc.europa.eu/public/extensions/COVID-19/COVID-19.html#global-overview-tab](https://qap.ecdc.europa.eu/public/extensions/COVID-19/COVID-19.html)

Beus, T. (2020, 30 september). Alle coronamaatregelen per land: wat is nou het meest effectief? Pointer. [https://pointer.kro-ncrv.nl/artikelen/alle-coronamaatregelen-per-land-wat-is-nou-het-meest-effectief](https://pointer.kro-ncrv.nl/artikelen/alle-coronamaatregelen-per-land-wat-is-nou-het-meest-effectief)

Coronavirus Government Response Tracker. (2020, 18 maart). Blavatnik School of Government. [https://www.bsg.ox.ac.uk/research/research-projects/coronavirus-government-response-tracker](https://www.bsg.ox.ac.uk/research/research-projects/coronavirus-government-response-tracker)

Reisadviezen en COVID-19. (z.d.). RIVM. Geraadpleegd op 25 november 2020, van [https://www.rivm.nl/coronavirus-covid-19/reisadviezen](https://www.rivm.nl/coronavirus-covid-19/reisadviezen)

Oxford University. (2020, 5 april). OxCGRT/covid-policy-tracker. GitHub - Oxford. [https://github.com/OxCGRT/covid-policy-tracker](https://github.com/OxCGRT/covid-policy-tracker)

Oxford COVID-19 Government Response Tracker. (2020, april). Calculation and presentation of the stringency Index4.0. [https://www.bsg.ox.ac.uk/sites/default/files/Calculation%20and%20presentation%20of%20the%20Stringency%20Index.pdf](https://www.bsg.ox.ac.uk/sites/default/files/Calculation%20and%20presentation%20of%20the%20Stringency%20Index.pdf)

The Royal Society. (2020, augustus). Reproduction number (R) and growth rate (r) of the COVID-19 epidemic in the UK. [https://royalsociety.org/-/media/policy/projects/set-c/set-covid-19-R-estimates.pdf](https://royalsociety.org/-/media/policy/projects/set-c/set-covid-19-R-estimates.pdf)

Gallagher, B. J. (2020, 27 november). Coronavirus: What is the R number and how is it calculated? BBC News. [https://www.bbc.com/news/health-52473523](https://www.bbc.com/news/health-52473523)

Wikipedia contributors. (2020f, december 2). Basic reproduction number. Wikipedia. [https://en.wikipedia.org/wiki/Basic_reproduction_number](https://en.wikipedia.org/wiki/Basic_reproduction_number)

Wikipedia contributors. (2020d, november 19). Köppen climate classification. Wikipedia - Köppen. [https://en.wikipedia.org/wiki/K%C3%B6ppen_climate_classification](https://en.wikipedia.org/wiki/K%C3%B6ppen_climate_classification)

Wikipedia contributors. (2020e, november 24). List of countries and dependencies by population. Wikipedia - Countries. [https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population)

Pandit, J. J. (2020, 1 december). Managing the R0 of COVID-19: Mathematics fights back. Association of Anaesthetists. [https://associationofanaesthetists-publications.onlinelibrary.wiley.com/doi/10.1111/anae.15151](https://associationofanaesthetists-publications.onlinelibrary.wiley.com/doi/10.1111/anae.15151)

Coronavirus disease (COVID-19). (2020, 12 oktober). Coronovirus disease (COVID-19). [https://www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub/q-a-detail/coronavirus-disease-covid-19](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub/q-a-detail/coronavirus-disease-covid-19)

Roser, M. (2020, 4 maart). Coronavirus Pandemic (COVID-19) - Statistics and Research. Our World in Data. [https://ourworldindata.org/coronavirus](https://ourworldindata.org/coronavirus)

COVID-19 in the environment. (2021, January 1). ScienceDirect. [https://www.sciencedirect.com/science/article/abs/pii/S0045653520321688?casa_token=sXl6LsxTwMIAAAAA:l0pzq5y0_4on1hyUWXqekqRK6o2HERxQynku4INwjks89g68SkNPFKCGJv6ahK9lnax_XKjinw](https://www.sciencedirect.com/science/article/abs/pii/S0045653520321688?casa_token=sXl6LsxTwMIAAAAA:l0pzq5y0_4on1hyUWXqekqRK6o2HERxQynku4INwjks89g68SkNPFKCGJv6ahK9lnax_XKjinw)

Lectoraat Data Intelligence. (z.d.). Hevner based design science research process. [https://dataintelligence.zuyd.nl/](https://dataintelligence.zuyd.nl/). Geraadpleegd 5 november 2020, van [https://dataintelligence.zuyd.nl/wp-content/uploads/2020/02/Hevnerdesign-science-process-A4.pdf](https://dataintelligence.zuyd.nl/wp-content/uploads/2020/02/Hevnerdesign-science-process-A4.pdf)

Redactie Timemanagement.nl. (2020, 7 augustus). Verwachtingsmanagement voorkomt teleurstellingen | Timemanagment.nl. Timemanagement.nl. [https://timemanagement.nl/verwachtingsmanagement/](https://timemanagement.nl/verwachtingsmanagement/)

Duckett, J. (2011). HTML and CSS: Design and Build Websites. Indianapolis: John Wiley Sons Inc.

Duckett, J. (2014). JavaScript and JQuery: Interactive Front-End Web Development. Indianapolis: John Wiley Sons Inc.  

Narayan, R. (2020, 7 juni). _Rendering markdown from Flask_. DEV Community. https://dev.to/mrprofessor/rendering-markdown-from-flask-1l41

Bhatia, A. (z.d.). _Why Masks Work Better Than You Think: An Interactive Essay_. Aatishb. Geraadpleegd op 27 januari 2021, van https://aatishb.com/maskmath/

van den Heuvel, E., Regis, M., & Zhan, Z. (2020). _STATISTICAL APPROACH FOR MAKING PREDICTIONSOF CONFIRMED INFECTIONAND DEATHS ON CORONA VIRUS_. https://assets.tue.nl/fileadmin/content/pers/2020/03%20March/TUe%20-%20Technical_Report_Prediction_Corona_Virus.pdf

WHO. (2020, 4 augustus). _Estimating mortality from COVID-19_. Case fatality ratio. https://www.who.int/news-room/commentaries/detail/estimating-mortality-from-covid-19

_Prediction of epidemic trends in COVID-19 with logistic model and machine learning technics_. (2020, 1 oktober). PubMed Central (PMC). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7328553/

Boudrioua, M. S., & Boudrioua, A. (2020, 22 mei). _Predicting the COVID-19 epidemic in Algeria using the SIR model_. ResearchGate. https://www.researchgate.net/publication/341039067_Predicting_the_COVID-19_epidemic_in_Algeria_using_the_SIR_model

Vasconcelos, G. L. (2020, 1 januari). _Modelling fatality curves of COVID-19 and the effectiveness of intervention strategies_. medRxiv. https://www.medrxiv.org/content/10.1101/2020.04.02.20051557v3.full

Froese, H. (2020, 22 april). _Modelling Coronavirus: Beyond the SIR Model | Towards Data Science_. Medium. https://towardsdatascience.com/infectious-disease-modelling-beyond-the-basic-sir-model-216369c584c4

Harrison, E. M., Docherty, A., & Semple, C. (2020, oktober). _COVID-19: time from symptom onset until death in UKhospitalised patients_. https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/928729/S0803_CO-CIN_-_Time_from_symptom_onset_until_death.pdf

Epidemic Calculator. (2020). Epidemic Calculator. https://gabgoh.github.io/COVID/?CFR=0.02&D_hospital_lag=5&D_incbation=5.2&D_infectious=2.9&D_recovery_mild=11.1&D_recovery_severe=28.6&I0=1&InterventionAmt=0.76&InterventionTime=84.26666666666668&P_SEVERE=0.2&R0=2.2&Time_to_death=32&logN=16.79
