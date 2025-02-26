# 3b
from Message import Message
from User import User

# 3c
class Twitter:
    def __init__(self):
        self.users_list = []

# 3d - we would not want to add get and set functions, due to privacy concerns.
# 3e
    def register(self, un, pwd):
        if self.find(un) is None:
            self.users_list.append(User(un, pwd))

        else:
            print("UserName Taken.")

    def find(self, un):
        for user in self.users_list:
            if user.get_user_name() == un:
                return user
        return None

# 3f
    def messages_popular_show(self):
        for user in self.users_list:
            popular = user.popular_message()
            if popular is None:
                print("This user has not published any messages yet.")

            else:
                print(popular)