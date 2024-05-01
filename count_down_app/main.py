# Accept user's inputs of goal and deadline
# {goal:"",deadline:""}
# and then return the remaing days
import logging
from datetime import date
logging.basicConfig(level=logging.INFO)
user_inputs = input("Please enter your goal and deadline (e.g. yyyy-mm-dd) separated by colon :\n")

user_inputs_dict = {"goal":user_inputs.split(":")[0],"deadline":user_inputs.split(":")[1]}
deadline_date = date(int(user_inputs_dict["deadline"].split("-")[0]),int(user_inputs_dict["deadline"].split("-")[1]),int(user_inputs_dict["deadline"].split("-")[2]))
current_date = date.today()
def numOfDays(date1, date2):
    if date2 > date1:   
        return (date2-date1).days
    else:
        return (date1-date2).days
    
logging.info(f"Remaining days for your goal <{user_inputs_dict["goal"]}> is {numOfDays(deadline_date, current_date)}")
