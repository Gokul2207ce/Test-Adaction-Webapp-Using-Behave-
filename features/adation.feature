Feature: booking hotel booking using adaction
     
    Scenario:login adaction applcation with valid username and password

        Given user launch the url
        
        When user validte login fields are displayed

        And user enter the username in username field

        And user enter the password i password field

        Then click the login button and it will navigate the search hotel page
        
    Scenario: search hotels fro adaction applcation 

        When validate the searchhotel detials

        And user search the location in location field

        And user search the mention location hotels and enter the hotel field 

        And user enter the room type into the roomtype field

        And user enter the no of rooms in the noofrooms field

        And user enter the booking date into checkindate field

        And user enter the vecate date into checkinout

        And user enter no of adult per room into adultperroom field

        And user enter no of children per room into childperroom field

        Then click on the search button it to be navigateon the select hotel page

    Scenario:select the booking hotel using adaction application

        When validate the select hotel page 

        And user click or select the the booking hotels into the select button fields

        Then click the continue button it to be navigate onthe book a hotel page    

    Scenario:some other user detials put an input into the book a hotelpage 

        When validate the book a hotel in fields

        And user enter a valid firstname in firstname field

        And user enter a valid lastname in lastname field
        
        And user enter the valid billing address in billing address fiels

        And user enter the valid card number in credit card number

        And user enter the card type in credit card type

        And user click on the valid date in expiry date box

        And user click on the valid year in expiry year box

        And user enter the valid CCV number in CCV number field

        Then user click on the book now button it wll navigate to book confirmation button
        
    Scenario:user go on booking confirmation page in adaction application    

        When valid the search history field is displayed

        Then click on the search history button it will navigate onthe Booked Itinerary

    Scenario: user cancel the booking hotel using adaction applcation

        When validate the Booked Itinerary of all fields 

        And user select the button     

        Then user click on The Cancel Select Button then alert of confirmation then finally booking hotels are successfully canceled

        



