import fitz

import utils

def load_page(file_path, num):
    file = fitz.open(file_path)
    page = file.load_page(int(num))
    page_img = page.get_pixmap(dpi=96).tobytes()
    page_img = f"<img width='100%' height='100%' src='data:image/png;base64,{utils.img_to_base64(page_img)}'>"
    return page_img

def read(file_path):
    """
    Read and show placeholders for all the pages.
    """
    file = fitz.open(file_path)
    for i in range(file.page_count):
        page = file.load_page(i)
        page_width = int(page.mediabox.width)
        page_height = int(page.mediabox.height)

        # JavaScript does not support multiline strings so the strings
        # are written like this for readability
        html_content = (
            f"<div class='page' data-booktype='pdf' data-filepath='{file_path}' style='width: {page_width}pt; height: {page_height}pt;' id='{i}'></div>"
        )
        js_code = (
            'let read_zone = document.getElementsByClassName("read-zone")[0];'
            # The string in 'html_content' already used single quote so the JS
            # code should use double quote
            f'read_zone.innerHTML += "{html_content}";'
        )

        yield js_code

# Testing purpose only
# if __name__ == "__main__":
#     file = fitz.open("test/test_4.pdf")
#     pages = []
#     for i in range(file.page_count):
#         page = file.load_page(i)
#         print(page.mediabox.width)
#         print(page.mediabox.height)