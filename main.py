import requests
import time
from bs4 import BeautifulSoup

TOKEN = "xxxxxxxxxx:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
chat_id = "xxxxxxxxx"

def notify(item, price):
	message = "El articulo: " + item + " tiene un precio de:" + str(price)
	url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
	print(requests.get(url).json()) # this sends the message

def get_price(html_response):
    # Assuming the HTML response is stored in the variable 'html_response'
    soup = BeautifulSoup(html_response, 'html.parser')

    # Find the span element with class 'discountedPrice'
    price_span = soup.find('span', {'class': 'discountedPrice'})

    # Get the price text from the span element
    price = price_span.text.strip()

    # Print the price
    print(price)
    return float(price[1:])

def consulta_precio(url):
	try:
		headers = {
		    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30'
		}
		
		response = requests.get(url, headers=headers)
		
		return get_price(response.text)
		
	except:
		print("Error al realizar la consulta de: " + url)
		return 0.0

while(True):
	file = open('articulos_petco.txt', 'r')
	lista = file.readlines()
	
	for articulo in lista:
		url = articulo.split("|")[0]
		precio = float(articulo.split("|")[1])
		alternative = articulo.split("|")[2]
		price = consulta_precio(url)
		if (price < precio):
			notify(alternative, price)
			time.sleep(5)
			print("Hay oferta")
		else:
			print("No hay oferta")
			notify(alternative, price)
			time.sleep(5)
	print("\r\n Sleep 600 minutes")
	time.sleep(86400)
