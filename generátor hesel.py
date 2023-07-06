import random
import string
import tkinter as tk

def generovat_heslo(delka=8, male_pismena=True, velka_pismena=True, cislice=True, spec_znaky=True):
    znaky = ""
    if male_pismena:
        znaky += string.ascii_lowercase
    if velka_pismena:
        znaky += string.ascii_uppercase
    if cislice:
        znaky += string.digits
    if spec_znaky:
        znaky += string.punctuation

    heslo = ''.join(random.choice(znaky) for _ in range(delka))
    return heslo

def generovat_heslo_tlacitko():
    delka_hesla = delka_entry.get()
    try:
        delka_hesla = int(delka_hesla)
        male_pismena = male_pismena_var.get()
        velka_pismena = velka_pismena_var.get()
        cislice = cislice_var.get()
        spec_znaky = spec_znaky_var.get()

        heslo = generovat_heslo(delka_hesla, male_pismena, velka_pismena, cislice, spec_znaky)
        vystup_text.configure(text=heslo)
    except ValueError:
        vystup_text.configure(text="Zadej délku hesla.")

root = tk.Tk()
root.title("Generátor hesla")

# velikost okna
root.geometry("400x300")

delka_label = tk.Label(root, text="Délka hesla:")
delka_label.pack()

delka_entry = tk.Entry(root)
delka_entry.pack()

# Zaškrtávací políčka pro volbu typů znaků
male_pismena_var = tk.BooleanVar(value=True)
male_pismena_checkbutton = tk.Checkbutton(root, text="Malá písmena", variable=male_pismena_var)
male_pismena_checkbutton.pack()

velka_pismena_var = tk.BooleanVar(value=True)
velka_pismena_checkbutton = tk.Checkbutton(root, text="Velká písmena", variable=velka_pismena_var)
velka_pismena_checkbutton.pack()

cislice_var = tk.BooleanVar(value=True)
cislice_checkbutton = tk.Checkbutton(root, text="Číslice", variable=cislice_var)
cislice_checkbutton.pack()

spec_znaky_var = tk.BooleanVar(value=True)
spec_znaky_checkbutton = tk.Checkbutton(root, text="Speciální znaky", variable=spec_znaky_var)
spec_znaky_checkbutton.pack()

generovat_tlacitko = tk.Button(root, text="Generovat heslo", command=generovat_heslo_tlacitko)
generovat_tlacitko.pack()

vystup_text = tk.Label(root, text="")
vystup_text.pack()

root.mainloop()
