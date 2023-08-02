from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import requests
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

url = "https://www.shoppersdrugmart.ca/en/store-locator/store/"
start_num = 2
end_num = 9999
found_data = []
missing_data = []

webdriver_service = Service('C:\\Temp\\chromedriver.exe')
options = Options()
options.binary_location = 'C:\\Temp\\chrome-win64\\chrome.exe'

driver = webdriver.Chrome(service=webdriver_service, options=options)
wait = WebDriverWait(driver, 10)

def extract_location(s):
    start = s.find('-') + 1 # Find the position of hyphen and add 1 to start after it
    end = s.find('in') # Find the position of 'in'
    return s[start:end].strip() # Extract the substring and remove any leading or trailing spaces


with open('pharmacies.csv', 'w', newline='', encoding='utf-8') as file:  # write headers to CSV file
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['First name', 'Last name', 'Store number', 'Drug store name', 'Street address', 'City Province Postal code', 'Phone'])

with open('missing_data.txt', 'w') as file:  # write header to missing data file
    file.write("Store numbers with no data or 404 error:\n")

while start_num <= end_num:
    try:
        response = requests.get(url + str(start_num))
        if response.status_code != 200:  # if page does not load correctly
            print(f"Page {start_num} not found")
            missing_data.append(start_num)
            with open('missing_data.txt', 'a') as file:  # write missing data to a file after each page
                file.write(f"{start_num}\n")
            start_num += 1
            continue

        driver.get(url + str(start_num))

        pharmacist = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'header__pharmasists-owner-button')]"))).text
        pharmacists = pharmacist.split(', ') 

        drug_store_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//h1[contains(@class, 'header__heading-label')]"))).text or ""
        drug_store_name = extract_location(drug_store_name)
        
        street_address = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='details__address']/p[2]"))).text or ""
        city_province_postal_code = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='details__address']/p[3]"))).text or ""

        phone = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='details__contact-phone']/a[1]"))).text or ""
        
        if len(pharmacists) == 0:
            print(f"No pharmacist found on page {start_num}")
            missing_data.append(start_num)
            with open('missing_data.txt', 'a') as file:  # write missing data to a file after each page
                file.write(f"{start_num}\n")
            start_num += 1
        else:
            for pharmacist in pharmacists:
                full_name = pharmacist.strip().split(' ')
                if len(full_name) >= 2: # At least a first name and last name
                    first_name = full_name[0]
                    last_name = ' '.join(full_name[1:])
                    found_data.append([first_name, last_name, start_num])

                    print(f"Data found on page {start_num}: {first_name}, {last_name}, {start_num}")

                    with open('pharmacies.csv', 'a', newline='', encoding='utf-8') as file:  # append to CSV file after each page
                        writer = csv.writer(file, delimiter=';')
                        writer.writerow([first_name, last_name, start_num, drug_store_name, street_address, city_province_postal_code, phone])

            start_num += 1

    except Exception as e:
        print(f"Error occurred on page {start_num}: {e}")
        start_num += 1  # increment start_num even in case of exceptions

driver.quit()  
