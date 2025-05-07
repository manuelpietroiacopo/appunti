*CONSIDERATA OGNI SPECIALIZZAZIONE, INDICARNE NOME E L'INCASSO TOTALE DEGLI ULTIMI DUE ANNI.*

con MEDICO (**Matricola**, Cog., Nome, Spec., Parcella, Città)


SELECT M.Specializzazione, SUM(Parcella) AS IncassoBiennale

FROM Medico M1  
INNER JOIN     on V.Matricola=M1.Medico  
VISITA V 

WHERE (YEAR(V.Data)>=(YEAR (CURDATE())-1)

GROUP BY M.Specializzazione



***INDICARE NOME E COGNOME DEI PAZIENTI CHE SONO STATI VISITATI ALMENO DUE VOLTE DALLA DOTTORESSA GIALLI RITA.***


SELECT P.Nome,  P.Cognome

FROM Visita V  
INNER JOIN

Medico M on V.Medico = M.Matricola

INNER JOIN 

Paziente P on V.Paziente = P.CodFiscale

WHERE M.Cognome = “Giallini” AND M.Nome = “Rita”

GROUP BY V.Paziente, P.Cognome, P.Nome

HAVING COUNT ( * ) >=2


---

SI CONSIDERI LA REALTA':
PAZIENTE (**CF**, Cognome, Nome, Sesso, DataNascita, Città, Reddito)
MEDICO (**Matricola**, Cognome, Nome, Spec., Parcella, Città)
VISITA (**Medico, Paziente, Data**, Mutuata)

*Scrivere query che, per ogni spec., ritorna numero medici che hanno visitato, dopo la prima volta, per una volta all'anno per almeno la metà degli anni successivi.*

RAGIONAMENTO:
	`trovo l'anno k in cui si son incontrati la prima volta, conto gli anni da k a anno corrente in cui c'è una visita, seleziono poi i medici per cui numero di visite > (annocorrente-k)/2, seleziono poi le specializzazioni`


[[COMMON TABLE EXPRESSION (CTE)|WITH]] prima_visita as(
[^1]SELECT V.Medico, V.Paziente, MIN (YEAR (V.Data)) AS PrimaVisita
FROM Visita V
GROUP BY V.Medico, V.Paziente
),
GROUP BY Specializzazione


[^1]: con questo blocco seleziono la prima visita di quel dottore a quel paziente
