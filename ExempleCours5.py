#Fonction sans paramètre ni retour

def alerter():
    print("Intrusion détectée dans le réseau !")

alerter()


# Fonction avec paramètre sans retour

def alerter(adresse_ip):
    print(f"Intrusion détectée depuis l'adresse IP : {adresse_ip}")

alerter("192.168.1.10")


# Fonction avec paramètres multiples

def analyser_trafic(paquets_recus, paquets_perdus):
    print(f"Paquets reçus : {paquets_recus}, Paquets perdus : {paquets_perdus}")

analyser_trafic(5000, 200)


# Fonction avec paramètres par défaut

def analyser_trafic(paquets_recus=5000, paquets_perdus=200):
    print(f"Paquets reçus : {paquets_recus}, Paquets perdus : {paquets_perdus}")
    
analyser_trafic()
analyser_trafic(7000)


# Fonction avec valeur de retour

def calculer_temps_connexion(temps_initial, temps_final):
    return temps_final - temps_initial

duree_connexion = calculer_temps_connexion(10, 18)
print(f"Durée de connexion : {duree_connexion} heures")



# Exemple d’utilisation

def analyse_trafic_reseau(paquets, seuil_anomalie):
    anomalies_detectees = 0
    for paquet in paquets:
        if paquet > seuil_anomalie:
            print(f"Anomalie détectée : Paquet {paquet} dépasse le seuil {seuil_anomalie}")
            anomalies_detectees += 1
        else:
            print(f"Paquet {paquet} est dans la limite normale.")
    
    print(f"Nombre total d'anomalies détectées : {anomalies_detectees}")
    
    if anomalies_detectees > 3:
        print("Alerte : Trop d'anomalies détectées dans le réseau !")
    else:
        print("Le trafic est dans les limites acceptables.")

paquets_reseau = [120, 300, 450, 600, 50, 700, 900, 80, 250]
seuil_critique = 500
analyse_trafic_reseau(paquets_reseau, seuil_critique)


# Fonction pour surveiller les connexions réseau et détecter des IP suspectes
def surveillance_connexions(adresses_ip, ip_blacklist):
    connexions_suspectes = 0
    
    # Boucle pour analyser chaque adresse IP dans la liste
    for ip in adresses_ip:
        if ip in ip_blacklist:
            print(f"Alerte : Connexion suspecte détectée depuis l'adresse IP {ip}")
            connexions_suspectes += 1
        else:
            print(f"Connexion autorisée depuis l'adresse IP {ip}")
    
    # Affichage du nombre total de connexions suspectes détectées
    print(f"Nombre total de connexions suspectes : {connexions_suspectes}")
    
    # Condition pour vérifier si le nombre de connexions suspectes dépasse un certain seuil
    if connexions_suspectes > 0:
        print("Action requise : Analyse approfondie nécessaire des connexions suspectes.")
    else:
        print("Aucune connexion suspecte détectée.")

# Exemple d'utilisation
# Liste des adresses IP tentant de se connecter au réseau
adresses_ip_reseau = [
    "192.168.1.10", "10.0.0.5", "172.16.0.1", 
    "192.168.1.12", "203.0.113.5", "192.168.1.15"
]

# Liste noire des adresses IP suspectes (par exemple, IP connues pour des attaques)
ip_blacklist = ["203.0.113.5", "192.168.1.15", "198.51.100.2"]

# Appel de la fonction pour surveiller les connexions réseau
surveillance_connexions(adresses_ip_reseau, ip_blacklist)
