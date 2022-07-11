import marko

def read(file_path):
    file = open(file_path, "r", encoding='utf-8')
    file_content = ''
    for i in file.readlines():
        file_content += str(i)
    parsed_text = marko.convert(file_content)
    return parsed_text

def prep_content(str_content):
    page_content = '<div class="page" style="width: 210mm"><div class="page-content" style="padding: 1.5cm">{}</div></div>'.format(str(str_content))
    return page_content

# if __name__ == "__main__":
#     pass