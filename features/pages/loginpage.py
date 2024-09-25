from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time 

class login_page:
    def __init__(self,abc):
      self.driver=abc
      self.__username=self.driver.find_element(By.XPATH,"//input[@name='username']")
      self.__password=self.driver.find_element(By.XPATH,"//input[@name='password']")
      self.__login_button =self.driver.find_element(By.XPATH,"//input[@type='Submit']")

    def getusername(self):
      return self.__username

    def getpassword(self):
       return self.__password

    def get_login_button(self):
       return self.__login_button
    
    def enter_username(self,username):
       self.__username.send_keys(username)

    def enter_password(self,password):
       self.__password.send_keys(password)

    def click_login_button(self):
       self.__login_button.click()
 
class searcHoltels:
    def __init__(self,bcd):
       self.driver=bcd
       self.__locations=self.driver.find_element(By.XPATH,"//select[@name='location']")
       self.__hotels=self.driver.find_element(By.XPATH,"//select[@name='hotels']")
       self.__roomstype=self.driver.find_element(By.XPATH,"//select[@name='room_type']")
       self.__noofrooms=self.driver.find_element(By.XPATH,"//select[@name='room_nos']")
       self.__checkindate=self.driver.find_element(By.XPATH,"//input[@name='datepick_in']")
       self.__checkinout=self.driver.find_element(By.XPATH,"//input[@name='datepick_out']")
       self.__adultperroom=self.driver.find_element(By.XPATH,"//select[@name='adult_room']")
       self.__childprroom=self.driver.find_element(By.XPATH,"//select[@name='child_room']")
       self.__searchbutton=self.driver.find_element(By.XPATH,"//input[@type='submit']")  

    def get_location(self):
       return self.__locations
    def get_hotel(self):
       return self.__hotels
    def get_roomtype(self):
       return self.__roomstype
    def get_numberofrooms(self):
       return self.__noofrooms
    def get_checkindate(self):
       return self.__checkindate
    def get_checkinout(self):
       return self.__checkinout
    def get_adultperroom(self):
       return self.__adultperroom
    def get_childperroom(self):
       return self.__childprroom
    def get_searchbutton(self):
       return self.__searchbutton
 
    def enter_the_location(self,location):
       sc=Select(self.__locations)
       sc.select_by_index(location)

    def enter_the_hotels(self,hotels):
       sc=Select(self.__hotels)  
       sc.select_by_index(hotels)

    def enter_the_roomstype(self,roomstype):  
       sc=Select(self.__roomstype)
       sc.select_by_index(roomstype)

    def enter_the_noofrooms(self,noofrooms):   
       sc=Select(self.__noofrooms)
       sc.select_by_index(noofrooms)

    def enter_the_checkindate(self,checkindate):   
       self.__checkindate.clear()
       self.__checkindate.send_keys(checkindate)

    def enter_the_checkinout(self,checkinout):   
       self.__checkinout.clear()
       self.__checkinout.send_keys(checkinout)

    def enter_the_adultperroom(self,adultperroom):   
       sc=Select(self.__adultperroom)
       sc.select_by_index(adultperroom)

    def enter_the_childperroom(self,childperroom):   
       sc=Select(self.__childprroom)
       sc.select_by_index(childperroom)

    def search_button(self):
       self.__searchbutton.click()   

class detials_of_book_hotels:

    def __init__(self,bcd):
        self.driver=bcd
        self.__firstname=self.driver.find_element(By.XPATH,"//input[@name='first_name']")
        self.__lastname=self.driver.find_element(By.XPATH,"//input[@name='last_name']")
        self.__billingaddress=self.driver.find_element(By.XPATH,"//textarea[@name='address']")
        self.__cardnumber=self.driver.find_element(By.XPATH,"//input[@name='cc_num']")
        self.__cardtype=self.driver.find_element(By.XPATH,"//select[@name='cc_type']")
        self.__expiarydate=self.driver.find_element(By.XPATH,"//select[@name='cc_exp_month']")
        self.__expiaryear=self.driver.find_element(By.XPATH,"//select[@name='cc_exp_year']")
        self.__ccvnumber=self.driver.find_element(By.XPATH,"//input[@name='cc_cvv']")
        self.__booknow=self.driver.find_element(By.XPATH,"//input[@type='button']")

    def get_firstname(self):
       return self.__firstname
    def get_lastname(self):
       return self.__lastname 
    def get_billingaddress(self):
       return self.__billingaddress
    def get_cardnumber(self):
       return self.__cardnumber 
    def get_cardtype(self):
       return self.__cardtype
    def get_expiarydate(self):
       return self.__expiarydate 
    def get_exxpiryear(self):
       return self.__expiaryear
    def get_ccvnumber(self):
       return self.__ccvnumber 
    def get_booknow(self):
       return self.__booknow           

    def vaild_firstname(self,firstname):
        self.__firstname.send_keys(firstname)
    def vaild_lastname(self,lastname):    
        self.__lastname.send_keys(lastname)
    def vaild_billingaddress(self,billingaddress):    
        self.__billingaddress.send_keys(billingaddress)
    def vaild_cardnumber(self,cardnumber):        
        self.__cardnumber.send_keys(cardnumber)
    def vaild_cardtype(self,cardtype):           
        sc=Select(self.__cardtype)
        sc.select_by_index(cardtype)
    def vaild_expirydate(self,expirydate):           
        sc=Select(self.__expiarydate)
        sc.select_by_index(expirydate)
    def vaild_expiryyear(self,expiryyear):              
        sc=Select(self.__expiaryear)
        sc.select_by_index(expiryyear)
    def vaild_ccvnumber(self,ccvnumber):                  
        self.__ccvnumber.send_keys(ccvnumber)
    def click_booknow(self):    
        self.__booknow.click()

class my_booking_history:
    def __init__(self,bcd):
        self.driver=bcd
        time.sleep(5)
        self.__history=self.driver.find_element(By.XPATH,"(//input[@type='button'])[2]")
    def get_search_history(self):
        return self.__history
    def opened(self):
        self.__history.click()
        




    
      

