# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
# Other programming languages often use curly-brackets for this purpose.
calculate_to_unit = 24;
name_of_unit = "hours";
def days_to_unit(d):
    if(d < 0):
        print("Sorry...our application only accepts positive number for days, please try again.")
        exit();
    print(f"{d} days are {d*calculate_to_unit} {name_of_unit}")
 
user_input = input("Please Enter your Desired Number of Days:")
# print(type(user_input))
days_to_unit(int(user_input))