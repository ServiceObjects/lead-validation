using lead_validation_dot_net_examples;


//Your license key from Service Objects.
//Trial license keys will only work on the
//trail environments and production license
//keys will only work on production environments.
string LicenseKey = "LICENSE KEY";

bool IsProductionKey = false;

// LeadValidation - ValidateLead_V3 - REST SDK
ValidateLeadV3RestSdkExample.Go(LicenseKey, IsProductionKey);

// LeadValidation - ValidateLead_V3 - SOAP SDK
ValidateLeadV3SoapSdkExample.Go(LicenseKey, IsProductionKey);
