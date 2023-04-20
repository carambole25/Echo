text = "Bonjour peu tu me donner la meteo de demain a Paris ?"
with open("fichier_transversale_1.txt", "w") as f:
    f.write(text)
    
import os
os.system("node characterAi_api.js")