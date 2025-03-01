""" # pip install pdf2image Pillow

from pdf2image import convert_from_path
from PIL import Image
import os

# Chemin vers le fichier PDF
pdf_path = 'C:/Users/hp/Documents/GitHub/fabdoulaye.github.io/assets/certifications/datacamp/certificate_Data Manipulation with pandas.pdf'

# Convertir le PDF en images (une image par page)
images = convert_from_path(pdf_path)

# Sauvegarder la première page en tant qu'image
image_path = 'C:/Users/hp/Documents/GitHub/fabdoulaye.github.io/assets/certifications/images/Data Manipulation with pandas.jpg'
images[0].save(image_path, 'JPEG')

print(f"L'image a été créée avec succès : {image_path}") """

import os
import fitz  # PyMuPDF

certification_folder = 'dataCamp/Certificate' # "mlops" #'datascientist' #'DataCamp'

# Obtenir la liste de tous les fichiers PDF dans le répertoire spécifié
pdf_directory = 'C:/Users/hp/Documents/GitHub/fabdoulaye.github.io/assets/certifications/'+ certification_folder + '/'
pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]

# Faire la conversion pour chaque fichier PDF
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_directory, pdf_file)

    # Ouvrir le document PDF
    pdf_document = fitz.open(pdf_path)

    # Sélectionner la première page
    page = pdf_document.load_page(0)

    # Convertir la page en image
    pix = page.get_pixmap()

    # Définir le chemin de l'image de sortie
    image_name = os.path.splitext(pdf_file)[0] + '.jpg'
    image_path = os.path.join('C:/Users/hp/Documents/GitHub/fabdoulaye.github.io/assets/certifications/images/', image_name)

    # Sauvegarder l'image
    pix.save(image_path)

    print(f"L'image a été créée avec succès : {image_path}")


""" pdf_path = 'C:/Users/hp/Documents/GitHub/fabdoulaye.github.io/assets/certifications/datacamp/certificate_Data Manipulation with pandas.pdf'

# Ouvrir le document PDF
pdf_document = fitz.open(pdf_path)

# Sélectionner la première page
page = pdf_document.load_page(0)

# Convertir la page en image
pix = page.get_pixmap()

# Sauvegarder l'image
image_path = 'C:/Users/hp/Documents/GitHub/fabdoulaye.github.io/assets/certifications/images/Data Manipulation with pandas.jpg'
pix.save(image_path)

print(f"L'image a été créée avec succès : {image_path}") """