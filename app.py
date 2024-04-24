# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
# Other programming languages often use curly-brackets for this purpose.
calculate_to_unit = 24;
name_of_unit = "hours";

def days_to_unit(d):
    print(f"{d} days are {d*calculate_to_unit} {name_of_unit}")
    render_again = input("Do you want to continuing calculation? (y/n) :\n")
    if(render_again == 'y' or render_again == 'Y'):
        get_user_input()
    else:
        print("Thanks for using our application and see you later👋")
       
def validate_user_input(input):
    if(input.isnumeric()):
        days_to_unit(int(input))
    else:
        print("🚫 Sorry...our application only accepts *positive whole numbers* for days, please try again👇")
        get_user_input()
    
def get_user_input():
    user_input = input("Enter your Desired Number of Days:\n")
    validate_user_input(user_input)
    
get_user_input()

