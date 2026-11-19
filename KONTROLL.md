# Django eelkursuse lõplik kontroll

## 1. Millised ülesanded said tehtud?
Kõik seitse eelkursuse praktilist ülesannet said edukalt läbitud:
- **Ülesanne 1:** Projekti `config` ja rakenduse `books` loomine ning virtuaalkeskkonna `.venv` seadistamine.
- **Ülesanne 2:** URL-ide (`urls.py`), vaatefunktsioonide (`views.py`) ja HTML-mallide (`templates/`) loomine ja ühendamine.
- **Ülesanne 3:** Dünaamilise sisu kuvamine Django mallikeele muutujate (`{{ ... }}`) ja märgendite (`{% for %}`, `{% if %}`) abil.
- **Ülesanne 4:** Andmemudeli `Book` loomine, täiendamine väljaga `genre` ning andmebaasimigratsioonide rakendamine.
- **Ülesanne 5:** Administraatori kasutaja (`superuser`) loomine ja `Book` mudeli registreerimine ning haldamine Django Adminis.
- **Ülesanne 6:** Andmete pärimine ja filtreerimine andmebaasist Django ORM-i ja QuerySeti abil (sh vaade `/available/`).
- **Ülesanne 7:** Lõplik kontroll, dokumenteerimine ja projekti üleslaadimine GitHubi.

## 2. Mis oli kõige keerulisem?
Kõige rohkem tähelepanu nõudis virtuaalkeskkonna esmane seadistamine ja jälgimine, et mudeli väljade nimed (`is_available`) ning `views.py` kontekstisõnastiku võtmed kattuksid täpselt HTML-mallides kasutatud muutujanimedega.

## 3. Mis vahe on Django mudelil, view'l ja mallil?
Django järgib MVT (*Model-View-Template*) arhitektuuri, kus igal osal on kindel roll:
- **Mudel (`models.py`):** Kirjeldab andmete struktuuri ja välju ning suhtleb ORM-i kaudu andmebaasiga.
- **View (`views.py`):** Sisaldab rakenduse äriloogikat — võtab vastu kasutaja HTTP-päringu, küsib mudelilt vajalikud andmed ja edastab need mallile.
- **Mall (`templates/*.html`):** Vastutab esitluskihi ehk kasutajaliidese eest, määrates, kuidas andmed HTML-ina veebilehel välja näevad.

## 4. Kuidas liiguvad andmed andmebaasist veebilehele?
1. Kasutaja avab brauseris URL-i (nt `/available/`) ja brauser saadab serverile HTTP-päringu.
2. Django suunab päringu `config/urls.py` ja `books/urls.py` kaudu vastavale `views.py` funktsioonile.
3. Vaatefunktsioon teeb Django ORM-i abil päringu (nt `Book.objects.filter(is_available=True)`), mille mudel tõlgib SQL-käsuks ja küsib andmed SQLite'i andmebaasist.
4. Andmebaas tagastab kirjed Pythoni objektidena (`QuerySet`), mille vaatefunktsioon pakib `context` sõnastikku ja annab edasi funktsioonile `render()`.
5. Django mallimootor täidab HTML-mallis olevad muutujad ja tsüklid saadud andmetega ning saadab valmis HTML-lehe `HttpResponse` vastusena brauserisse.