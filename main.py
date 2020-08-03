from bs4 import BeautifulSoup
import urllib.request
import re
import csv


#Website you will be scraping from
url = "https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709&PageSize=96"

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
regex = re.compile('^tocsection-')
workbook = "products.csv"
file = open(workbook, "w")
models = []
prices = []

#Finding All the data from within that tag
product_model = soup.findAll("a", attrs={"class": "item-title"})
product_price = soup.find_all("li", attrs={"class": "price-current"})


#Parsing the data from all the extra html

for a in product_model:
    models.append(a.getText()[0:70].strip())
for li in product_price:
    prices.append(li.getText().split('\n')[0].strip()[0:7])


#with open('products.csv', 'a', newline='') as f:
    #r = csv.reader(f)
    #data = [line for line in r]




#converting list from data to Dictionary
dictionary = dict(zip(models, prices))


with open('products.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Model','Prices'])
    
    
    
   
    
    #writing to CSV file 
    for key, value in dictionary.items():
        writer.writerow([key, value])
    print('Your results have been printed to a csv file')
file.close()