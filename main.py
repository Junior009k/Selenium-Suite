import time
from selenium import webdriver
from SeleniumSuite import *
from Dynamic import Dynamic

main=Dynamic()

main.seleniumObject.startDriver()
main.login()
main.showCase()
main.seleniumObject.stopDriver()


#//*[@id="entity_control-powerapps_onegrid_control_container"]/div/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[6]/div/div/div/div/div[1]/label
#/html/body/div[3]/div[1]/div/div/div[1]/div[4]/div[2]/div/div[1]/div/div/div[2]/div/section/div[3]/div/div/div[2]/div/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div/div[2]/div[6]/div/div/div/div
#/html/body/div[3]/div[1]/div/div/div[1]/div[4]/div[2]/div/div[1]/div/div/div[2]/div/section/div[3]/div/div/div[2]/div/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[6]/div/div/div/div