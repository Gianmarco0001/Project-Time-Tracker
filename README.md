# Project-Time-Tracker

**Project-Time-Tracker** è un programma Python che monitora automaticamente il tempo speso su progetti in **Blender** o **TouchDesigner**, calcola il valore economico in base alla tariffa oraria e mantiene un log giornaliero.

**Project-Time-Tracker** is a Python program that automatically tracks time spent on **Blender** or **TouchDesigner** projects, calculates the economic value based on hourly rate, and keeps a daily log.

---

## Caratteristiche principali / Main Features

* Rilevamento automatico dei processi **Blender** e **TouchDesigner** / Automatic detection of **Blender** and **TouchDesigner** processes.
* Rilevamento del file di progetto aperto (se disponibile) / Detection of the open project file (if available).
* Timer automatico all’apertura del progetto e stop alla chiusura / Automatic timer on project opening and stop on closing.
* Possibilità di impostare **tariffe diverse per progetto** / Ability to set **different rates per project**.
* Log giornaliero con tempo cumulativo per progetto / Daily log with cumulative time per project.
* Visualizzazione del valore economico dei progetti / Display of the economic value of projects.
* Salvataggio dei dati in formato JSON (`project_time_log.json`) / Data saved in JSON format (`project_time_log.json`).


---

## Installazione / Installation

1. Assicurati di avere Python 3.8+ installato / Make sure Python 3.8+ is installed.
2. Installa le librerie necessarie / Install required libraries:

```bash
pip install psutil
```

---

## Esecuzione / Execution

### 1. Da Python / From Python

```bash
python project_tracker.py
```

---

## Utilizzo / Usage

1. Avvia il programma / Launch the program.
2. Premi **“Imposta Tariffa Progetto”** per aggiungere la tariffa oraria per ogni progetto / Click **“Set Project Rate”** to add hourly rate for each project.
3. Apri Blender o TouchDesigner con un progetto / Open Blender or TouchDesigner with a project.
4. Il timer parte automaticamente / Timer starts automatically.
5. Quando chiudi l’applicazione, il tempo viene salvato automaticamente nel file JSON / When closing the application, time is automatically saved in the JSON file.
6. Premi **“Mostra Valore Progetti”** per visualizzare le ore lavorate e il valore economico / Click **“Show Project Value”** to see worked hours and economic value.

---

## Struttura del file JSON / JSON File Structure

```json
{
  "MyProject.blend": {
    "rate": 50,
    "log": {
      "2025-09-04": 3600,
      "2025-09-05": 1800
    }
  }
}
```

* `rate` → tariffa oraria del progetto in € / hourly rate of the project in €.
* `log` → tempo speso ogni giorno in secondi / time spent each day in seconds.

---

## Personalizzazione / Customization

* Modifica `DATA_FILE` nello script per cambiare il percorso del file JSON / Modify `DATA_FILE` in the script to change the JSON file path.
* Aggiungi altre applicazioni da monitorare modificando `MONITORED_APPS` / Add other applications to monitor by editing `MONITORED_APPS`.
* Modifica l’intervallo di monitoraggio cambiando `self.root.after(5000, ...)` (in millisecondi) / Change the monitoring interval by editing `self.root.after(5000, ...)` (in milliseconds).

---

## Note / Notes

* Funziona su Windows. Su Linux/macOS il monitor dei processi potrebbe richiedere adattamenti / Works on Windows. On Linux/macOS the process monitoring may require adjustments.
* Per rendere l’eseguibile portatile, includi `project_time_log.json` nella stessa cartella dell’exe / To make the executable portable, include `project_time_log.json` in the same folder as the exe.

---

## Disclaimer / Avvertenza

Questo software è fornito "così com'è", senza garanzie di alcun tipo. L'utente utilizza il programma a proprio rischio. / This software is provided "as-is", without any warranty. The user uses the program at their own risk.

## License / Licenza

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.  
Questo progetto è rilasciato sotto la **MIT License** – vedi il file [LICENSE](LICENSE) per i dettagli.

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
