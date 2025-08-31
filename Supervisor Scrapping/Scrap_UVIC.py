import csv
import requests
from bs4 import BeautifulSoup


url_victoria_masc = "https://www.uvic.ca/graduate/programs/graduate-programs/credential-pages/electrical-computer-engineering-cred/electrical-and-computer-engineering-masc.php"
r = requests.get(url_victoria_masc)
soup = BeautifulSoup(r.text, "lxml")

supervisors = []

cards = soup.find_all("div", class_="card-body")

for card in cards:
    name_tag = card.find("h3", class_="card-title profile__name")
    title_tag = card.find("strong", class_="profile__title")
    area_tag = card.find("span", class_="profile__area")
    email_tag = card.find("a", class_="profile__email")

    name = name_tag.get_text(strip=True) if name_tag else ""
    title = title_tag.get_text(strip=True) if title_tag else ""
    area = area_tag.get_text(strip=True) if area_tag else ""
    email = email_tag.get_text(strip=True) if email_tag else ""

    supervisors.append([name, title, area, email])

# Save to CSV
with open("uvic_supervisors.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # Header
    writer.writerow(["Name", "Title", "Research Area", "Email"])
    # Data
    writer.writerows(supervisors)

print("✅ Data saved to uvic_supervisors.csv")