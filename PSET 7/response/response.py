from validator_collection import validators, checkers, errors


def main():
    email_address = input("What's your email address? ")
    email_address = checkers.is_email(email_address)
    if email_address == True:
        print("Valid")
    else:
        print("Invalid")


main()
