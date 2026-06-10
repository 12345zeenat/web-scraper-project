import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

print("Total jobs found:", len(jobs))

for job in jobs[:5]:
    title = job.find("h2").text.strip()
    print(title)
