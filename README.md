Scrapy and Selenium Projects
This repository contains three projects that utilize web scraping techniques using Scrapy and Selenium.

1. Garmin Products Spider
Overview
The Garmin Products Spider (garmin_products) is a Scrapy spider designed to scrape product information from the Garmin Bulgaria website.

Usage
To run this spider, execute the following command:

bash
Copy code
scrapy crawl garmin_products -o "C:/Users/Desktop/dpc-blank/dpc_proj/db/results_garmin.json"

This command will start the spider and save the results to results_garmin.json file.

2. Brosbg Spider
Overview
The Brosbg Spider (brosbg) is a Scrapy spider that scrapes product information from the brosbg.com website.

Usage
To execute this spider, use the following command:

bash
Copy code
"C:/Users/Desktop/dpc-blank/dpc_proj/db/results_brosbg.json"
The spider will run and save the output to results_brosbg.json.

3. Vexio Info Extraction using Selenium
Overview
The Vexio Info Extraction script (selenium_vexi.py) uses Selenium with Python to extract product information from the vexio.ro website.

Usage
To run this script, execute it from the command line:

bash
Copy code
python selenium_vexi.py
The script will scrape data from the first 11 pages of products and save the results to vexio_info.json.
