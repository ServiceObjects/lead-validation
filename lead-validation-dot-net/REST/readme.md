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
// 1. Build the input
//
//  Required fields:
//               LicenseKey
//               IsLive
// 
// Optional:
//        FullName
//        Salutation
//        FirstName
//        BusinessName
//        BusinessDomain
//        BusinessEIN
//        Address1
//        Address2
//        Address3
//        Address4
//        Address5
//        Locality
//        AdminArea
//        PostalCode
//        Country
//        Phone1
//        Phone2
//        Email
//        IPAddress
//        Gender
//        DateOfBirth
//        UTCCaptureTime
//        OutputLanguage
//        TestType
//        LicenseKey
//        IsLive
//        TimeoutSeconds

using lead_validation_dot_net.REST;

ValidateLeadV3Client.ValidateLeadV3Input validateLeadInput = new(
    FullName: "Tim Cook",
    Salutation: "",
    FirstName: "",
    LastName: "",
    BusinessName: "Apple",
    BusinessDomain: "",
    BusinessEIN: "",
    Address1: "27 E Cota St",
    Address2: "Suite 500",
    Address3: "",
    Address4: "",
    Address5: "",
    Locality: "Cupertino",
    AdminArea: "CA",
    PostalCode: "",
    Country: "USA",
    Phone1: "1-408-996-1010",
    Phone2: "",
    Email: "tim.cook@apple.com",
    IPAddress: "",
    Gender: "",
    DateOfBirth: "",
    UTCCaptureTime: "",
    OutputLanguage: "English",
    TestType: "business-noip",
    LicenseKey: "YOUR LICENSE KEY",
    IsLive: true,
    TimeoutSeconds: 15
);

// 2. Call the sync Invoke() method.
LVResponse response = ValidateLeadV3Client.Invoke(validateLeadInput);

// 3. Inspect results.
if (response.Error is null)
{
    Console.WriteLine("\r\n* Lead Validation Info *\r\n");
    Console.WriteLine($"OverallCertainty  : {response.OverallCertainty}");
    Console.WriteLine($"OverallQuality    : {response.OverallQuality}");
    Console.WriteLine($"LeadType          : {response.LeadType}");
    Console.WriteLine($"LeadCountry       : {response.LeadCountry}");
    Console.WriteLine($"NoteCodes         : {response.NoteCodes}");
    Console.WriteLine($"NoteDesc          : {response.NoteDesc}");
    Console.WriteLine($"NameCertainty     : {response.NameCertainty}");
    Console.WriteLine($"NameQuality       : {response.NameQuality}");
    Console.WriteLine($"FirstName         : {response.FirstName}");
    Console.WriteLine($"LastName          : {response.LastName}");
    Console.WriteLine($"FirstNameClean    : {response.FirstNameClean}");
    Console.WriteLine($"LastNameClean     : {response.LastNameClean}");
    Console.WriteLine($"NameNoteCodes     : {response.NameNoteCodes}");
    Console.WriteLine($"NameNoteDesc      : {response.NameNoteDesc}");
    Console.WriteLine($"AddressCertainty  : {response.AddressCertainty}");
    Console.WriteLine($"AddressQuality    : {response.AddressQuality}");
    Console.WriteLine($"Address1          : {response.Address1}");
    Console.WriteLine($"Address2          : {response.Address2}");
    Console.WriteLine($"Address3          : {response.Address3}");
    Console.WriteLine($"Address4          : {response.Address4}");
    Console.WriteLine($"Address5          : {response.Address5}");
    Console.WriteLine($"AddressLocality   : {response.AddressLocality}");
    Console.WriteLine($"AddressAdminArea  : {response.AddressAdminArea}");
    Console.WriteLine($"AddressPostalCode : {response.AddressPostalCode}");
    Console.WriteLine($"AddressCountry    : {response.AddressCountry}");
    Console.WriteLine($"AddressNoteCodes  : {response.AddressNoteCodes}");
    Console.WriteLine($"AddressNoteDesc   : {response.AddressNoteDesc}");
    Console.WriteLine($"EmailCertainty    : {response.EmailCertainty}");
    Console.WriteLine($"EmailQuality      : {response.EmailQuality}");
    Console.WriteLine($"EmailCorrected    : {response.EmailCorrected}");
    Console.WriteLine($"EmailNoteCodes    : {response.EmailNoteCodes}");
    Console.WriteLine($"EmailNoteDesc     : {response.EmailNoteDesc}");
    Console.WriteLine($"IPAddressCertainty: {response.IPAddressCertainty}");
    Console.WriteLine($"IPAddressQuality  : {response.IPAddressQuality}");
    Console.WriteLine($"IPCountry         : {response.IPCountry}");
    Console.WriteLine($"IPLocality        : {response.IPLocality}");
    Console.WriteLine($"IPAdminArea       : {response.IPAdminArea}");
    Console.WriteLine($"IPNoteCodes       : {response.IPNoteCodes}");
    Console.WriteLine($"IPNoteDesc        : {response.IPNoteDesc}");
    Console.WriteLine($"Phone1Certainty   : {response.Phone1Certainty}");
    Console.WriteLine($"Phone1Quality     : {response.Phone1Quality}");
    Console.WriteLine($"Phone1Locality    : {response.Phone1Locality}");
    Console.WriteLine($"Phone1AdminArea   : {response.Phone1AdminArea}");
    Console.WriteLine($"Phone1Country     : {response.Phone1Country}");
    Console.WriteLine($"Phone1NoteCodes   : {response.Phone1NoteCodes}");
    Console.WriteLine($"Phone1NoteDesc    : {response.Phone1NoteDesc}");
    Console.WriteLine($"Phone2Certainty   : {response.Phone2Certainty}");
    Console.WriteLine($"Phone2Quality     : {response.Phone2Quality}");
    Console.WriteLine($"Phone2Locality    : {response.Phone2Locality}");
    Console.WriteLine($"Phone2AdminArea   : {response.Phone2AdminArea}");
    Console.WriteLine($"Phone2Country     : {response.Phone2Country}");
    Console.WriteLine($"Phone2NoteCodes   : {response.Phone2NoteCodes}");
    Console.WriteLine($"Phone2NoteDesc    : {response.Phone2NoteDesc}");

    Console.WriteLine("\r\n* Phone Contact *\r\n");
    if (response.PhoneContact != null)
    {
        Console.WriteLine($"Name   : {response.PhoneContact.Name}");
        Console.WriteLine($"Address: {response.PhoneContact.Address}");
        Console.WriteLine($"City   : {response.PhoneContact.City}");
        Console.WriteLine($"State  : {response.PhoneContact.State}");
        Console.WriteLine($"Zip    : {response.PhoneContact.Zip}");
        Console.WriteLine($"Type   : {response.PhoneContact.Type}");
    }
    else
    {
        Console.WriteLine("No phone contact found.");
    }

    Console.WriteLine("\r\n* Information Components *\r\n");
    if (response.InformationComponents?.Length > 0)
    {
        foreach (var component in response.InformationComponents)
        {
            Console.WriteLine($"{component.Name}: {component.Value}");
        }
    }
    else
    {
        Console.WriteLine("No information components found.");
    }
}
else
{
    Console.WriteLine("\r\n* Error *\r\n");
    Console.WriteLine($"Error Type    : {response.Error.Type}");
    Console.WriteLine($"Error TypeCode: {response.Error.TypeCode}");
    Console.WriteLine($"Error Desc    : {response.Error.Desc}");
    Console.WriteLine($"Error DescCode: {response.Error.DescCode}");
}
```
