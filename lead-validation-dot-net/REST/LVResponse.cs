
    public class LVResponse
{
        public string OverallCertainty { get; set; }
        public string OverallQuality { get; set; }
        public string LeadType { get; set; }
        public string LeadCountry { get; set; }
        public string NoteCodes { get; set; }
        public string NoteDesc { get; set; }
        public string NameCertainty { get; set; }
        public string NameQuality { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string FirstNameClean { get; set; }
        public string LastNameClean { get; set; }
        public string NameNoteCodes { get; set; }
        public string NameNoteDesc { get; set; }
        public string AddressCertainty { get; set; }
        public string AddressQuality { get; set; }
        public string Address1 { get; set; }
        public string Address2 { get; set; }
        public string Address3 { get; set; }
        public string Address4 { get; set; }
        public string Address5 { get; set; }
        public string AddressLocality { get; set; }
        public string AddressAdminArea { get; set; }
        public string AddressPostalCode { get; set; }
        public string AddressCountry { get; set; }
        public string AddressNoteCodes { get; set; }
        public string AddressNoteDesc { get; set; }
        public string EmailCertainty { get; set; }
        public string EmailQuality { get; set; }
        public string EmailCorrected { get; set; }
        public string EmailNoteCodes { get; set; }
        public string EmailNoteDesc { get; set; }
        public string IPAddressCertainty { get; set; }
        public string IPAddressQuality { get; set; }
        public string IPCountry { get; set; }
        public string IPLocality { get; set; }
        public string IPAdminArea { get; set; }
        public string IPNoteCodes { get; set; }
        public string IPNoteDesc { get; set; }
        public string Phone1Certainty { get; set; }
        public string Phone1Quality { get; set; }
        public string Phone1Locality { get; set; }
        public string Phone1AdminArea { get; set; }
        public string Phone1Country { get; set; }
        public string Phone1NoteCodes { get; set; }
        public string Phone1NoteDesc { get; set; }
        public string Phone2Certainty { get; set; }
        public string Phone2Quality { get; set; }
        public string Phone2Locality { get; set; }
        public string Phone2AdminArea { get; set; }
        public string Phone2Country { get; set; }
        public string Phone2NoteCodes { get; set; }
        public string Phone2NoteDesc { get; set; }
        public PhoneContact PhoneContact { get; set; }
        public InformationComponent[] InformationComponents { get; set; }
        public Error Error { get; set; }
        public override string ToString()
        {
            string Output = $"\n{{OverallCertainty: {OverallCertainty} " +
                $"\nOverallQuality: {OverallQuality} " +
                $"\nLeadType: {LeadType} " +
                $"\nLeadCountry: {LeadCountry} " +
                $"\nNoteCodes:  {NoteCodes} " +
                $"\nNoteDesc: {NoteDesc} " +
                $"\nNameCertainty:  {NameCertainty} " +
                $"\nNameQuality:   {NameQuality} " +
                $"\nFirstName: {FirstName} " +
                $"\nLastName: {LastName} " +
                $"\nFirstNameClean: {FirstNameClean} " +
                $"\nLastNameClean: {LastNameClean} " +
                $"\nNameNoteCodes: {NameNoteCodes} " +
                $"\nNameNoteDesc: {NameNoteDesc} " +
                $"\nAddressCertainty: {AddressCertainty} " +
                $"\nAddressQuality: {AddressQuality} " +
                $"\nAddress1: {Address1} " +
                $"\nAddressLine2: {Address2} " +
                $"\nAddressLine3: {Address3} " +
                $"\nAddressLine4: {Address4} " +
                $"\nAddressLine5: {Address5} " +
                $"\nAddressLocality: {AddressLocality} " +
                $"\nAddressAdminArea: {AddressAdminArea} " +
                $"\nAddressPostalCode: {AddressPostalCode} " +
                $"\nAddressCountry: {AddressCountry} " +
                $"\nAddressNoteCodes: {AddressNoteCodes} " +
                $"\nAddressNoteDesc: {AddressNoteDesc} " +
                $"\nEmailCertainty: {EmailCertainty} " +
                $"\nEmailQuality: {EmailQuality} " +
                $"\nEmailCorrected: {EmailCorrected} " +
                $"\nEmailNoteCodes: {EmailNoteCodes} " +
                $"\nEmailNoteDesc: {EmailNoteDesc} " +
                $"\nIPAddressCertainty: {IPAddressCertainty} " +
                $"\nIPAddressQuality: {IPAddressQuality} " +
                $"\nIPCountry: {IPCountry} " +
                $"\nIPLocality: {IPLocality} " +
                $"\nIPAdminArea: {IPAdminArea} " +
                $"\nIPCountry: {IPCountry} " +
                $"\nIPNoteCodes: {IPNoteCodes} " +
                $"\nIPNoteDesc: {IPNoteDesc} " +
                $"\nPhone1Certainty: {Phone1Certainty} " +
                $"\nPhone1Quality: {Phone1Quality} " +
                $"\nPhone1Locality: {Phone1Locality} " +
                $"\nPhone1AdminArea: {Phone1AdminArea} " +
                $"\nPhone1Country: {Phone1Country} " +
                $"\nPhone1NoteCodes: {Phone1NoteCodes} " +
                $"\nPhone1NoteDesc: {Phone1NoteDesc} " +
                $"\nPhone2Certainty: {Phone2Certainty} " +
                $"\nPhone2Quality: {Phone2Quality} " +
                $"\nPhone2Locality: {Phone2Locality} " +
                $"\nPhone2AdminArea: {Phone2AdminArea} " +
                $"\nPhone2Country: {Phone2Country} " +
                $"\nPhone2NoteCodes: {Phone2NoteCodes} " +
                $"\nPhone2NoteDesc: {Phone2NoteDesc} " +
                $"\nPhoneContact: {{{PhoneContact}}} " +
                $"\nInformationComponents: [";
            if (InformationComponents != null && InformationComponents.Length > 0)
            {
                foreach (InformationComponent A in InformationComponents)
                {
                    Output += "{" + A.ToString() + "}\n";
                }
            }
            Output += "]" +
            $"\nError: {{{Error}}}\n";
            return Output;
        }
    }

    public class Error
    {
        public string Type { get; set; }
        public string TypeCode { get; set; }
        public string Desc { get; set; }
        public string DescCode { get; set; }
        public override string ToString()
        {
            return $"{{Type: {Type} " +
                $"\nTypeCode: {TypeCode} " +
                $"\nDesc: {Desc} " +
                $"\nDescCode: {DescCode}}}";
        }
    }

    public class PhoneContacts
    {
        public PhoneContact[] PhoneContact { get; set; }
        public override string ToString()
        {
            string Output = "PhoneContacts: [";
            if (PhoneContact != null && PhoneContact.Length > 0)
            {
                foreach (PhoneContact A in PhoneContact)
                {
                    Output += "{" + A.ToString() + "}\n";
                }
            }
            return Output += "]\n";
        }
    }

    public class PhoneContact
    {
        public string Name { get; set; }
        public string Address { get; set; }
        public string City { get; set; }
        public string State { get; set; }
        public string Zip { get; set; }
        public string Type { get; set; }
        public override string ToString()
        {
            return $"Name: {Name} " +
                $"\nAddress: {Address} " +
                $"\nCity: {City} " +
                $"\nState: {State} " +
                $"\nZip: {Zip} " +
                $"\nType: {Type}\n";
        }
    }

    public class InformationComponent
    {
        public string Name { get; set; }
        public string Value { get; set; }
        public override string ToString()
        {
            return $"Name: {Name} " +
                $"\nValue: {Value}\n";
        }
    }
