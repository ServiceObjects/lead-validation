![Service Objects Logo](https://www.serviceobjects.com/wp-content/uploads/2021/05/SO-Logo-with-TM.gif "Service Objects Logo")

# LV - Lead Validation

The DOTS Lead Validation system (LV) evaluates information customers provide and scores the data quality into pass/fail/review categories. By evaluating the information quality of a contact, online marketers can more effectively weed-out fraudulent contacts.Online fraudsters are more likely to provide inaccurate contact information because the address and phone number can be easily traced. Unlike other validation services that perform simple data checks on single variables, Service Objects Lead Validation solution is able to cross-validate that a contact’s name, address, phone numbers, e-mail and IP address are all matched each other and are related to the consumer.

## [Service Objects Website](https://serviceobjects.com)
## [Developer Guide/Documentation](https://www.serviceobjects.com/docs/)

# LV - ValidateLead_V3

Our Lead Validation service cross-validates, corrects and scores over 130 key data points to help your business more accurately identify quality leads for US and Canada. Works with leading CRM and marketing automation platforms.
This document defines the input, output, and behavior of the web services in LV.

## [ValidateLead_V3 Developer Guide/Documentation](https://www.serviceobjects.com/docs/dots-lead-validation/lv-operations/lv-validatelead_v3-recommended-operation/)

## ValidateLead_V3 Request URLs (Query String Parameters)

>[!CAUTION]
>### *Important - Use query string parameters for all inputs.  Do not use path parameters since it will lead to errors due to optional parameters and special character issues.*


### JSON
#### Trial

https://trial.serviceobjects.com/LV/api.svc/json/ValidateLead_V3?FullName=Tim+Cook&Salutation=&FirstName=&LastName=&BusinessName=Apple&BusinessDomain=&BusinessEIN=&Address1=1+Infinite+Loop&Address2=&Address3=&Address4=&Address5=&Locality=Cupertino&AdminArea=CA&PostalCode=&Country=USA&Phone1=1-408-996-1010&Phone2=&Email=tim%40apple.com&IPAddress=&Gender=&DateOfBirth=&UTCCaptureTime=&OutputLanguage=English&TestType=business-noip&LicenseKey={LicenseKey}

#### Production

https://sws.serviceobjects.com/LV/api.svc/json/ValidateLead_V3?FullName=Tim+Cook&Salutation=&FirstName=&LastName=&BusinessName=Apple&BusinessDomain=&BusinessEIN=&Address1=1+Infinite+Loop&Address2=&Address3=&Address4=&Address5=&Locality=Cupertino&AdminArea=CA&PostalCode=&Country=USA&Phone1=1-408-996-1010&Phone2=&Email=tim%40apple.com&IPAddress=&Gender=&DateOfBirth=&UTCCaptureTime=&OutputLanguage=English&TestType=business-noip&LicenseKey={LicenseKey}

#### Production Backup

https://swsbackup.serviceobjects.com/LV/api.svc/json/ValidateLead_V3?FullName=Tim+Cook&Salutation=&FirstName=&LastName=&BusinessName=Apple&BusinessDomain=&BusinessEIN=&Address1=1+Infinite+Loop&Address2=&Address3=&Address4=&Address5=&Locality=Cupertino&AdminArea=CA&PostalCode=&Country=USA&Phone1=1-408-996-1010&Phone2=&Email=tim%40apple.com&IPAddress=&Gender=&DateOfBirth=&UTCCaptureTime=&OutputLanguage=English&TestType=business-noip&LicenseKey={LicenseKey}

### XML
#### Trial

https://trial.serviceobjects.com/LV/api.svc/xml/ValidateLead_V3?FullName=Tim+Cook&Salutation=&FirstName=&LastName=&BusinessName=Apple&BusinessDomain=&BusinessEIN=&Address1=1+Infinite+Loop&Address2=&Address3=&Address4=&Address5=&Locality=Cupertino&AdminArea=CA&PostalCode=&Country=USA&Phone1=1-408-996-1010&Phone2=&Email=tim%40apple.com&IPAddress=&Gender=&DateOfBirth=&UTCCaptureTime=&OutputLanguage=English&TestType=business-noip&LicenseKey={LicenseKey}

#### Production

https://sws.serviceobjects.com/LV/api.svc/xml/ValidateLead_V3?FullName=Tim+Cook&Salutation=&FirstName=&LastName=&BusinessName=Apple&BusinessDomain=&BusinessEIN=&Address1=1+Infinite+Loop&Address2=&Address3=&Address4=&Address5=&Locality=Cupertino&AdminArea=CA&PostalCode=&Country=USA&Phone1=1-408-996-1010&Phone2=&Email=tim%40apple.com&IPAddress=&Gender=&DateOfBirth=&UTCCaptureTime=&OutputLanguage=English&TestType=business-noip&LicenseKey={LicenseKey}

#### Production Backup

https://swsbackup.serviceobjects.com/LV/api.svc/xml/ValidateLead_V3?FullName=Tim+Cook&Salutation=&FirstName=&LastName=&BusinessName=Apple&BusinessDomain=&BusinessEIN=&Address1=1+Infinite+Loop&Address2=&Address3=&Address4=&Address5=&Locality=Cupertino&AdminArea=CA&PostalCode=&Country=USA&Phone1=1-408-996-1010&Phone2=&Email=tim%40apple.com&IPAddress=&Gender=&DateOfBirth=&UTCCaptureTime=&OutputLanguage=English&TestType=business-noip&LicenseKey={LicenseKey}
