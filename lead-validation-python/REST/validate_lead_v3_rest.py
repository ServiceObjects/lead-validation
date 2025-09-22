from lv_response import LVResponse, PhoneContact, InformationComponent, Error
import requests

# Endpoint URLs for ServiceObjects Lead Validation (LV) API
primary_url = "https://sws.serviceobjects.com/lv/api.svc/json/ValidateLead_V3?"
backup_url = "https://swsbackup.serviceobjects.com/lv/api.svc/json/ValidateLead_V3?"
trial_url = "https://trial.serviceobjects.com/lv/api.svc/json/ValidateLead_V3?"

def validate_lead_v3(full_name: str,
                    salutation: str,
                    first_name: str,
                    last_name: str,
                    business_name: str,
                    business_domain: str,
                    business_ein: str,
                    address1: str,
                    address2: str,
                    address3: str,
                    address4: str,
                    address5: str,
                    locality: str,
                    admin_area: str,
                    postal_code: str,
                    country: str,
                    phone1: str,
                    phone2: str,
                    email: str,
                    ip_address: str,
                    gender: str,
                    date_of_birth: str,
                    utc_capture_time: str,
                    output_language: str,
                    test_type: str,
                    license_key: str,
                    is_live: bool) -> LVResponse:
    """
    Call ServiceObjects Lead Validation (LV) API's ValidateLead_V3 endpoint
    to retrieve lead validation information for a given US or Canada lead.

    Parameters:
        full_name: The contacts full name. Optional.
        salutation: Salutation of the contact. Optional.
        first_name: First name of the contact . Optional.
        last_name: Last name of the contact . Optional.
        business_name: The contacts company . Optional.
        business_domain: Website domain associated with the business. Optional.
        business_ein: Company Tax Number for US leads. Optional.
        address1: Address line 1 of the contact or business address. Optional.
        address2: Address line 2 of the contact or business address. Optional.
        address3: Address line 3 of the contact or business address. Optional.
        address4: Address line 4 of the contact or business address. Optional.
        address5: Address line 5 of the contact or business address. Optional.
        locality: The city of the contacts postal address. Optional.
        admin_area: The state or province of the contacts postal address. Optional.
        postal_code: The zip or postal code of the contacts postal address. Optional.
        country: The country of the contacts postal address . Optional.
        phone1: The contacts primary phone number. Optional.
        phone2: The contacts secondary phone number. Optional.
        email: The contacts email address. Optional.
        ip_address: The contacts IP address in IPv4. Optional.
        gender: The contacts gender. Optional.
        date_of_birth: The contacts date of birth. Optional.
        utc_capture_time: The time the lead was submitted. Optional.
        output_language: Language for some output information. Optional.
        test_type: The type of validation to perform. Required.
        license_key: Your ServiceObjects license key.
        is_live: Use live or trial servers.

    Returns:
        LVResponse: Parsed JSON response with lead validation results or error details.

    Raises:
        RuntimeError: If the API returns an error payload.
        requests.RequestException: On network/HTTP failures (trial mode).
    """
    params = {
        "FullName": full_name,
        "Salutation": salutation,
        "FirstName": first_name,
        "LastName": last_name,
        "BusinessName": business_name,
        "BusinessDomain": business_domain,
        "BusinessEIN": business_ein,
        "Address1": address1,
        "Address2": address2,
        "Address3": address3,
        "Address4": address4,
        "Address5": address5,
        "Locality": locality,
        "AdminArea": admin_area,
        "PostalCode": postal_code,
        "Country": country,
        "Phone1": phone1,
        "Phone2": phone2,
        "Email": email,
        "IPAddress": ip_address,
        "Gender": gender,
        "DateOfBirth": date_of_birth,
        "UTCCaptureTime": utc_capture_time,
        "OutputLanguage": output_language,
        "TestType": test_type,
        "LicenseKey": license_key,
    }
    # Select the base URL: production vs trial
    url = primary_url if is_live else trial_url

    try:
        # Attempt primary (or trial) endpoint
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        # If API returned an error in JSON payload, trigger fallback
        error = data.get('Error')
        if not (error is None or error.get('TypeCode') != "3"):
            if is_live:
                # Try backup URL
                response = requests.get(backup_url, params=params, timeout=10)
                data = response.json()

                # If still error, propagate exception
                if 'Error' in data:
                    raise RuntimeError(f"LV service error: {data['Error']}")
            else:
                # Trial mode error is terminal
                raise RuntimeError(f"LV trial error: {data['Error']}")

        # Convert JSON response to LVResponse for structured access
        error = Error(**data.get("Error", {})) if data.get("Error") else None
        phone_contact = PhoneContact(**data.get("PhoneContact", {})) if data.get("PhoneContact") else None

        return LVResponse(
            OverallCertainty=data.get("OverallCertainty"),
            OverallQuality=data.get("OverallQuality"),
            LeadType=data.get("LeadType"),
            LeadCountry=data.get("LeadCountry"),
            NoteCodes=data.get("NoteCodes"),
            NoteDesc=data.get("NoteDesc"),
            NameCertainty=data.get("NameCertainty"),
            NameQuality=data.get("NameQuality"),
            FirstName=data.get("FirstName"),
            LastName=data.get("LastName"),
            FirstNameClean=data.get("FirstNameClean"),
            LastNameClean=data.get("LastNameClean"),
            NameNoteCodes=data.get("NameNoteCodes"),
            NameNoteDesc=data.get("NameNoteDesc"),
            AddressCertainty=data.get("AddressCertainty"),
            AddressQuality=data.get("AddressQuality"),
            Address1=data.get("Address1"),
            Address2=data.get("Address2"),
            Address3=data.get("Address3"),
            Address4=data.get("Address4"),
            Address5=data.get("Address5"),
            AddressLocality=data.get("AddressLocality"),
            AddressAdminArea=data.get("AddressAdminArea"),
            AddressPostalCode=data.get("AddressPostalCode"),
            AddressCountry=data.get("AddressCountry"),
            AddressNoteCodes=data.get("AddressNoteCodes"),
            AddressNoteDesc=data.get("AddressNoteDesc"),
            EmailCertainty=data.get("EmailCertainty"),
            EmailQuality=data.get("EmailQuality"),
            EmailCorrected=data.get("EmailCorrected"),
            EmailNoteCodes=data.get("EmailNoteCodes"),
            EmailNoteDesc=data.get("EmailNoteDesc"),
            IPAddressCertainty=data.get("IPAddressCertainty"),
            IPAddressQuality=data.get("IPAddressQuality"),
            IPCountry=data.get("IPCountry"),
            IPLocality=data.get("IPLocality"),
            IPAdminArea=data.get("IPAdminArea"),
            IPNoteCodes=data.get("IPNoteCodes"),
            IPNoteDesc=data.get("IPNoteDesc"),
            Phone1Certainty=data.get("Phone1Certainty"),
            Phone1Quality=data.get("Phone1Quality"),
            Phone1Locality=data.get("Phone1Locality"),
            Phone1AdminArea=data.get("Phone1AdminArea"),
            Phone1Country=data.get("Phone1Country"),
            Phone1NoteCodes=data.get("Phone1NoteCodes"),
            Phone1NoteDesc=data.get("Phone1NoteDesc"),
            Phone2Certainty=data.get("Phone2Certainty"),
            Phone2Quality=data.get("Phone2Quality"),
            Phone2Locality=data.get("Phone2Locality"),
            Phone2AdminArea=data.get("Phone2AdminArea"),
            Phone2Country=data.get("Phone2Country"),
            Phone2NoteCodes=data.get("Phone2NoteCodes"),
            Phone2NoteDesc=data.get("Phone2NoteDesc"),
            PhoneContact=phone_contact,
            InformationComponents=[
                InformationComponent(Name=comp.get("Name"), Value=comp.get("Value"))
                for comp in data.get("InformationComponents", [])
            ] if "InformationComponents" in data else [],
            Error=error
        )

    except requests.RequestException as req_exc:
        # Network or HTTP-level error occurred
        if is_live:
            try:
                # Fallback to backup URL
                response = requests.get(backup_url, params=params, timeout=10)
                response.raise_for_status()
                data = response.json()
                if "Error" in data:
                    raise RuntimeError(f"LeadValidation backup error: {data['Error']}") from req_exc

                error = Error(**data.get("Error", {})) if data.get("Error") else None
                phone_contact = PhoneContact(**data.get("PhoneContact", {})) if data.get("PhoneContact") else None

                return LVResponse(
                    OverallCertainty=data.get("OverallCertainty"),
                    OverallQuality=data.get("OverallQuality"),
                    LeadType=data.get("LeadType"),
                    LeadCountry=data.get("LeadCountry"),
                    NoteCodes=data.get("NoteCodes"),
                    NoteDesc=data.get("NoteDesc"),
                    NameCertainty=data.get("NameCertainty"),
                    NameQuality=data.get("NameQuality"),
                    FirstName=data.get("FirstName"),
                    LastName=data.get("LastName"),
                    FirstNameClean=data.get("FirstNameClean"),
                    LastNameClean=data.get("LastNameClean"),
                    NameNoteCodes=data.get("NameNoteCodes"),
                    NameNoteDesc=data.get("NameNoteDesc"),
                    AddressCertainty=data.get("AddressCertainty"),
                    AddressQuality=data.get("AddressQuality"),
                    Address1=data.get("Address1"),
                    Address2=data.get("Address2"),
                    Address3=data.get("Address3"),
                    Address4=data.get("Address4"),
                    Address5=data.get("Address5"),
                    AddressLocality=data.get("AddressLocality"),
                    AddressAdminArea=data.get("AddressAdminArea"),
                    AddressPostalCode=data.get("AddressPostalCode"),
                    AddressCountry=data.get("AddressCountry"),
                    AddressNoteCodes=data.get("AddressNoteCodes"),
                    AddressNoteDesc=data.get("AddressNoteDesc"),
                    EmailCertainty=data.get("EmailCertainty"),
                    EmailQuality=data.get("EmailQuality"),
                    EmailCorrected=data.get("EmailCorrected"),
                    EmailNoteCodes=data.get("EmailNoteCodes"),
                    EmailNoteDesc=data.get("EmailNoteDesc"),
                    IPAddressCertainty=data.get("IPAddressCertainty"),
                    IPAddressQuality=data.get("IPAddressQuality"),
                    IPCountry=data.get("IPCountry"),
                    IPLocality=data.get("IPLocality"),
                    IPAdminArea=data.get("IPAdminArea"),
                    IPNoteCodes=data.get("IPNoteCodes"),
                    IPNoteDesc=data.get("IPNoteDesc"),
                    Phone1Certainty=data.get("Phone1Certainty"),
                    Phone1Quality=data.get("Phone1Quality"),
                    Phone1Locality=data.get("Phone1Locality"),
                    Phone1AdminArea=data.get("Phone1AdminArea"),
                    Phone1Country=data.get("Phone1Country"),
                    Phone1NoteCodes=data.get("Phone1NoteCodes"),
                    Phone1NoteDesc=data.get("Phone1NoteDesc"),
                    Phone2Certainty=data.get("Phone2Certainty"),
                    Phone2Quality=data.get("Phone2Quality"),
                    Phone2Locality=data.get("Phone2Locality"),
                    Phone2AdminArea=data.get("Phone2AdminArea"),
                    Phone2Country=data.get("Phone2Country"),
                    Phone2NoteCodes=data.get("Phone2NoteCodes"),
                    Phone2NoteDesc=data.get("Phone2NoteDesc"),
                    PhoneContact=phone_contact,
                    InformationComponents=[
                        InformationComponent(Name=comp.get("Name"), Value=comp.get("Value"))
                        for comp in data.get("InformationComponents", [])
                    ] if "InformationComponents" in data else [],
                    Error=error
                )
            except Exception as backup_exc:
                raise RuntimeError("LeadValidation service unreachable on both endpoints") from backup_exc
        else:
            raise RuntimeError(f"LeadValidation trial error: {str(req_exc)}") from req_exc
