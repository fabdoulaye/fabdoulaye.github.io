import os
import re

organisme = 'DataScientest' # 'DataCamp' #'DataScientest'
certification_folder = 'dpm' # 'dataCamp/Certificate' # 'datascientist' #'DataCamp'
diploma = 'Data Product Manager' # 'Machine Learning Engineer' #'Data Scientist'
groupe = 'dataCamp'
logos = 'dst-new-logo.png' #'Datacamp.png' # 'dst-new-logo.png' #'ds-logo.png'

##### Liste les noms des fichiers pour les posts de certification
# Remplacez 'votre_repertoire' par le chemin de votre répertoire
repertoire = 'C:/Users/hp/Documents/GitHub/fabdoulaye.github.io/assets/certifications/' + certification_folder + '/'

# crée une nouvelle liste de dates avec les dates d'obtention des certificats
dates = ['2024-08-13', '2024-10-11', '2024-10-15', '2024-08-22', '2024-11-12', '2025-01-12']
# dates_datacamp_mlops = ['2024-06-07', '2024-06-30', '2024-06-23', '2024-06-30']
# dates_mlops = ['2024-08-13', '2024-06-10', '2024-02-23', '2024-05-13', '2024-03-06', '2024-03-18', 
#          '2024-08-08', '2024-04-01', '2024-07-28']

# Crée une nouvelle liste de filenames formatée pour les posts de certification
post_filenames = []


# Vérifiez si le répertoire existe
if os.path.exists(repertoire):
    # Liste les fichiers dans le répertoire
    filenames = os.listdir(repertoire)

    # Crée une nouvelle liste de filenames avec l'extension '2023-02' suivi de 'datascientest' et change l'extension en '.markdown'
    # post_filenames = [f"2023-03-11-datascientest-{os.path.splitext(fichier)[0]}.markdown" for fichier in filenames]
    for date, fichier in zip(dates, filenames) : #for fichier in filenames:
        base_name, _ = os.path.splitext(fichier)
        new_name = f"{date}-{base_name}.markdown"
        post_filenames.append(new_name)

    # Affiche les nouveaux noms de fichiers
    for post_filename in post_filenames:
        print(post_filename)
else:
    print(f"Le répertoire {repertoire} n'existe pas.") 
    

# Pour créer ces fichiers en une fois avec Python, 
# Ce code crée un fichier .markdown pour chaque certification avec le contenu approprié. Il utilise un modèle de contenu pour chaque fichier et une liste de noms de fichiers pour les noms de fichiers. Il crée également un dictionnaire pour mapper les titres aux catégories et aux noms d'image et de PDF. Enfin, il crée les fichiers et écrit le contenu.

""" # List of filenames with 'datacamp' added at the beginning
filenames = [
    'datacamp-intermediate-data-visualization-seaborn.markdown',
    'datacamp-introduction-data-visualization-seaborn.markdown',
    'datacamp-introduction-dax-powerbi.markdown',
    'datacamp-introduction-powerbi.markdown',
    'datacamp-introduction-statistics-python.markdown',
    'datacamp-working-categorical-data-python.markdown',
    'datacamp-data-manipulation-pandas.markdown',
    'datacamp-dealing-missing-data-python.markdown',
    'datacamp-exploratory-data-analysis-python.markdown',
    'datacamp-intermediate-importing-data-python.markdown',
    'datacamp-intermediate-python.markdown',
    'datacamp-introduction-data-visualization-matplotlib.markdown',
    'datacamp-introduction-data-visualization-plotly.markdown',
    'datacamp-introduction-git.markdown',
    'datacamp-introduction-importing-data-python.markdown',
    'datacamp-introduction-python.markdown',
    'datacamp-introduction-regression-statsmodels-python.markdown',
    'datacamp-introduction-to-sql.markdown',
    'datacamp-joining-data-sql.markdown',
    'datacamp-joining-data-pandas.markdown',
    'datacamp-machine-learning-tree-based-models-python.markdown',
    'datacamp-object-oriented-programming-python.markdown',
    'datacamp-python-data-science-toolbox-part1.markdown',
    'datacamp-python-data-science-toolbox-part2.markdown',
    'datacamp-supervised-learning-scikit-learn.markdown',
    'datacamp-understanding-data-visualization.markdown',
    'datacamp-unsupervised-learning-python.markdown',
    'datacamp-web-scraping-python.markdown',
    'datacamp-writing-functions-python.markdown',
    'datacamp-track-python-fundamentals.markdown'
] """

# Content template for each file
content_template = """---
lng_pair: id_certification_datacamp_ml
title: "{title}"
category: Certifications
tags: [{category}, {diploma}]
img: "/assets/certifications/images/{logos}"
comments_disable: true
date: {date} 22:00:00 +0100
---

## 🎓 {diploma} - {title}

J'ai obtenu la certification **{title}** de **{category}**.

![Aperçu de la certification](/assets/certifications/images/{image})  

Vous pouvez la consulter en cliquant sur le lien ci-dessous :

📜 **[Voir la certification (PDF)](/assets/certifications/{certification_folder}/{pdf})** 
"""



# Dictionary to map titles to categories and image names
certifications = {}
for filename in post_filenames:
    # base_name = filename.replace("2023-03-11-datascientest-", "").replace(".markdown", "")  #os.path.splitext(filename)[0]
    
    end_index = filename.find(".markdown")
    start_index = filename.find("DPM-")
    base_name = filename[start_index:end_index]

    # "2024-02-23-MLOps-Bash and Linux.markdown"
    # Extraction de la partie requise sans utiliser regex
    start_index = start_index + len("DPM-")
    titre = filename[start_index:end_index]
    
    certifications[titre] = (organisme, logos, diploma, f"{base_name}.jpg", f"{base_name}.pdf", certification_folder, filename[:10])
print(certifications)


# Create directory if it doesn't exist
output_dir = 'fr/_posts'
os.makedirs(output_dir, exist_ok=True)

# Create files and write content
for filename, (title, (category, logos, diploma, image, pdf, certification_folder, date)) in zip(post_filenames, certifications.items()):
    content = content_template.format(title=title, category=category, logos=logos, diploma=diploma, image=image, pdf=pdf, certification_folder=certification_folder , date=date)
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
 
print("Files created successfully.")


