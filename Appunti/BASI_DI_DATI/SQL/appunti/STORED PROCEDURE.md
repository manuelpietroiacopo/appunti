Sono blocchi di codice memorizzati nel database che possono essere richiamati a richiesta. (Come delle funzioni).

Per delimitare un blocco di funzione si usa DELIMITER $ $
e poi CREATE PROCEDURE *nomeprocedura* (*eventuali variabili*).
Per iniziare il blocco di funzione, si mette un inizio, **BEGIN** e una volta terminato il blocco **END** e poi di nuovo DELIMITER; .
Per chiamare una funzione si usa la funzione CALL.




---

### VALORI IN INGRESSO E IN USCITA

Di default i valori sono in ingresso:
SE dichiarati **IN** possono essere letti ma non modificati,
mentre se passati come **OUT** possono essere modificati.
(E' parallelo al passaggio per riferimento e valore in C++: IN è come passare il valore, mentre OUT  è come passare il riferimento, con risultato l'effettiva modifica nel database).

---

### ISTRUZIONI CONDIZIONALI

IF e CASE:
si possono usare per modificare il flusso di esecuzione in base al risultato dell'istruzione:

es. 
Scrivere una stored procedure che riceva come parametro un intero t e una specializzazione s e restituisca in uscita true se il numero di visite della specializzazione s nel mese in corso è superiore a t, false se è inferiore, e NULL se è uguale.

![[IMG-20250516102828148.png]]