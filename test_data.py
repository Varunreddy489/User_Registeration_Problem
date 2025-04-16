import json
import pytest
from loguru import logger

from user_registration_problem import (
    validate_password,
    validate_email_samples,
    validate_mobile_number,
    validate_first_and_last_name,
)

logger.add(
    "test_validation_errors_{time}.log",
    rotation="1 min",
    retention="10 days",
    level="ERROR",
)

logger.add("test_success.log", rotation="1 mb", retention="10 days", level="SUCCESS")


def load_test_data():
    with open("validation_test_data.json", "r") as f:
        return json.load(f)


test_data = load_test_data()
valid_tuples = test_data.get("True", [])
invalid_tuples = test_data.get("False", [])


@pytest.mark.parametrize("test_tuple", valid_tuples)
def test_individual_valid_tuples(test_tuple):
    name, mobile, password, email = test_tuple

    try:
        assert validate_first_and_last_name(name), f"Valid name failed: {name}"
        assert validate_mobile_number(mobile), f"Valid mobile failed: {mobile}"
        assert validate_password(password), f"Valid password failed: {password}"
        assert validate_email_samples(email), f"Valid email failed: {email}"
        logger.success(f" Validation Success for valid tuple: {test_tuple}")
    except AssertionError as e:
        logger.error(
            f" Validation failed for valid tuple: {test_tuple} | Reason: {str(e)}"
        )
        raise


@pytest.mark.parametrize("test_tuple", invalid_tuples)
def test_individual_invalid_tuples(test_tuple):
    name, mobile, password, email = test_tuple

    is_name_valid = validate_first_and_last_name(name)
    is_mobile_valid = validate_mobile_number(mobile)
    is_password_valid = validate_password(password)
    is_email_valid = validate_email_samples(email)

    validation_results = [
        is_name_valid,
        is_mobile_valid,
        is_password_valid,
        is_email_valid,
    ]

    if all(validation_results):
        logger.error(
            f" Invalid tuple unexpectedly passed all validations: {test_tuple}"
        )
    assert (
        False in validation_results
    ), f"Invalid tuple unexpectedly passed all validations: {test_tuple}"
    