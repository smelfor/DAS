## M1.3 - Eigenschappen van distributies **
<!--REF\label{/opdrachten-module-1/eigenschappen}-->

In deze opdracht gaan we kijken naar de [eigenschappen](/module-1/basisbegrippen) van distributies en hoe deze veranderen als je een translatie of vermenigvuldiging toepast. We kijken naar de Normaal en Poisson distributies. 

Download voor deze opdracht het bestand [M1.3_Eigenschappen.py](https://das.mprog.nl/course/12%20Opdrachten%20Module%201/30%20Eigenschappen/M1.3_Eigenschappen.py) zorg dat deze in dezelfde folder staat as het `DAS_DatasetGenerator.py` bestand. 

### Normale distributie
We beginnen met het maken van een Gaussische dataset $$\text{dg}(x)$$ met 500 punten. Deze maken we aan met de functie **`genereerDistributieDG(N)`** waarbij **`N`** het aantal datapunten is die we willen genereren. We kiezen voor een dataset met 500 punten.

		dg = ds.genereerDistributieDG(500)

Deze regel code vind je in het `M1.3_Eigenschappen.py` bestand.

> Schrijf een functie die de volgende statistieken uitrekent voor de dataset:
> 
> - het gemiddelde
> - de mediaan
> - de variantie
> - de standaardafwijking

**NB:** Het is de bedoeling dat je de formules zelf programmeert. Je mag geen gebruik maken van standaard functies van python die dit direct voor je teruggeven. Uiteraard mag je wel gebruiken maken van functies als **`len()`** en **`sort()`**.<br>
Let wel op dat als je de functie **`sort()`** gebruikt bij een lijst, dat de oorspronkelijke volgorde van de lijst daarna weg is. Dat is vaak niet zo handig als je met data bezig bent. Gebruik daarom liever de **`sorted()`** functie en maak een kopie van de data: 

	p = [3,2,4,1]
	l = sorted(p)

`l` is nu de gesorteerde lijst `[1,2,3,4]`. 



> **M1.3a) Stel nu dat je de dataset vergroot en dat je niet 500 maar 1000 meetwaardes hebt in je set. Wat denk je dan dat er gebeurt met elk van deze statistieken? Schrijf hier eerst op wat je verwacht, kwantificeer het resultaat waar het kan.**

We gaan nu kijken naar het effect van een translatie van de dataset.

> - Kopieer de originele dataset en manipuleer de waardes in de dataset met de volgende translatie: 
> $$ x' = x + 2$$<br><br>
> 
> - Plot daarna de originele en de getransleerde dataset over elkaar heen. Controleer of de punten inderdaad zijn opgeschoven.<br><br>
>
> - Welke van de eigenschappen verwacht je dat er veranderen? Controleer dit door voor de originele en getransleerde dataset alle variabelen uit te rekenen.

Nu gaan we kijken naar het effect van een vermenigvuldiging van x.

> - Kopieer de originele dataset en manipuleer de waardes met de volgende multiplicatie:  
>  $$ x' = 2x$$<br>
> 
> - Plot nu de gemultipliceerde dataset toe aan je plot zodat je de originele, de translatie en multiplicatie in 1 figuur ziet. <br><br>
>
> - **M1.3b) Maak nu één plot waar de drie histogrammen voor de normaalverdeling te zien zijn. De originele, de translatie en de multiplicatie. Zorg dat de histogram goed leesbaar is en kijk hiervoor nog eens naar de richtlijnen.**  <br>
> TIP: gebruik de plot optie `alpha` om de histogrammen doorzichtig te maken. Dit helpt bij het zichtbaar maken van de overlappende gebieden.
> 	`plt.hist(dg, alpha=0.6)`
> <br><br>
>
> - **M1.3c) Maak een tabel met de vier berekende statistieken voor de 3 normaalverdelingen. Let goed op de notatie.**  <br><br>
>
> - **M1.3d) Welke van de statistieken veranderen en hoe?**

<!--Voor 2022: maak een instructie over het gebruik van de alpha optie om de histogrammen te laten zien als ze overlappen.-->

### Poisson
We gaan nu kijken wat het effect is van translatie en multiplicatie op een Poisson distributie $$dp(k)$$. De Poisson distributie krijg je door de volgende functie aan te roepen.

 			dp = ds.genereerDistributieDP(500)

Herhaal nu de vragen b-d voor de Poisson verdeling: 

> - **M1.3e) Maak nu een plot waar de drie histogrammen voor de Poisson verdeling te zien zijn. De originele, de translatie en de multiplicatie. Zorg dat de histogram goed leesbaar is en kijk hiervoor nog eens naar de richtlijnen.**  <br><br>
>
>
> - **M1.3f) Maak een tabel met de vier berekende statistieken voor de 3 Poisson verdelingen. Let goed op de notatie.**  <br><br>
>
>
> - **M1.3g) Welke van de statistieken veranderen en hoe?**

