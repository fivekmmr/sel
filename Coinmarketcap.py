from bs4 import BeautifulSoup
import requests

website = requests.get('https://coinmarketcap.com/').text
soup = BeautifulSoup(website, 'html.parser')

table_body = soup.tbody
table_rows = table_body.contents

prices = {}

for tr in table_rows[:10]:
        name, price = tr.contents[2:4]
        fixed_name = name.p.string
        fixed_price = price.a.string

        prices[fixed_name] = fixed_price

print(prices)