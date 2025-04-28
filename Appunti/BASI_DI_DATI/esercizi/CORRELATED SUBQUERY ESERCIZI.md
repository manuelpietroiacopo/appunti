
###### *Indicare la matricola dei medici che hanno visitato per la prima volta almeno un paziente nel mese di Ottobre 2013.*

SELECT DISTINCT V1.Medico
FROM Visita V1
WHERE YEAR(V1.Data) = 2013
AND MONTH(V1.Data) = 10
AND V1.Paziente NOT IN ( 
				SELECT V2.Paziente
				FROM Visita V2
				WHERE V2.Medico = V1.Medico
				AND V2.Data < V1.Data 
				    );
	Fa in modo che selezioni record che non sono nel risultato dell'interrogazione che restituisce medico dei pazienti dove una data visita è antecedente ad un'altra, e quindi non esistono date prima di ottobre 2013.


---


###### *(Una visita di controllo è una visita in cui un medico visita un paziente già visitato precedentemente almeno una volta). Indicare medico, paziente e data delle visite di controllo del mese di Gennaio 2016.*

[[SELECT]] V1.Medico, V1.Paziente, V1.Data
[[FROM]] Visita V1
[[WHERE]] MONTH(V1.Data) = 1
AND YEAR(V1.Data) = 2016
AND [[EXISTS]]
(
[[SELECT]] *
[[FROM]] Visita V2
[[WHERE]] V2.Medico = V1.Medico
AND V2.Paziente = V1.Paziente
AND V2.Data < V1.Data
);
