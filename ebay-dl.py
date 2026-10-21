import argparse
import requests
from bs4 import BeautifulSoup
import json

parser = argparse.ArgumentParser()
parser.add_argument('--search', required=True)
parser.add_argument('--filename', required=True)
args = parser.parse_args()
output = []
url = 'https://www.ebay.com/sch/i.html?_nkw=' + args.search + "& _pgn=1"
response = ""
for i in range(1, 11):
    print(url)
    response = requests.get(url, timeout=10).text
    url = 'https://www.ebay.com/sch/i.html?_nkw=' + args.search + "&_pgn=" + str(i+1)
    soup = BeautifulSoup(response, "html.parser")
    for listing in soup.select('.s-item'):
        item = {}
        if listing.select_one(".s-item__title") == None:
            item['name'] = None
        else:
            item['name'] = listing.select_one(".s-item__title").text.strip()
        if listing.select_one(".s-item__price") == None:
            item['price'] = None
        else:
            item['price'] = int(listing.select_one(".s-item__price").text.strip().replace('$', "").split())
        if listing.select_one(".SECONDARY_INFO") == None:
            item['status'] = None
        else:
            item['status'] = listing.select_one(".SECONDARY_INFO").text.strip()
        if listing.select_one(".s-item__shipping") == None:
            item['shipping'] = None
        else:
            item['shipping'] = listing.select_one(".s-item__shipping").text.strip()
        if listing.select_one(".s-item__free-returns") == None:
            item['free_returns'] = None
        else:
            item['free_returns'] = listing.select_one(".s-item__free-returns").text.strip()
        if listing.select_one(".s-item__hotness") == None:
            item['items_sold'] = None
        else:
            item['items_sold'] = listing.select_one(".s-item__hotness").text.strip()
        output.append(item)

with open(args.search + '.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2)
    print('Saved products.json')