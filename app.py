import requests
from bs4 import BeautifulSoup
import re
import json

def fetch_swc_registry_bugs():
    swc_url = "https://swcregistry.io/"
    response = requests.get(swc_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table')
    rows = table.find_all('tr')[1:]  # Skip the header row
    
    swc_data = []
    for row in rows:
        td_elements = row.find_all('td')
        if len(td_elements) >= 3:
            ID = td_elements[0].get_text().strip()
            ID_link = td_elements[0].find('a', href=True)['href']
            title = td_elements[1].get_text().strip()
            cwe_relationship = td_elements[2].get_text().strip()
            cwe_link = td_elements[2].find('a', href=True)['href']
            
            swc_data.append({
                "ID": ID,
                "ID_Link": ID_link,
                "Title": title,
                "CWE_Relationship": cwe_relationship,
                "CWE_Link": cwe_link
            })
    
    return swc_data

def fetch_cwe_membership(cwe_link):
    response = requests.get(cwe_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Navigate to the 'Memberships' section and target rows with 'class="primary Category"'
    memberships_div = soup.find('div', {'id': 'Memberships'})
    categorizations = []
    if memberships_div:
        for tr in memberships_div.find_all('tr', {'class': 'primary Category'}):
            td_elements = tr.find_all('td')
            if len(td_elements) >= 4:
                if td_elements[3].get_text().startswith("Comprehensive Categorization:"):
                    category = td_elements[3].get_text().replace("Comprehensive Categorization: ", "").strip()
                    link = td_elements[3].find('a', href=True)['href']
                    number = td_elements[2].get_text().strip()
                    categorizations.append({
                        "Type": "Comprehensive Categorization",
                        "Category": category,
                        "Number": number,
                        "Link": link
                    })
    return categorizations

def main():
    swc_data = fetch_swc_registry_bugs()
    
    # Loop through each row to fetch the membership details
    for row in swc_data:
        cwe_link = row["CWE_Link"]
        if cwe_link:  # Check if the link exists
            categorizations = fetch_cwe_membership(cwe_link)
            row["Categorizations"] = categorizations
    
    # Write the data to a JSON file
    with open('data/swc_cwe_data.json', 'w') as outfile:
        json.dump(swc_data, outfile, indent=4)

if __name__ == "__main__":
    main()