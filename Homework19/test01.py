from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time


def test_01():
    driver = Chrome()
    driver.get('https://google.com')

    search_field_locator = "//textarea[@type='search']"
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys('how to use webdriver')
    element.send_keys(Keys.ENTER)
    time.sleep(5)
    #python_search_result_locator = '//div[@aria-label="how to use webdriver manager in python"]'
   # python_search_element = driver.find_element(by='xpath', value=python_search_result_locator)
   # python_search_element.click()
    second_page = driver.find_element(by='xpath', value=search_field_locator)
    time.sleep(5)
    assert second_page.text == 'how to use webdriver'


def test_02():
    driver = Chrome()
    driver.get('https://google.com')

    search_field_locator = "//textarea[@type='search']"
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys('how to use webdriver')
    element.send_keys(Keys.ENTER)
    time.sleep(5)
    first_link_locator = "//h3[text()='Selenium Webdriver Tutorial in Java with Examples']"
    first_link = driver.find_element(by='xpath', value=first_link_locator)
    first_link.click()
    time.sleep(5)
    desired_text_locator = "//p[@class='guide-banner-section__heading']"
    desired_text = driver.find_element(by='xpath', value=desired_text_locator)
    assert desired_text.text == 'Run Selenium Tests on Cloud'


def test_03():
    driver = Chrome()
    driver.get('https://geekach.com.ua')
    first_element_menu_locator = '//div[@class="products-menu__title"]'
    first_element_menu = driver.find_element(by='xpath', value=first_element_menu_locator)
    first_element_menu.click()
    products_locator = '//li[@class="catalog-grid__item"]'
    products = driver.find_elements(by='xpath', value=products_locator)
    assert len(products) == 20
    time.sleep(5)

