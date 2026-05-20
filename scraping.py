import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: URL
url = "http://quotes.toscrape.com"

# Step 2: Request
response = requests.get(url)

# Step 3: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Extract Data
quotes = soup.find_all("span", class_="text")

data = []
for quote in quotes:
    data.append(quote.text)

# Step 5: Save to CSV
df = pd.DataFrame(data, columns=["Quotes"])
df.to_csv("quotes.csv", index=False)

print("Data scraped successfully!")