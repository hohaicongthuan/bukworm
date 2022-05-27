import marko

def read(file_path):
    file = open(file_path, "r", encoding='utf-8')
    file_content = ''
    for i in file.readlines():
        file_content += str(i)
    parsed_text = marko.convert(file_content)
    return parsed_text

def prep_content(str_content):
    page_content = '<div class="page"><div class="page-content">' + str(str_content) + '</div></div>'
    return page_content

# if __name__ == "__main__":
#     pass