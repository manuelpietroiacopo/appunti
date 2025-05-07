ELIMINARE LE ANOMALIE con le forme normali


#### FORMA NORMALE DI BOYCE-CODD

![c](immagini/Pasted%20image%2020250507095803.png)

**TEOREMA:**

Uno schema R(T, F) è in BCDNF se e solo se ogni dipendenza funzionale non banale X->Y app. F, X è una superchiave.

**COROLLARIO:**
Uno schema R(T, F) con F copertura minimale è in BCNF se e solo se per ogni dipendenza funzionale elementare X->A app. F, X è una superchiave.


Quindi, per capire se è in forma normale secondo [[#FORMA NORMALE DI BOYCE-CODD|BOYCE CODD]], dobbiamo controllare che ogni elemento nelle dipendenze funzionali sia superchiave.

es.
R(PDOCS) con PD chiave
F {PD->OCS, CDO->PS, SDO->PC, CD->S}

Per controllare, calcolo le chiusure sugli attributi rispetto ad F:
PD+=PDOCS chiave
CDO+=CDOPS superchiave (chiave candidata)
SDO+=SDOPC superchiave (chiave candidata)
CD+=CDS non superchiave
CD viola la BCNF!

Lo schema R non è in BCNF.


---
#### DECOMPOSIZIONE DI SCHEMI

Dato uno schema R(T), l'insieme p={R1(T1),.., Rk(Tk)} è una decomposizione di R se e solo se UiTi=T (LE TUTTI GLI SCHEMI RIUNITI RIDANNO LO SCHEMA ORIGINALE).
ATTENZIONE PERO' A **PRESERVARE LE DIPENDENZE E I DATI: ALTRIMENTI NON SI MANTIENE L'EQUIVALENZA TRA SCHEMA ORIGINARIO E LA DECOMPOSIZIONE**

![cas](immagini/Pasted%20image%2020250507153616.png)
