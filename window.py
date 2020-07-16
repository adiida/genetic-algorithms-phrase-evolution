import tkinter as tk


class Window():
    """Class for display information about the population"""
    def __init__(self, window):
        window.title("Genetic Algorithms: Evolve to Target Phrase")
        window.rowconfigure(0, minsize=600, weight=1)
        window.columnconfigure(1, minsize=600, weight=1)

        self.txt_all_phrase = tk.Text(window)
        fr_info = tk.Frame(window, relief=tk.RAISED, bd=2)
        self.lbl_best = tk.Label(master=fr_info, text="Best phrase: ")
        self.lbl_gen = tk.Label(master=fr_info, text="Total generations: ")
        self.lbl_fit = tk.Label(master=fr_info, text="Average fitness: ")
        self.lbl_pop = tk.Label(master=fr_info, text="Total population: ")
        self.lbl_mut = tk.Label(master=fr_info, text="Mutation rate: ")

        self.lbl_best.grid(row=0, column=0, sticky="ew", padx=150, pady=5)
        self.lbl_gen.grid(row=1, column=0, sticky="ew", padx=150, pady=5)
        self.lbl_fit.grid(row=2, column=0, sticky="ew", padx=150, pady=5)
        self.lbl_pop.grid(row=3, column=0, sticky="ew", padx=150, pady=5)
        self.lbl_mut.grid(row=4, column=0, sticky="ew", padx=150, pady=5)

        fr_info.grid(row=0, column=0, sticky="ns")
        self.txt_all_phrase.grid(row=0, column=1, sticky="nsew")

    def update_info(self, best_phr, gen, avg_fit, pop_size, mut_rate, all_phr):
        self.lbl_best["text"] = "Best phrase: {0}".format(best_phr)
        self.lbl_gen["text"] = "Total generations: {0}".format(gen)
        self.lbl_fit["text"] = "Average fitness: {0}".format(avg_fit)
        self.lbl_pop["text"] = "Total population: {0}".format(pop_size)
        self.lbl_mut["text"] = "Mutation rate: {0}%".format(mut_rate)
        self.txt_all_phrase.delete("1.0", tk.END)
        self.txt_all_phrase.insert(tk.END, all_phr)

        self.lbl_best.update()
        self.lbl_gen.update()
        self.lbl_fit.update()
        self.lbl_pop.update()
        self.lbl_mut.update()
        self.txt_all_phrase.update()
