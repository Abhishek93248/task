import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

# Navigate to flipkart.com
driver.get("https://www.flipkart.com/")
# time.sleep(5)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Samsung Galaxy S10")
search_box.submit()
# time.sleep(5)

mobiles_accessories_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@title='Mobiles & Accessories']"))
)
mobiles_accessories_link.click()


price_high_to_low_filter = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//div[text()='Price -- High to Low']"))
)
price_high_to_low_filter.click()


samsung_filter_div = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='SAMSUNG']"))
)
samsung_filter_div.click()

time.sleep(5)



# checkbox = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div/div[1]/div/section[4]/label/input"))
#     )
# checkbox=driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div/div[1]/div/section[4]/label/input")
# driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
# # time.sleep(10)
# # print(checkbox)
# checkbox.click()

# if not checkbox.is_selected():

#     checkbox.click()

#     print("Flipkart Assured checkbox selected successfully!")



WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@data-id, 'MOB')]")))

results = driver.find_elements(By.XPATH, "//div[contains(@data-id, 'MOB')]")

def print_product(result,i):
    
    product_link = result.find_element(By.XPATH, ".//a").get_attribute("href")
    product_name = result.find_element(By.XPATH, ".//a/div[2]/div[1]/div[1]").text
    product_price = result.find_element(By.XPATH, ".//a/div[2]/div[2]/div[1]/div[1]/div[1]").text
    print("Product Name:", product_name)
   
    print("Product Price:", product_price)
    print("Product Link:", product_link)


i=0
while i<len(results):
    try:
        print_product(results[i],i)
        i=i+1
    except Exception as e:
        results = driver.find_elements(By.XPATH, "//div[contains(@data-id, 'MOB')]")



   


# for result in results:
#     print_product(result)
      # Introduce a 1-second delay between printing each product
# print_product(results[4])
driver.quit()
