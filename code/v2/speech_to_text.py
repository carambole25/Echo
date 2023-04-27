import speech_recognition as sr 

listener = sr.Recognizer() #appel reconnaissance vocale

def ecrire_fichier_transversale_1(text):
    with open("fichier_transversale_1.txt", "w") as file:
        file.write(text)

def ecouter():
    try:
        with sr.Microphone() as source: #utilisation du microphone
            print("parlez maintenant")
            voix = listener.listen(source) #générer une voix
            text = listener.recognize_google(voix, language='fr-FR') #assurer la reconnaissance avec Google en français
            text = str(text.lower()).replace("\n", "") 
    except:
        pass
    return text

text = ecouter()
ecrire_fichier_transversale_1(text=)
