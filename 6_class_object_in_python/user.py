# 1- Object is an instance of class. In the other word, Class is an object constructor
# Class is a blueprint
# 2- Object will be created with initial values : tom = User("tt@g.com","tom","secret","chief")
class User:
    # Constructor
    def __init__(self,email,name,password,title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = title
    # Methods  
    def change_password(self,new_password):
        self.password = new_password
    
    def change_job_title(self,new_title):
        self.current_job_title = new_title
    
    def get_user_info(self):
        print(f"User {self.name} currently works as {self.current_job_title} and you can contact her via email {self.email}")

