import phonenumbers
from phonenumbers import geocoder

def track_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, "PH")
        region = geocoder.description_for_number(parsed_number, "en")
        return region
    except phonenumbers.phonenumberutil.NumberParseException:
        return "Invalid phone number"

phone_number = "+639266659001"  

location = track_phone_number(phone_number)
print(f"The location of {phone_number} is: {location}")