from requests import get
from server import Serv
from http.server import HTTPServer 
user_name = input("Please enter a github user name to list all repositories belong to it:\n")
resposne = get(f"https://api.github.com/users/{user_name}/repos")
# response.json() is a list of dictionary similar to whta we have in javascript array of json.
# An important reminder here is thet server ONLY understands strings " " , so response varibale without 
# .json() is a string "[{},{},...,{}]" not an actual list [{},{},...,{}]
print(resposne.json()[0]["name"])

# Write a web application which uses javascript as client side and python for server side.
# create a search bar which will get a user input for user name and will list all the repo name correspond to that specific user name
# First we need to set up a server via python and create a GET API to response back the
# repositories blong to the user name
httpd = HTTPServer(('localhost',8080),Serv)
httpd.serve_forever()