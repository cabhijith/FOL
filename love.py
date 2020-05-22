from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep
import pickle 
#---------------------------------------------------------------------------------------
chromedriver_path = "/Users/abhijithchandran/Desktop/Fountain_of_Love/chromedriver 3"
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)

def LoggingIn (user, passs):
    username = webdriver.find_element_by_name('username')
    username.send_keys(user)

    password = webdriver.find_element_by_name('password')
    password.send_keys(passs)

    sleep (3)

    login_form = webdriver.find_element_by_xpath('//*[@id= "react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
    login_form.click()
    sleep(4)


def get_profile(username): 
        LoggingIn ('username', 'password') #Enter your username/password
        sleep(5)
        webdriver.get ('https://www.instagram.com/' + username)
        sleep(3)
        sleep(2)
        profile =  webdriver.find_element_by_css_selector(".fAR91.sqdOP.L3NKy._4pI4F._8A5w5").click() #react-root > section > main > div > header > section > div.Y2E37 > div._862NM > div > button
       
       
sleep(2)
get_profile('something123417') #The profile you want to target. 
print('Sleeping')
sleep(10)

print('I am gonna really sleep boi')
sleep(7300)
while True: 
    message = webdriver.find_elements_by_css_selector(".iXTil")
    try: 
         message = message[-1]
    except: 
        #Accounting for the sudden move to the details section when multiple clicks are performed.
        details = webdriver.find_elements_by_css_selector(".wpO6b.ZQScA")
        details = details[1]
        details.click()
        # sleep(1)
        continue 

    actionChains = ActionChains(webdriver)
    actionChains.double_click(message).perform()

    sleep(1.5)
    try: 
        heart = webdriver.find_elements_by_css_selector(".wpO6b.ZQScA")
        heart = heart[-1]
        heart.click()
    except: 
        continue 
