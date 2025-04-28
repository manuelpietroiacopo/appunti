Le date in SQL vengono gestite in maniera particolare:

![Pasted image 20250419160158.png](immagini/Pasted%20image%2020250419160158.png)

La funzione DATE_FORMAT permette di manipolare l'impostazione della data, così da poter ottenere la data secondo il formato desiderato, di seguito l'esempio:
*Indicare matricola e data di laurea (nel formato ‘dd|mm|yyyy, nome_giorno’) [...]*
SELECT Matricola, DATE_FORMAT(==DataLaurea==, ‘%d|%m|%Y, %W’)

oppure:
*Indicare la matricola degli studenti che si sono laureati di mercoledì*

[[SELECT]] Matricola
[[FROM]] Studente
[[WHERE]] [[DATE IN SQL|DATE_FORMAT]](DataLaurea, ‘%w’) = 3;               mercoledì è il terzo giorno

---
##### CONFRONTO TRA DATE
Per confrontare le date tra di loro, c'è bisogno di utilizzare le funzioni **DAY, MONTH, YEAR**
che rispettivamente ritornano degli interi in base al giorno, mese o anno.
es.
*selezionare gli studenti che si sono laureati nel 2005*
SELECT Matricola
FROM Studenti 
WHERE DataLaurea IS NOT NULL AND YEAR(DataLaurea)=2005           (CONTROLLO CHE SIA                                                                                                                          EFFETTIVAMENTE LAUREATO                                                                                                                      E CHE LA DATA SIA 2005)                                                   

---
##### DATA ODIERNA
Per conoscere la data odierna, si utilizza la funzione **CURRENT_DATE**() o **CURDATE()** che ritorna la data odierna secondo il formato standard 'yyyy-mm-dd'

---
##### CALCOLARE UN LASSO DI TEMPO
Per calcolare un lasso di tempo non si può calcolare la differenza tra interi: bisogna infatti utilizzare la funzione **DATEDIFF(datauno, datadue)**: questo ritorna la differenza di giorni tra le due date. Si può anche passare una data come data e non intero: 'yyyy-mm-dd'.


###### DATE_SUB() E DATE_ADD():
permettono di sottrarre o aggiungere intervalli di tempo, espressi con la keyword **INTERVAL** a date:

DATE_SUB(DataVisita, INTERVAL 4 MONTHS) aggiunge 4 mesi alla DataVisita

VA PRIMA IL NUMERO E POI ANNO, MESE O GIORNO


es.
*Indicare la matricola e il mese di iscrizione degli studenti che si sono laureati dopo cinque anni esatti dal giorno dell’iscrizione.*

[[SELECT]] Matricola, MONTH(DataIscrizione)
[[FROM]] Studente
[[WHERE]] DataLaurea = [[DATE_ADD]](DataIscrizione, INTERVAL 5 YEAR);


