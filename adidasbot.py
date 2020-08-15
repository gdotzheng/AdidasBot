import time
from details import info
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver import ChromeOptions, Chrome
from webdriver_manager.chrome import ChromeDriverManager

def adidasbot(info):

    # Asking user for shoe model, size and retry delay
    model = input('Enter Desired Model\nex: BB6168\n')
    size = input('Enter Desired Size\n')
    delay = int(input('Set retry (minutes) delay if Out of Stock\n'))

    # Keeping chromedriver open the whole time
    options = ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.set_page_load_timeout('10')

    # Shoe URL
    driver.get('https://www.adidas.com/us/ultraboost-shoes/{}.html'.format(model))

    while True:
        try:
            driver.refresh()

            # Checks to see if shoe size is available
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[3]/div/div[2]/section[1]/div[1]/div[2]/button/span[text()="{}"]'.format(size))

            # Selects shoe size
            print('Size {} found'.format(size))
            driver.find_element_by_xpath('//span[contains(text(), "{}")]'.format(size)).click()

            # Adding shoes to bag
            print('Adding to cart')
            driver.find_element_by_xpath('//span[contains(text(), "Add To Bag")]').click()

            # Proceed to delivery page
            driver.implicitly_wait(10)
            driver.get('https://www.adidas.com/us/delivery')

            # Entering in delivery information
            print('Inputting delivery information')
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/form/div/div[1]/div/div[1]/div/div/div[1]/input').send_keys(info["fname"])
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/form/div/div[1]/div/div[2]/div/div/div[1]/input').send_keys(info["lname"])
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/form/div/div[1]/div/div[3]/div/div/div[1]/input').send_keys(info["address"])
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/form/div/div[1]/div/div[5]/div/div/div[1]/input').send_keys(info["city"])
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/form/div/div[1]/div/div[6]/span/div/div/select/option[text()="{}"]'.format(info["state"])).click()
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/form/div/div[1]/div/div[7]/div/div/div[1]/input').send_keys(info["zip"])
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/form/div/div[4]/div/div[1]/div/div/div[1]/input').send_keys(info["phone"])
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/form/div/div[4]/div/div[2]/div/div/div[1]/input').send_keys(info["email"])

            # Unchecks newsletter box
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/div[7]/div/div/div/label/input').click()

            # Proceed to payment page
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/div[9]/button').click()

            # Entering in payment information
            print('Inputting card information')
            driver.implicitly_wait(30)
            driver.find_element_by_name('card.number').send_keys(info["cardnumber"])
            driver.implicitly_wait(30)
            driver.find_element_by_name('card.cvv').send_keys(info["cvv"])
            driver.implicitly_wait(30)
            driver.find_element_by_xpath('//form/div[4]/div[2]/input').send_keys(info["expiration"])
            
            # Placing the order
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/button').click()
            print('Purchase complete')

            break

        except NoSuchElementException:

            # Refreshes webpage every mintue to check for restocks
            print("Cannot find size, Retrying in {} minute(s)".format(delay))
            time.sleep((delay*60))
            pass

adidasbot(info)