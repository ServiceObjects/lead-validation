from validate_lead_v3_rest_example import validate_lead_v3_rest_sdk_go
from validate_lead_v3_soap_example import validate_lead_v3_soap_sdk_go

if __name__ == "__main__":
   # Your license key from Service Objects.  
    # Trial license keys will only work on the trial environments and production  
    # license keys will only work on production environments.
    #   
    license_key = "LICENSE KEY"  
    is_live = True

    # LeadValidation - ValidateLead_V3 - REST SDK
    validate_lead_v3_rest_sdk_go(is_live, license_key)

    # LeadValidation - ValidateLead_V3 - SOAP SDK
    validate_lead_v3_soap_sdk_go(is_live, license_key)
