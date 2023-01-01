# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

user2 = {
    'name': 'morna',
    'valid': False #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  # code here
    def wrap(*args, **kwargs):
        if args[0]['valid']:#because *args stores the values as a tuple and it stores the given dictionary in the 0 index position of the tuple
            fn(*args, **kwargs)
        else:
            print('You are not validated')# prints the message and does not execute the function because it is not called
    return wrap

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
message_friends(user2)