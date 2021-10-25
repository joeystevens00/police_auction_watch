from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from .models import AuctionArgs

def check_auctions(args: AuctionArgs):
    url = f"https://propertyroom.com/s/{args.query}/1" # First page of results

    opts = FirefoxOptions()
    opts.add_argument("--headless")
    #This example requires Selenium WebDriver 3.13 or newer
    with webdriver.Firefox(options=opts) as driver:
        wait = WebDriverWait(driver, 10)
        driver.get(url)
        if args.police_only:
            police_only_filter = driver.find_element(By.CSS_SELECTOR, 'span[title="Police & Other Clients"]')
            police_only_filter = police_only_filter.find_element_by_css_selector("input")
            police_only_filter.click()

        wait.until(presence_of_element_located((By.CSS_SELECTOR, '.section .product-boxes div')))

        # Sort by latest added
        sorting_options = driver.find_element(By.CSS_SELECTOR, '.sorting-options ul')\
            .find_elements_by_css_selector("li")[-1]\
            .find_element_by_css_selector('select')
        sorting_options.click()
        opened_recently_option = sorting_options.find_element_by_css_selector('option[value="openedRecently"]')
        opened_recently_option.click()

        # Log the most recent item
        product_items = driver.find_elements(By.CSS_SELECTOR, '.section .product-boxes div')
        latest_item = product_items[0]
        item_name = latest_item.find_element_by_css_selector('.product-name-category a').text
        time_remaining = latest_item.find_element_by_css_selector('.time-bids-category ul li').text
        last_price = latest_item.find_element_by_css_selector('.time-bids-category ul li:nth-child(2)').text

        return {"name": item_name, "time_remaining": time_remaining,  "last_price": last_price}
