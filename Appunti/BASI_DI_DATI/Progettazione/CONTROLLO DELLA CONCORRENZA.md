Posso dividere il lavoro delle basi di dati su più calcolatori: aumentando il numero di calcolatori aumenta l'efficienza, ma questo fino ad un certo numero di calcolatori, raggiunto un numero massimo l'efficienza non migliora più.


#### TRANSAZIONE: 
==Una transazione è una sequenza composta da operazioni elementari (indivisibili) di lettura e scrittura e da operazioni di transazione.==
Le operazioni di transazioni sono: 
- begin $b(t)$: inizio di transazione
- commit $c(t)$: terminazione con successo
- abort $a(t)$: indica la terminazione a causa di un guasto, non va a buon fine
Una transazione ha le seguenti proprietà:
- atomicità: solo le transazioni che terminano con successo (committed) modificano la base di dati; O TUTTO O NIENTE

- **isolamento**: quando una transazione e eseguita contemporaneamente ad altre, lo stato finale della base di dati deve essere lo stesso che otterrebbe se la transazione fosse eseguita da sola E' garantito dal gestore della concorrenza.

- durabilità: gli effetti delle transazioni terminate con successo devono sopravvivere ai guasti.

Una generica transazione, con omissione di $begin$ e $abort$ (aggiunte automaticamente dal DBMS e $abort$ generato automaticamente dal gestore della concorrenza), è rappresentata così:
#### $$T=p_1...p_n$$
Dove $p_i$ è un'operazione elementare, ovvero $p_i$ $\in$ {$r(x), w(x)$} per un qualche oggetto $x \in D$
 
###### **RIASSUMENDO, PER SEMPLIFICARE:**

- la base di dati è un insieme prefissato di oggetti indipendenti che possono essere solo letti o modificati;
- una transazione legge o modifica un dato oggetto al più una volta;
- tutte le transazioni terminano con successo;

---

### **GESTIONE DELLE TRANSAZIONI**

Il gestore della concorrenza si assicura che le transazioni eseguite siano gestite in maniera corretta e sicura, rispettano le proprietà [[ACID]].

Spesso e volentieri le transazioni vengono effettuate in parallelo, quindi le operazioni di lettura e scrittura simultaneamente anche su dati condivisi, ciò porta dei vantaggi:
- massimizzare le prestazioni del sistema;
- ridurre tempi di attesa degli utenti;
- bilanciare carichi di lavoro;
- gestire grandi volumi di dati e richieste simultanee;

Il gestore, senza un oppportuno meccanisco di controllo della concorrenza, ricevendo richieste simultanee e dovendo eseguire operazioni in parallelo, questo può generare *anomalie*, ovvero problemi tra operazioni di diverse transizioni.

---
### ECCO ALCUNI ESEMPI DI PROBLEMI

#### PERDITA DI AGGIORNAMENTO
es. 
$T_1 = r_1(x)w_1(x)$
$T_2 = r_2(x)w_2(x)$
$x$ vale 2 all'inizio, e a regola il risultato finale dovrebbe essere 4.

Nota come $T_1,T_2$ scrivono sullo stesso oggetto.

Il DBMS fa un'operazione alla volta:
$T1$              $T2$
$b_1$      
$r_1(x)$ 
$x$<-$(x+1)$
		$b_2(x)$
		$r_2(x)$
        $x$<-$(x+1)$
$w_1(x)$
$c_1$
         $w_2(x)$
          $c_2$

Il problema qui è che, $T_1$ e $T_2$ svolgono in parallello ma riscrivono sullo stesso oggetto, dunque: $T_1$ aggiorna $x$ di 1, ma non lo scrive ancora sul DB, nel frattempo parte anche $T_2$ e aggiorna anch'esso $x$, senza però contare l'aggiornamento di $T_1$, PERCHE' NON E' STATO SCRITTO ANCORA; alla fine, $T_1$ scrive il suo valore $x+1$, nel nostro caso 2+1=3, e $T_2$ sovrascrive 3 con 3, non "combinando" le due transazioni.


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

