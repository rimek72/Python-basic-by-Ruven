# Address book
# The info will be in a list of dicts

# Call the list "people"

# Each dict  in "people" will contain:
# - first_name
# - last_name
# - email
# - phone

# Ask the user, repeatedly, to enter a command

# - q (quit)
# - a (add -- ask 4 questions, use the 4 answers to create a dict, and add the dict to people)
# - l (list -- see all of the people in the address book)
# - f (find -- ask the user for a search string; show all people where the search string exists *INSIDE*
#    first name, last name, and/or email

people = []
filename = 'people.data'

while True:
    print(people)

    user_choice = input('Enter choice: ').strip()

    if user_choice == 'q':
        break

    elif user_choice == 'a':
        new_person = {}
        for one_field in ['first_name', 'last_name', 'email', 'phone']:
            new_person[one_field] = input(f'Enter {one_field}: ').strip()

        people.append(new_person)


        # first_name = input('Enter first name: ').strip()
        # last_name = input('Enter last name: ').strip()
        # email = input('Enter email: ').strip()
        # phone = input('Enter phone: ').strip()
        #
        # new_person = {'first_name':first_name,
        # 'last_name':last_name,
        # 'email':email,
        # 'phone':phone}
        #
        # people.append(new_person)

    elif user_choice == 'l':
        for one_person in people:
            print(f'{one_person["last_name"]}, {one_person["first_name"]}')
            print(f'\t{one_person["phone"]}')
            print(f'\t{one_person["email"]}')

    elif user_choice == 'f':
        look_for = input('Enter search string: ').strip()
        for one_person in people:
            if (look_for in one_person['first_name'] or
                look_for in one_person['last_name'] or
                look_for in one_person['email']):

                print(f'{one_person["last_name"]}, {one_person["first_name"]}')
                print(f'\t{one_person["phone"]}')
                print(f'\t{one_person["email"]}')

    elif user_choice == 'w':   # tab-separated, one person/record per line
        with open(filename, 'w') as outfile:
            for one_person in people:   # get dicts, one at a time
                outfile.write(f'{one_person["first_name"]}\t{one_person["last_name"]}\t{one_person["phone"]}\t{one_person["email"]}\n')

    elif user_choice == 'r':
        people = []

        for one_line in open(filename):
            first_name, last_name, phone, email = one_line.strip().split('\t')

            people.append({'first_name':first_name,
                           'last_name':last_name,
                           'phone':phone,
                           'email': email})

    else:
        print(f'{user_choice} is not valid.')


