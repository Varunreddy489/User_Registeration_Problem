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


def validate_mobile_number(mobile_number):
    """
    Validate the given mobile number is valid or not
    :param mobile_number:
    :return: bool value based on the condition matches
    """
    pattern = r"^91\s[6-9]\d{9}"

    return bool(re.fullmatch(pattern, mobile_number))


def validate_password(password):

    #usecase-5
    if len(password)<8:
        return False

    #usecase-6
    if not re.search(r"[A-Z]", password):
        return False

    #usecase-7
    if not re.search(r"\d", password):
        return False
    


First_Name = input("Enter your first name :")
validate_first_and_last_name(First_Name)

last_name = input("Enter your last name :")
validate_first_and_last_name(last_name)

mail_id = input("Enter your mail id: ")
validate_email_id(mail_id)

mobile_number = input("Enter your mobile number: ")
validate_mobile_number(mobile_number)

password = input("Enter your password :")
validate_password(password)