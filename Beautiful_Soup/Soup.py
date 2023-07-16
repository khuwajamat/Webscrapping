import pandas as pd
import csv
from urllib import request
import re
import requests
from bs4 import BeautifulSoup

#we are using 6 links enough to get 100 webpages which we will be scrapping information from
url = ['https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&marketplace=FLIPKART&page=1','https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&marketplace=FLIPKART&page=2','https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&marketplace=FLIPKART&page=3','https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&marketplace=FLIPKART&page=4','https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&marketplace=FLIPKART&page=5','https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&marketplace=FLIPKART&page=6']

#Empty lists to be filled with scrapped info

phone_links = []
phone_specs =[]

for i in url:
    try:
        response = requests.get(i)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the phone details on the page
        phone_details = soup.find_all('div', {'class': '_1AtVbE'})

        for phone in phone_details[3:]:

            herf = str('https://www.flipkart.com'+phone.find('a')['href'])
            phone_links.append(herf)
            
            #creating a scrapper for each page and extracting info
            response2 = requests.get(herf)
            soup2 = BeautifulSoup(response.content, 'html.parser')



            #Extract relevant information
            name = phone.find('div', {'class': '_4rR01T'}).text.split(">")
            price = phone.find('div', {'class': '_30jeq3 _1_WHN1'}).text.split(">")
            rating = phone.find('div', {'class': '_3LWZlK'}).text.split(">")
            Memory = phone.find('li', {'class': 'rgWa7D'}).text
            Screen = phone.find('li', {'class': 'rgWa7D'}).find_next_sibling().text
            Camera = phone.find('li', {'class': 'rgWa7D'}).find_next_sibling().find_next_sibling().text
            Battery = phone.find('li', {'class': 'rgWa7D'}).find_next_sibling().find_next_sibling().find_next_sibling().text
            Processor = phone.find('li', {'class': 'rgWa7D'}).find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text
            Warranty = phone.find('li', {'class': 'rgWa7D'}).find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text

            
            phone_specs.append(', '.join([item[0] for item in [name, price, rating]])+ Memory+Screen+ Camera+ Battery+Warranty+Processor)
    except:
        print('error here')


#Export the Phone_links as a text file
with open('Phone_links.txt', 'w') as outfile:
    outfile.writelines((str(i)+'\n' for i in phone_links))

df = pd.DataFrame(phone_specs)

# Export the DataFrame phone_specs as a text file
df.to_csv('Phone specs.txt', sep='\t', index=False)

