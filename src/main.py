# Built-in Libraries Import
import os

# Third-party Libraries Import
import webview

# Internal Libraries Import
from lib.epubviewer import epubviewer
from lib.mdviewer import mdviewer
from lib.msdocviewer import msdocviewer
from lib.pdfviewer import pdfviewer

def get_content(file_path):
    # Read EPUB file, prepare content and send to JS to display

    file_name, file_ext = os.path.splitext(file_path)

    match file_ext.lower():
        case '.epub':
            meta_inf, docs, rsrc = epubviewer.read(file_path)
            book_content = epubviewer.prep_content(docs, rsrc)
            return book_content
        case '.md':
            book_content = mdviewer.read(file_path)
            book_content = mdviewer.prep_content(book_content)
            return book_content
        case _:
            book_content = ''
            return book_content

def open_file():
    types = ('Ebook file (*.epub;*.pdf;*.docx;*.md)', 'All files (*.*)')
    path = window.create_file_dialog(dialog_type=webview.OPEN_DIALOG, directory='.', allow_multiple=False, file_types=types)
    return path

def exit():
    window.destroy()

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

if __name__ == "__main__":

    window = webview.create_window("BUKWORM", "frontend/index.html")
    window.expose(get_content, open_file, exit)
    webview.start(main_func, window, debug=True)

    # for item in book.get_items():
    #     print("==================================================================================")
    #     print("ITEM:", item)
    #     print("----------------------------------------------------------------------------------")
    #     print("NAME:", os.path.basename(item.get_name()))
    #     # print("----------------------------------------------------------------------------------")
    #     # print(item.get_content())
    #     print("==================================================================================")
