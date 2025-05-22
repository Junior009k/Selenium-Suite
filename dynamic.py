import time
from Notification import Mail
from selenium import webdriver
from SeleniumSuite import *

class Dynamic:
    notification=Mail()
    seleniumObject=SeleniumSuite("https://sidesys.crm2.dynamics.com/main.aspx?appid=52a8ce47-f7cf-417d-8eee-3bf324bea667&pagetype=dashboard&id=d201a642-6283-4f1d-81b7-da4b1685e698&type=system&_canOverride=true",webdriver)
    def login(self):
        time.sleep(5) 
        self.seleniumObject.maximizar()
        self.seleniumObject.sendEntry(USER,'//*[@id="i0116"]')
        time.sleep(1) 
        self.seleniumObject.sendClic('//*[@id="idSIButton9"]')
        time.sleep(3) 
        self.seleniumObject.sendEntry(PASSWORDUSER,'//*[@id="i0118"]')
        time.sleep(1)   
        self.seleniumObject.sendClic('//*[@id="idSIButton9"]')
        time.sleep(3) 
        self.seleniumObject.sendClic('//*[@id="idSIButton9"]')
        time.sleep(25) 
        
    def showCase(self):
        self.seleniumObject.sendClic('//*[@id="sitemap-entity-nav_cases"]/div/div/div[2]')
        time.sleep(3) 
        self.readStatusCase()
        time.sleep(15) 
        
    def readStatusCase(self):
        try:
            i=1
            while i<20:
                ticket=self.seleniumObject.Read(f'//*[@id="entity_control-powerapps_onegrid_control_container"]/div/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div/div[{i}]/div[2]/div/div/div/div/div[1]/div/a/div/span')
                status=self.seleniumObject.Read(f'//*[@id="entity_control-powerapps_onegrid_control_container"]/div/div/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div/div[{i}]/div[6]/div/div/div/div/div[1]/label/div')
                print(f'{ticket} : {status}')
                if status=='Asignado STAC':
                    try:
                        self.notification.sendEmail(ticket)
                    except:
                        pass
                i=i+1
        except:
            
            pass