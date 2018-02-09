should_continue = True
if should_continue: 
    print('Hello')

# known_people = ['John', 'Henry', 'William']
# person = input('Enter the person you know:')
# if person in known_people:
#     print ('You know {}!'.format(person))
# if person not in known_people:
#     print ('Hello random person!')

# known_cats = ['Sparky', 'Lemon', 'Meow']
# input_cat = input('Enter a cat-name:')
# print('Known cat') if input_cat in known_cats else print('unknown cat')

def who_do_you_know():
    #Ask a user for a list of people they know
    people_string = input('Enter a list of people you know, separated by commas: ')
    user_list = people_string.split(',') 
    print(user_list)
    users_without_spaces = []
    for user in user_list:
        users_without_spaces.append(user.strip())
    #Split the input into a list
    print(users_without_spaces)
    return users_without_spaces
    #Return the list

def ask_user():
    #Ask a user for their name
    user_name = input('What is your name?')
    print('you know this person') if user_name in who_do_you_know() else print('unknown person')

ask_user()