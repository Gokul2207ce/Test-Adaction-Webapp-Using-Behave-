from behave import given,when,then 
from pages.loginpage import login_page
from pages.loginpage import searcHoltels
from pages.selectpage import select_hotel
from pages.loginpage import detials_of_book_hotels
from pages.loginpage import my_booking_history
from pages.selectpage import finalprocess
from utils.config import config

@given(u'user launch the url')
def url_launch(context):
    context.driver.get(config.BASIC_URL)

@when(u'user validte login fields are displayed')
def validate_all_login_fields(context):
    context.lp=login_page(context.driver)
    context.lp.getusername().is_displayed()
    context.lp.getpassword().is_displayed()
    context.lp.get_login_button().is_displayed()

@when(u'user enter the username in username field')
def valid_username(context):
    context.lp.enter_username(config.USERNAME)

@when(u'user enter the password i password field')
def valid_password(context):
    context.lp.enter_password(config.PASSWORD)
    
@then(u'click the login button and it will navigate the search hotel page')
def loginbutton(context):
    context.lp.click_login_button()    

@when(u'validate the searchhotel detials')
def validate_the_search_hotel_detials(context):
    context.lp=searcHoltels(context.driver)
    context.lp.get_location().is_displayed()
    context.lp.get_hotel().is_displayed()
    context.lp.get_roomtype().is_displayed()
    context.lp.get_numberofrooms().is_displayed()
    context.lp.get_checkindate().is_displayed()
    context.lp.get_checkinout().is_displayed()
    context.lp.get_adultperroom().is_displayed()
    context.lp.get_childperroom().is_displayed()
    context.lp.get_searchbutton().is_displayed()
   


@when(u'user search the location in location field')
def valid_location(context):
    context.lp.enter_the_location(config.LOCATION)
    
@when(u'user search the mention location hotels and enter the hotel field')
def valid_hotels(context):
    context.lp.enter_the_hotels(config.HOTELS)

@when(u'user enter the room type into the roomtype field')
def valid_roomtype(context):
    context.lp.enter_the_roomstype(config.ROOMSTYPE)

@when(u'user enter the no of rooms in the noofrooms field')
def valid_noofrooms(context):
    context.lp.enter_the_noofrooms(config.NOOFROOMS)

@when(u'user enter the booking date into checkindate field')
def valid_checkindate(context):
    context.lp.enter_the_checkindate(config.CHECKINDATE)

@when(u'user enter the vecate date into checkinout')
def valid_checkinout(context):
    context.lp.enter_the_checkinout(config.CHCKINOUT)

@when(u'user enter no of adult per room into adultperroom field')
def valid_adultperroom(context):
    context.lp.enter_the_adultperroom(config.ADULTPERROOM)
    
@when(u'user enter no of children per room into childperroom field')
def valid_childperroom(context):
    context.lp.enter_the_childperroom(config.CHILDPERROM)

@then(u'click on the search button it to be navigateon the select hotel page')
def valid_searchbutton(context):
    context.lp.search_button()


@when(u'validate the select hotel page')
def verify_hotelbutton(context):
    context.lp=select_hotel(context.driver)
    context.lp.get_select_button().is_displayed()
    context.lp.get_continue_button().is_displayed()

@when(u'user click or select the the booking hotels into the select button fields')
def click_select(context):
    context.lp.click_search_button()

@then(u'click the continue button it to be navigate onthe book a hotel page')
def click_continue(context):
    context.lp.click_continue_button()

@when(u'validate the book a hotel in fields')
def assertvalues(context):
    context.lp=detials_of_book_hotels(context.driver)
    context.lp.get_firstname().is_displayed()
    context.lp.get_lastname().is_displayed()
    context.lp.get_billingaddress().is_displayed()
    context.lp.get_cardnumber().is_displayed()
    context.lp.get_cardtype().is_displayed()
    context.lp.get_expiarydate().is_displayed()
    context.lp.get_exxpiryear().is_displayed()
    context.lp.get_ccvnumber().is_displayed()
    context.lp.get_booknow().is_displayed()

@when(u'user enter a valid firstname in firstname field')
def valid_the_firstname(context):
    context.lp.vaild_firstname(config.FIRSTNAME)

@when(u'user enter a valid lastname in lastname field')
def valid_the_lastname(context):
    context.lp.vaild_lastname(config.LASTNAME)

@when(u'user enter the valid billing address in billing address fiels')
def valid_the_billing_addresss(context):
    context.lp.vaild_billingaddress(config.BILLINGADDRESS)

@when(u'user enter the valid card number in credit card number')
def valid_the_credit_cardno(context):
    context.lp.vaild_cardnumber(config.CARDNO)

@when(u'user enter the card type in credit card type')
def valid_the_cardtype(context):
    context.lp.vaild_cardtype(config.CARDTYPE)

@when(u'user click on the valid date in expiry date box')
def valid_the_expiry_date(context):
    context.lp.vaild_expirydate(config.EXPIRYDATE)

@when(u'user click on the valid year in expiry year box')
def valid_expiry_year(context):
    context.lp.vaild_expiryyear(config.EXPIRYYEAR)

@when(u'user enter the valid CCV number in CCV number field')
def valid_the_ccv_no(context):
    context.lp.vaild_ccvnumber(config.CCVNUMBER)

@then(u'user click on the book now button it wll navigate to book confirmation button')
def click_on_booknow(context):
    context.lp.click_booknow()

@when(u'valid the search history field is displayed')
def validate_libiary(context):
    context.lp=my_booking_history(context.driver)
    context.lp.get_search_history().is_displayed()

@then(u'click on the search history button it will navigate onthe Booked Itinerary')
def click_libiary(context):
    context.lp.opened()

@when(u'validate the Booked Itinerary of all fields')
def validate_the_field(context):
    context.lp=finalprocess(context.driver)
    context.lp.get_click_the_hotel().is_displayed()
    context.lp.get_cancel_the_booking().is_displayed()
@when(u'user select the button')
def first_step(context):
    context.lp.finished_frst_step1()
@then(u'user click on The Cancel Select Button then alert of confirmation then finally booking hotels are successfully canceled')
def second_step(context):
    context.lp.finished_in_step2()
