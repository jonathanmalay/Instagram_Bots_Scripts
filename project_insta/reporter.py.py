from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = 'C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe'
profile_url = 'https://www.instagram.com/%s/'
login_url  = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
username = input('enter the username you want to block aviv: ')
nash2019 = ('nashshodedi3' , 'nashshodedi4' , 'nashshodedi6' , 'nashshodedi8' , 'nashshodedi10' , 'nashshodedi13' 
,'nashshodedi15' , 'nashshodedi17' , 'nashshodedi21' , 'nashnashomer76' , 'mmaupdates_everyday' , 'mahmu762002' , 'jordyshodedy')

def report(num):
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
    menu_element = driver.find_element_by_css_selector('#react-root > section > main > div > header > section > div.nZSzR > div.AFWDX > button > span')
    menu_element.click()
    sleep(2)
    report_button = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > button:nth-child(1)')
    report_button.click()
    sleep(2)
    spam_button = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div.Igw0E.IwRSH.eGOV_._4EzTm.XfCBB.g6RW6 > div > ul > li:nth-child(2) > button')
    spam_button.click()
    sleep(2)
    x_button = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div:nth-child(1) > div > div:nth-child(3) > button > span')
    x_button.click()
    driver.close()
def main():
    for i in range(len(nash2019)):
        report(i)
main()