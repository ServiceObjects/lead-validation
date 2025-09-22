from dataclasses import dataclass
from typing import Optional, List


@dataclass
class InformationComponent:
    """Information Component for API responses."""
    Name: Optional[str] = None
    Value: Optional[str] = None

    def __str__(self) -> str:
        return f"Name={self.Name}, Value={self.Value}"


@dataclass
class PhoneContact:
    """Phone Contact for lead validation responses."""
    Name: Optional[str] = None
    Address: Optional[str] = None
    City: Optional[str] = None
    State: Optional[str] = None
    Zip: Optional[str] = None
    Type: Optional[str] = None

    def __str__(self) -> str:
        return (f"PhoneContact: Name={self.Name}, Address={self.Address}, City={self.City}, "
                f"State={self.State}, Zip={self.Zip}, Type={self.Type}")


@dataclass
class Error:
    """Error object for API responses."""
    Type: Optional[str] = None
    TypeCode: Optional[str] = None
    Desc: Optional[str] = None
    DescCode: Optional[str] = None

    def __str__(self) -> str:
        return (f"Error: Type={self.Type}, TypeCode={self.TypeCode}, "
                f"Desc={self.Desc}, DescCode={self.DescCode}")


@dataclass
class LVResponse:
    """Response from ValidateLead_V3 API, containing lead validation information."""
    OverallCertainty: Optional[str] = None
    OverallQuality: Optional[str] = None
    LeadType: Optional[str] = None
    LeadCountry: Optional[str] = None
    NoteCodes: Optional[str] = None
    NoteDesc: Optional[str] = None
    NameCertainty: Optional[str] = None
    NameQuality: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    FirstNameClean: Optional[str] = None
    LastNameClean: Optional[str] = None
    NameNoteCodes: Optional[str] = None
    NameNoteDesc: Optional[str] = None
    AddressCertainty: Optional[str] = None
    AddressQuality: Optional[str] = None
    Address1: Optional[str] = None
    Address2: Optional[str] = None
    Address3: Optional[str] = None
    Address4: Optional[str] = None
    Address5: Optional[str] = None
    AddressLocality: Optional[str] = None
    AddressAdminArea: Optional[str] = None
    AddressPostalCode: Optional[str] = None
    AddressCountry: Optional[str] = None
    AddressNoteCodes: Optional[str] = None
    AddressNoteDesc: Optional[str] = None
    EmailCertainty: Optional[str] = None
    EmailQuality: Optional[str] = None
    EmailCorrected: Optional[str] = None
    EmailNoteCodes: Optional[str] = None
    EmailNoteDesc: Optional[str] = None
    IPAddressCertainty: Optional[str] = None
    IPAddressQuality: Optional[str] = None
    IPCountry: Optional[str] = None
    IPLocality: Optional[str] = None
    IPAdminArea: Optional[str] = None
    IPNoteCodes: Optional[str] = None
    IPNoteDesc: Optional[str] = None
    Phone1Certainty: Optional[str] = None
    Phone1Quality: Optional[str] = None
    Phone1Locality: Optional[str] = None
    Phone1AdminArea: Optional[str] = None
    Phone1Country: Optional[str] = None
    Phone1NoteCodes: Optional[str] = None
    Phone1NoteDesc: Optional[str] = None
    Phone2Certainty: Optional[str] = None
    Phone2Quality: Optional[str] = None
    Phone2Locality: Optional[str] = None
    Phone2AdminArea: Optional[str] = None
    Phone2Country: Optional[str] = None
    Phone2NoteCodes: Optional[str] = None
    Phone2NoteDesc: Optional[str] = None
    PhoneContact: Optional['PhoneContact'] = None
    InformationComponents: Optional[List['InformationComponent']] = None
    Error: Optional['Error'] = None

    def __post_init__(self):
        if self.InformationComponents is None:
            self.InformationComponents = []

    def __str__(self) -> str:
        info_components_string = ', '.join(str(component) for component in self.InformationComponents) if self.InformationComponents else 'None'
        phone_contact = str(self.PhoneContact) if self.PhoneContact else 'None'
        error = str(self.Error) if self.Error else 'None'
        return (f"LVResponse: OverallCertainty={self.OverallCertainty}, OverallQuality={self.OverallQuality}, "
                f"LeadType={self.LeadType}, LeadCountry={self.LeadCountry}, NoteCodes={self.NoteCodes}, NoteDesc={self.NoteDesc}, "
                f"NameCertainty={self.NameCertainty}, NameQuality={self.NameQuality}, FirstName={self.FirstName}, LastName={self.LastName}, "
                f"FirstNameClean={self.FirstNameClean}, LastNameClean={self.LastNameClean}, NameNoteCodes={self.NameNoteCodes}, NameNoteDesc={self.NameNoteDesc}, "
                f"AddressCertainty={self.AddressCertainty}, AddressQuality={self.AddressQuality}, Address1={self.Address1}, Address2={self.Address2}, "
                f"Address3={self.Address3}, Address4={self.Address4}, Address5={self.Address5}, AddressLocality={self.AddressLocality}, "
                f"AddressAdminArea={self.AddressAdminArea}, AddressPostalCode={self.AddressPostalCode}, AddressCountry={self.AddressCountry}, "
                f"AddressNoteCodes={self.AddressNoteCodes}, AddressNoteDesc={self.AddressNoteDesc}, EmailCertainty={self.EmailCertainty}, "
                f"EmailQuality={self.EmailQuality}, EmailCorrected={self.EmailCorrected}, EmailNoteCodes={self.EmailNoteCodes}, EmailNoteDesc={self.EmailNoteDesc}, "
                f"IPAddressCertainty={self.IPAddressCertainty}, IPAddressQuality={self.IPAddressQuality}, IPCountry={self.IPCountry}, "
                f"IPLocality={self.IPLocality}, IPAdminArea={self.IPAdminArea}, IPNoteCodes={self.IPNoteCodes}, IPNoteDesc={self.IPNoteDesc}, "
                f"Phone1Certainty={self.Phone1Certainty}, Phone1Quality={self.Phone1Quality}, Phone1Locality={self.Phone1Locality}, "
                f"Phone1AdminArea={self.Phone1AdminArea}, Phone1Country={self.Phone1Country}, Phone1NoteCodes={self.Phone1NoteCodes}, Phone1NoteDesc={self.Phone1NoteDesc}, "
                f"Phone2Certainty={self.Phone2Certainty}, Phone2Quality={self.Phone2Quality}, Phone2Locality={self.Phone2Locality}, "
                f"Phone2AdminArea={self.Phone2AdminArea}, Phone2Country={self.Phone2Country}, Phone2NoteCodes={self.Phone2NoteCodes}, Phone2NoteDesc={self.Phone2NoteDesc}, "
                f"PhoneContact={phone_contact}, InformationComponents=[{info_components_string}], Error={error}")
