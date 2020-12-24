
def main():
    user = get_user_name()
    length = length(user)
    hi = hello_world()
    result = "Your name " user + " is " + str(length) " long. \n" + hi
    return result
    
def get_user_name():
    name = input("Please enter your name: ")
    return name

def return_length(object): 
    length = len(object)
    return length
    
def hello_world():
    result = "Hello World!"
    return result
    
print (main())



