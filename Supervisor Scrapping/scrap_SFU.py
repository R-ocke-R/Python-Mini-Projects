import csv
import requests
from bs4 import BeautifulSoup


url_SFU = "https://www.sfu.ca/fas/computing/people/faculty.html"
base_url = "https://www.sfu.ca"
r = requests.get(url_SFU)
soup = BeautifulSoup(r.text, "lxml")

supervisors = []

for profile in soup.find_all('div', class_='clf-fdi__profile'):
    # Name and profile link
    name_tag = profile.find('a', class_='faculty-name')
    full_name = name_tag.text.strip()
    profile_link = base_url + name_tag['href']

    # Split name "Last, First"
    if ',' in full_name:
        last_name, first_name = [n.strip() for n in full_name.split(',', 1)]
    else:
        first_name, last_name = full_name, ''

    # Position
    position_tag = profile.find('span', class_='position')
    position = position_tag.text.strip() if position_tag else ''

    # Email
    email_tag = profile.find('a', class_='email')
    email = email_tag.text.strip() if email_tag else ''

    supervisors.append([first_name, last_name, profile_link, position, email])



with open("sfu_supervisors.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # Header
    writer.writerow(["First Name", "Last Name", "Profile Link", "Position", "Email"])
    # Data
    writer.writerows(supervisors)

print(f"CSV created successfully with {len(supervisors)} entries.")