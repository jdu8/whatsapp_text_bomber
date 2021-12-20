from selenium import webdriver
import time
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


PATH="driver\chromedriver.exe"

driver=webdriver.Chrome(PATH)
driver.get("https://web.whatsapp.com/")

print("Waiting for phone to be connected........")
while True:
    try:
        e=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        print("Connected")
        break
    except NoSuchElementException:
        pass

contact=input("Contact Name/Number: ")
num=int(input("Number of Messages: "))
msg=input("Message: ")
e.send_keys(contact)
time.sleep(5)

while True:
    try:
        element=driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[14]/div/div/div[2]')
        print("Contact Found")
        element.click()
        break
    except NoSuchElementException:
        pass

msger=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')

for i in range(num):
    msger.send_keys(msg)
    msger.send_keys(Keys.RETURN)
