from selenium.webdriver.common.by import By

from pageObjects.Employee_Management import Employee_Management
from utilities.BaseClass import BaseClass


class Dashboard(BaseClass):

    def __init__(self,driver):
        self.driver = driver


    p = (By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')

    def pim(self):
        self.driver.find_element(*Dashboard.p).click()
        #self. driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        pi = Employee_Management(self.driver)
        return pi