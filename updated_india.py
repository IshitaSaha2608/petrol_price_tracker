import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

base_url = "https://www.mypetrolprice.com/4/Petrol-price-in-"
city = input("Enter the city: ")
encoded_city = quote(city)  # Properly encode the city name for the URL
url = f"{base_url}{encoded_city}"
response = requests.get(url)
print(response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    price_span = soup.find('span', itemprop='price')  # Find the <span> element with itemprop='price'

    if price_span:
        price = price_span.get_text()
        print(f"Petrol price in {city}: {price}")
    else:
        print("Price information not found on the page.")
else:
    print("Error: 401")
