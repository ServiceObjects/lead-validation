import { ValidateLeadV3Client } from '../lead-validation-nodejs/REST/validate_lead_v3_rest.js';

async function ValidateLeadV3ClientGo(licenseKey, isLive) {
    console.log("\n-------------------------------------------");
    console.log("LeadValidation - ValidateLead_V3 - REST SDK");
    console.log("-------------------------------------------");

    const fullName = "Tim Cook";
    const salutation = "";
    const firstName = "";
    const lastName = "";
    const businessName = "Apple";
    const businessDomain = "";
    const businessEIN = "";
    const address1 = "27 E Cota St";
    const address2 = "Suite 500";
    const address3 = "";
    const address4 = "";
    const address5 = "";
    const locality = "Cupertino";
    const adminArea = "CA";
    const postalCode = "93101";
    const country = "US";
    const phone1 = "1-408-996-1010";
    const phone2 = "";
    const email = "tim.cook@apple.com";
    const ipAddress = "192.168.1.1";
    const gender = "";
    const dateOfBirth = "1";
    const utcCaptureTime = "";
    const outputLanguage = "English";
    const testType = "business-noip";
    const timeoutSeconds = 15;

    console.log("\n* Input *\n");
    console.log(`FullName       : ${fullName}`);
    console.log(`Salutation     : ${salutation}`);
    console.log(`FirstName      : ${firstName}`);
    console.log(`LastName       : ${lastName}`);
    console.log(`BusinessName   : ${businessName}`);
    console.log(`BusinessDomain : ${businessDomain}`);
    console.log(`BusinessEIN    : ${businessEIN}`);
    console.log(`Address1       : ${address1}`);
    console.log(`Address2       : ${address2}`);
    console.log(`Address3       : ${address3}`);
    console.log(`Address4       : ${address4}`);
    console.log(`Address5       : ${address5}`);
    console.log(`Locality       : ${locality}`);
    console.log(`AdminArea      : ${adminArea}`);
    console.log(`PostalCode     : ${postalCode}`);
    console.log(`Country        : ${country}`);
    console.log(`Phone1         : ${phone1}`);
    console.log(`Phone2         : ${phone2}`);
    console.log(`Email          : ${email}`);
    console.log(`IPAddress      : ${ipAddress}`);
    console.log(`Gender         : ${gender}`);
    console.log(`DateOfBirth    : ${dateOfBirth}`);
    console.log(`UTCCaptureTime : ${utcCaptureTime}`);
    console.log(`OutputLanguage : ${outputLanguage}`);
    console.log(`TestType       : ${testType}`);
    console.log(`LicenseKey     : ${licenseKey}`);
    console.log(`IsLive         : ${isLive}`);
    console.log(`Timeout Seconds: ${timeoutSeconds}`);

    try {
        const response = await ValidateLeadV3Client.invoke(
            fullName, salutation, firstName, lastName, businessName, businessDomain, businessEIN,
            address1, address2, address3, address4, address5, locality, adminArea, postalCode, country,
            phone1, phone2, email, ipAddress, gender, dateOfBirth, utcCaptureTime, outputLanguage, testType, licenseKey,
            isLive, timeoutSeconds
        );

        if (response.Error) {
            console.log("\n* Error *\n");
            console.log(`Error Type    : ${response.Error.Type}`);
            console.log(`Error TypeCode: ${response.Error.TypeCode}`);
            console.log(`Error Desc    : ${response.Error.Desc}`);
            console.log(`Error DescCode: ${response.Error.DescCode}`);
            return;
        }

        console.log("\n* Lead Validation Info *\n");
        if (response) {
            console.log(`OverallCertainty  : ${response.OverallCertainty}`);
            console.log(`OverallQuality    : ${response.OverallQuality}`);
            console.log(`LeadType          : ${response.LeadType}`);
            console.log(`LeadCountry       : ${response.LeadCountry}`);
            console.log(`NoteCodes         : ${response.NoteCodes}`);
            console.log(`NoteDesc          : ${response.NoteDesc}`);
            console.log(`NameCertainty     : ${response.NameCertainty}`);
            console.log(`NameQuality       : ${response.NameQuality}`);
            console.log(`FirstName         : ${response.FirstName}`);
            console.log(`LastName          : ${response.LastName}`);
            console.log(`FirstNameClean    : ${response.FirstNameClean}`);
            console.log(`LastNameClean     : ${response.LastNameClean}`);
            console.log(`NameNoteCodes     : ${response.NameNoteCodes}`);
            console.log(`NameNoteDesc      : ${response.NameNoteDesc}`);
            console.log(`AddressCertainty  : ${response.AddressCertainty}`);
            console.log(`AddressQuality    : ${response.AddressQuality}`);
            console.log(`Address1          : ${response.Address1}`);
            console.log(`Address2          : ${response.Address2}`);
            console.log(`Address3          : ${response.Address3}`);
            console.log(`Address4          : ${response.Address4}`);
            console.log(`Address5          : ${response.Address5}`);
            console.log(`AddressLocality   : ${response.AddressLocality}`);
            console.log(`AddressAdminArea  : ${response.AddressAdminArea}`);
            console.log(`AddressPostalCode : ${response.AddressPostalCode}`);
            console.log(`AddressCountry    : ${response.AddressCountry}`);
            console.log(`AddressNoteCodes  : ${response.AddressNoteCodes}`);
            console.log(`AddressNoteDesc   : ${response.AddressNoteDesc}`);
            console.log(`EmailCertainty    : ${response.EmailCertainty}`);
            console.log(`EmailQuality      : ${response.EmailQuality}`);
            console.log(`EmailCorrected    : ${response.EmailCorrected}`);
            console.log(`EmailNoteCodes    : ${response.EmailNoteCodes}`);
            console.log(`EmailNoteDesc     : ${response.EmailNoteDesc}`);
            console.log(`IPAddressCertainty: ${response.IPAddressCertainty}`);
            console.log(`IPAddressQuality  : ${response.IPAddressQuality}`);
            console.log(`IPCountry         : ${response.IPCountry}`);
            console.log(`IPLocality        : ${response.IPLocality}`);
            console.log(`IPAdminArea       : ${response.IPAdminArea}`);
            console.log(`IPNoteCodes       : ${response.IPNoteCodes}`);
            console.log(`IPNoteDesc        : ${response.IPNoteDesc}`);
            console.log(`Phone1Certainty   : ${response.Phone1Certainty}`);
            console.log(`Phone1Quality     : ${response.Phone1Quality}`);
            console.log(`Phone1Locality    : ${response.Phone1Locality}`);
            console.log(`Phone1AdminArea   : ${response.Phone1AdminArea}`);
            console.log(`Phone1Country     : ${response.Phone1Country}`);
            console.log(`Phone1NoteCodes   : ${response.Phone1NoteCodes}`);
            console.log(`Phone1NoteDesc    : ${response.Phone1NoteDesc}`);
            console.log(`Phone2Certainty   : ${response.Phone2Certainty}`);
            console.log(`Phone2Quality     : ${response.Phone2Quality}`);
            console.log(`Phone2Locality    : ${response.Phone2Locality}`);
            console.log(`Phone2AdminArea   : ${response.Phone2AdminArea}`);
            console.log(`Phone2Country     : ${response.Phone2Country}`);
            console.log(`Phone2NoteCodes   : ${response.Phone2NoteCodes}`);
            console.log(`Phone2NoteDesc    : ${response.Phone2NoteDesc}`);

            console.log("\n* Phone Contact *\n");
            if (response.PhoneContact) {
                console.log(`Name   : ${response.PhoneContact.Name}`);
                console.log(`Address: ${response.PhoneContact.Address}`);
                console.log(`City   : ${response.PhoneContact.City}`);
                console.log(`State  : ${response.PhoneContact.State}`);
                console.log(`Zip    : ${response.PhoneContact.Zip}`);
                console.log(`Type   : ${response.PhoneContact.Type}`);
            } else {
                console.log("No phone contact found.");
            }

            console.log("\n* Information Components *\n");
            if (response.InformationComponents && response.InformationComponents.length > 0) {
                response.InformationComponents.forEach((component) => {
                    console.log(`${component.Name}: ${component.Value}`);
                });
            } else {
                console.log("No information components found.");
            }
        } else {
            console.log("No lead validation info found.");
        }
    } catch (e) {
        console.log("\n* Error *\n");
        console.log(`Error Message: ${e.message}`);
    }
}

export { ValidateLeadV3ClientGo };