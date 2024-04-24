my_list = ["Alex","Lisa","Bianca"]
print(f"Before append : {my_list}")
my_list.append("Mike")
print(f"After append : {my_list}")
# Reminds me of array in javascript
# Order does matter in list
# May include duplicated item
my_list.remove(my_list[0])
print(f"After removing the first item : {my_list}")