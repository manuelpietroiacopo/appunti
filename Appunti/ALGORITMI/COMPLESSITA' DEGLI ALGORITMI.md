La complessità e il costo degli algoritmi si valuta in base:
- alla dimensione dei dati forniti
- al tempo di esecuzione e allo spazio occupato in memoria

###### Profiling:
tecnica di analisi che permette di misurare le prestazioni di un programma in base a degli indici come l'utilizzo di memoria, il numero di chiamate di funzione e altri: va tenuto a mente che questa misurazione dipende dai fattori ambientali, quali calcolatore, linguaggio di programmazione e simili, ed è dunque inutile comparare due programmi in linguaggi diversi su calcolatori diversi.


###### Misurazione complessità:
è fondamentale poichè permette di prescindere le prestazioni del calcolatore e del linguaggio utilizzato.
Per ogni algoritmo si misura il tempo di esecuzione, che a seconda delle istanze potrebbe variare, e vanno valutati quindi: 
- il caso ==peggiore==
- il caso ==migliore==
- il caso ==medio==
es.
![cia](Pasted%20image%2020250429094556.png)

*L'algoritmo in questione ritorna il massimo di un vettore: 
il costo è così calcolato: 
- l'assegnamento m = a[0] costa 1 poichè costante;
- l'assegnamento int i = 1 costa 1;
- i < n costa n;
- i++ costa 1 x (n-1) (non arriverà a n ma n-1, dopo uscirà);
- m < a[i] costa (n-1) (verrà valutato NEL CASO PEGGIORE n-1 volte);
- m = a[i] costa NEL CASO PEGGIORE (n-1), poichè potrebbe aggiornarsi sempre;

Il costo totale è dunque:
1+1+n+n-1+n-1+n-1=> 4n (i costi costanti non interessano per cifre piccole, BISOGNA CONTROLLARE IL COMPORTAMENTO ASINTOTICO).

---
## LIMITI 

##### LIMITE ASINTOTICO SUPERIORE: notazione O grande

**f(n) è di ordine O( g(n) ) se esistono intero n0 e c>0 t.c. per ogni n>=n0: f (n) < c x g(n)**

ovvero: se per un intero definito n0, f(n) sta "sotto" a c x g(n):
es.
![ci](Pasted%20image%2020250429102626.png)


100 n sta "sotto" a 2n^2 dopo 50 e se c=50: dunque, valutando due programmi Q e P, non sappiamo come si comportano fino a n0=1 o n0=50, da lì sappiamo che Q conviene per c=50  (infatti 50 x P(n) = 100 n^2 che costa più di 100 n)

![graph](Pasted%20image%2020250429105536.png)
es. 
-  f(n)=100n
- g(n)=5n

f(n) è O(g(n)): basta scegliere c>20 e per n0=1, ed è verificato.
###### A COSA SERVE FARE QUESTE VALUTAZIONI ASINOTICHE?
Valutando le funzioni e il loro comportamento asintotico, sappiamo che ad un certo punto una converrà rispetto ad un'altra, così da capire quale scegliere per risparmiare tempo e spazio: ATTENZIONE! è comunque una valutazione approssimativa.

---

#### INSIEME DI REGOLE

![[Pasted image 20250429105700.png]]

![[Pasted image 20250429105734.png]]


---
![[Pasted image 20250429105835.png]]

*non si possono valutare in maniera asintotica*

---
![[Pasted image 20250429105902.png]]

*Schema per comprendere i comportamenti delle funzioni*

**TEOREMA:**
**Una qualsiasi funzione polinomiale ha minore complessità di una qualsiasi funzione esponenziale.**



##### LIMITE ASINTOTICO INFERIORE: notazione Ω

**f(n) è Ω ( g(n) ) se esistono un intero n0 e un c>0 t.c. per ogni n>=n0  : f(n)>=c x g(n)** 

Quindi se dato un intero e una costante, f(n) sta "sopra" a g(n) per una data costante c e dopo un intero n0:

es.
2n^2 +3n +2 è Ω (n) per n0=1 e c=1

(*nel caso di polinomi si considera solo il grado massimo, quindi 2n^2, che in questo caso sta "sopra" a n per tutte le c e n0 >=1*)

es.
n^2 è Ω (2n^2) per n0=1 e c=1/2

In questo caso sono uguali, infatti 2*(1/2)n^2=n^2, e n^2  = n^2 banalmente.




![[Pasted image 20250429140024.png]]

---


#### LIMITE ASINTOTICO STRETTO: notazione Θ

**f(n) è Θ (g(n)) se f(n) è O g(n) e f(n) è Ω (g(n))**

In breve, f(n) e g(n) hanno stesso ordine di complessità:
è vero quindi se esistono n0 e c1, c2 >0 t.c.. per ogni n>=n0 c1 g(n) <= f(n) <= c2 g(n).

![fsa](imalg/Pasted%20image%2020250502103729.png)


---

### COMPLESSITA' PROGRAMMI ITERATIVI

