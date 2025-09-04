import os
import time
import json
import psutil
from datetime import datetime
from tkinter import Tk, simpledialog, messagebox, Button

# File per salvare i dati
DATA_FILE = "project_time_log.json"

# Carica dati precedenti
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        project_data = json.load(f)
else:
    project_data = {}

# Lista dei processi da monitorare
MONITORED_APPS = {
    "blender": "Blender",
    "TouchDesigner.exe": "TouchDesigner"
}

class AdvancedTimeTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Project Time Tracker")
        self.running = False
        self.start_time = 0
        self.current_project = ""
        self.hourly_rate = 0

        Button(root, text="Imposta Tariffa Progetto", command=self.set_rate).pack(pady=5)
        Button(root, text="Mostra Valore Progetti", command=self.show_value).pack(pady=5)
        self.monitor_processes()

    def set_rate(self):
        project_name = simpledialog.askstring("Progetto", "Nome del progetto:")
        if not project_name:
            return
        rate = simpledialog.askfloat("Tariffa Oraria", f"Tariffa oraria per '{project_name}' (€)?")
        if rate is not None:
            if project_name not in project_data:
                project_data[project_name] = {}
            project_data[project_name]["rate"] = rate
            messagebox.showinfo("Tariffa impostata", f"Progetto '{project_name}' → €{rate:.2f}/h")
            self.save_data()

    def monitor_processes(self):
        active_project = None

        for proc in psutil.process_iter(['name', 'cmdline']):
            try:
                name = proc.info['name']
                cmdline = proc.info['cmdline']
                for key, app_name in MONITORED_APPS.items():
                    if key.lower() in name.lower():
                        # Rileva il file aperto se possibile
                        if cmdline and len(cmdline) > 1:
                            # Assume che il primo argomento sia il file
                            file_path = cmdline[1]
                            project_name = os.path.basename(file_path)
                        else:
                            project_name = app_name
                        active_project = project_name
            except (psutil.NoSuchProcess, IndexError):
                continue

        if active_project and not self.running:
            self.start_project(active_project)
        elif self.running and active_project != self.current_project:
            self.stop_project()

        self.root.after(5000, self.monitor_processes)  # Controlla ogni 5 secondi

    def start_project(self, project_name):
        self.current_project = project_name
        self.start_time = time.time()
        self.running = True
        # Assicura che il progetto abbia un rate
        if project_name not in project_data or "rate" not in project_data[project_name]:
            rate = simpledialog.askfloat("Tariffa Oraria", f"Tariffa oraria per '{project_name}' (€)?")
            if rate is None:
                rate = 0
            if project_name not in project_data:
                project_data[project_name] = {}
            project_data[project_name]["rate"] = rate
            self.save_data()
        messagebox.showinfo("Progetto avviato", f"Rilevato progetto '{project_name}'. Timer avviato.")

    def stop_project(self):
        elapsed = time.time() - self.start_time
        self.running = False
        today = datetime.today().strftime("%Y-%m-%d")

        # Aggiorna dati progetto
        if "log" not in project_data[self.current_project]:
            project_data[self.current_project]["log"] = {}
        if today not in project_data[self.current_project]["log"]:
            project_data[self.current_project]["log"][today] = 0
        project_data[self.current_project]["log"][today] += elapsed

        self.save_data()
        messagebox.showinfo("Progetto chiuso", f"Progetto '{self.current_project}' fermato.\nTempo speso oggi: {elapsed/60:.2f} minuti.")
        self.current_project = ""

    def show_value(self):
        if not project_data:
            messagebox.showinfo("Valore", "Nessun progetto registrato.")
            return
        msg = ""
        for proj, data in project_data.items():
            total_seconds = sum(data.get("log", {}).values())
            hours = total_seconds / 3600
            value = hours * data.get("rate", 0)
            msg += f"{proj}: {hours:.2f} ore → €{value:.2f}\n"
        messagebox.showinfo("Valore progetti", msg)

    def save_data(self):
        with open(DATA_FILE, "w") as f:
            json.dump(project_data, f, indent=4)

root = Tk()
app = AdvancedTimeTracker(root)
root.mainloop()
