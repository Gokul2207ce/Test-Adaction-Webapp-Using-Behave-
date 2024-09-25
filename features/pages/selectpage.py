from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
class select_hotel():
    def __init__(self,abc):
        self.driver=abc
        self.__selectedhotel=self.driver.find_element(By.XPATH,"//input[@name='radiobutton_0']")
        self.__continue=self.driver.find_element(By.XPATH,"//input[@type='submit']")

    def get_select_button(self):
        return self.__selectedhotel

    def get_continue_button(self):    
        return self.__continue
    
    def click_search_button(self):
        self.__selectedhotel.click()

    def click_continue_button(self):
        self.__continue.click()
        
class finalprocess():
    def __init__(self,bcd):
        self.driver=bcd
        self.__click=self.driver.find_element(By.XPATH,"//input[@name='ids[]']")
        self.__cancelselected=self.driver.find_element(By.XPATH,"//input[@name='cancelall']")

    def get_click_the_hotel(self):
        return self.__click
    def get_cancel_the_booking(self):
        return self.__cancelselected
    
    def finished_frst_step1(self):
        self.__click.click()
    def  finished_in_step2(self):    
        self.__cancelselected.click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        print("******booking process complete******")        
