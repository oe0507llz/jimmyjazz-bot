from selenium import webdriver
import time
import requests
import random
from bs4 import BeautifulSoup as bs
import threading

#product_link = 'http://www.jimmyjazz.com/mens/footwear/jordan-retro-1-high-og-nrg/861428-007?color=Black'
product_link = 'http://www.jimmyjazz.com/mens/footwear/nike-air-more-money-qs/AJ7383-300?color=Dark%20Green'

product_response = requests.get(product_link)
#print product_response.text.encode('utf')
product_soup = bs(product_response.text, "html.parser")
div = product_soup.find("div",{"class": "box_wrapper"})
all_sizes = div.find_all("a")
	
sizes_in_stock = []
	
for size in all_sizes:
	if "piunavailable" not in size["class"]:
		size_id = size["id"]
		sizes_in_stock.append(size_id.split("_")[1])
print sizes_in_stock

ThreadCount = 4

size_chosen = random.choice(sizes_in_stock)

print size_chosen

def check_exists_by_css_selector(css_selector):
    try:
        browser.find_element_by_css_selector(css_selector)
    except NoSuchElementException:
        return False
    return True


		
def SneakerBot(address, sizes_in_stock):
	counter = counter+1


	browser = webdriver.Chrome()

	browser.get(product_link)
	time.sleep(1)
	if (check_exists_by_css_selector('#contentInformation > div.form > div.buttons > a.ltkmodal-close.ltkmodal-no-thanks')):
		browser.find_element_by_css_selector('#contentInformation > div.form > div.buttons > a.ltkmodal-close.ltkmodal-no-thanks').click()
	time.sleep(1)
	browser.find_element_by_css_selector('#itemcode_{}'.format(size_chosen)).click()
	#browser.find_element_by_css_selector('#itemcode_11368770').click()
	browser.find_element_by_css_selector('#add_to_bag_btn').click()
	time.sleep(3)
	browser.get('http://www.jimmyjazz.com/cart')
	browser.find_element_by_css_selector('#btn_check_out_now').click()
	browser.find_element_by_css_selector('#container > div > div > div.content_container > div.content > div.checkout_login.clear-block > div.checkout_login_column.display-desktop > div > div:nth-child(3) > a').click()

	browser.find_element_by_css_selector('#edit-billing-email').send_keys('xxxxxxxxxxxx@gmail.com')
	browser.find_element_by_css_selector('#edit-billing-email-confirm').send_keys('xxxxxxxxxx@gmail.com')
	browser.find_element_by_css_selector('#edit-billing-phone').send_keys('XXXXXXXXXX')
	browser.find_element_by_css_selector('#edit-shipping-first-name').send_keys('XXXXXXXXXX')
	browser.find_element_by_css_selector('#edit-shipping-last-name').send_keys('XXX')
	browser.find_element_by_css_selector('#edit-shipping-address1').send_keys('XXXXXXXXXXXXX')
	browser.find_element_by_css_selector('#edit-shipping-city').send_keys('XXXXXX')
	browser.find_element_by_css_selector('#edit-shipping-state > option:nth-child(38)').click()

	browser.find_element_by_css_selector('#edit-shipping-zip').send_keys('XXXXX')
	browser.find_element_by_css_selector('#edit-billing-same-as-shipping').click()
	browser.find_element_by_css_selector('#edit-cc-number').send_keys('XXXXXXXXXXXXXXXXX')
	browser.find_element_by_css_selector('#edit-cc-exp-month').send_keys('XX')
	browser.find_element_by_css_selector('#edit-cc-exp-year').send_keys('XX')

	browser.find_element_by_css_selector('#edit-cc-cvv').send_keys('XXX')

	browser.find_element_by_css_selector('#edit-submit').click()
	time.sleep(1)
	browser.find_element_by_css_selector('#edit-submit').click()

with open('address_info.csv', newline='') as csvfile:
        address_list = csv.reader(csvfile, delimiter=',', quotechar='|')

threads = [threading.Thread(name='ThreadNumber{}'.format(n), target=SneakerBot, args=(address, sizes_in_stock)) for address in address_list for n in range(ThreadCount)]

for t in threads: t.start()
