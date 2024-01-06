import phonenumbers
from phonenumbers import geocoder, carrier

def track_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, "PH")
        region = geocoder.description_for_number(parsed_number, "en")
        carrier_name = carrier.name_for_number(parsed_number, "en")
        return region, carrier_name
    except phonenumbers.phonenumberutil.NumberParseException:
        return "Invalid phone number"

phone_number = "+63"  

location, network = track_phone_number(phone_number)
print(f"The location of {phone_number} is: {location}")
print(f"The network provider for {phone_number} is: {network}")