import os
import sys

import webview

from epubviewer import epubviewer
from mdviewer import mdviewer
from msdocviewer import msdocviewer
from pdfviewer import pdfviewer


def open_file(file_path=""):
    if (file_path == ""):
        types = ("Ebook file (*.epub;*.pdf;*.docx;*.md)", "All files (*.*)")
        file_path = window.create_file_dialog(dialog_type=webview.OPEN_DIALOG, directory=".", allow_multiple=False, file_types=types)
        file_path = file_path[0]
        if (file_path == ""):    # User cancelled the open file dialog
            return 0

    # print(f"File path = {path}")

    if not (os.path.isfile(file_path)):
        print("File does not exist or is not a file, please check again.")
        return -1

    _, file_ext = os.path.splitext(file_path)
    file_ext.lower()

    if (file_ext == ".epub"):
        meta_inf, docs, rsrc = epubviewer.read(file_path)
        book_content = epubviewer.prep_content(docs, rsrc)
    elif (file_ext == ".md"):
        book_content = mdviewer.read(file_path)
        book_content = mdviewer.prep_content(book_content)
    elif (file_ext == ".pdf"):
        book_content = pdfviewer.read(file_path)
    else:
        book_content = ""

    clean_read_zone()
    for i in book_content:
        window.evaluate_js(i)
        # print(i)
        
    return 0


def clean_read_zone():
    window.evaluate_js(
        "var read_zone = document.getElementsByClassName('read-zone')[0];"
        "read_zone.innerHTML = '';"
    )


def load_page(file_path, num):
    page_img = pdfviewer.load_page(file_path, num)
    return page_img
    # print(
    #     f"let page = document.getElementById('{num}');"
    #     f'page.innerHTML = "{page_img}";'
    # )
    # window.evaluate_js(
    #     f"let page = document.getElementById('{num}');"
    #     f'page.innerHTML = "{page_img}";'
    # )


def exit():
    window.destroy()


def main(window):
    if (len(sys.argv) > 1):
        file_path = sys.argv[1]
        open_file(file_path)


if __name__ == "__main__":

    window = webview.create_window("BUKWORM", "gui/index.html")
    window.expose(open_file, exit, load_page)
    webview.start(main, window, debug=True)

    # for item in book.get_items():
    #     print("==================================================================================")
    #     print("ITEM:", item)
    #     print("----------------------------------------------------------------------------------")
    #     print("NAME:", os.path.basename(item.get_name()))
    #     # print("----------------------------------------------------------------------------------")
    #     # print(item.get_content())
    #     print("==================================================================================")
