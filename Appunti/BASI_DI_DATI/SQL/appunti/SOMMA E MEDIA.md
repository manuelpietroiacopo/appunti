La funzione **SUM** restiuisce la somma dei valori degli attributi scelti dei record che rispettano la condizione scelta:
es.

*Supponendo che Umberto Manzi sia il marito di Antonella Lepre, calcolare il reddito totale della famiglia Manzi.*

[[SELECT]] [[SOMMA E MEDIA|SUM]](Reddito) AS RedditoTotale
[[FROM]] Paziente
[[WHERE]] (Cognome = ‘Lepre’
	AND Nome = ‘Antonella’)
OR
	(Cognome = ‘Manzi’
	AND Nome = ‘Umberto’);

---
La funzione **AVG** ritorna la media dei valori degli attributi scelti:
es.
*Ritorna il reddito medio dei pazienti nati dopo il 1950*

SELECT AVG(Reddito) AS RedditoMedio
FROM Paziente
WHERE DataNascita > ‘1950-12-31’;

---
## MINIMO E MASSIMO

Le funzioni MIN() e MAX() ritornano il minimo e il massimo degli attributi su una tabella scelta, ma solo come valore. Può essere infatti più laborioso risalire al record al quale appartiene il valore.
