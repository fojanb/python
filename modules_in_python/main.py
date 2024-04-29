# dictionary reminds me of object in javascript
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
# Other programming languages often use curly-brackets for this purpose.
import logging
calculate_to_unit = 24;
logger = logging.getLogger("MAIN")
def days_to_unit(numberOfDays,conversionUnit):
    match conversionUnit :
        case "hours": 
            print(f"✅ {numberOfDays} days are {numberOfDays*calculate_to_unit} {conversionUnit}")
        case "minutes": 
            print(f"✅ {numberOfDays} days are {numberOfDays*calculate_to_unit*60} {conversionUnit}")
        case "seconds": 
            print(f"✅ {numberOfDays} days are {numberOfDays*calculate_to_unit*60*60} {conversionUnit}")
        case _ :
            logger.error("❌ Not a vaild conversion unit.")
            # print("❌ Not a vaild conversion unit. ")
            
            
def not_a_valid_data_type(a_valid_type,name,message):
    if(not a_valid_type):
        print(f"❌ Your {name} is not accepted, only *{message}* are accepted.")
    
def validate_user_input(input):
    if(input["number_of_days"].isnumeric() and input["conversion_unit"].isalpha()):
        days_to_unit(int(input["number_of_days"]),input["conversion_unit"])
    else:
        not_a_valid_data_type(input["conversion_unit"].isalpha(),"conversion_unit","alphabet")
        not_a_valid_data_type(input["number_of_days"].isnumeric(),"number_of_days","positive whole number")
        
def get_user_input():
    user_input = input("Enter your number of days and conversion unit separated with : e.g. 10:hours \n")
    user_dict = {"number_of_days":user_input.split(":")[0],"conversion_unit":user_input.split(":")[1]}
    validate_user_input(user_dict)
    import helper
    helper.rerender_app()
    
get_user_input()

