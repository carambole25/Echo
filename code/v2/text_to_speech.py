# importation de la bibliothèque requis
import win32com.client

def recuperation_reponse():
    with open("fichier_transversale_2.txt", "r") as file:
        reponse = file.readlines()

    return reponse

def traitement(reponse):
    msg = ""
    for i in reponse:
        msg += i+"  "
    msg = msg.replace("\n", "")
    msg = msg.replace("*", "")
    msg = msg.replace("Ã»", "u")
    msg = msg.replace("Ãª", "ai")
    msg = msg.replace("Ã©", "ai")
    msg = msg.replace("Ã", "a")
    msg = msg.replace("Ã«", "ai")
    msg = msg.replace("Ã¤", "a")
    msg = msg.replace("Ã¢", "a")
    msg = msg.replace("Ã¨", "ai")
    print(msg)
    return msg

def speech(msg):
    speaker = win32com.client.Dispatch("SAPI.SpVoice") #appel de la méthode 
    speaker.Speak(msg) #sortie audio

rep = recuperation_reponse()
msg = traitement(rep)
speech(msg)
