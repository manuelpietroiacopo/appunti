Il conteggio avviene attraverso la funzione **COUNT( * )** 

Il ritorno di questa funzione è un unico record con un attributo contentente un intero che indica il conto totale dei record che verificano la condizione desiderata:
es.
*Indicare il numero di visite effettuate in data 1° Marzo 2013*

[[SELECT]] COUNT( * ) AS VisitePrimoMarzo                                ridenominazione
[[FROM]] Visita
[[WHERE]] Data = ‘2013-03-01’;

il ritorno è           ![Pasted image 20250419163921](../../../immagini/Pasted%20image%2020250419163921.png)


#### COME OPERA?

Prima di tutto fa la selezione dei record scelti, e poi "comprime" tutto e restiuisce un unico record con l'intero.


#### COUNT DISTINCT:
Possono sorgere problemi nel momento in cui ci possono essere duplicati e ci interessa solo uno dei vari record: viene utile allora utilizzare COUNT (DISTINCT NomeAttributo), così da non avere duplicati di quel attributo.

