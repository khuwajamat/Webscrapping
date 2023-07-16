from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import csv

gecko_path = 'C:/Users/yangxinchen/Desktop/geckodriver'
ser = Service(gecko_path)
options = webdriver.chrome.options.Options()
# options.headless = False
url = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&marketplace=FLIPKART&page='

# Create a CSV file and write the header
csv_file = open('scraped_data.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(csv_file)
header = [
    "Name",
    "Price",
    "Discount",
    "Average Rating",
    "Rating Count",
    "Review Count",
    "Memory Details",
    "Screen Dimension",
    "Lens Detail",
    "Battery Capacity",
    "Processor",
    "Warranty",
    "Color",
    "Product Link"
]
writer.writerow(header)

def geturl(pagenum):
    driver = webdriver.Chrome(options=options, service=ser)
    driver.get(url + str(pagenum))
    product_link = []
    time.sleep(6)

    # Find all the product containers
    product_containers = driver.find_elements(By.XPATH, "//a[@class='_1fQZEK']")
    for container in product_containers:
        product_link.append(container.get_attribute("href"))
    driver.quit()
    return product_link


# Actual program:
# time.sleep(6)

for i in range(1, 10):
    link_list = geturl(i)
    driver = webdriver.Chrome(options=options, service=ser)

    for i in range(len(link_list)):
        # time.sleep(6)
        driver.get(link_list[i])
        # Iterate over the product containers and extract the information
        print("product loop num:" + str(i))
        # Extract the product information
        name = driver.find_element(By.XPATH, "//span[contains(@class, 'B_NuCI')]").text
        print("name:" + str(name))
        split_string = name.split("(")
        color_orgin = split_string[1].strip(")")
        color = color_orgin.split(",")[0]

        price = driver.find_element(By.XPATH, "//div[contains(@class, '_30jeq3 _16Jk6d')]").text

        # Check if the product has a discount
        try:
            discount = driver.find_element(By.XPATH, "//div[contains(@class, '_3Ay6Sb _31Dcoz')]").text
        except NoSuchElementException:
            discount = "No Discount"

        avg_rating = driver.find_element(By.XPATH, "//div[contains(@class, '_3LWZlK')]").text
        rating_count_review_coun = driver.find_element(By.XPATH, "//span[contains(@class, '_2_R_DZ')]").text
        rating_count = rating_count_review_coun.split("&")[0]
        review_count = rating_count_review_coun.split("&")[1]

        # Initialize variables for optional fields
        processor = "N/A"
        screen_dimension = "N/A"
        warranty = "N/A"
        RAM = "N/A"
        battery_capacity = "N/A"
        lens_detail = "N/A"
        memory_details = "N/A"

        try:
            processor_element = driver.find_element(By.XPATH,
                                                    '//td[contains(text(),"Processor Type")]/following-sibling::td/ul/li')
            processor = processor_element.text
        except NoSuchElementException:
            processor = None

        try:
            screen_dimension = driver.find_element(By.XPATH,
                                                   '//div[contains(text(), "Highlights")]/following-sibling::div[1]/ul/li[2]').text
        except NoSuchElementException:
            screen_dimension = None

        try:
            warranty = driver.find_element(By.XPATH, '//div[@class="_352bdz"]').text
        except NoSuchElementException:
            warranty = None

        try:
            battery_capacity = driver.find_element(By.XPATH,
                                                   '//div[contains(text(), "Highlights")]/following-sibling::div[1]/ul/li[4]').text
        except NoSuchElementException:
            battery_capacity = None

        try:
            lens_detail = driver.find_element(By.XPATH,
                                              '//div[contains(text(), "Highlights")]/following-sibling::div[1]/ul/li[3]').text
        except NoSuchElementException:
            lens_detail = None

        try:
            memory_details = driver.find_element(By.XPATH,
                                                 '//div[contains(text(), "Highlights")]/following-sibling::div[1]/ul/li[1]').text
        except NoSuchElementException:
            memory_details = None

        # Print the extracted information
        # print("Name:", name)
        # print("Price:", price)
        # print("Discount:", discount)
        # print("Average Rating:", avg_rating)
        # print("Rating Count:", rating_count)
        # print("Review Count:", review_count)
        # print("Memory Details:", memory_details)
        # print("Screen Dimension:", screen_dimension)
        # print("Lens Detail:", lens_detail)
        # print("Battery Capacity:", battery_capacity)
        # print("Processor:", processor)
        # print("Warranty:", warranty)
        # print("Color:", color)
        print("Product Link:", link_list[i])
        print()
        # Write the extracted information to the CSV file
        row = [
            name,
            price,
            discount,
            avg_rating,
            rating_count,
            review_count,
            memory_details,
            screen_dimension,
            lens_detail,
            battery_capacity,
            processor,
            warranty,
            color,
            link_list[i]
        ]
        writer.writerow(row)

        time.sleep(10)
    driver.quit()
# Close the CSV file
csv_file.close()
