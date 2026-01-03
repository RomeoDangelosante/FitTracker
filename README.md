# FitTracker - Diario di Allenamento

Progetto di sviluppo web realizzato con Python e Flask.
L'applicazione permette agli utenti di registrarsi, accedere e tenere traccia dei propri allenamenti in palestra, calcolando il peso totale sollevato.

## Funzionalità
- **Autenticazione**: Login e Registrazione sicura.
- **Repository Pattern**: Gestione pulita delle query SQL.
- **Dashboard**: Visualizzazione cronologica degli allenamenti.
- **Statistiche**: Calcolo automatico del volume (Serie x Ripetizioni x Peso).

## Installazione

1. Clona il repository.
2. Crea un virtual environment: `python -m venv venv`
3. Attiva il venv.
4. Installa le dipendenze: `pip install -r requirements.txt`
5. Inizializza il DB: `flask --app app init-db`
6. Avvia: `python run.py`
