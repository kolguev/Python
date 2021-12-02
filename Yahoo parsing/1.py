from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import bs4

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.avito.ru/")
# driver.find_element_by_id("email").send_keys("dflvdlmfbdmf@gamil.com")
# time.sleep(15)
# driver.find_element_by_id("pass").send_keys("9279oidOxvxcv")
driver.find_element_by_xpath("//input[@id='search']").send_keys("Play station")
driver.find_element_by_xpath(
    "//button[@class='index-buttonElement-3wfmP button-button-2Fo5k button-size-s-3-rn6 button-default-mSfac']"
).click()

page = driver.page_source
# driver.quit()

# page = bs4.BeautifulSoup(page, features="html.parser")
# print(page.find(text="Новая PS5 (Play Station 5)"))


# //button[contains(text(),'Войти')]