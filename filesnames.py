import os


groupe =  'dataCamp/Certificate' #'mlops' # 'datascientist'

# Remplacez 'cheminVersRepertoire' par le chemin de votre répertoire
repertoire = 'C:/Users/hp/Documents/GitHub/fabdoulaye.github.io/assets/certifications/' + groupe + '/'

# Vérifiez si le répertoire existe
if os.path.exists(repertoire):
    # Liste les fichiers dans le répertoire
    filenames = os.listdir(repertoire)

    # Affiche les noms de fichiers
    for fichier in filenames:
        print(fichier)
else:
    print(f"Le répertoire {repertoire} n'existe pas.")
    
# crée une nouvelle liste de dates avec les dates d'obtention des certificats
dates_mlops = ['2024-06-07', '2024-06-30', '2024-06-23', '2024-06-30']

groupe = 'dataCamp'
# Crée une nouvelle liste de filenames avec les modifications demandées
post_filenamess = []
for date, fichier in zip(dates_mlops, filenames) : #for fichier in filenames:
    base_name, _ = os.path.splitext(fichier)
    new_name = f"{date}-{groupe}-{base_name}.markdown"
    post_filenamess.append(new_name)

# Affiche les nouveaux noms de fichiers
for new_fichier in post_filenamess:
    print(new_fichier)
   

