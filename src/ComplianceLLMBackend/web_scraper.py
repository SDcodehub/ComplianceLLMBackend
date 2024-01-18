import requests
from bs4 import BeautifulSoup


def extract_compliance_information(url, output_file):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Use sets to track unique entries
        unique_headings = set()
        unique_paragraphs = set()
        unique_lists = set()
        unique_tables = set()
        
        # Extract all elements in the order they appear
        with open(output_file, 'w', encoding='utf-8') as file:
            for element in soup.find_all():
                if element.name == 'h2' or element.name == 'h3':
                    heading_text = element.text.strip()
                    if heading_text not in unique_headings:
                        file.write(f"{heading_text}\n\n")
                        unique_headings.add(heading_text)
                elif element.name == 'p':
                    paragraph_text = element.text.strip()
                    if paragraph_text not in unique_paragraphs:
                        file.write(f"{paragraph_text}\n\n")
                        unique_paragraphs.add(paragraph_text)
                elif element.name == 'ul':
                    list_items = [li.text.strip() for li in element.find_all('li')]
                    unique_list_items = frozenset(list_items)
                    if unique_list_items not in unique_lists:
                        for li in unique_list_items:
                            file.write(f"- {li}\n")
                        file.write('\n')
                        unique_lists.add(unique_list_items)
                elif element.name == 'table':
                    table_rows = []
                    for row in element.find_all('tr'):
                        columns = [column.text.strip() for column in row.find_all(['th', 'td'])]
                        table_rows.append('\t'.join(columns))
                    unique_table_rows = frozenset(table_rows)
                    if unique_table_rows not in unique_tables:
                        for row in unique_table_rows:
                            file.write(f"{row}\n")
                        file.write('\n')
                        unique_tables.add(unique_table_rows)
        
        print(f"Information written to {output_file}")
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")


