from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException
import time 
import string

#Open  FB 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("start-maximized")  #open Browser in maximized mode
chrome_options.add_argument('--no-sandbox') #bypass OS security model
chrome_options.add_argument("disable-infobars") #disabling infobars
chrome_options.add_argument("--disable-extensions") #disables extensions
chrome_options.add_argument('--disable-dev-shm-usage') #overcome limited resource problems
chrome_options.add_argument("--disable-gpu") #applicable to windows os only

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)
driver.get("https://facebook.com")
userid="oreosocial695@gmail.com"
pwd="Alreadyhacked"
time.sleep(5)


#Login To FB
emailelement= driver.find_element_by_xpath('//*[@id="email"]')
emailelement.send_keys(userid)
print("Entered id")
passwordfield= driver.find_element_by_xpath('//*[@id="pass"]')
passwordfield.send_keys(pwd)
print("Entered pwd")
button= driver.find_element_by_name('login')
button.click()
print("Logged in")
time.sleep(2)

driver.get("https://www.facebook.com/events/birthdays/")
time.sleep(5)
birthdayslist= driver.find_elements_by_class_name("j83agx80.pybr56ya.rz4wbd8a.sj5x9vvc.a8nywdso")
birthdayslist[0].find_element_by_class_name('_1mf._1mj')
candidate = 0
for b in birthdayslist:
    print('Today birthday for loop')
    name = b.find_element_by_tag_name("h2")

    linkTag = b.find_element_by_tag_name("a")
    link = linkTag.get_attribute("href")

    imageTag = b.find_element_by_tag_name("image")
    image = imageTag.get_attribute("xlink:href")

    age = b.find_element_by_class_name(
        'd2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.lr9zc1uh.a8c37x1j.fe6kdd0r.mau55g9w.c8b282yb.keod5gw0.nxhoafnm.aigsh9s9.d9wwppkn.mdeji52x.sq6gx45u.a3bd9o3v.b1v8xokw.m9osqain')
    candidate = candidate + 1
    textbox = b.find_element_by_class_name('_1mf._1mj')
    wish = "Happy Birthday"
    textbox.send_keys(wish)
    textbox.send_keys(Keys.ENTER)

print(candidate)

time.sleep(5)
#Closing the session
driver.close()