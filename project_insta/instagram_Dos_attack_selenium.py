from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

chromedriver_path = 'C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe' 
driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(3)
username = 'your username here'
password = 'your passowrd here'

def login():
    #login to the instagram account
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    sleep(2)
    driver.find_element_by_name('username').send_keys(username)
    sleep(1)
    driver.find_element_by_name('password').send_keys(password)
    sleep(1)
    driver.find_element_by_name('password').send_keys(Keys.ENTER)
    sleep(3)

def get_following_list():
    #get the vjayas profile and get into the following list
    driver.get('https://www.instagram.com/thevjayas/')
    sleep(3)
    driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a').click()
    sleep(2)
    following_list = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div.isgrP > ul')
    following_list.click()
    sleep(2)

def follow(num):
    #follow a user from his location in the following list
    sleep(2)
    if num < 13:
        follow_button = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li[%s]/div/div[3]/button' % str(num))
    else:
        follow_button = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li[%s]/div/div[2]/button' % str(num))
   
    if num % 10 == 0 :
        sleep(6)
    if follow_button.text == 'Following':
        unfollow_sec(num)
        sleep(2)
    
    elif follow_button.text == 'Follow':
        follow_button.click()

    if follow_button.text == 'Following':
        print("follow successfully account #" + str(num - 1))

def scroll_down(i):
    #scrolling down the instagram following page
    if i > 12:
        driver.execute_script("window.scrollTo({0}, {1})".format(80 / (i-1) , 80 * (i-1)))

def unfollow(num):
    #unfollow a user from his location in the instagram list
    sleep(2)
    if num < 13:
        unfollow_button = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li[%s]/div/div[3]/button' % str(num))
    else:
        unfollow_button = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li[%s]/div/div[2]/button' % str(num))
    if unfollow_button.text == 'Follow':
        follow_sec(num)
        sleep(5)
    unfollow_button.click()
    sleep(2)
    submit_unfollow = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]')
    submit_unfollow.click()
    sleep(1.5)
    if unfollow_button.text == 'Follow': 
        print('unfollow successfully account #' + str(num - 1))

def follow_sec(num ):
    sleep(2)
    if num < 13:
        follow_button = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li[%s]/div/div[3]/button' % str(num))
    else:
        follow_button = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li[%s]/div/div[2]/button' % str(num))
    follow_button.click()
    if follow_button.text == 'Follow':
        sleep(4)
        follow(num)
    if follow_button.text == 'Following':
        print("follow second successfully account #" + str(num - 1))

def unfollow_sec(num):
    sleep(2)
    if num < 13:
        unfollow_button = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li[%s]/div/div[3]/button' % str(num))
    else:
        unfollow_button = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li[%s]/div/div[2]/button' % str(num))
    unfollow_button.click()
    sleep(2)
    submit_unfollow = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]')
    submit_unfollow.click()
    sleep(1.5)
    if unfollow_button.text == 'Follow': 
        print('unfollow second successfully account #' + str(num - 1))
    sleep(5)
   
def vjaya():
    #login to the account
    login()
    #getting the following list of vjayas page
    get_following_list()
    #follow all the following list
    for i in range(2 , 153):
        if i < 10:
            follow(i)
            sleep(1)
        else:
           scroll_down(i)
           sleep(2)
           follow(i)
    #reget all the following list
    get_following_list()
    #unfollow all the following list
    for i in range(2 , 153):
        if i < 10:
            unfollow(i)
            sleep(1)
        else:
           scroll_down(i)
           sleep(2)
           unfollow(i)
    #close the webdriver
    driver.close()
    
vjaya()