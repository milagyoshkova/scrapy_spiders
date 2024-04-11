import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/98.0")


driver = webdriver.Firefox(options=firefox_options)

try:
    with open("C:\\Users\\GZHel\\Desktop\\dpc-blank\\dpc_proj\\db\\vexio_info.json", "w", encoding="utf-8") as file:

        
        # Iterate through pages of products (from 1 to 11)
        for page_number in range(1, 12):    #this range is to test the bottom line of commented is all information   
        # for page_number in range(1, 96724):    


            page_url = f"https://www.vexio.ro/desktop-server-monitoare/pagina{page_number}/"
            driver.get(page_url)
            print(f"Scanning page: {page_url}")

            
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "product_box_1")))
            time.sleep(2)  

           
            for i in range(1, 25):
                try:
                    #
                    product_box_xpath = f'//*[@id="product_box_{i}"]'
                    product_title_xpath = f'{product_box_xpath}//div/div[2]/h2/a'
                    product_image_xpath = f'{product_box_xpath}//div/div[1]/a[1]/img'
                    product_price_xpath = f'{product_box_xpath}//div/div[4]/div[2]/div[1]/div[2]/strong'
                    product_old_price_xpath = f'{product_box_xpath}//div/div[4]/div[2]/div[1]/div[1]'
                    product_availability_xpath = f'{product_box_xpath}//div/div[4]/div[1]'
                    
                    
                    product_title_element = driver.find_element(By.XPATH, product_title_xpath)
                    product_title = product_title_element.text
                    
                    product_image_element = driver.find_element(By.XPATH, product_image_xpath)
                    product_image_url = product_image_element.get_attribute("src")
                    
                    product_price_element = driver.find_element(By.XPATH, product_price_xpath)
                    product_price = product_price_element.text
                    
                    try:
                        product_old_price_element = driver.find_element(By.XPATH, product_old_price_xpath)
                        product_old_price = product_old_price_element.text
                    except NoSuchElementException:
                        product_old_price = "No old price"
                    
                    product_availability_element = driver.find_element(By.XPATH, product_availability_xpath)
                    product_availability = product_availability_element.text
                    
                    
                    file.write(f"Product {i} info on page {page_number}:\n")
                    file.write(f"Title: {product_title}\n")
                    file.write(f"Image URL: {product_image_url}\n")
                    file.write(f"Current Price: {product_price}\n")
                    file.write(f"Old Price: {product_old_price}\n")
                    file.write(f"Availability: {product_availability}\n\n")
                    
                    time.sleep(1) 
                except NoSuchElementException as e:
                    print(f"Error extracting info for product {i} on page {page_number}: {str(e)}\n")
            
            if page_number == 3:
                try:
                    button_span_xpath = '/html/body/div[12]/div/div/div[1]/button/span'
                    button_span_element = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, button_span_xpath))
                    )
                    time.sleep(1)  
                    button_span_element.click() 
                    print("Successfully clicked the close button on the third page.")
                except NoSuchElementException:
                    print("Close button not found on the third page.")
    
    print("Product information from the first 11 pages successfully written to 'vexio_info.json'")

except Exception as e:
    print("Error extracting information from the page:", str(e))

finally:
    
    driver.quit()
