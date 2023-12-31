import requests
from bs4 import BeautifulSoup
import json
from swc_registry import SWC
import re

def fetch_swc_registry_bugs():
    # Create an SWC instance to access the registry content
    swc_instance = SWC('SWC-100')  # We just use 'SWC-100' as a dummy to get an instance
    registry = swc_instance._swc_content
    
    swc_data = []
    for swc_id, details in registry.items():
        swc = SWC(swc_id)

        cwe_relationship = swc.relationships
        # Extracting the CWE link using regex
        cwe_link_match = re.search(r'\((https?://[^\)]+)\)', cwe_relationship)
        cwe_link = cwe_link_match.group(1) if cwe_link_match else ''

        swc_data.append({
            "ID": swc_id,
            "ID_Link": f"https://swcregistry.io/docs/{swc_id}",  # Assuming a standard link structure
            "Title": swc.title,
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
            row["CWECompCat"] = categorizations
    
    # Write the data to a JSON file
    with open('data/swc_cwe_data.json', 'w') as outfile:
        json.dump(swc_data, outfile, indent=4)

if __name__ == "__main__":
    main()
