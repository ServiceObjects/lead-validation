using System;
using LVReference;
using lead_validation_dot_net.SOAP;

namespace lead_validation_dot_net_examples
{
    public static class ValidateLeadV3SoapSdkExample
    {
        public static void Go(string licenseKey, bool isLive)
        {
            Console.WriteLine("\r\n-------------------------------------------");
            Console.WriteLine("LeadValidation - ValidateLead_V3 - SOAP SDK");
            Console.WriteLine("-------------------------------------------");

            string FullName = "Tim Cook";
            string Salutation = "";
            string FirstName = "";
            string LastName = "";
            string BusinessName = "Apple";
            string BusinessDomain = "";
            string BusinessEIN = "";
            string Address1 = "27 E Cota St";
            string Address2 = "Suite 500";
            string Address3 = "";
            string Address4 = "";
            string Address5 = "";
            string Locality = "Cupertino";
            string AdminArea = "CA";
            string PostalCode = "93101";
            string Country = "USA";
            string Phone1 = "1-408-996-1010";
            string Phone2 = "";
            string Email = "tim.cook@apple.com";
            string IPAddress = "";
            string Gender = "";
            string DateOfBirth = "";
            string UTCCaptureTime = "";
            string OutputLanguage = "English";
            string TestType = "business-noip";

            Console.WriteLine("\r\n* Input *\r\n");
            Console.WriteLine($"FullName      : {FullName}");
            Console.WriteLine($"Salutation    : {Salutation}");
            Console.WriteLine($"FirstName     : {FirstName}");
            Console.WriteLine($"LastName      : {LastName}");
            Console.WriteLine($"BusinessName  : {BusinessName}");
            Console.WriteLine($"BusinessDomain: {BusinessDomain}");
            Console.WriteLine($"BusinessEIN   : {BusinessEIN}");
            Console.WriteLine($"Address1      : {Address1}");
            Console.WriteLine($"Address2      : {Address2}");
            Console.WriteLine($"Address3      : {Address3}");
            Console.WriteLine($"Address4      : {Address4}");
            Console.WriteLine($"Address5      : {Address5}");
            Console.WriteLine($"Locality      : {Locality}");
            Console.WriteLine($"AdminArea     : {AdminArea}");
            Console.WriteLine($"PostalCode    : {PostalCode}");
            Console.WriteLine($"Country       : {Country}");
            Console.WriteLine($"Phone1        : {Phone1}");
            Console.WriteLine($"Phone2        : {Phone2}");
            Console.WriteLine($"Email         : {Email}");
            Console.WriteLine($"IPAddress     : {IPAddress}");
            Console.WriteLine($"Gender        : {Gender}");
            Console.WriteLine($"DateOfBirth   : {DateOfBirth}");
            Console.WriteLine($"UTCCaptureTime: {UTCCaptureTime}");
            Console.WriteLine($"OutputLanguage: {OutputLanguage}");
            Console.WriteLine($"TestType      : {TestType}");
            Console.WriteLine($"LicenseKey    : {licenseKey}");
            Console.WriteLine($"IsLive        : {isLive}");

            var lv = new ValidateLeadV3Validation(isLive);
            ContactInternational response = lv.ValidateLead_V3Async(
                FullName, Salutation, FirstName, LastName, BusinessName, BusinessDomain, BusinessEIN,
                Address1, Address2, Address3, Address4, Address5, Locality, AdminArea, PostalCode, Country,
                Phone1, Phone2, Email, IPAddress, Gender, DateOfBirth, UTCCaptureTime, OutputLanguage, TestType, licenseKey
            ).Result;

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
                Console.WriteLine($"FirstNameClean    : {response.FirstNameLatin}");
                Console.WriteLine($"LastNameClean     : {response.LastNameLatin}");
                Console.WriteLine($"NameNoteCodes     : {response.NameNoteCodes}");
                Console.WriteLine($"NameNoteDesc      : {response.NameNoteDesc}");
                Console.WriteLine($"AddressCertainty  : {response.AddressCertainty}");
                Console.WriteLine($"AddressQuality    : {response.AddressQuality}");
                Console.WriteLine($"Address1          : {response.AddressLine1}");
                Console.WriteLine($"Address2          : {response.AddressLine2}");
                Console.WriteLine($"Address3          : {response.AddressLine3}");
                Console.WriteLine($"Address4          : {response.AddressLine4}");
                Console.WriteLine($"Address5          : {response.AddressLine5}");
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
                Console.WriteLine($"IPAddressCertainty: {response.IPCertainty}");
                Console.WriteLine($"IPAddressQuality  : {response.IPQuality}");
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
        }
    }
}