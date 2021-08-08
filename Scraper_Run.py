import Web_Scrapping as gs
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("start-maximized")
options.add_argument("headless")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:/Users/George/Documents/ds_salary_proj/chromedriver/chromedriver.exe')
driver.get('https://www.google.co.in')
print("Page Title is : %s" %driver.title)



path = "C:/Users/George/Documents/ds_salary_proj/chromedriver/chromedriver"

df = gs.get_jobs("data scientist",15,False, path, 15)

