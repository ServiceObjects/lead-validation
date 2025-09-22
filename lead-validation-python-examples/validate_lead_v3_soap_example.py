import sys
import os

sys.path.insert(0, os.path.abspath("../lead-validation-python/SOAP"))

from validate_lead_v3_soap import ValidateLeadV3Soap


def validate_lead_v3_soap_sdk_go(is_live: bool, license_key: str) -> None:
    print("\r\n-------------------------------------------")
    print("LeadValidation - ValidateLead_V3 - SOAP SDK")
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
        service = ValidateLeadV3Soap(license_key, is_live, timeout_ms=10000)
        response = service.validate_lead_v3(
            full_name, salutation, first_name, last_name, business_name, business_domain, business_ein,
            address1, address2, address3, address4, address5, locality, admin_area, postal_code, country,
            phone1, phone2, email, ip_address, gender, date_of_birth, utc_capture_time, output_language, test_type
        )

        if hasattr(response, 'Error') and response.Error:
            print("\r\n* Error *\r\n")
            print(f"Error Type    : {getattr(response.Error, 'Type', '')}")
            print(f"Error TypeCode: {getattr(response.Error, 'TypeCode', '')}")
            print(f"Error Desc    : {getattr(response.Error, 'Desc', '')}")
            print(f"Error DescCode: {getattr(response.Error, 'DescCode', '')}")

        print("\r\n* Lead Validation Info *\r\n")
        if response:
            print(f"OverallCertainty  : {getattr(response, 'OverallCertainty', '')}")
            print(f"OverallQuality    : {getattr(response, 'OverallQuality', '')}")
            print(f"LeadType          : {getattr(response, 'LeadType', '')}")
            print(f"LeadCountry       : {getattr(response, 'LeadCountry', '')}")
            print(f"NoteCodes         : {getattr(response, 'NoteCodes', '')}")
            print(f"NoteDesc          : {getattr(response, 'NoteDesc', '')}")
            print(f"NameCertainty     : {getattr(response, 'NameCertainty', '')}")
            print(f"NameQuality       : {getattr(response, 'NameQuality', '')}")
            print(f"FirstName         : {getattr(response, 'FirstName', '')}")
            print(f"LastName          : {getattr(response, 'LastName', '')}")
            print(f"FirstNameClean    : {getattr(response, 'FirstNameLatin', '')}")
            print(f"LastNameClean     : {getattr(response, 'LastNameLatin', '')}")
            print(f"NameNoteCodes     : {getattr(response, 'NameNoteCodes', '')}")
            print(f"NameNoteDesc      : {getattr(response, 'NameNoteDesc', '')}")
            print(f"AddressCertainty  : {getattr(response, 'AddressCertainty', '')}")
            print(f"AddressQuality    : {getattr(response, 'AddressQuality', '')}")
            print(f"Address1          : {getattr(response, 'AddressLine1', '')}")
            print(f"Address2          : {getattr(response, 'AddressLine2', '')}")
            print(f"Address3          : {getattr(response, 'AddressLine3', '')}")
            print(f"Address4          : {getattr(response, 'AddressLine4', '')}")
            print(f"Address5          : {getattr(response, 'AddressLine5', '')}")
            print(f"AddressLocality   : {getattr(response, 'AddressLocality', '')}")
            print(f"AddressAdminArea  : {getattr(response, 'AddressAdminArea', '')}")
            print(f"AddressPostalCode : {getattr(response, 'AddressPostalCode', '')}")
            print(f"AddressCountry    : {getattr(response, 'AddressCountry', '')}")
            print(f"AddressNoteCodes  : {getattr(response, 'AddressNoteCodes', '')}")
            print(f"AddressNoteDesc   : {getattr(response, 'AddressNoteDesc', '')}")
            print(f"EmailCertainty    : {getattr(response, 'EmailCertainty', '')}")
            print(f"EmailQuality      : {getattr(response, 'EmailQuality', '')}")
            print(f"EmailCorrected    : {getattr(response, 'EmailCorrected', '')}")
            print(f"EmailNoteCodes    : {getattr(response, 'EmailNoteCodes', '')}")
            print(f"EmailNoteDesc     : {getattr(response, 'EmailNoteDesc', '')}")
            print(f"IPAddressCertainty: {getattr(response, 'IPCertainty', '')}")
            print(f"IPAddressQuality  : {getattr(response, 'IPQuality', '')}")
            print(f"IPCountry         : {getattr(response, 'IPCountry', '')}")
            print(f"IPLocality        : {getattr(response, 'IPLocality', '')}")
            print(f"IPAdminArea       : {getattr(response, 'IPAdminArea', '')}")
            print(f"IPNoteCodes       : {getattr(response, 'IPNoteCodes', '')}")
            print(f"IPNoteDesc        : {getattr(response, 'IPNoteDesc', '')}")
            print(f"Phone1Certainty   : {getattr(response, 'Phone1Certainty', '')}")
            print(f"Phone1Quality     : {getattr(response, 'Phone1Quality', '')}")
            print(f"Phone1Locality    : {getattr(response, 'Phone1Locality', '')}")
            print(f"Phone1AdminArea   : {getattr(response, 'Phone1AdminArea', '')}")
            print(f"Phone1Country     : {getattr(response, 'Phone1Country', '')}")
            print(f"Phone1NoteCodes   : {getattr(response, 'Phone1NoteCodes', '')}")
            print(f"Phone1NoteDesc    : {getattr(response, 'Phone1NoteDesc', '')}")
            print(f"Phone2Certainty   : {getattr(response, 'Phone2Certainty', '')}")
            print(f"Phone2Quality     : {getattr(response, 'Phone2Quality', '')}")
            print(f"Phone2Locality    : {getattr(response, 'Phone2Locality', '')}")
            print(f"Phone2AdminArea   : {getattr(response, 'Phone2AdminArea', '')}")
            print(f"Phone2Country     : {getattr(response, 'Phone2Country', '')}")
            print(f"Phone2NoteCodes   : {getattr(response, 'Phone2NoteCodes', '')}")
            print(f"Phone2NoteDesc    : {getattr(response, 'Phone2NoteDesc', '')}")

            print("\r\n* Phone Contact *\r\n")
            if hasattr(response, 'PhoneContact') and response.PhoneContact:
                print(f"Name   : {getattr(response.PhoneContact, 'Name', '')}")
                print(f"Address: {getattr(response.PhoneContact, 'Address', '')}")
                print(f"City   : {getattr(response.PhoneContact, 'City', '')}")
                print(f"State  : {getattr(response.PhoneContact, 'State', '')}")
                print(f"Zip    : {getattr(response.PhoneContact, 'Zip', '')}")
                print(f"Type   : {getattr(response.PhoneContact, 'Type', '')}")
            else:
                print("No phone contact found.")

            print("\r\n* Information Components *\r\n")
            if hasattr(response, 'InformationComponents') and response.InformationComponents:
                components = response.InformationComponents.InformationComponent
                if not isinstance(components, list):
                    components = [components]
                for component in components:
                    print(f"{getattr(component, 'Name', '')}: {getattr(component, 'Value', '')}")
            else:
                print("No information components found.")
        else:
            print("No lead validation info found.")

    except Exception as e:
        print("\r\n* Error *\r\n")
        print(f"Exception occurred: {str(e)}")