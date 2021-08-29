import tkinter
from tkinter import messagebox
#le messagebox permet d'afficher des genres de barres d'avertissemment ou des trucs du genre
#from tkinter import *
app = tkinter.Tk()
app.title("Mon premier programme en fenÊtre")
#app.minsize(640,480)

#app.maxsize(1280,720)

#app.geometry("900x800") #geometry definit la taille de ma fenetre

#app.resizable(width=False, height= False)
#<nom variable> = <nom_widget_parent>(<widget_parent>, <parent>.....)
#label_welcome = tkinter.Label(app, text ="Bienvenue dans mon programme")
#cela défint juste le label mais ne l'affiche pas puisque la méthode d'affichage n'est pas spécifier
#label_welcome.pack()
#maintenant le texte s'affiche et centralise ce que je voulais afficher
#message_welcome = tkinter.Message(app, text ="test widget message")
#message_welcome.pack()
#le widget message lui aussi affiche du texte mais sur plusieur lignes
#le widget suivant permet de faire entrer un truc sur l'interface un genre de input
#enter_name = tkinter.Entry(app, )
# l'attribut(width="") permet de modifier le champ que ressort entry ,avec l'attribut show (show="(?))" je peux cacher le texte saisie dans entry
#enter_name.pack()
def hello():
    print("Hello sur mon premier terminal !")
#button_one = tkinter.Button(app, text="click HERE", command = hello)
#button_one.pack()
#check_widget = tkinter.Checkbutton(app, text="cocher!")
#check_widget.pack()
radio_widget0 = tkinter.Radiobutton(app, text="Homme", value=1)
radio_widget1 = tkinter.Radiobutton(app, text="Femme", value=0)
#le widget permet de faire un choix entre deux truc
radio_widget0.pack()
radio_widget1.pack()
#les widget radio permettent d'afficher le genre de truc avec leqelle on peut sélectionné l'age de l'utilisateur
scale_w = tkinter.Scale(app,from_=9, to=100)
scale_w.pack()
spin_w = tkinter.Spinbox(app, from_=1, to=10)
spin_w.pack()

def test_msg_dialog():
    messagebox.showerror("ERREUR", "Un problème est survenu !")#a part showerror il y a : showinfo,showwarning,askquestion(un genre de oui ou non),askokcancel,askyesno,askretrycancel
btn = tkinter.Button(app, text="Bouton test de déclanchement du message dialogue", command= test_msg_dialog)
btn.pack()

app.mainloop()
