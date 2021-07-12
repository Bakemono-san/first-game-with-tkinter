from tkinter import *

def deplacement():
    global dx,dy
    #condition pour rebond
    if zone.coords(balle)[1]<0 :
        dy=-1*dy
    if zone.coords(balle)[3]>500:
        looser = Label(zone,text="you loosed",font=("sans-serif",20),bg="black",fg="white")
        looser.pack()

    if (zone.coords(balle)[0]<0) or (zone.coords(balle)[2]>500):
        dx=-1*dx
    
    #ici on test la collision de la balle et de la raquette
    if (zone.coords(balle)[3]>zone.coords(raquette)[1]) and (zone.coords(balle)[0]<zone.coords(raquette)[2]) and (zone.coords(balle)[2]>zone.coords(raquette)[0]):
           dy= -1*dy
   
    #deplacement
    zone.move(balle,dx,dy)

    #zone.move(1,dx,dx)
    
    #repetition de la fonction
    fenetre.after(20,deplacement)

#deplacement a droite
def droite(event):
    if zone.coords(raquette)[2] != 500:
        zone.move(raquette,10,0)

#deplacement a gauche
def gauche(event):
    if zone.coords(raquette)[0] != 0:
        zone.move(raquette,-10,0)

#vitesse de deplacement de la balle
dx = 4
dy = 4

# la fenetre
fenetre = Tk()

zone = Canvas(fenetre,width=500,height=500,bd=0,bg="white")
zone.pack(padx=10,pady=10)

#creation dune balle
balle = zone.create_oval(20,20,40,40,fill="orange")

#creation d'une raquette
raquette = zone.create_rectangle(400,480,500,490,fill="blue")

#deplacement de la balle
zone.bind_all('<Right>',droite)
zone.bind_all('<Left>',gauche)

#lancement du mouvement
deplacement()

fenetre.mainloop()