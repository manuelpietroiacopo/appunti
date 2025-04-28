
Una CTE è una tabella dotata di identificatore che viene usata prima di una query per ottenere un risultato intermedio. (Crea una tabella con delle operazioni che vogliamo fare (ad esempio proiezioni, selezioni, ecc.))

L'identificatore può essere messo prima o dopo, attraverso l'operatore AS.

es.
*Indicare il numero di pazienti di Siena, mai visitati da ortopedici*
WITH ==ortopedici== AS                                CTE1
(
SELECT M.Matricola AS Medico
FROM Medico M
WHERE M.Specializzazione = ‘Ortopedia’
)

, ==paz_visitati_ortopedici== AS                      CTE2
(
SELECT V.Paziente AS CodFiscale
FROM Visita V NATURAL JOIN [[ortopedici]] O
)

SELECT COUNT( * )
FROM Paziente P
NATURAL LEFT OUTER JOIN
==paz_visitati_ortopedici== PVO                    CTE2
WHERE P.Citta = ‘Siena’
AND PVO.Matricola IS NULL;