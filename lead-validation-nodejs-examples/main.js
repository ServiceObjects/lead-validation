import {ValidateLeadV3ClientGo} from './validate_lead_v3_rest_example.js';
import {ValidateLeadV3SoapGo} from './validate_lead_v3_soap_example.js';

export async function main()
{
    //Your license key from Service Objects.
    //Trial license keys will only work on the
    //trail environments and production license
    //keys will only work on production environments.
    const licenseKey = "LICENSE KEY";
    const isLive = true;

    // FastTax – GetBestMatch - REST SDK
    await ValidateLeadV3ClientGo(licenseKey, isLive);

    // FastTax – GetBestMatch - SOAP SDK
    await ValidateLeadV3SoapGo(licenseKey, isLive);

}
main().catch((error) => {
  console.error("An error occurred:", error);
  process.exit(1);
});