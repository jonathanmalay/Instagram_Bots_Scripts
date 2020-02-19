from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = 'C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe'
profile_url = 'https://www.instagram.com/%s/'
login_url  = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
username = input('enter the username you want to block: ')
nash2019 = ('nashshodedi3' , 'nashshodedi4' , 'nashshodedi6' , 'nashshodedi8' , 'nashshodedi10' , 'nashshodedi13' 
,'nashshodedi15' , 'nashshodedi17' , 'nashshodedi21' , 'nashnashomer76' , 'mmaupdates_everyday' , 'mahmu762002' , 'jordyshodedy')

def like(num):
    driver = webdriver.Chrome(executable_path=driver_path)
    sleep(2)
    driver.get(login_url)
    sleep(3)
    driver.find_element_by_name('username').send_keys(nash2019[num])
    sleep(1)
    driver.find_element_by_name('password').send_keys('nash2019')
    sleep(2)
    driver.find_element_by_name('password').send_keys(Keys.ENTER)
    sleep(3)
    driver.get(profile_url % username)
    sleep(2)
    photo= driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[3]')
    photo.click()


like(1)    