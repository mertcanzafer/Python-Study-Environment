import re

# Final regular expression updated.
regex = re.compile(
    r'^(?:"[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~.\s-]+"|[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+(\.[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+)*)@'
    r'(?:(?!-)[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+(?<!\.)(?<!\.web)|\[[0-9]{1,3}(\.[0-9]{1,3}){3}\])$'
)


def IsValid(email):
    if regex.match(email):
        print(f"Valid:   {email}")
    else:
        print(f"Invalid: {email}")


# Get the input from the user
terminate = ''

while terminate != 'q':
    mail = input("Enter a mail: ")
    IsValid(mail)
    terminate = input(
        "Press q to exit or press anything if you wanna continue: ")
    terminate = terminate.lower()
