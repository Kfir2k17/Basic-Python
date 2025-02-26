# 2b
from datetime import date, datetime
from Message import Message

# 2c
class User:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.messages = []

    def publish(self, text):
        d = date.today()
        full_time = str(datetime.now().time())
        t = full_time[:5:]
        msg = Message(text, d, t)
        self.messages.append(msg)

# 2f
    def show_all(self):
        for item in self.messages:
            print(item)

# 2d
    def set_password(self, password):
        self.password = password

# 2e
    def get_password(self):
        return self.password

    def get_user_name(self):
        return self.user_name

# 2g
    def find_message(self, t):
        for item in self.messages:
            if item.text == t:
                return item
        return None

# 2h
    def popular_message(self):
        if not self.messages:
            return None
        popular = self.messages[0]
        for item in self.messages:
            if item.likes > popular.likes:
                popular = item
        return popular
