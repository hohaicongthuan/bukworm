import fitz

from lib import utils

def read(file_path):
    file = fitz.open(file_path)
    pages = []
    for i in range(file.page_count):
        page = file.load_page(i).get_pixmap(dpi=96).tobytes()
        pages.append("<div class='page' style='width: fit-content' id='page-{}'><img style='width: 210mm;' src='data:image/png;base64,{}'></div>".format(i, utils.img_to_base64(page)))
    return pages

# if __name__ == "__main__":
#     pass