Una [[SUBQUERY]] è un'alternativa al [[JOIN]], che permette di risolvere tutte le query senza utilizzarlo. E' una [[QUERY]] dentro un'altra query. E' una sorta di "filtro".
Si utilizza l'operatore IN: con gli operatori [[SELECT]], [[FROM]], [[WHERE]] decido cosa prendere (filtro) e poi con IN prendo il risultato dell'outer query che è presente anche nella subquery, ottenendo così vari [[RECORD]] che soddisfano l'interrogazione. 

---
### **UNCORRELATED SUBQUERY**

Si incapsulano nel [[WHERE]] per ottenere risultati usati dalla outer query per determinare il result set finale.

###### **RISULTATO:** Un record fa parte del risultato se i valori che assume su un sottoinsieme di attributi si trova anche in (almeno) un record del result set della subquery.

es.
[[SELECT]] M.Nome, M.Cognome, M.Parcella
[[FROM]] Medico M                                                     OUTER QUERY
[[WHERE]] M.Specializzazione = ‘Ortopedia'
AND M.Matricola ==IN==
(

SELECT V.Medico                                                    
FROM Visita V                                          QUESTA E' LA [[SUBQUERY]]
WHERE YEAR(V.Data) = 2013                                 

);

Si distinguono le [[SUBQUERY SCALARI]] e le altre.

Si può anche utilizzare il ==NOT IN==, il quale permette di trovare i record che non soddisfano la condizione, è come la sottrazione.

Data una query con [[SUBQUERY]] è sempre possibile passare alla versione basata su join, e viceversa.

**Si possono annidare INFINITE [[SUBQUERY]].**


---
### **CORRELATED SUBQUERY**

In una [[#**CORRELATED SUBQUERY**|CORRELATED SUBQUERY]] dipende da ciascuna tupla della outer query.

Una [[#**CORRELATED SUBQUERY**|CORRELATED SUBQUERY]] è eseguita **PER OGNI** record della query esterna e il suo risultato ne dipende.


##### Costrutto **EXISTS**

Si utilizza nelle [[SUBQUERY]], e permette **di verificare che il result set di una subquery contenga almeno un record**.


