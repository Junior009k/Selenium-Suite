import time
from selenium import webdriver
from SeleniumSuite import SeleniumSuite

main=SeleniumSuite("https://sidesys.crm2.dynamics.com/main.aspx?appid=52a8ce47-f7cf-417d-8eee-3bf324bea667&forceUCI=1&pagetype=dashboard&id=d201a642-6283-4f1d-81b7-da4b1685e698&type=system&_canOverride=true",webdriver)

main.startDriver()
time.sleep(5) 
main.maximizar()
main.sendEntry("junior.aquino@sidesys.com",'//*[@id="i0116"]')
time.sleep(1) 
main.sendClic('//*[@id="idSIButton9"]')
time.sleep(3) 
main.read('//*[@id="idSIButton9"]')
main.sendEntry("Sidesys*202504$",'//*[@id="i0118"]')
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
main.stopDriver()
#//*[@id="fluent-default-layer-host"]/div[3]/div/div/div/div/div/div/ul/li[4]/button/div/span

