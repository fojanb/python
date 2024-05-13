from user import User
from post import Post
# Calling a class is similar to calling a function:
app_user_1 = User("tt@g.com","tom","secret","chief")
app_user_1.get_user_info()
app_user_1.change_job_title("DevOps")
app_user_1.get_user_info()

post_1 = Post("good morning all. i am back",app_user_1.name)
post_1.get_post_info()


