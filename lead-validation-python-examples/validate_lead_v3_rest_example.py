import sys
import os

sys.path.insert(0, os.path.abspath("../lead-validation-python/REST"))

from validate_lead_v3_rest import validate_lead_v3


def validate_lead_v3_rest_sdk_go(is_live: bool, license_key: str) -> None:
    print("\r\n-------------------------------------------")
    print("LeadValidation - ValidateLead_V3 - REST SDK")
    print("-------------------------------------------")

    full_name = "Tim Cook"
    salutation = ""
    first_name = ""
    last_name = ""
    business_name = "Apple"
    business_domain = ""
    business_ein = ""
    address1 = "27 E Cota St"
    address2 = "Suite 500"
    address3 = ""
    address4 = ""
    address5 = ""
    locality = "Cupertino"
    admin_area = "CA"
    postal_code = "93101"
    country = "US"
    phone1 = "1-408-996-1010"
    phone2 = ""
    email = "tim.cook@apple.com"
    ip_address = "192.168.1.1"
    gender = ""
    date_of_birth = "1"
    utc_capture_time = ""
    output_language = "English"
    test_type = "business-noip"
    timeout_seconds = 15

    print("\r\n* Input *\r\n")
    print(f"FullName      : {full_name}")
    print(f"Salutation    : {salutation}")
    print(f"FirstName     : {first_name}")
    print(f"LastName      : {last_name}")
    print(f"BusinessName  : {business_name}")
    print(f"BusinessDomain: {business_domain}")
    print(f"BusinessEIN   : {business_ein}")
    print(f"Address1      : {address1}")
    print(f"Address2      : {address2}")
    print(f"Address3      : {address3}")
    print(f"Address4      : {address4}")
    print(f"Address5      : {address5}")
    print(f"Locality      : {locality}")
    print(f"AdminArea     : {admin_area}")
    print(f"PostalCode    : {postal_code}")
    print(f"Country       : {country}")
    print(f"Phone1        : {phone1}")
    print(f"Phone2        : {phone2}")
    print(f"Email         : {email}")
    print(f"IPAddress     : {ip_address}")
    print(f"Gender        : {gender}")
    print(f"DateOfBirth   : {date_of_birth}")
    print(f"UTCCaptureTime: {utc_capture_time}")
    print(f"OutputLanguage: {output_language}")
    print(f"TestType      : {test_type}")
    print(f"LicenseKey    : {license_key}")
    print(f"IsLive        : {is_live}")

    try:
        response = validate_lead_v3(
            full_name, salutation, first_name, last_name, business_name, business_domain, business_ein,
            address1, address2, address3, address4, address5, locality, admin_area, postal_code, country,
            phone1, phone2, email, ip_address, gender, date_of_birth, utc_capture_time, output_language,
            test_type, license_key, is_live
        )

        print("\r\n* Lead Validation Info *\r\n")
        if response and not response.Error:
            print(f"OverallCertainty  : {response.OverallCertainty}")
            print(f"OverallQuality    : {response.OverallQuality}")
            print(f"LeadType          : {response.LeadType}")
            print(f"LeadCountry       : {response.LeadCountry}")
            print(f"NoteCodes         : {response.NoteCodes}")
            print(f"NoteDesc          : {response.NoteDesc}")
            print(f"NameCertainty     : {response.NameCertainty}")
            print(f"NameQuality       : {response.NameQuality}")
            print(f"FirstName         : {response.FirstName}")
            print(f"LastName          : {response.LastName}")
            print(f"FirstNameClean    : {response.FirstNameClean}")
            print(f"LastNameClean     : {response.LastNameClean}")
            print(f"NameNoteCodes     : {response.NameNoteCodes}")
            print(f"NameNoteDesc      : {response.NameNoteDesc}")
            print(f"AddressCertainty  : {response.AddressCertainty}")
            print(f"AddressQuality    : {response.AddressQuality}")
            print(f"Address1          : {response.Address1}")
            print(f"Address2          : {response.Address2}")
            print(f"Address3          : {response.Address3}")
            print(f"Address4          : {response.Address4}")
            print(f"Address5          : {response.Address5}")
            print(f"AddressLocality   : {response.AddressLocality}")
            print(f"AddressAdminArea  : {response.AddressAdminArea}")
            print(f"AddressPostalCode : {response.AddressPostalCode}")
            print(f"AddressCountry    : {response.AddressCountry}")
            print(f"AddressNoteCodes  : {response.AddressNoteCodes}")
            print(f"AddressNoteDesc   : {response.AddressNoteDesc}")
            print(f"EmailCertainty    : {response.EmailCertainty}")
            print(f"EmailQuality      : {response.EmailQuality}")
            print(f"EmailCorrected    : {response.EmailCorrected}")
            print(f"EmailNoteCodes    : {response.EmailNoteCodes}")
            print(f"EmailNoteDesc     : {response.EmailNoteDesc}")
            print(f"IPAddressCertainty: {response.IPAddressCertainty}")
            print(f"IPAddressQuality  : {response.IPAddressQuality}")
            print(f"IPCountry         : {response.IPCountry}")
            print(f"IPLocality        : {response.IPLocality}")
            print(f"IPAdminArea       : {response.IPAdminArea}")
            print(f"IPNoteCodes       : {response.IPNoteCodes}")
            print(f"IPNoteDesc        : {response.IPNoteDesc}")
            print(f"Phone1Certainty   : {response.Phone1Certainty}")
            print(f"Phone1Quality     : {response.Phone1Quality}")
            print(f"Phone1Locality    : {response.Phone1Locality}")
            print(f"Phone1AdminArea   : {response.Phone1AdminArea}")
            print(f"Phone1Country     : {response.Phone1Country}")
            print(f"Phone1NoteCodes   : {response.Phone1NoteCodes}")
            print(f"Phone1NoteDesc    : {response.Phone1NoteDesc}")
            print(f"Phone2Certainty   : {response.Phone2Certainty}")
            print(f"Phone2Quality     : {response.Phone2Quality}")
            print(f"Phone2Locality    : {response.Phone2Locality}")
            print(f"Phone2AdminArea   : {response.Phone2AdminArea}")
            print(f"Phone2Country     : {response.Phone2Country}")
            print(f"Phone2NoteCodes   : {response.Phone2NoteCodes}")
            print(f"Phone2NoteDesc    : {response.Phone2NoteDesc}")

            print("\r\n* Phone Contact *\r\n")
            if response.PhoneContact:
                print(f"Name   : {response.PhoneContact.Name}")
                print(f"Address: {response.PhoneContact.Address}")
                print(f"City   : {response.PhoneContact.City}")
                print(f"State  : {response.PhoneContact.State}")
                print(f"Zip    : {response.PhoneContact.Zip}")
                print(f"Type   : {response.PhoneContact.Type}")
            else:
                print("No phone contact found.")

            print("\r\n* Information Components *\r\n")
            if response.InformationComponents and len(response.InformationComponents) > 0:
                for component in response.InformationComponents:
                    print(f"{component.Name}: {component.Value}")
            else:
                print("No information components found.")
        else:
            print("No lead validation info found.")

        if response.Error:
            print("\r\n* Error *\r\n")
            print(f"Error Type    : {response.Error.Type}")
            print(f"Error TypeCode: {response.Error.TypeCode}")
            print(f"Error Desc    : {response.Error.Desc}")
            print(f"Error DescCode: {response.Error.DescCode}")

    except Exception as e:
        print("\r\n* Error *\r\n")
        print(f"Error Message: {str(e)}")
