from colorsys import yiq_to_rgb
import os

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

import utils


def read(file):
    book = epub.read_epub(file)
    
    # Get book's metadata
    meta_data = {}
    meta_data['title'] = book.get_metadata('DC', 'title')
    meta_data['author'] = book.get_metadata('DC', 'creator')
    meta_data['contributor'] = book.get_metadata('DC', 'contributor')
    meta_data['publisher'] = book.get_metadata('DC', 'publisher')
    meta_data['rights'] = book.get_metadata('DC', 'rights')
    meta_data['coverage'] = book.get_metadata('DC', 'coverage')
    meta_data['date'] = book.get_metadata('DC', 'date')
    meta_data['description'] = book.get_metadata('DC', 'description')

    # Get book's content
    book_docs = []  # Only document type items
    book_rsrc = {}  # Any items but document type items
    for item in book.get_items():
        if (item.get_type() == ebooklib.ITEM_DOCUMENT):
            book_docs.append(item.get_content())
        else:
            book_rsrc[os.path.basename(item.get_name())] = item.get_content()

    return meta_data, book_docs, book_rsrc

def prep_content(docs, resources):
    # Reformat the content to display on the frontend
    for count, i in enumerate(docs):
        page_content = BeautifulSoup(i, "html.parser")
        # Replace all <img> src with base64 version of the image
        for img in page_content.find_all("img"):
            img_name = os.path.basename(img["src"])
            img['src'] =  f"data:image/jpeg;base64,{utils.img_to_base64(resources[img_name])}"
        html_content = str(page_content.body).replace("<body>", "").replace("</body>", "")
        html_content = html_content.replace('"', "'")
        html_content = html_content.splitlines()
        html_content = " ".join(html_content)
        # JavaScript does not support multiline strings so the strings
        # are written like this for readability
        html_content = (
            f"<div class='page' data-booktype='epub' style='width: 210mm' id='{count}'>"
                "<div class='page-content' style='padding: 1.5cm'>"
                    f"{html_content}"
                "</div>"
            "</div>"
        )
        js_code = (
            'let read_zone = document.getElementsByClassName("read-zone")[0];'
            # The string in 'html_content' already used single quote so the JS
            # code should use double quote
            f'read_zone.innerHTML += "{html_content}";'
        )
        yield js_code
