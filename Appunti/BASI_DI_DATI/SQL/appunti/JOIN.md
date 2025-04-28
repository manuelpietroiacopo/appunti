
Il [[JOIN]] è un operatore che permette di combinare i dati di più tabelle, ne esistono di vario tipo:

---
#### INNER JOIN:

Combina tutti i record di una prima tabella con i record di una seconda tabella, affiancando l'un l'altro tutti quelli che verificano una condizione data.

es.
*Indicare nome e cognome dei medici che hanno effettuato almeno una visita.*

MEDICO ⨝ (MEDICO.Matricola = VISITA.Medico) VISITA        

Sapendo che nella tabella VISITA ho la matricola del medico che visita il paziente, con la condizione di uguaglianza, vado ad ottenere una tabella che contiene gli attributi di MEDICO e di VISITA, con **Matricola** e **Medico** vicini, con lo stesso valore. Otterrò dunque le matricole dei medici che esistono sia in MEDICO (quindi che sono medici), e in VISITA, dunque che hanno effettuato almeno una visita.

**SINTASSI SQL:**
[[SELECT]] DISTINCT M.Nome, M.Cognome
FROM Visita V
INNER JOIN
Medico M ON V.Medico = M.Matricola;

---
#### JOIN NATURALE:

Combina i record della prima tabella aventi valori uguali su tutti gli attributi omonimi.

es.
*Indicare nome e cognome dei medici che hanno effettuato almeno una visita*

[[SELECT]] DISTINCT M.Nome, M.Cognome
[[FROM]] Visita V
NATURAL [[JOIN]] Medico M;


---
#### PRODOTTO CARTESIANO:

Restituisce tutte le possibili combinazioni tra record. 
es. 
[[SELECT]] COUNT(DISTINCT P.CodFiscale)
[[FROM]] Paziente P
CROSS JOIN
Medico M
[[WHERE]] P.Nome = M.Nome;


---

#### JOIN ESTERNI:

Il join esterno sinistro e destro operano, a seconda del verso scelto, come un join normale, accostando quindi tra loro i record che soddisfano la condizione imposta, ma non scartando poi i record non compresi (DIPENDE DAL JOIN SCELTO): ossia, nel caso del **left outer join** mantengo tutti i record della tabella di sinistra, e analogamente con il **right outer join**.

es.
*Indicare le visite effettuate da medici che non lavorano più presso la clinica*

[[SELECT]] V.*
[[FROM]] Visita V
==LEFT OUTER JOIN==                          mantengo tutti i record di Visita
Medico M ON V.Medico = M.Matricola
[[WHERE]] M.Matricola IS NULL

in questa query interessandomi i valori null, i join che normalmente non avverrebbero, mettono NULL all'altra tabella, andando così a capire quali medici non ci sono più. (IL [[WHERE]] permette di selezionare proprio quelle).

---
#### SELF JOIN:
Permette di combinare una tabella con i record di sé stessa che rispettano una condizione.

es.
*Indicare il codice fiscale dei pazienti che sono stati visitati più di una volta da uno stesso medico della clinica, nel mese corrente.*

[[SELECT]] DISTINCT V1.Paziente
[[FROM]] Visita V1
==INNER JOIN==
Visita V2 ON (
V2.Medico = V1.Medico
AND V2.Paziente = V1.Paziente
AND V2.Data <> V1.Data
)
[[WHERE]] [[DATE IN SQL|MONTH]](V1.Data) = MONTH(CURRENT_DATE)
AND YEAR(V1.Data) = YEAR(CURRENT_DATE)
AND MONTH(V2.Data) = MONTH(CURRENT_DATE)
AND YEAR(V2.Data) = YEAR(CURRENT_DATE);