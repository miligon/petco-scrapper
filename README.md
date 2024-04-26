# Petco Scrapper

Script to look for offers in petco Mexico(my cats wants yummy food xD), this scripts uses BeautifulSoup4 to look in thec contents of the page.

The scripts reads a watch list named articulos_petco.txt, in this file is possible to configure many products and set a target price. When product has a price lower than the target price the script sends a telegram notification.

Requirements:
```
pip install bs4 requests
```

Set the TOKEN and chat_id variables with yours to make the telegram notification to work.

To run:
```
python main.py
```
