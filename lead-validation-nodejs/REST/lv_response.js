/**
 * Information Component for API responses.
 */
export class InformationComponent {
    constructor(data = {}) {
        this.Name = data.Name || null;
        this.Value = data.Value || null;
    }

    toString() {
        return `Name = ${this.Name}, Value = ${this.Value}`;
    }
}

/**
 * Phone Contact for lead validation responses.
 */
export class PhoneContact {
    constructor(data = {}) {
        this.Name = data.Name || null;
        this.Address = data.Address || null;
        this.City = data.City || null;
        this.State = data.State || null;
        this.Zip = data.Zip || null;
        this.Type = data.Type || null;
    }

    toString() {
        return `PhoneContact: Name = ${this.Name}, Address = ${this.Address}, City = ${this.City}, State = ${this.State}, Zip = ${this.Zip}, Type = ${this.Type}`;
    }
}

/**
 * Error object for API responses.
 */
export class Error {
    constructor(data = {}) {
        this.Type = data.Type || null;
        this.TypeCode = data.TypeCode || null;
        this.Desc = data.Desc || null;
        this.DescCode = data.DescCode || null;
    }

    toString() {
        return `Error: Type = ${this.Type}, TypeCode = ${this.TypeCode}, Desc = ${this.Desc}, DescCode = ${this.DescCode}`;
    }
}

/**
 * Response from ValidateLead_V3 API, containing lead validation information.
 */
export class LVResponse {
    constructor(data = {}) {
        this.OverallCertainty = data.OverallCertainty || null;
        this.OverallQuality = data.OverallQuality || null;
        this.LeadType = data.LeadType || null;
        this.LeadCountry = data.LeadCountry || null;
        this.NoteCodes = data.NoteCodes || null;
        this.NoteDesc = data.NoteDesc || null;
        this.NameCertainty = data.NameCertainty || null;
        this.NameQuality = data.NameQuality || null;
        this.FirstName = data.FirstName || null;
        this.LastName = data.LastName || null;
        this.FirstNameClean = data.FirstNameClean || null;
        this.LastNameClean = data.LastNameClean || null;
        this.NameNoteCodes = data.NameNoteCodes || null;
        this.NameNoteDesc = data.NameNoteDesc || null;
        this.AddressCertainty = data.AddressCertainty || null;
        this.AddressQuality = data.AddressQuality || null;
        this.Address1 = data.Address1 || null;
        this.Address2 = data.Address2 || null;
        this.Address3 = data.Address3 || null;
        this.Address4 = data.Address4 || null;
        this.Address5 = data.Address5 || null;
        this.AddressLocality = data.AddressLocality || null;
        this.AddressAdminArea = data.AddressAdminArea || null;
        this.AddressPostalCode = data.AddressPostalCode || null;
        this.AddressCountry = data.AddressCountry || null;
        this.AddressNoteCodes = data.AddressNoteCodes || null;
        this.AddressNoteDesc = data.AddressNoteDesc || null;
        this.EmailCertainty = data.EmailCertainty || null;
        this.EmailQuality = data.EmailQuality || null;
        this.EmailCorrected = data.EmailCorrected || null;
        this.EmailNoteCodes = data.EmailNoteCodes || null;
        this.EmailNoteDesc = data.EmailNoteDesc || null;
        this.IPAddressCertainty = data.IPAddressCertainty || null;
        this.IPAddressQuality = data.IPAddressQuality || null;
        this.IPCountry = data.IPCountry || null;
        this.IPLocality = data.IPLocality || null;
        this.IPAdminArea = data.IPAdminArea || null;
        this.IPNoteCodes = data.IPNoteCodes || null;
        this.IPNoteDesc = data.IPNoteDesc || null;
        this.Phone1Certainty = data.Phone1Certainty || null;
        this.Phone1Quality = data.Phone1Quality || null;
        this.Phone1Locality = data.Phone1Locality || null;
        this.Phone1AdminArea = data.Phone1AdminArea || null;
        this.Phone1Country = data.Phone1Country || null;
        this.Phone1NoteCodes = data.Phone1NoteCodes || null;
        this.Phone1NoteDesc = data.Phone1NoteDesc || null;
        this.Phone2Certainty = data.Phone2Certainty || null;
        this.Phone2Quality = data.Phone2Quality || null;
        this.Phone2Locality = data.Phone2Locality || null;
        this.Phone2AdminArea = data.Phone2AdminArea || null;
        this.Phone2Country = data.Phone2Country || null;
        this.Phone2NoteCodes = data.Phone2NoteCodes || null;
        this.Phone2NoteDesc = data.Phone2NoteDesc || null;
        this.PhoneContact = data.PhoneContact ? new PhoneContact(data.PhoneContact) : null;
        this.InformationComponents = (data.InformationComponents || []).map(component => new InformationComponent(component));
        this.Error = data.Error ? new Error(data.Error) : null;
    }

    toString() {
        const infoComponentsString = this.InformationComponents.length
            ? this.InformationComponents.map(component => component.toString()).join(', ')
            : 'null';
        return `LVResponse: OverallCertainty = ${this.OverallCertainty}, OverallQuality = ${this.OverallQuality}, ` +
            `LeadType = ${this.LeadType}, LeadCountry = ${this.LeadCountry}, NoteCodes = ${this.NoteCodes}, NoteDesc = ${this.NoteDesc}, ` +
            `NameCertainty = ${this.NameCertainty}, NameQuality = ${this.NameQuality}, FirstName = ${this.FirstName}, LastName = ${this.LastName}, ` +
            `FirstNameClean = ${this.FirstNameClean}, LastNameClean = ${this.LastNameClean}, NameNoteCodes = ${this.NameNoteCodes}, NameNoteDesc = ${this.NameNoteDesc}, ` +
            `AddressCertainty = ${this.AddressCertainty}, AddressQuality = ${this.AddressQuality}, Address1 = ${this.Address1}, Address2 = ${this.Address2}, ` +
            `Address3 = ${this.Address3}, Address4 = ${this.Address4}, Address5 = ${this.Address5}, AddressLocality = ${this.AddressLocality}, ` +
            `AddressAdminArea = ${this.AddressAdminArea}, AddressPostalCode = ${this.AddressPostalCode}, AddressCountry = ${this.AddressCountry}, ` +
            `AddressNoteCodes = ${this.AddressNoteCodes}, AddressNoteDesc = ${this.AddressNoteDesc}, EmailCertainty = ${this.EmailCertainty}, ` +
            `EmailQuality = ${this.EmailQuality}, EmailCorrected = ${this.EmailCorrected}, EmailNoteCodes = ${this.EmailNoteCodes}, EmailNoteDesc = ${this.EmailNoteDesc}, ` +
            `IPAddressCertainty = ${this.IPAddressCertainty}, IPAddressQuality = ${this.IPAddressQuality}, IPCountry = ${this.IPCountry}, ` +
            `IPLocality = ${this.IPLocality}, IPAdminArea = ${this.IPAdminArea}, IPNoteCodes = ${this.IPNoteCodes}, IPNoteDesc = ${this.IPNoteDesc}, ` +
            `Phone1Certainty = ${this.Phone1Certainty}, Phone1Quality = ${this.Phone1Quality}, Phone1Locality = ${this.Phone1Locality}, ` +
            `Phone1AdminArea = ${this.Phone1AdminArea}, Phone1Country = ${this.Phone1Country}, Phone1NoteCodes = ${this.Phone1NoteCodes}, Phone1NoteDesc = ${this.Phone1NoteDesc}, ` +
            `Phone2Certainty = ${this.Phone2Certainty}, Phone2Quality = ${this.Phone2Quality}, Phone2Locality = ${this.Phone2Locality}, ` +
            `Phone2AdminArea = ${this.Phone2AdminArea}, Phone2Country = ${this.Phone2Country}, Phone2NoteCodes = ${this.Phone2NoteCodes}, Phone2NoteDesc = ${this.Phone2NoteDesc}, ` +
            `PhoneContact = ${this.PhoneContact ? this.PhoneContact.toString() : 'null'}, InformationComponents = [${infoComponentsString}], ` +
            `Error = ${this.Error ? this.Error.toString() : 'null'}`;
    }
}

export default LVResponse;