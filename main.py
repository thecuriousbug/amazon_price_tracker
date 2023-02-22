import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

BUY_PRICE = 1500
MY_EMAIL = "sagar.python1810@gmail.com"
PASSWORD = "dfcflguuatrwvluy"

URL = "https://www.amazon.in/Rockerz-450-Wireless-Bluetooth-Headphone/dp/B07PR1CL3S/ref=sr_1_2?keywords=boat+450+rockerz&qid=1676608671&sprefix=boat+450+r%2Caps%2C404&sr=8-2"


response = requests.get(url=URL, headers={"Accept-Language":"en-US,en;q=0.8", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"})

soup = BeautifulSoup(response.content , "lxml")

title = (soup.find(id="productTitle").get_text().strip())
#print(title)



price = (soup.find(class_ = "a-price-whole").getText())
price = price.replace(",", "")  # Remove comma from string
price_as_float = float(price)

print(price_as_float)
#print(soup.prettify())


if price_as_float <= BUY_PRICE:
    message = f"{title} is now {price_as_float}"
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
    to_addrs=MY_EMAIL, 
    msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}")