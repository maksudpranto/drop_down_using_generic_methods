from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from generic_method import *

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

drop_down_industry = driver.find_element(By.ID, 'Form_submitForm_Industry')
drop_down_country = driver.find_element(By.ID, 'Form_submitForm_Country')

# print_all_values(drop_down_country)
stop_after_specific_value(drop_down_country, 'Bangladesh')

# drop_down(drop_down_industry, 'Education')
# drop_down(drop_down_country, 'Bangladesh')
