# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
# Other programming languages often use curly-brackets for this purpose.
calculate_to_unit = 24;
name_of_unit = "hours";

def days_to_unit(d):
    print(f"✅ {d} days are {d*calculate_to_unit} {name_of_unit}")
       
def validate_user_input(input):
    if(input.isnumeric()):
        days_to_unit(int(input))
    else:
        print(f"❌ Your input = {input} is not accepted, only *positive whole numbers* are accepted.")
        
def rerender_app():
    render_again = input("Do you want to continuing calculation? (y/n) :\n")
    if(render_again == 'y' or render_again == 'Y'):
        get_user_input()
    else:
        print("👋 Thanks for using our application and see you later.")
    
def get_user_input():
    user_input = input("Enter your list of numbers separated with one space bewtween them i.e. 10 20 30\n")
    print(user_input.split())
    print(set(user_input.split()))
    for number_of_days in set(user_input.split()):
        validate_user_input(number_of_days)
    rerender_app()
    
get_user_input()

