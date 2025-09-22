from suds.client import Client
from suds import WebFault
from suds.sudsobject import Object


class ValidateLeadV3Soap:
    def __init__(self, license_key: str, is_live: bool = True, timeout_ms: int = 15000):
        """
        Parameters:
            license_key: Service Objects LV license key.
            is_live: Whether to use live or trial endpoints.
            timeout_ms: SOAP call timeout in milliseconds.
        """
        
        self.is_live = is_live
        self._timeout_s = timeout_ms / 1000.0
        self.license_key = license_key

        # WSDL URLs
        self._primary_wsdl = (
            "https://sws.serviceobjects.com/lv/soap.svc?wsdl"
            if is_live
            else "https://trial.serviceobjects.com/lv/soap.svc?wsdl"
        )
        self._backup_wsdl = (
            "https://swsbackup.serviceobjects.com/lv/soap.svc?wsdl"
            if is_live
            else "https://trial.serviceobjects.com/lv/soap.svc?wsdl"
        )

    def validate_lead_v3(self,
                        full_name: str,
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
                        test_type: str) -> Object:
        """
        Calls the ValidateLead_V3 SOAP API to retrieve lead validation information.

        Parameters:
            full_name: The contacts full name. Optional.
            salutation: Salutation of the contact. Optional.
            first_name: First name of the contact. Optional.
            last_name: Last name of the contact. Optional.
            business_name: The contacts company. Optional.
            business_domain: Website domain associated with the business (e.g., "serviceobjects.com"). Optional.
            business_ein: Company Tax Number for US leads. Optional.
            address1: Address line 1 of the contact or business address. Optional.
            address2: Address line 2 of the contact or business address. Optional.
            address3: Address line 3 of the contact or business address. Optional.
            address4: Address line 4 of the contact or business address. Optional.
            address5: Address line 5 of the contact or business address. Optional.
            locality: The city of the contacts postal address. Optional.
            admin_area: The state or province of the contacts postal address. Optional.
            postal_code: The zip or postal code of the contacts postal address. Optional.
            country: The country of the contacts postal address. Optional.
            phone1: The contacts primary phone number. Optional.
            phone2: The contacts secondary phone number. Optional.
            email: The contacts email address. Optional.
            ip_address: The contacts IP address in IPv4. Optional.
            gender: The contacts gender. Optional.
            date_of_birth: The contacts date of birth. Optional.
            utc_capture_time: The time the lead was submitted. Optional.
            output_language: Language for some output information. Optional.
            test_type: The type of validation to perform. Required.

        Returns:
            suds.sudsobject.Object: SOAP response containing lead validation details or error.

        Raises:
            RuntimeError: If both primary and backup endpoints fail.
            ValueError: If the license key is empty or null.
        """
        # Common kwargs for both calls
        call_kwargs = dict(
            FullName=full_name,
            Salutation=salutation,
            FirstName=first_name,
            LastName=last_name,
            BusinessName=business_name,
            BusinessDomain=business_domain,
            BusinessEIN=business_ein,
            Address1=address1,
            Address2=address2,
            Address3=address3,
            Address4=address4,
            Address5=address5,
            Locality=locality,
            AdminArea=admin_area,
            PostalCode=postal_code,
            Country=country,
            Phone1=phone1,
            Phone2=phone2,
            Email=email,
            IPAddress=ip_address,
            Gender=gender,
            DateOfBirth=date_of_birth,
            UTCCaptureTime=utc_capture_time,
            OutputLanguage=output_language,
            TestType=test_type,
            LicenseKey=self.license_key,
        )

        # Attempt primary
        try:
            client = Client(self._primary_wsdl, timeout=self._timeout_s)
            response = client.service.ValidateLead_V3(**call_kwargs)

            # If response is None or fatal error code, trigger fallback
            if response is None or (hasattr(response, "Error") and response.Error and response.Error.TypeCode == "3"):
                raise ValueError("Primary returned no result or Error.TypeCode=3")

            return response

        except (WebFault, ValueError, Exception) as primary_ex:
            # Attempt backup
            try:
                client = Client(self._backup_wsdl, timeout=self._timeout_s)
                response = client.service.ValidateLead_V3(**call_kwargs)
                if response is None:
                    raise ValueError("Backup returned no result")
                return response
            except (WebFault, Exception) as backup_ex:
                msg = (
                    "Both primary and backup endpoints failed.\n"
                    f"Primary error: {str(primary_ex)}\n"
                    f"Backup error: {str(backup_ex)}"
                )
                raise RuntimeError(msg)
