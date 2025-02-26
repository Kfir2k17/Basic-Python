# 1b
class Message:
    def __init__(self, text, date, time):
        self.text = text
        self.date = date
        self.time = time
        self.likes = 0

    def add_like(self):
        self.likes += 1

    def get_text(self):
        return self.text

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_likes(self):
        return self.likes

    def __str__(self):
        s = f"text: {self.text} "
        s += f"date: {self.date} "
        s += f"time: {self.time} "
        s += f"likes: {self.likes} "
        return s
