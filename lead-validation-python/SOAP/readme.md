![Service Objects Logo](https://www.serviceobjects.com/wp-content/uploads/2021/05/SO-Logo-with-TM.gif "Service Objects Logo")

# LV - Lead Validation

The DOTS Lead Validation system (LV) evaluates information customers provide and scores the data quality into pass/fail/review categories. By evaluating the information quality of a contact, online marketers can more effectively weed-out fraudulent contacts.

Online fraudsters are more likely to provide inaccurate contact information because the address and phone number can be easily traced. Unlike other validation services that perform simple data checks on single variables, Service Objects Lead Validation solution is able to cross-validate that a contact’s name, address, phone numbers, e-mail and IP address are all matched each other and are related to the consumer.

## [Service Objects Website](https://serviceobjects.com)

# LV - ValidateLead_V3

Our Lead Validation service cross-validates, corrects and scores over 130 key data points to help your business more accurately identify quality leads for US and Canada. Works with leading CRM and marketing automation platforms.

This document defines the input, output, and behavior of the web services in LV.

### [ValidateLead_V3 Developer Guide/Documentation](https://www.serviceobjects.com/docs/dots-lead-validation/lv-operations/lv-validatelead_v3-recommended-operation/)

## Library Usage

```
# 1. Build the input
#  Required fields:
#               LicenseKey
#               IsLive
#
# Optional:
#        FullName
#        Salutation
#        FirstName
#        BusinessName
#        BusinessDomain
#        BusinessEIN
#        Address1
#        Address2
#        Address3
#        Address4
#        Address5
#        Locality
#        AdminArea
#        PostalCode
#        Country
#        Phone1
#        Phone2
#        Email
#        IPAddress
#        Gender
#        DateOfBirth
#        UTCCaptureTime
#        OutputLanguage
#        TestType

from validate_lead_v3_soap import ValidateLeadV3Soap
 
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
license_key = "YOUR LICENSE KEY"

# 2. Call the sync Invoke() method.
service = ValidateLeadV3Soap(license_key, True, timeout_ms=10000))
response = service.validate_lead_v3(
    full_name, salutation, first_name, last_name, business_name, business_domain, business_ein,
    address1, address2, address3, address4, address5, locality, admin_area, postal_code, country,
    phone1, phone2, email, ip_address, gender, date_of_birth, utc_capture_time, output_language, test_type
)

# 3. Inspect results.
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
```
