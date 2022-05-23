import base64
import os

import ebooklib
from ebooklib import epub

from bs4 import BeautifulSoup

import webview

def img_to_base64(img):
    return base64.b64encode(img).decode('ascii')

def read_epub(file):
    book = epub.read_epub(file)
    
    # Get book's metadata
    meta_data = {}
    meta_data['title']          = book.get_metadata('DC', 'title')
    meta_data['author']         = book.get_metadata('DC', 'creator')
    meta_data['contributor']    = book.get_metadata('DC', 'contributor')
    meta_data['publisher']      = book.get_metadata('DC', 'publisher')
    meta_data['rights']         = book.get_metadata('DC', 'rights')
    meta_data['coverage']       = book.get_metadata('DC', 'coverage')
    meta_data['date']           = book.get_metadata('DC', 'date')
    meta_data['description']    = book.get_metadata('DC', 'description')

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
    prepped_content = []

    count = 0
    for i in docs:
        page_content = BeautifulSoup(i, 'html.parser')

        # Replace all <img> src with base64 version of the image
        for img in page_content.find_all('img'):
            img_name = os.path.basename(img['src'])
            img['src'] =  "data:image/jpeg;base64," + img_to_base64(resources[img_name])
        
        page_content = '<div class="page" id="page-' + str(count) + '"><div class="page-content">' + str(page_content.body) + '</div></div>'
        page_content = page_content.replace("<body>", "").replace("</body>", "")
        prepped_content.append(page_content)

        count += 1
    
    return prepped_content

def get_content():
    return book_content

def main_func(window):
    test_books = [
        "test/test_1.epub",
        "test/test_2.epub",
        "test/test_3.epub",
        "test/test_4.epub",
        "test/test_5.epub",
        "test/test_6.epub",
        "test/test_7.epub",
        "test/test_8.epub"
    ]

    global book_content
    meta_inf, docs, resources = read_epub("test/test_1.epub")
    book_content = prep_content(docs, resources)

if __name__ == "__main__":
    window = webview.create_window("An E-book Reader", "frontend/index.html")
    window.expose(get_content)
    webview.start(main_func, window, debug=True)

    # for item in book.get_items():
    #     print("==================================================================================")
    #     print("ITEM:", item)
    #     print("----------------------------------------------------------------------------------")
    #     print("NAME:", os.path.basename(item.get_name()))
    #     # print("----------------------------------------------------------------------------------")
    #     # print(item.get_content())
    #     print("==================================================================================")
