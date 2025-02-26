# 1a
from Message import Message
# 2a
from User import User
# 3a
from Twitter import Twitter

# 1b
"""
msg1 = Message("11/9", "2024-11-9", "11:09")
msg2 = Message("hemoglobin", "2024-11-9", "11:10")
msg3 = Message("mazgan", "2024-11-9", "11:12")
"""

# 1c
# print(f"{msg1}\n{msg2}\n{msg3}")

"""
# 2c
us1 = User("Ofek Perry", "Niv12")
us2 = User("Itay Schwager", "Matan333")


# 2d
us1.publish("Grr1")
us1.publish("Grr2")
us1.publish("Grr3")

us2.publish("Hi1")
us2.publish("Hi2")
us2.publish("Hi3")

# 2e + f
msg1 = us1.find_message("Grr1")
msg2 = us2.find_message("Hi2")
print(msg1)
print(msg2)

# 2g
msg1.add_like()
msg1.add_like()
msg2.add_like()
msg2.add_like()
"""

# 3c
t = Twitter()

# 3d
t.register("Ofek Perry", "Niv12")
# 3e
t.register("Ofek Perry", "Niv12")

# 3f
t.register("Itay Schwager", "Matan333")

# 3g
us1 = t.find("Ofek Perry")

# 3h
us1.show_all()

t.messages_popular_show()