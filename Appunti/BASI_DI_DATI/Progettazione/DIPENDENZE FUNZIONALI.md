
Durante la fase di progettazione e la traduzione verso il modello logico, l'obiettivo principale è quello di valutare l'opzione migliore degli schemi di relazione, in termini di qualità.
###### Approccio seguito:
Top-down: prima si raggruppano degli attributi che hanno senso tra di loro come nel mondo reale, ed eventualmente poi questi si decompongono successivamente.

E' importante nel frattempo anche non perdere i dati e i concetti espressi prima della traduzione e contemporaneamente minimizzare le ridondanze, ovvero la memorizzazione ripetuta della stessa informazione, per evitare di dover effettuare più aggiornamenti eventuali per mantenere la costanza dello stesso dato (esempio un dato che accomuna più tuple che viene poi aggiornato, il quale andrebbe aggiornato per tutte le tuple che contengono lo stesso dato e sprecando tempo e memoria).


#### COME FARE QUINDI?

Uno schema di relazione deve essere semplice alla vista, va spiegato facilmente, non bisogna ingarbugliarsi con attributi provienenti da tipi di entità e relazioni diverse così da complicarne la comprensione, altrimenti si andrà incontro ad un'ambiguità semantica.

Uno schema va poi progettato in modo che **non si possano presentare anomalie di inserimento, cancellazione o modifica**.

Se queste possono verificarsi è bene rilevarle e assicurarsi che le basi di dati operino in maniera corretta.

###### EVITARE FREQUENTI VALORI NULL

Bisogna evitare di mettere una relazione i cui attributi contengono tanti valori NULL, o perlomeno di limitarne la presenza in casi eccezionali.


![Ciao](immagini/Pasted%20image%2020250424110915.png)
Il problema esiste nel momento in cui l'IVA cambia poichè il TotDaPagare va cambiato per ogni record; a CodProd va attribuita la giusta percentuale di IVA. 
Per evitare problemi conviene togliere TotDaPagare dalla tabella Fattura.

---

![hh](immagini/Pasted%20image%2020250424110955.png)

Per evitare ridondanze e inconsistenze (NumAb deve essere uguale per tutti i cittadini con NomeCittaRes uguale), si può sistemare dividendo Anagrafe in due relazioni separate:
- Persona (CF, NomePersona, ViaRes, NomeCittaRes)
- ListaComuni (NomeCitta, NumAb)
con vincolo di integrità NomeCittaRes su NomeCitta

---

## **DIPENDENZA FUNZIONALE**

Esprime legame semantico tra due gruppi di attributi di uno schema di relazione R.
Vale per tutte le istanze della relazione.
Acronimo FD (functional dipendency)

Una dipendenza funzionale è una proprietà, non di uno stato particolare (ergo vale sempre).

Non si può dedurre da uno stato valido, ma bisogna conoscere la semantica degli attributi di R a priori.

---
## FORME NORMALI

Una forma normale è una **proprietà** che garantisce la 'qualità', ovvero l'==assenza== di difetti, ovvero:

- Ridondanza (duplicazione di informazioni)
- Comportamenti poco desiderabili

(Le forme normali sono di solito definite sul modello relazionale, ma hanno senso in altri contesti, ad esempio il modello E-R)

---
#### NORMALIZZAZIONE

Passaggio da schema non normalizzato in schema normalizzato, quindi non presenta i [[#FORME NORMALI|problemi]] sovraelencati.
La normalizzazione va utilizzata come tecnica di verifica dei risultati della progettazione di una base di dati.
Non costituisce una metodologia di progettazione, quindi non bisogna partire da questo, ma va creato prima lo schema e poi normalizzato.

---
es. Schema con anomalie 

![hh](immagini/Pasted%20image%2020250424112614.png)

Lo stipendio è ridondante, è presente in ogni tupla, e nel caso in cui questo vari, bisogna cambiarlo per ogni tupla.
Se uno degli impiegati annulla la partecipazione a tutti i progetti, va cancellato (**anomalia di cancellazione**)
Essendo progetto chiave, un impiegato che non ne ha non viene inserito (es. un nuovo impiegato).
(**anomalia di inserimento**)

**QUESTO ACCADE PERCHE' ABBIAMO CREATO UN'UNICA TABELLA CON INFORMAZIONI DIVERSE E SCONNESSE DIRETTAMENTE TRA LORO: abbiamo fatto un brodo!**

(Una soluzione potrebbe essere: creare la tabella Impiegato, con attributi: Cognome, Funzione e Stipendio,  una tabella Partecipazione: Progetto, Impiegato, Bilancio; con vincolo d'integrità tra Cognome e Impiegato).



---
## **DEFINIZIONE DI FD**

![hh](immagini/Pasted%20image%2020250424112942.png)






![hh](immagini/Pasted%20image%2020250424114850.png)


---


| ![hh](immagini/Pasted%20image%2020250424115516.png) | ![hh](immagini/Pasted%20image%2020250424115705.png) |
| --------------------------------------------------- | --------------------------------------------------- |

Impiegato->Stipendio **RIPETIZIONI**
Progetto->Bilancio **RIPETIZIONI**
Impiegato, Progetto->Funzione **NO RIPETIZIONI (PERCHE' CHIAVE)**

LE [[#**DIPENDENZA FUNZIONALE**|FD]] sono utilizzate per verificare eventuali anomalie e per normalizzare uno schema.

---
### **IMPLICAZIONE**

Sia F un insieme di FD su R(Z) e sia X->Y:
- Si dice che F implica (logicamente) X->Y (CON SIMBOLO F|= X->Y) se, per ogni possibile istanza r di R che verifica tutte le dipendenze funzionali in F, risulta verificata anche la dipendenza X->Y
- Si dice che X->Y è implicata (logicamente) da F.


###### PROBLEMA
La definizione di implicazione non è direttamente utilizzabile nella pratica 
• Essa prevede una quantificazione universale sulle istanze della base di dati (“per ogni istanza …”) 
• Non abbiamo un algoritmo per calcolare tutte le dipendenze funzionali implicate da un insieme

---
#### REGOLE DI ARMSTRONG
• **Armstrong** (1974) ha fornito delle ==regole di inferenza== che permettono di derivare costruttivamente tutte le dipendenze funzionali che sono implicate da un dato insieme iniziale F:

RIFLESSIVITA': se Y contenuto in X, allora X->Y

ADDITIVITA': se X->Y allora XZ->YZ per ogni Z

TRANSITIVITA': se X->Y e Y->Z, allora X->Z	

---
### DERIVAZIONE (|-)
Dati: 
• un insieme di regole di inferenza RI, 
• un insieme di dipendenze funzionali e 
• una dipendenza funzionale f
• una derivazione di f da F secondo RI è una sequenza finita f1, f2,..., fm, dove

- fm=f
-  ogni fi è elemento di F oppure è ottenuta dalle altre dipendenze utilizzando la regola dell'interferenza RI

![hh](immagini/Pasted%20image%2020250424122008.png)



![hh](immagini/Pasted%20image%2020250424122026.png)

---
### DIMOSTRAZIONI

| ![hh](immagini/Pasted%20image%2020250424190257.png) | ![hh](immagini/Pasted%20image%2020250424190305.png) |     |
| --------------------------------------------------- | --------------------------------------------------- | --- |
| ![hh](immagini/Pasted%20image%2020250424190313.png) | ![hh](immagini/Pasted%20image%2020250424190328.png) |     |

---
### CORRETTEZZA E COMPLETEZZA


![hh](immagini/Pasted%20image%2020250424190947.png)


Corretto: se dalla deduzione/implicazione funzionale si ricava la dipendenza logica.
es. CF->Matricola (ogni codice fiscale identifica una matricola)
controes. Città->CAP (una città può avere più CAP, e perciò non dipende necessariamente, in sostanza Città non è chiave).

Completo: se dalla dipendenza logica si ottiene sempre la deduzione funzionale.

---

### CHIUSURA DEGLI ATTRIBUTI

![hh](immagini/Pasted%20image%2020250424190438.png)


Appartengono ad X tutti gli elementi che possono essere derivati da X, ovvero che ne dipendono.

---

## TEOREMA DELLA CHIUSURA DEGLI ATTRIBUTI


![hh](immagini/Pasted%20image%2020250424190519.png)

Ovvero: se da F deriva la dipendenza tra X e Y, allora Y fa parte dell'insieme X+, ovvero tutti gli elementi che possono essere determinati a partire da X, ovvero che dipendono da questo.
In questo caso Y dipende da X.

---
## TEOREMA

**LE REGOLE DI INFERENZA DI ARMSTRONG SONO CORRETTE E COMPLETE**, ma non sono le uniche!!!!!
IMPORTANTE
![hh](immagini/Pasted%20image%2020250424192711.png)

___

![hh](immagini/Pasted%20image%2020250424192746.png)

---
![hh](immagini/Pasted%20image%2020250424131800.png)

In sostanza, nello schema di FD, una chiave è tale se non è possibile ricavarla da altro se non sè stessa.
(Banalmente se sta solo a sinistra della freccia)

Per determinare una chiave parto dagli elementi che non compaiono mai a destra e calcolo la chiusura.
Gli elementi che compaiono solo a destra NON saranno MAI parte della chiave.

----
![hh](immagini/Pasted%20image%2020250424192247.png)


Dato lo schema R e le dipendenze funzionali F, calcolo F+, ovvero la chiusura di tutte le dipendenze funzionali implicate da F: 
in breve è l'insieme delle dipedenze derivabili da F, l'insieme di dipendenze di partenza.
Può essere molto costoso nei casi reali: il costo è esponenziale per numero di attributi, e in casi reali costa molto.
E' più pratico e utile infatti conoscere X+, ovvero l'insieme di attributi ottenibili dall'attributo di partenza X: per ottenere l'insieme che risponde alla domanda:"Quali attributi posso ottenere a partire da X?", è necessario applicare le leggi di Armstrong sull'insieme di dipendenze F sullo schema R e aggiungere, ogni volta che un attributo è ottenibile da una dipendenza, questo all'insieme, fino a che: 
A) ho ottenuto tutti gli attributi di partenza, quindi X è chiave
B) controllando ciclicamente, applicando eventualmente [[#DERIVAZIONE|le leggi di Armstrong]] sulle dipendenze, gli attributi del ciclo precedente rispetto al corrente sono gli stessi: ciò vuol dire che non è possibile ottenerne altri.
![hh](immagini/Pasted%20image%2020250426170044.png)




![hh](immagini/Pasted%20image%2020250426161228.png)

---

Dato uno schema R(T) e due insieme di DF F e G us R(T), questi sono equivalenti se e solo se F+=G+


es. F {A ->C, AC ->D, E ->AD, E ->H}
G {A -> CD, E -> AH}

1) Tutte le DF di F appartengono a G+
G |= A -> C: A -> CD |- A->C
AC -> D: A->CD => AC -> CD => AC -> D
E -> AD: E -> AH => E -> A e anche A -> CD => A -> D DUNQUE E -> AD
E -> H: E ->AH => E -> H

2) Tutte le DF di G appartengono a F+

---

### COPERTURA MINIMALE:
F è una copertura minimale se e solo se:
1) Ogni parte destra di una DF di F ha un unico attributo; (es. A->CD diventa A->C e A->D)
2) Le DF di F non contengono[[#ATTRIBUTI ESTRANEI| attributi estranei]] (attributo a sinistra che non cambia nulla); 
3) Non esistono DF ridondanti;

2 ) Data X -> Y appartenente a F, A app. a X è un attributo estraneo se e solo se: 
es. F {A->B, AB->C} ---> AB->C contiene estranei? A è estraneo? Se e solo se {A->B, AB->C} equivale {A->B, B->C}.

AB->C appart. {A->B, B->C}+

B è estraneo: {A->B, AB->C} = {A->B, A->C} 
            ABC                      ABC

3 ) F equivale F-{X->Y}            es. A->B, B->C, A->C <------ A->C RIDONDANTE




----
###### ATTRIBUTI ESTRANEI: 
si dice estraneo un attributo il quale gli attributi derivati dalle dipendenze dov'è compreso questo, si possono ricavare senza lui.
![dsa](immagini/Pasted%20image%2020250430114454.png)




### OK, MA PER CALCOLARE LA COPERTURA MINIMALE, COME FACCIO?


Dato R(T, F): 
- Controllo prima che tutti le dipendenze diano un solo attributo per volta, es. X->Y, e nel caso non sia così, es. X->YZ, riscrivo come X->Y, X->Z;
- Controllo eventuali attributi estranei, nel caso in cui ci siano dipendenze con a sinistra due o più attributi, es. XY->Z, e togliendo uno dei due, X o Y, se riesco ad avere la stessa copertura;
- Controllo le varie ridonanze, non considerando una dipendenza e vedendo se riesco a ricavare lo/gli stesso/i attributo/i: es. X->Y ridondante? Sì se riesco a ricavare, partendo da X, Y senza usare quella dipendenza.