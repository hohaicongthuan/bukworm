import os

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

import utils


def read(file):
    """
    Read and prepare content to show on the frontend
    """
    book = epub.read_epub(file)

    for item in book.get_items():
        if (item.get_type() == ebooklib.ITEM_DOCUMENT):
            page_content = BeautifulSoup(item.get_body_content(), "html.parser")
            item_name, _ = os.path.splitext(os.path.basename(item.get_name()))

            # Replace all img links to base64 encoded ones
            for img in page_content.find_all("img"):
                img_data = book.get_item_with_href(img["src"].replace("../", "")).get_content()
                encoded_img = utils.img_to_base64(img_data)
                img["src"] =  f"data:image/jpeg;base64,{encoded_img}"

            # Reformat all IDs
            for i in page_content.find_all(id=True):
                i["id"] = f"{item_name}-{i['id']}"

            # Reformat all links
            for i in page_content.find_all(href=True):
                if (
                    i["href"].startswith("http") or
                    "@" in i["href"] or
                    i["href"].startswith("mailto")
                ): # External link or Email link
                    # Set this so that the link'll open in external browser not
                    # right in the app (the app itself is kinda a browser)
                    i["target"] = "_blank"
                elif (i["href"].startswith("#")): # Internal link within this page
                    i["href"].replace("#", f"#{item_name}-{i['href']}")
                elif ("#" in i["href"]): # Internal link point to a section of another page
                    split = i["href"].split("#")
                    target_name, _ = os.path.splitext(os.path.basename(split[0]))
                    i["href"] = f"#{target_name}-{split[1]}"
                elif (): # Email link
                    continue
                elif ("." in i["href"]): # Internal link point to another page
                    target_name, _ = os.path.splitext(os.path.basename(i["href"]))
                    i["href"] = f"#{target_name}"
                else:
                    print(f"This link is neither internal nor external: {i}")

            html_content = str(page_content).replace('"', "'")
            html_content = " ".join(html_content.splitlines())
            # JavaScript does not support multiline strings so the strings
            # are written like this for readability
            html_content = f"""
                <div class='page' style='width: 210mm' id='{item_name}'>
                    <div class='page-content' style='padding: 1.5cm'>
                        {html_content}
                    </div>
                </div>
            """
            html_content = " ".join(html_content.splitlines())
            js_code = f"""
                let read_zone = document.getElementsByClassName("read-zone")[0];
                read_zone.innerHTML += "{html_content}";
            """
            js_code = " ".join(js_code.splitlines())

            yield js_code


def prep_info(file):
    """
    Prepare file info content to display on the frontend
    """
    book = epub.read_epub(file)

    # Each of these variables will contain a list
    title = book.get_metadata('DC', 'title')
    author = book.get_metadata('DC', 'creator')
    contributor = book.get_metadata('DC', 'contributor')
    publisher = book.get_metadata('DC', 'publisher')
    rights = book.get_metadata('DC', 'rights')
    coverage = book.get_metadata('DC', 'coverage')
    date = book.get_metadata('DC', 'date')
    description = book.get_metadata('DC', 'description')

    # If the list is not empty, there'll always be a tuple in it
    title, *_ = title[0] if title else ("", "")
    author, *_ = author[0] if author else ("", "")
    contributor, *_ = contributor[0] if contributor else ("", "")
    publisher, *_ = publisher[0] if publisher else ("", "")
    rights, *_ = rights[0] if rights else ("", "")
    coverage, *_ = coverage[0] if coverage else ("", "")
    date, *_ = date[0] if date else ("", "")
    description, *_ = description[0] if description else ("", "")

    return_content = f"""
    Title: {title}<br>
    Author: {author}<br>
    Contributer: {contributor}<br>
    Publisher: {publisher}<br>
    Rights: {rights}<br>
    Coverage: {coverage}<br>
    Date: {date}<br>
    Description: {description}
    """

    # JavaScript doesn't support multiline strings
    return_content = return_content.splitlines()
    return_content = " ".join(return_content)

    return return_content

def prep_toc(file):
    """
    Prepare Table of Content to display on the frontend
    
    Note: This function returns a flat, one level list Table of Content (TOC)
    based on the file list returned by the epub.get_items() function (for now),
    which is NOT a proper way to parse TOC. It should be parsed using the file
    "toc.ncx" in the EPUB file.
    """
    book = epub.read_epub(file)
    toc = ""
    for item in book.get_items():
        if (item.get_type() == ebooklib.ITEM_DOCUMENT):
            item_name = os.path.basename(item.get_name())
            item_name, _ = os.path.splitext(item_name)
            toc += f"<li><a href='#{item_name}'>{item_name}</a></li>"
    return f"<ul>{toc}</ul>"


# FOR TESTING PURPOSES ONLY
# if __name__ == "__main__":
    # for i in ["test/test_1.epub", "test/test_2.epub", "test/test_3.epub", "test/test_4.epub"]:
    #     book = epub.read_epub(i)
    #     for item in book.get_items():
    #         print(item.get_name())
    #     print()

    # book = read("test/test_3.epub")
    # for i in book:
    #     print(i, "\n")
    