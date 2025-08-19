---
layout: links
# multilingual page pair id, this must pair with translations of this page. (This name must be unique)
lng_pair: id_links

# publish date (used for seo)
# if not specified, site.time will be used.
#date: 2022-03-03 12:32:00 +0000

# for override items in _data/lang/[language].yml
#title: My title
#button_name: "My button"
# for override side_and_top_nav_buttons in _data/conf/main.yml
#icon: "fa fa-bath"

# seo
# if not specified, date will be used.
#meta_modify_date: 2022-03-03 12:32:00 +0000
# check the meta_common_description in _data/owner/[language].yml
#meta_description: ""

# optional
# please use the "image_viewer_on" below to enable image viewer for individual pages or posts (_posts/ or [language]/_posts folders).
# image viewer can be enabled or disabled for all posts using the "image_viewer_posts: true" setting in _data/conf/main.yml.
#image_viewer_on: true
# please use the "image_lazy_loader_on" below to enable image lazy loader for individual pages or posts (_posts/ or [language]/_posts folders).
# image lazy loader can be enabled or disabled for all posts using the "image_lazy_loader_posts: true" setting in _data/conf/main.yml.
#image_lazy_loader_on: true
# exclude from on site search
#on_site_search_exclude: true
# exclude from search engines
#search_engine_exclude: true
# to disable this page, simply set published: false or delete this file
#published: false


# you can always move this content to _data/content/ folder
# just create new file at _data/content/links/[language].yml and move content below.
###########################################################
#                Links Page Data
###########################################################
page_data:
  main:
    header: "Liens utiles"
    info: "Sélection de ressources pour la cybersécurité, la programmation, la gestion de projet, la data science et plus."

  # To change order of the Categories, simply change order. (you don't need to change list order.)
  category:
    - title: "MOOC & Formation"
      type: id_mooc
      color: "#4A90E2"
    - title: "Cybersécurité"
      type: id_cyber
      color: "#B97AFF"
    - title: "Programmation"
      type: id_programming
      color: "#62b462"
    - title: "Data Science"
      type: id_datascience
      color: "#F4A273"
    - title: "Mac & Logiciels"
      type: id_mac
      color: "#888888"
    - title: "Outils Divers"
      type: id_tools
      color: "#F4D35E"

  list:
    -
    # MOOC & Formation
    - type: id_mooc
      title: "MOOC Gestion de Projet"
      url: "https://moocgdp.gestiondeprojet.pm/"
      info: "Cours en ligne sur la gestion de projet."
    - type: id_mooc
      title: "Cnam - TP Base de données"
      url: "http://deptfod.cnam.fr/bd/tp"
      info: "Travaux pratiques de base de données du Cnam."
    - type: id_mooc
      title: "Modules de spécialisation MOOC GdP"
      url: "https://www.mindomo.com/fr/mindmap/mooc-gdp-modules-de-specialisation-c70c80bcc32040a3871c91367b304373"
      info: "Carte mentale des modules de spécialisation du MOOC GdP."

    # Cybersécurité
    - type: id_cyber
      title: "HackUTT"
      url: "https://hackutt.notion.site/hackutt/HackUTT-d251422fbe9d4a2bb39567c57294d6c4"
      info: "Ressources et challenges cybersécurité."
    - type: id_cyber
      title: "Pwned Labs"
      url: "https://pwnedlabs.io/dashboard"
      info: "Plateforme de labs pour la sécurité offensive."
    - type: id_cyber
      title: "eForensics Magazine"
      url: "https://eforensicsmag.com/"
      info: "Magazine en ligne sur la cybersécurité et la forensique."
    - type: id_cyber
      title: "OWASP Top 10"
      url: "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/"
      info: "Principaux risques de sécurité des applications web."

    # Programmation
    - type: id_programming
      title: "Stack Overflow"
      url: "https://stackoverflow.com/"
      info: "Questions et réponses pour les programmeurs."
    - type: id_programming
      title: "GitHub"
      url: "https://github.com/"
      info: "Plateforme de développement collaboratif et de partage de code."
    - type: id_programming
      title: "HackerRank"
      url: "https://www.hackerrank.com/"
      info: "Entraînement et challenges de programmation."
    - type: id_programming
      title: "Codewars"
      url: "https://www.codewars.com/"
      info: "Exercices de code pour progresser en algorithmique."

    # Data Science
    - type: id_datascience
      title: "DataScientest Career Services"
      url: "https://paper-tax-5ac.notion.site/DataScientest-Career-Services-d7fab23e69ee4ac0a78fd641499eb906"
      info: "Ressources carrière DataScientest."
    - type: id_datascience
      title: "Practical Business Python"
      url: "https://pbpython.com/"
      info: "Blog sur l’utilisation de Python en entreprise."
    - type: id_datascience
      title: "Spark SQL Guide"
      url: "https://spark.apache.org/docs/latest/sql-programming-guide.html"
      info: "Documentation officielle Spark SQL."

    # Mac & Logiciels
    - type: id_mac
      title: "Mac OS X Facile"
      url: "http://www.osxfacile.com/bonjour.html"
      info: "Astuces et guides pour Mac OS X."
    - type: id_mac
      title: "OldApps Mac"
      url: "http://mac.oldapps.com/"
      info: "Anciennes versions de logiciels pour Mac."
    - type: id_mac
      title: "Logiciels Mac: Softonic"
      url: "http://www.softonic.fr/mac"
      info: "Téléchargement de logiciels pour Mac."

    # Outils Divers
    - type: id_tools
      title: "Dropbox"
      url: "https://www.dropbox.com/home#:::"
      info: "Stockage et partage de fichiers en ligne."
    - type: id_tools
      title: "Diagrams.net"
      url: "https://app.diagrams.net/?src=about"
      info: "Création de diagrammes en ligne."
    - type: id_tools
      title: "Visorando"
      url: "https://www.visorando.com/"
      info: "Idées de randonnées pédestres et VTT."
---