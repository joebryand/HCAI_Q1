# HCAI_Q1 Anomalie detection
Deze git repository is gemaakt na aanleiding van een project voor Royal Haskoning om anomaliën te kunnen detecteren in de productie van peniciline. Hiervoor is een dataset aangeleverd met daarin alle sensorwaarde van 100 batches peniciline voor elke 12 minuten. Deze dataset en tussentijds opgeslagen datasets zijn te vinden door middel van de volgende link: https://hogeschoolutrecht-my.sharepoint.com/personal/pim_jansen_student_hu_nl/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fpim%5Fjansen%5Fstudent%5Fhu%5Fnl%2FDocuments%2Fdatasets%20prj%201

Omdat de datasets niet in deze repository staan kan de code alleen opnieuw gerunt worden als de datasets in dezelfde map zijn opgeslagen als de code. 

Bij de dataset horen twee papers van de onderzoekers die de dataset hebben gecreërd.[1] Zij beschrijven hierin hoe zij door middel van PCA de data hebben kunnen classificeren. Daarnaast hebben we ook nog andere papers gelezen om goede modellen te achterhalen voor ons probleem. Eén van deze papers is die van Andrey Kharitonov.[2] Hierin vergelijkt hij verschillende medellen om een soortgelijk probleem mee op te lossen. 

Alle drie de groeps genoten hebben één model uitgewerkt om deze later te kunnen vergelijken. Deze github repository bevat alle code van het clssificeren van de batches d.m.v. principal component analysis (PCA). De code is opgesplits in verschillende delen. voor elk deel is een jupyter notebook aangemaakt, en bevat alle nodige uitleg aan het begin en gedurende elk notebook. De volgorde van de code luid als volgd:

1. NOC_batch.ipynb
2. Dif_batches.ipynb
3. PCA_plotting.ipynb
4. PCA_classification.ipynb

Hiernaast zijn er ook nog een aantal stukken code geschreven om het proces beter te maken of voor extra inzichten:
- pooled_batches.ipynb : kan eventueel tussen stap 2 en 3 gebruikt worden om de dif_batches te poolen.
- gif_maker.py : maakt van de plots uit stap 3 een gif zodat deze beter bekeken kunnen worden.

Aan het einde van notebook stap 4:'PCA_classification', staat een conclusie uit het onderzoek en aanbevelingen voor de toekomst. Hieronder staat een kopie van deze aanbevelingen. Aangeraden wordt te kijken in het notebook voor uitleg bij de aanbevelingen en visuele ondersteuning.

## Conclusie
Wat we uit het onderzoek kunnen halen is dat:
- We alle 10 de fautieve batches kunnen onderscheiden, maar dat er hierdoor ook 42 van de goede batches als foutief gelabeld worden. 
- We 3 fautive batches kunnen onderscheiden, zonder een goede batch verkeerd te labelen. 

Dit zijn de twee extreme gevallen, maar er zit ook nog een interessante waarde tussen. Het kiezen van de beste grens zal per casus verschillen, voor deze casus zou ik willen stellen dat er gestreeft moet worden naar 0 false positives (batches labelen als fout, die eigenlijk goed waren). Hierom zou ik kiezen voor het extreme geval waarbij 3 fautieve batches kunnen worden onderscheiden en geen goede batches verkeerd gelabeld worden. op deze manier is het systeem namelijk altijd een verbetering op de oude situatie, waar niet een foutieve batch van te voren kon worden onderscheden. 

## Aanbevelingen
Het onderscheiden van drie batches is geen topprestatie, dus zal het model nog door ontwikkeld of geoptimaliseerd moeten worden, voor betere prestaties. Aanbevolen wordt de volgende dingen te doen:
- Het veranderen van de poolsize. Hier is nog niet veel onderzoek naar gedaan maar kan een grote invloed hebben op de uitkomsten. Er zijn drie manieren waarop gepoold kan worden.
    1. Bij het nemen van een poolsize van 1 oftewel niet te poolen kan goed gekeken worden naar een bepaald moment maar niet over een langer termijn.
    2. Bij het nemen van een grote poolsize, zoals alle timestamps tot een bepaald moment, kan goed gekeken worden naar de verandering over een langer termijn maar juist niet op één moment.
    3. Door het verschil te berekenen tussen de huidige timestamp en één of een aantal timestamps daarvoor kan de snelheid waarmee het systeem afwijkt bekeken worden.
Tijdens dit onderzoek is gekozen om een tussenweg hierin te nemen door te poolen in batches van 20. Er is echter een betere manier om beide methoden te combineren en dat is door, letterlijk beide methode te combineren. Op deze manier gedraagd het model zich als een PID-regelaar, een veel gebruikte methode in de control engineering om fisieke systemen mee te kunnen controleren. Hierbij is optie 1 de P-regelaar, optie 2 de I-regelaar en optie 3 de D-regelaar. Samen maken zij een PID regelaar.
- Het aantal principal components waar de PCA naar toe werkt kan worden aangepast. Uit mijn ervaring heeft het aanpassen van het aantal pc's geen aanzienlijke impact op het resultaat, maar het zou kunnen zorgen voor het laatste beetje optimalisatie die het model nodig heeft.
- Er zou beter gekeken kunnen worden naar hoe de NOC_batch te construeren. Hierbij kan gedacht worden aan:
    - Het aantal en welke batches dat gebruikt worden om de NOC-batch mee te maken.
    - Naast het gemiddelde van de batches, ook een sprijdingsfactor bepalen op iedere timestamp. Hierdoor kan per moment een andere waarde gegeven worden aan een bepaalde afwijking.

## Bibliografie

[1]I. T. Jolliffe and J. Cadima, “Principal component analysis: a review and recent developments,” Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences, vol. 374, no. 2065, p. 20150202, Apr. 2016, doi: 10.1098/rsta.2015.0202. [Online]. Available: https://royalsocietypublishing.org/doi/10.1098/rsta.2015.0202. [Accessed: Nov. 01, 2022]

[2]A. Kharitonov, A. Nahhas, M. Pohl, and K. Turowski, “Comparative analysis of machine learning models for anomaly detection in manufacturing,” Procedia Computer Science, vol. 200, pp. 1288–1297, Jan. 2022, doi: 10.1016/j.procs.2022.01.330. [Online]. Available: https://www.sciencedirect.com/science/article/pii/S1877050922003398. [Accessed: Nov. 01, 2022]