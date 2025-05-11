import tkinter as tk

def calculer_impot():
    try:
        revenu = float(entree_revenu.get())
        abattement = float(entree_abattement.get()) / 100
        taux = float(entree_taux.get()) / 100
        impot = (revenu - (revenu * abattement)) * taux
        total = ((revenu - impot) * 0.12) + impot
        revenu_net = revenu - (revenu * abattement)
        reste = revenu - total
        resultat_label.config(text=f"Montant impôts : {impot:.2f} €")
        resultat_label2.config(text=f"Montant à mettre de côté (+12%) : {round(total)} €", fg="green")
        resultat_label3.config(text=f"Revenu Net Imposable : {revenu_net:.2f} €")
        resultat_label4.config(text=f"Reste : {round(reste)} €")
    except ValueError:
        resultat_label.config(text="Veuillez entrer des valeurs valides.", fg="red")
        resultat_label2.config(text="")
        resultat_label3.config(text="")
        resultat_label4.config(text="")

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Impôts Micro-Entreprise")

# Widgets
tk.Label(fenetre, text="Revenu brut (€) :").grid(row=0, column=0, padx=10, pady=5)
entree_revenu = tk.Entry(fenetre)
entree_revenu.grid(row=0, column=1)

tk.Label(fenetre, text="Abattement fiscal (%) :").grid(row=1, column=0, padx=10, pady=5)
entree_abattement = tk.Entry(fenetre)
entree_abattement.insert(0, "34")  # Valeur par défaut
entree_abattement.grid(row=1, column=1)

tk.Label(fenetre, text="Taux d'IR 2026 (%) :").grid(row=2, column=0, padx=10, pady=5)
entree_taux = tk.Entry(fenetre)
entree_taux.insert(0, "26.1")  # Valeur par défaut
entree_taux.grid(row=2, column=1)

bouton_calcul = tk.Button(fenetre, text="Calculer", command=calculer_impot)
bouton_calcul.grid(row=3, column=0, columnspan=2, pady=10)

resultat_label = tk.Label(fenetre, text="")
resultat_label.grid(row=5, column=0, columnspan=2, pady=10)

resultat_label2 = tk.Label(fenetre, text="")
resultat_label2.grid(row=6, column=0, columnspan=2)

resultat_label3 = tk.Label(fenetre, text="")
resultat_label3.grid(row=4, column=0, columnspan=2)

resultat_label4 = tk.Label(fenetre, text="")
resultat_label4.grid(row=7, column=0, columnspan=2, pady=10)

bouton_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.grid(row=8, column=0, columnspan=2, pady=5)

# Lancement de l'application
fenetre.mainloop()
