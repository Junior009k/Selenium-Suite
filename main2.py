import time
from selenium import webdriver
from SeleniumSuite import *


main.startDriver()
time.sleep(5) 
main.maximizar()
main.sendEntry(USER,'//*[@id="i0116"]')
time.sleep(1) 
main.sendClic('//*[@id="idSIButton9"]')
time.sleep(3) 
main.read('//*[@id="idSIButton9"]')
main.sendEntry(PASSWORD,'//*[@id="i0118"]')
time.sleep(1) 
main.sendClic('//*[@id="idSIButton9"]')
time.sleep(3) 
main.sendClic('//*[@id="idSIButton9"]')
time.sleep(35) 
main.sendClic('//*[@id="sitemap-entity-nav_cases"]')

time.sleep(3) 
main.stopDriver()
#main.sendClic('//*[@id="Dropdown516-list11"]')
time.sleep(3) 
#main.sendClic('//*[@id="fluent-default-layer-host"]/div[3]/div/div/div/div/div/div[3]/form/div[3]/button')
time.sleep(300)
time.sleep(300)
main.stopDriver()
#//*[@id="fluent-default-layer-host"]/div[3]/div/div/div/div/div/div/ul/li[4]/button/div/span

