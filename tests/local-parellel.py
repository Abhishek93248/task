
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
import time

def print_product(result,i):
    
    product_link = result.find_element(By.XPATH, ".//a").get_attribute("href")
    product_name = result.find_element(By.XPATH, ".//a/div[2]/div[1]/div[1]").text
    product_price = result.find_element(By.XPATH, ".//a/div[2]/div[2]/div[1]/div[1]/div[1]").text
    print("Product Name:", product_name)
   
    print("Product Price:", product_price)
    print("Product Link:", product_link)


    
def get_browserstack_options(os_name, os_version, browser_name, browser_version):
    bstack_options = {
        "os": os_name,
        "osVersion": os_version,
        "browserName": browser_name,
        "browserVersion": browser_version,
        "sessionName": "BStack Build Name: " + "browserstack-build-1",
        "userName": "abhishektiwari_MxA5Hc",
        "accessKey": "5X2W7xo3D2HUouwB2915"
    }
    return bstack_options

# Define the platform-browser combinations
capabilites = [
    {"os": "Windows", "osVersion": "11", "browserName": "Chrome", "browserVersion": "latest"},
    {"os": "Windows", "osVersion": "11", "browserName": "Firefox", "browserVersion": "latest"},
    {"os": "OS X", "osVersion": "Big Sur", "browserName": "Chrome", "browserVersion": "latest"},
    {"os": "OS X", "osVersion": "Ventura", "browserName": "Chrome", "browserVersion": "latest"},
]

def run(platform):
    options = None
    if platform["browserName"] == "Chrome":
        options = ChromeOptions()
    elif platform["browserName"] == "Firefox":
        options = FirefoxOptions()

    bstack_options = get_browserstack_options(platform["os"], platform["osVersion"],
                                              platform["browserName"], platform["browserVersion"])

    options.set_capability('bstack:options', bstack_options)
    
    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub",
        options=options
    )
    driver.get("https://www.flipkart.com/")


    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Samsung Galaxy S10")
    search_box.submit()


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




    time.sleep(3)

    checkbox=driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div/div[1]/div/section[4]/label")
    driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
    driver.execute_script("arguments[0].click();", checkbox)

    time.sleep(1)


    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@data-id, 'MOB')]")))

    results = driver.find_elements(By.XPATH, "//div[contains(@data-id, 'MOB')]")




    i=0
    while i<len(results):
        try:
            print_product(results[i],i)
            i=i+1
        except Exception as e:
            results = driver.find_elements(By.XPATH, "//div[contains(@data-id, 'MOB')]")

    print("session over")
    print()
    driver.quit()


for cap in capabilites:
    
    Thread(target=run, args=(cap,)).start()



