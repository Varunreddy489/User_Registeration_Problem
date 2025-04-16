import re

First_Name = input("Enter your first name :")


def validate_first_and_last_name(First_Name):
    """
    Function to validate the first and last name
    :param First_Name:
    :return: bool value based on the condition matches
    """
    pattern = r"^[A-Z][a-z]{2,}$"
    return bool(re.fullmatch(pattern, First_Name))


print(validate_first_and_last_name(First_Name))