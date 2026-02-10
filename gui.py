"""Interface gráfica simples para o organizador usando Tkinter.

Permite escolher a pasta, modo (simulação ou executar) e preset de agrupamento.
"""
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
import logging
from typing import Optional

from app import organizar_arquivos


class TextHandler(logging.Handler):
    def __init__(self, text_widget: tk.Text):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record) + "\n"
        def append():
            self.text_widget.insert(tk.END, msg)
            self.text_widget.see(tk.END)
        self.text_widget.after(0, append)


def run_in_thread(target, *args, **kwargs):
    th = threading.Thread(target=target, args=args, kwargs=kwargs, daemon=True)
    th.start()


def main_gui():
    root = tk.Tk()
    root.title("Organizador de Arquivos")

    frm = tk.Frame(root, padx=8, pady=8)
    frm.pack(fill=tk.BOTH, expand=True)

    tk.Label(frm, text="Pasta:").grid(row=0, column=0, sticky=tk.W)
    path_var = tk.StringVar()
    tk.Entry(frm, textvariable=path_var, width=50).grid(row=0, column=1, sticky=tk.W)
    def browse():
        p = filedialog.askdirectory()
        if p:
            path_var.set(p)
    tk.Button(frm, text="Escolher...", command=browse).grid(row=0, column=2)

    grouping_var = tk.StringVar(value="extension")
    tk.Label(frm, text="Agrupar por:").grid(row=1, column=0, sticky=tk.W)
    tk.Radiobutton(frm, text="Extensão", variable=grouping_var, value="extension").grid(row=1, column=1, sticky=tk.W)
    tk.Radiobutton(frm, text="Mídia", variable=grouping_var, value="media").grid(row=1, column=2, sticky=tk.W)

    dry_var = tk.BooleanVar(value=True)
    tk.Checkbutton(frm, text="Simular (dry-run)", variable=dry_var).grid(row=2, column=1, sticky=tk.W)

    log_text = tk.Text(frm, height=12)
    log_text.grid(row=3, column=0, columnspan=3, pady=(8,0), sticky=tk.NSEW)
    frm.rowconfigure(3, weight=1)
    frm.columnconfigure(1, weight=1)

    # Connect logger to text widget
    handler = TextHandler(log_text)
    handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logging.getLogger().addHandler(handler)

    def do_run():
        path = path_var.get().strip()
        if not path:
            messagebox.showerror("Erro", "Escolha uma pasta primeiro")
            return
        run_in_thread(organizar_arquivos, path, dry_var.get(), grouping_var.get(), None)

    tk.Button(frm, text="Executar/Simular", command=do_run).grid(row=4, column=1, pady=8)

    root.mainloop()


if __name__ == "__main__":
    main_gui()
