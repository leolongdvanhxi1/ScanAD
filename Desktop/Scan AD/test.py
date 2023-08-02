from bs4 import BeautifulSoup

def extract_data_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.find_all(['strong', 'span', 'h3'])
    output = {}

    given_titles = ['Initial Access', 'Execution', 'Privilege Escalation', 'Defense Evasion', 'Credential Access', 'Discovery', 'Lateral Movement']
    current_title = None
    current_values = []
    for element in elements:
        if element.name == 'strong':
            title = element.text.strip()
            if title in given_titles:
                if current_title is not None:
                    output[current_title] = current_values
                current_title = title
                current_values = []
        elif element.name == 'span':
            if current_title is not None:
                value = element.text.strip()
                current_values.append(value)
        elif element.name == 'h3':
            if current_title is not None:
                output[current_title] = current_values
            current_title = None
            current_values = []

    if current_title is not None:
        output[current_title] = current_values

    return output

file_path = 'rule.html'
result = extract_data_from_html(file_path)
print(result)
