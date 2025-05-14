Posso dividere il lavoro delle basi di dati su più calcolatori: aumentando il numero di calcolatori aumenta l'efficienza, ma questo fino ad un certo numero di calcolatori, raggiunto un numero massimo l'efficienza non migliora più.


##### TRANSAZIONE: 
Una transazione è una sequenza composta da operazioni elementari (indivisibili) di lettura e scrittura e da operazioni di transazione.
Le operazioni di transazioni sono: 
- begin $b(t)$: inizio di transazione
- commit $c(t)$: terminazione con successo
- abort $a(t)$: indica la terminazione a causa di un guasto, non va a buon fine
Una transazione ha le seguenti proprietà:
- atomicità: solo le transazioni che terminano con successo (committed) modificano la base di dati; O TUTTO O NIENTE

- isolamento: quando una transazione e eseguita contemporaneamente ad altre, lo stato finale della base di dati deve essere lo stesso che otterrebbe se la transazione fosse eseguita da sola E' garantito dal gestore della concorrenza.

- durabilità: gli effetti delle transazioni terminate con successo devono sopravvivere ai guasti.


Tipicamente le operazioni di transazione non sono esplicitamente indicate dal programmatore; begin e commit sono aggiunte automaticamente dal DBMS, mentre abort e generato automaticamente dal gestore della concorrenza.


$T=p_1...p_n$


es. 
$T_1 = r_1(x)r_1(x)$
$T_2 = r_2(x)w_2(x)$

il DBMS fa un'operazione alla volta:
$T1$       $T2$
$b_1$         $b_2(x)$
$r_1(x)$    $r_2(x)$
       $x<-(x-1)$


---

##### NOTAZIONI:

Base di dati D
Oggetti in D x, y, z
Transazioni T1, T2, ..., T
Lettura di x: r(x) 
Scrittura di x: w(x)
Op. Trans T: B(T), C(T), A(T)

---
### SCHEDULE

$T={T_1,..,T_n}$
$S$ su $T$ è una sequenza di operazioni tale che:
- tutte le operazioni di $S$ sono quelle di $T_1,...,T_n$
- $S$ preserva l'ordinamento tra le operazioni di ogni transazione



##### SCHEDULE SERIALE: 
Sia $T = {T_1, . . . , T_n}$ un insieme di transazioni. Uno schedule S su T e uno schedule seriale se, per ogni coppia di transazioni $T_i , T_j ∈ T$ , tutte le operazioni di Ti sono eseguite prima di qualsiasi operazione di$T_j$, o viceversa.
##### *VIEW* EQUIVALENZA TRA SCHEDULE


---

#### CONFLICT SERIALIZZABILITA'
Uno schedule S è conflict-serializzabile se e solo se il suo grafo dei conflitti G(S) è aciclico.

---

