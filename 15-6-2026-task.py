# DAILY TASK- WEEK 2- DAY 3
'''Write regex functions to:
✓ Validate email address format
✓ Validate Indian phone number (10 digits)
✓ Extract all dates (DD/MM/YYYY) from a paragraph
✓ Mask credit card numbers - show only last 4 digits'''

import re
import logging

logger = logging.getLogger("ValidationApp")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


def validate_email(input_email):
    email_pattern = r'^[A-Za-z0-9_+%.-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    if re.fullmatch(email_pattern, input_email):
        logger.info("Valid email entered")
        return True

    logger.error("Invalid email entered")
    raise ValueError("Enter a valid email")


def validate_phone(input_phone):
    phone_pattern = r'^[6-9]\d{9}$'

    if re.fullmatch(phone_pattern, input_phone):
        logger.info("Valid phone number entered")
        return True

    logger.error("Invalid phone number entered")
    raise ValueError("Enter a valid Indian phone number")


def extract_dates(paragraph):
    date_pattern = re.compile(
        r"\b(?:0[1-9]|[12][0-9]|3[01])(?:/|-)(?:0[1-9]|1[0-2])(?:/|-)\d{4}\b"
    )

    dates = date_pattern.findall(paragraph)

    if dates:
        logger.info(f"{len(dates)} date(s) found")
        return dates

    logger.error("No dates found")
    raise ValueError("No dates found in the paragraph")


def mask_card(input_card):
    if not re.fullmatch(r"\d{16}", input_card):
        logger.error("Invalid credit card number")
        raise ValueError("Enter a valid 16-digit credit card number")

    masked = re.sub(r"\d(?=\d{4})", "*", input_card)

    logger.info("Credit card masked successfully")
    return masked

print("MENU:\n1.Email validation\n2.Phone validation\n3.Finding dates in a paragraph\n4.Masking credit card number\n0.Exit")

while True:
    try:
        choice = int(input("Enter the choice: "))
    except ValueError:
        logger.warning("Non-numeric menu choice entered")
        print("Please enter a number between 0 and 4.")
        continue

    match choice:

        case 0:
            logger.info("Application exited")
            print("Exiting...")
            break

        case 1:
            try:
                email = input("Enter email: ")
                validate_email(email)
                print("Email validated successfully.")
            except Exception as e:
                print("Error:", e)

        case 2:
            try:
                phone = input("Enter phone number: ")
                validate_phone(phone)
                print("Phone number validated successfully.")
            except Exception as e:
                print("Error:", e)

        case 3:
            try:
                paragraph = input("Enter paragraph: ")
                dates = extract_dates(paragraph)

                print("Dates found:")
                for date in dates:
                    print(date)

            except Exception as e:
                print("Error:", e)

        case 4:
            try:
                card = input("Enter 16-digit credit card number: ")
                print("Masked Card:", mask_card(card))

            except Exception as e:
                print("Error:", e)

        case _:
            logger.warning("Invalid menu option selected")
            print("Invalid choice. Please select between 0 and 4.")