import requests
base_url = "https://www.mypetrolprice.com/4/Petrol-price-in-"
city = input("Enter the city :: ")
url = base_url+city
response = requests.get(url)
print(response.status_code)
if response.status_code ==200 :
    print(response.json())
    data = response.content
    print(data)
    price = data['div']['span itemprop = price']
    print(price)
else :
    print("Error:401")