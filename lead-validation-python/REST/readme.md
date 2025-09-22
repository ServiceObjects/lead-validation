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
#
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

from validate_lead_v3_rest import validate_lead_v3
 
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
is_live = True
license_key = "YOUR LICENSE KEY"

# 2. Call the sync Invoke() method.
response = validate_lead_v3(
    full_name, salutation, first_name, last_name, business_name, business_domain, business_ein,
    address1, address2, address3, address4, address5, locality, admin_area, postal_code, country,
    phone1, phone2, email, ip_address, gender, date_of_birth, utc_capture_time, output_language,
    test_type, license_key, is_live
)

# 3. Inspect results.
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
```
