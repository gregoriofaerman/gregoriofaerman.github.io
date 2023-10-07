import os
from bs4 import BeautifulSoup

# Obtener la lista de archivos de la carpeta 'pages'
files = os.listdir("pages")

# Ordenar los archivos por fecha (puede requerir ajustes dependiendo del formato de fecha en los nombres de archivo)
files.sort(reverse=True)

# Generar el índice y el contenido de los artículos
index_html = ""
articles_html = ""

for file_name in files:
    if file_name.endswith(".md"):
        with open(os.path.join("pages", file_name), "r", encoding="utf-8") as file:
            # Analizar el contenido Markdown
            content = file.read()
            # Puedes utilizar una biblioteca Markdown para convertir el contenido Markdown a HTML si es necesario

            # Extraer la fecha y el título del nombre del archivo
            _, date, title = file_name.split("-", 2)
            date = date.replace("_", "-")
            title = title.replace(".md", "").replace("_", " ")

            # Generar el enlace al artículo en el índice
            index_html += f'<li><a href="{file_name}">{date} - {title}</a></li>'

            # Generar el contenido del artículo
            articles_html += f'<article id="{file_name}">{content}</article>'

# Insertar el índice y el contenido en index.html
with open("index.html", "r+", encoding="utf-8") as index_file:
    soup = BeautifulSoup(index_file, "html.parser")
    index_list = soup.find("ul")
    index_list.extend(BeautifulSoup(index_html, "html.parser"))

    main_content = soup.find("main")
    main_content.extend(BeautifulSoup(articles_html, "html.parser"))

    # Guardar los cambios en index.html
    index_file.seek(0)
    index_file.write(str(soup))
    index_file.truncate()
