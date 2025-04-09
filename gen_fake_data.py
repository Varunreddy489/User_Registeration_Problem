import re
import json
import random
from faker import Faker
from user_registration_problem import (
    validate_first_and_last_name,
    validate_email_samples,
    validate_password,
    validate_mobile_number,
)

fake = Faker()


# Function to generate valid names (matching the pattern)
def generate_valid_name():
    # Start with a capital letter followed by 2 or more lowercase letters
    first_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # Generate a random length between 2 and 10 for the rest of the name
    length = random.randint(2, 10)
    rest_of_name = "".join(
        random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(length)
    )
    return first_letter + rest_of_name


# Function to generate invalid names (not matching the pattern)
def generate_invalid_name():
    invalid_type = random.randint(1, 5)

    if invalid_type == 1:
        # First letter lowercase
        return fake.first_name().lower()
    elif invalid_type == 2:
        # All uppercase
        return fake.first_name().upper()
    elif invalid_type == 3:
        # Too short (only one lowercase letter after capital)
        first_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        return first_letter + random.choice("abcdefghijklmnopqrstuvwxyz")
    elif invalid_type == 4:
        # Contains numbers or special characters
        return fake.first_name() + random.choice("123456789!@#$%")
    else:
        # Empty string or space
        return random.choice(["", " ", "  "])


# Function to generate valid mobile number
def generate_valid_mobile():
    # Format: "91 [6-9]XXXXXXXXX"
    first_digit = random.choice("6789")
    rest_digits = "".join(random.choice("0123456789") for _ in range(9))
    return f"91 {first_digit}{rest_digits}"


# Function to generate invalid mobile number
def generate_invalid_mobile():
    invalid_type = random.randint(1, 5)

    if invalid_type == 1:
        # Wrong prefix
        first_digit = random.choice("6789")
        rest_digits = "".join(random.choice("0123456789") for _ in range(9))
        return f"92 {first_digit}{rest_digits}"
    elif invalid_type == 2:
        # Invalid first digit
        first_digit = random.choice("012345")
        rest_digits = "".join(random.choice("0123456789") for _ in range(9))
        return f"91 {first_digit}{rest_digits}"
    elif invalid_type == 3:
        # Too short
        first_digit = random.choice("6789")
        rest_digits = "".join(
            random.choice("0123456789") for _ in range(random.randint(4, 8))
        )
        return f"91 {first_digit}{rest_digits}"
    elif invalid_type == 4:
        # No space after 91
        first_digit = random.choice("6789")
        rest_digits = "".join(random.choice("0123456789") for _ in range(9))
        return f"91{first_digit}{rest_digits}"
    else:
        # Contains letters
        return f"91 {random.choice('6789')}{''.join(random.choice('0123456789abcdefgh') for _ in range(9))}"


# Function to generate valid password
def generate_valid_password():
    # Must be at least 8 characters
    # Must have at least one uppercase letter
    # Must have at least one digit
    # Must have exactly one special character

    # Start with the required characters
    uppercase = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digit = random.choice("0123456789")
    special = random.choice("!@#$%^&*()_+-={}[]:\"'<>,.?/")

    # Add more characters to reach at least 8
    min_additional_chars = max(
        5, random.randint(5, 12)
    )  # At least 5 more to make 8+ total
    additional = "".join(
        random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        for _ in range(min_additional_chars)
    )

    # Combine and shuffle
    pwd_chars = list(uppercase + digit + special + additional)
    random.shuffle(pwd_chars)
    return "".join(pwd_chars)


# Function to generate invalid password
def generate_invalid_password():
    invalid_type = random.randint(1, 4)

    if invalid_type == 1:
        # Too short (less than 8 characters)
        length = random.randint(1, 7)
        return "".join(
            random.choice(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
            )
            for _ in range(length)
        )
    elif invalid_type == 2:
        # No uppercase letter
        length = random.randint(8, 15)
        return "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz0123456789!")
            for _ in range(length)
        )
    elif invalid_type == 3:
        # No digits
        length = random.randint(8, 15)
        return "".join(
            random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!")
            for _ in range(length)
        )
    else:
        # No special character or more than one special character
        special_count = random.choice([0, 2, 3])
        specials = "".join(
            random.choice("!@#$%^&*()_+-={}[]:\"'<>,.?/") for _ in range(special_count)
        )
        other_length = random.randint(8, 12)
        other_chars = "".join(
            random.choice(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            )
            for _ in range(other_length)
        )
        pwd_chars = list(specials + other_chars)
        random.shuffle(pwd_chars)
        return "".join(pwd_chars)


# Function to generate valid email
def generate_valid_email():
    # The pattern is: ^[a-zA-Z0-9]+([._+-]?[a-zA-Z0-9]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z]{2,}){1,2}$

    # Username part
    username_length = random.randint(3, 15)
    username = "".join(
        random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        for _ in range(username_length)
    )

    # Sometimes add a separator followed by more characters
    if random.random() > 0.5:
        separator = random.choice([".", "-", "_", "+"])
        additional_length = random.randint(1, 8)
        additional = "".join(
            random.choice(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            )
            for _ in range(additional_length)
        )
        username += separator + additional

    # Domain part
    domain_length = random.randint(3, 10)
    domain = "".join(
        random.choice("abcdefghijklmnopqrstuvwxyz0123456789-")
        for _ in range(domain_length)
    )

    # TLD part
    tld_options = ["com", "org", "net", "edu", "gov", "io", "co", "info", "biz"]
    tld = random.choice(tld_options)

    # Sometimes add a second level TLD
    if random.random() > 0.7:
        country_tlds = ["us", "uk", "ca", "au", "in", "de", "fr", "jp", "br", "it"]
        second_tld = random.choice(country_tlds)
        return f"{username}@{domain}.{second_tld}.{tld}"
    else:
        return f"{username}@{domain}.{tld}"


# Function to generate invalid email
def generate_invalid_email():
    invalid_type = random.randint(1, 6)

    if invalid_type == 1:
        # No @ symbol
        username_length = random.randint(3, 15)
        username = "".join(
            random.choice(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            )
            for _ in range(username_length)
        )
        domain_length = random.randint(3, 10)
        domain = "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz0123456789")
            for _ in range(domain_length)
        )
        return f"{username}{domain}.{tld}"
    elif invalid_type == 2:
        # Invalid characters in username
        username = "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(3)
        )
        username += random.choice("!#$%^&*()[]{}|;:\"',<>/?")
        username += "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(3)
        )
        domain = "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(5)
        )
        tld = random.choice(["com", "org", "net"])
        return f"{username}@{domain}.{tld}"
    elif invalid_type == 3:
        # Consecutive dots in domain part
        username = "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(5)
        )
        domain = "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(3)
        )
        domain += ".."
        domain += "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(2)
        )
        tld = random.choice(["com", "org", "net"])
        return f"{username}@{domain}.{tld}"
    elif invalid_type == 4:
        # No TLD
        username = "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(5)
        )
        domain = "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(5)
        )
        return f"{username}@{domain}"
    elif invalid_type == 5:
        # TLD too short (single character)
        username = "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(5)
        )
        domain = "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(5)
        )
        return f"{username}@{domain}.{random.choice('abcdefghijklmnopqrstuvwxyz')}"
    else:
        # Too many TLD levels
        username = "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(5)
        )
        domain = "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(5)
        )
        return f"{username}@{domain}.co.uk.com"


# Generate 1000 valid tuples (all 4 elements must pass validation)
valid_tuples = []
while len(valid_tuples) < 1000:
    name = generate_valid_name()
    mobile = generate_valid_mobile()
    password = generate_valid_password()
    email = generate_valid_email()

    # Double-check all elements pass validation
    if (
        validate_first_and_last_name(name)
        and validate_mobile_number(mobile)
        and validate_password(password)
        and validate_email_samples(email)
    ):
        valid_tuples.append((name, mobile, password, email))

# Generate 1000 invalid tuples (at least one element must fail validation)
invalid_tuples = []
while len(invalid_tuples) < 1000:
    # Choose which element(s) to make invalid
    num_invalid = random.randint(1, 4)
    invalid_elements = random.sample([0, 1, 2, 3], num_invalid)

    # Generate elements
    name = (
        generate_valid_name() if 0 not in invalid_elements else generate_invalid_name()
    )
    mobile = (
        generate_valid_mobile()
        if 1 not in invalid_elements
        else generate_invalid_mobile()
    )
    password = (
        generate_valid_password()
        if 2 not in invalid_elements
        else generate_invalid_password()
    )
    email = (
        generate_valid_email()
        if 3 not in invalid_elements
        else generate_invalid_email()
    )

    # Verify at least one element fails validation
    if not (
        validate_first_and_last_name(name)
        and validate_mobile_number(mobile)
        and validate_password(password)
        and validate_email_samples(email)
    ):
        invalid_tuples.append((name, mobile, password, email))

# Convert to the required dictionary format
result_dict = {"True": valid_tuples, "False": invalid_tuples}

# Save as JSON file
with open("validation_test_data.json", "w") as f:
    json.dump(result_dict, f, indent=2)

print(
    f"Successfully generated 1000 valid and 1000 invalid data tuples and saved to validation_test_data.json"
)

# Print some samples
print("\nSample Valid Tuples:")
for i in range(min(5, len(valid_tuples))):
    print(valid_tuples[i])

print("\nSample Invalid Tuples:")
for i in range(min(5, len(invalid_tuples))):
    print(invalid_tuples[i])
