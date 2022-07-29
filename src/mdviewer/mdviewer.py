from bs4 import BeautifulSoup
import marko

def read(file_path):
    """
    Read and prepare content to show on the frontend
    """
    with open(file_path, "r", encoding='utf-8') as f:
        file_content = f.read()
        parsed_text = marko.convert(file_content)
        parsed_text = parsed_text.replace('"', "'")
        page_content = f"""
            <div class='page' style='width: 210mm'>
                <div class='page-content' style='padding: 1.5cm'>
                    {parsed_text}
                </div>
            </div>
        """
        # JavaScript does not support multiline strings
        page_content = " ".join(page_content.splitlines())
        js_code = f"""
            let read_zone = document.getElementsByClassName("read-zone")[0];
            read_zone.innerHTML += "{page_content}";
            """
        js_code = " ".join(js_code.splitlines())
        yield js_code


def prep_toc(file_path):
    """
    Prepare file Table of Content to display on the frontend
    """
    parsed_text = ""
    with open(file_path, "r", encoding="utf-8") as f:
        file_content = f.read()
        parsed_text = marko.convert(file_content)

    soup = BeautifulSoup(parsed_text, "html.parser")
    toc = ""
    for h in soup.find_all([head for head in [f"h{level}" for level in range(1, 7)]]):
        toc += f"<li><a href='#'>{h.string}</a></li>"

    return f"<ul>{toc}</ul>"


# TESTING PURPOSE ONLY
# if __name__ == "__main__":
#     print(prep_toc("README.md"))
