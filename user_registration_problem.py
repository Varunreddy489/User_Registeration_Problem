import re

def validate_first_and_last_name(First_Name):
    """
    Function to validate the first and last name
    :param First_Name:
    :return: bool value based on the condition matches
    """
    pattern = r"^[A-Z][a-z]{2,}$"
    return bool(re.fullmatch(pattern, First_Name))


def validate_email_id(mail):
    """
    Function to check the given mail id is correct or false
    :param mail:
    :return: bool value based on the condition matches
    """
    pattern = r"^[a-z]+(\.[a-z0-9]+)?@[a-z]+\.[a-z]{2,3}(\.[a-z]{2})?$"

    return bool(re.fullmatch(pattern, mail))



First_Name = input("Enter your first name :")

validate_first_and_last_name(First_Name)

last_name = input("Enter your last name :")

validate_first_and_last_name(last_name)


mail_id = input("Enter your mail id: ")

validate_email_id(mail_id)