#multiple itemas in a single variable 
#can do lists of list as well
lst = ["String", 1, 3.14, ["A new item"], "Kalob"]
#no point just printing
print(lst)
#better version
for item in lst:
    print("The item is: ", item)
    print("the class is: ",type(item))
