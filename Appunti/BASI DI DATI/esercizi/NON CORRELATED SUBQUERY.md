
*Indicare numero degli otorini aventi **parcella più alta della media** delle parcelle dei medici della loro specializzazione.*

SELECT COUNT ( * )
FROM Medico M1              [^1]
WHERE M1.Specializzazione = 'Otorinolaingoiatria'
	AND M1.Parcella > (
				SELECT AVG(M2.Parcella)                  [^1]
				FROM Medico M2                                                 **SUBQUERY**						WHERE M2.Specializzazione = ‘Otorinolaringoiatria’
						);



[^1]:  seleziona la media di tutte parcelle dei medici ove specializzazione è otorinolaingoiatria

---
*Indicare qual è il reddito massimo, e il nome e cognome di chi lo detiene.*


SELECT Reddito, Nome, Cognome
FROM Paziente
WHERE Reddito = (
			SELECT MAX(Reddito)           **SUBQUERY**
			FROM Paziente
);

