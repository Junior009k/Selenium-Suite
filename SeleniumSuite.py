
from Constante import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SeleniumSuite:
    #Constructor
    def __init__(self,url,driver):
        self.url=url
        self.driver=driver
    #Estable la url
    def setURL(self,url):self.url=url
    #Obtiene la url
    def getURL(self):return self.url
    #Estable la driver
    def setDriver(self,driver):self.driver=driver
    #Obtiene la driver
    def getDriver(self):return self.driver
    def sendEntry(self,text,xpath):self.driver.find_element("xpath",xpath).send_keys(text)
    def sendClic(self,xpath):self.driver.find_element("xpath",xpath).click()
    def Read(self,xpath):
        print(self.driver.find_element("xpath",xpath).text)
    def maximizar(self):self.driver.maximize_window()
    def scrollVertical(self,scroll, element):
        self.driver.execute_script(f"arguments[0].scrollLeft += {scroll};", self.driver.find_element("xpath", element) )  # Mueve 500px a la derecha
    def scrollHorizontal(self):self.driver.execute_script("window.scrollTo(document.body.scrollWidth, 0)")
    def allowWarning(self):
        
        time.sleep(2) 
        self.driver.find_element("xpath","//*[@id='details-button']").click()
        self.driver.execute_script("window.scrollTo(0, 45)")
        #self.driver.save_screenshot('screenie.png')
        time.sleep(1) 
        self.driver.find_element("xpath","//*[@id='proceed-link']").click()
        return "permito advertencia a esta url " + self.url
    def startDriver(self):
        service = Service(ChromeDriverManager().install())
        options = Options()
        options.binary_location = PATHCHROME 
        if PATHCHROME == '':self.setDriver(self.driver.Chrome(service=service))
        else:self.setDriver(self.driver.Chrome(service=service,options=options))
        #self.setDriver(self.driver.Chrome(executable_path='./chromedriver'))
        self.driver.get(self.url)

    def stopDriver(self):
        self.driver.close()