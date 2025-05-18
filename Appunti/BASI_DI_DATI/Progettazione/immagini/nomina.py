import os
import re
import shutil

# Cartella sorgente (immagini con nomi tipo IMG-...)
origine = '.'
# Cartella destinazione: "immagini"
destinazione = 'immagini'

# Crea la cartella "immagini" solo se esiste già. Se non esiste, crea
if not os.path.exists(destinazione):
    os.makedirs(destinazione)

# Pattern: trova IMG-... con estensione immagine
pattern = re.compile(r'^IMG-.*\.(png|jpg|jpeg)$', re.IGNORECASE)

# Trova tutti i file corrispondenti
file_immagini = [f for f in os.listdir(origine) if pattern.match(f)]

# Ordina per consistenza (opzionale)
file_immagini.sort()

# Lista per i riferimenti Markdown
markdown_lines = []

# Rinomina e genera riferimenti
for idx, filename in enumerate(file_immagini, start=1):
    nuovo_nome = f"{idx}.png"
    nuovo_percorso = os.path.join(destinazione, nuovo_nome)
    percorso_orig = os.path.join(origine, filename)
    
    # Sposta e rinomina forzando .png
    shutil.move(percorso_orig, nuovo_percorso)
    
    # Aggiungi riga Markdown
    markdown_lines.append(f"![w](immagini/{idx}.png)")

# Stampa i riferimenti Markdown
print("\n".join(markdown_lines))
