# Webscrapping
Scrapping of the website Flipkart.com for several phone products. We will be utilizing the power of web scraping using three different tools: BeautifulSoup, Selenium, and Scrapy. There are 2 files saved, including each phone link and details respectively. We then use the phones data to analyze different sale trending using different algorithms.


This project is done as a part of program at WNE, University of Warsaw. Our project aims to create a comprehensive mobile phone dataset by scraping data from the popular e-commerce website Flipkart.com. We will be utilizing the power of web scraping using three different tools: BeautifulSoup, Selenium, and Scrapy. We will save it in a structured format, such as CSV or Text for each of the methods used. The information that is extracted is the same in each case and for each method, there are 2 files saved. One file contains the links of each webpage for each phone. The second file contains useful information from each webpage to gather phone specifications.


Project Presentation-video about how to run these 3 scrapers
How to run？（text version）
BeautifulSoup
Scrapy
To run Scrapy using the command line, follow these steps:

Open a terminal or command prompt on your system.

Navigate to the directory where your Scrapy project is located. This is the directory that contains the scrapy.cfg file.

Use the scrapy crawl command followed by the spider name to run the spider. For example, if your spider's name is "myspider", run the following command: scrapy crawl myspider

Scrapy will start executing the spider, sending requests, and processing the responses. You will see the log messages and output in the terminal/command prompt.

You can also use additional options with the "scrapy crawl" command to customize the behavior of the spider:

"-o output.json" or "-o output.csv" : Use these options to specify the output format for the scraped data. You can choose to save the data in JSON or CSV format. For example: "scrapy crawl myspider -o output.csv"

Selenium
Running code immediately in Pycharm or other Idea ,and following step is automatic.
make sure that you have install package selenium,time,csv
finally the output will be a .csv document.
