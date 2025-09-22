import { soap } from 'strong-soap';

/**
 * <summary>
 * A class that provides functionality to call the ServiceObjects Lead Validation (LV) SOAP service's ValidateLead_V3 endpoint,
 * retrieving lead validation information for a given US or Canada lead with fallback to a backup endpoint for reliability in live mode.
 * </summary>
 */
class ValidateLeadV3Soap {
    /**
     * <summary>
     * Initializes a new instance of the ValidateLeadV3Soap class with the provided input parameters,
     * setting up primary and backup WSDL URLs based on the live/trial mode.
     * </summary>
     * @param {string} FullName - The contacts full name. Optional.
     * @param {string} Salutation - Salutation of the contact. Optional.
     * @param {string} FirstName - First name of the contact. Optional.
     * @param {string} LastName - Last name of the contact. Optional.
     * @param {string} BusinessName - The contacts company. Optional.
     * @param {string} BusinessDomain - Website domain associated with the business. Optional.
     * @param {string} BusinessEIN - Company Tax Number for US leads. Optional.
     * @param {string} Address1 - Address line 1 of the contact or business address. Optional.
     * @param {string} Address2 - Address line 2 of the contact or business address. Optional.
     * @param {string} Address3 - Address line 3 of the contact or business address. Optional.
     * @param {string} Address4 - Address line 4 of the contact or business address. Optional.
     * @param {string} Address5 - Address line 5 of the contact or business address. Optional.
     * @param {string} Locality - The city of the contacts postal address. Optional.
     * @param {string} AdminArea - The state or province of the contacts postal address. Optional.
     * @param {string} PostalCode - The zip or postal code of the contacts postal address. Optional.
     * @param {string} Country - The country of the contacts postal address (e.g., "United States", "US"). Optional.
     * @param {string} Phone1 - The contacts primary phone number. Optional.
     * @param {string} Phone2 - The contacts secondary phone number. Optional.
     * @param {string} Email - The contacts email address. Optional.
     * @param {string} IPAddress - The contacts IP address in IPv4. Optional.
     * @param {string} Gender - The contacts gender. Optional.
     * @param {string} DateOfBirth - The contacts date of birth. Optional.
     * @param {string} UTCCaptureTime - The time the lead was submitted. Optional.
     * @param {string} OutputLanguage - Language for some output information. Optional.
     * @param {string} TestType - The type of validation to perform. Required.
     * @param {string} LicenseKey - Your license key to use the service.    
     * @param {boolean} isLive - Value to determine whether to use the live or trial servers.
     * @param {number} timeoutSeconds - Timeout, in seconds, for the call to the service.
     * @throws {Error} Thrown if LicenseKey is empty or null.
     */
    constructor(FullName, Salutation, FirstName, LastName, BusinessName, BusinessDomain, BusinessEIN,
        Address1, Address2, Address3, Address4, Address5, Locality, AdminArea, PostalCode, Country,
        Phone1, Phone2, Email, IPAddress, Gender, DateOfBirth, UTCCaptureTime, OutputLanguage, TestType, LicenseKey,
        isLive = true, timeoutSeconds = 15) {

        this.args = {
            FullName, Salutation, FirstName, LastName, BusinessName, BusinessDomain, BusinessEIN,
            Address1, Address2, Address3, Address4, Address5, Locality, AdminArea, PostalCode, Country,
            Phone1, Phone2, Email, IPAddress, Gender, DateOfBirth, UTCCaptureTime, OutputLanguage, TestType, LicenseKey
        };

        this.isLive = isLive;
        this.timeoutSeconds = timeoutSeconds;

        this.LiveBaseUrl = 'https://sws.serviceobjects.com/LV/soap.svc?wsdl';
        this.BackupBaseUrl = 'https://swsbackup.serviceobjects.com/LV/soap.svc?wsdl';
        this.TrialBaseUrl = 'https://trial.serviceobjects.com/LV/soap.svc?wsdl';

        this._primaryWsdl = this.isLive ? this.LiveBaseUrl : this.TrialBaseUrl;
        this._backupWsdl = this.isLive ? this.BackupBaseUrl : this.TrialBaseUrl;
    }

    /**
     * <summary>
     * Asynchronously calls the ValidateLead_V3 SOAP endpoint, attempting the primary endpoint
     * first and falling back to the backup if the response is invalid (Error.TypeCode == '3') in live mode
     * or if the primary call fails.
     * </summary>
     * @returns {Promise<Object>} A promise that resolves to an object containing lead validation details or an error.
     * @throws {Error} Thrown if both primary and backup calls fail, with detailed error messages.
     */
    async invokeAsync() {
        try {
            const primaryResult = await this._callSoap(this._primaryWsdl, this.args);

            if (this.isLive && !this._isValid(primaryResult)) {
                console.warn("Primary returned Error.TypeCode == '3', falling back to backup...");
                const backupResult = await this._callSoap(this._backupWsdl, this.args);
                return backupResult;
            }

            return primaryResult;
        } catch (primaryErr) {
            try {
                const backupResult = await this._callSoap(this._backupWsdl, this.args);
                return backupResult;
            } catch (backupErr) {
                throw new Error(`Both primary and backup calls failed:\nPrimary: ${primaryErr.message}\nBackup: ${backupErr.message}`);
            }
        }
    }

    /**
     * <summary>
     * Performs a SOAP service call to the specified WSDL URL with the given arguments,
     * creating a client and processing the response into an object.
     * </summary>
     * @param {string} wsdlUrl - The WSDL URL of the SOAP service endpoint (primary or backup).
     * @param {Object} args - The arguments to pass to the ValidateLead_V3 method.
     * @returns {Promise<Object>} A promise that resolves to an object containing the SOAP response data.
     * @throws {Error} Thrown if the SOAP client creation fails, the service call fails, or the response cannot be parsed.
     */
    _callSoap(wsdlUrl, args) {
        return new Promise((resolve, reject) => {
            soap.createClient(wsdlUrl, { timeout: this.timeoutSeconds * 1000 }, (err, client) => {
                if (err) return reject(err);

                client.ValidateLead_V3(args, (err, result) => {
                    const response = result?.ValidateLead_V3Result;
                    try {
                        if (!response) {
                            return reject(new Error("SOAP response is empty or undefined."));
                        }
                        resolve(response);
                    } catch (parseErr) {
                        reject(new Error(`Failed to parse SOAP response: ${parseErr.message}`));
                    }
                });
            });
        });
    }

    /**
     * <summary>
     * Checks if a SOAP response is valid by verifying that it exists and either has no Error object
     * or the Error.TypeCode is not equal to '3'.
     * </summary>
     * @param {Object} response - The response object to validate.
     * @returns {boolean} True if the response is valid, false otherwise.
     */
    _isValid(response) {
        return response && (!response.Error || response.Error.TypeCode !== '3');
    }
}

export { ValidateLeadV3Soap };