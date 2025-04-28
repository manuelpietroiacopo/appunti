Il raggruppamento si effettua con il predicato [[GROUP BY]], e permette di dividere la tabella in base all'attributo scelto, che per ogni gruppo rimarrà costante. Ad esempio un [[database]] contenente i dati relativi a dei medici, questi possono essere divisi per specializzazione (la quale sarà un attributo). 
E' utile per utilizzare operatori di raggruppamento (come [[AVG]],  [[MIN]], [[MAX]] e altri) su una sola parte di tabella, senza perdere quelli che sarebbero gli "scarti". 
==**Quando si usa il raggruppamento OGNI gruppo genera UN SOLO record nel result set**
==es.
*Per ogni specializzazione, calcolare la parcella media dei suoi medici*
[[SELECT]] Specializzazione, [[AVG]](Parcella) AS ParcellaMedia
[[FROM]] Medico
[[GROUP BY]] Specializzazione;                                       divide per specializzazione (appena trova un                                                                                        valore diverso divide la tabella)

---
##### DIFFERENZA TRA **HAVING** E **WHERE**


| HAVING                        | WHERE                           |
| ----------------------------- | ------------------------------- |
| Agisce dopo il raggruppamento | Agisce prima del raggruppamento |

Nelle interrogazioni con raggruppamento, le condizioni esprimibili con operatori di aggregazione
devono sempre essere argomento della clausola having.
es.

*Indicare le specializzazioni con più di due medici di Pisa.*

[[SELECT]] Specializzazione
[[FROM]] Medico
[[WHERE]] Citta = ‘Pisa’                                        LA CONDIZIONE WHERE VIENE APPLICATA PRIMA                                                                               DEL GROUP BY, DUNQUE SI USA WHERE
[[GROUP BY]] Specializzazione                                               
[[#DIFFERENZA TRA **HAVING** E **WHERE**|HAVING]] [[CONTEGGIO IN SQL|COUNT]] ( * ) > 2;                                L'OPERATORE VIENE APPLICATO AI GRUPPI GIA'                                                                                  DIVISI, QUINDI UTILIZZO HAVING