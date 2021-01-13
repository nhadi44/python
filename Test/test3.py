from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%B %d, %Y %H:%M:%S")
print("Now is", dt_string)

value = input("Input ")