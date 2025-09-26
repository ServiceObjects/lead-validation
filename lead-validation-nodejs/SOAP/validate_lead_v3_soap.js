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
     * @param {string} fullName - The contacts full name (e.g., "Jane Doe"). Optional.
     * @param {string} salutation - Salutation of the contact (e.g., "Dr", "Mr"). Optional.
     * @param {string} firstName - First name of the contact (e.g., "Jane"). Optional.
     * @param {string} lastName - Last name of the contact (e.g., "Doe"). Optional.
     * @param {string} businessName - The contacts company (e.g., "Service Objects"). Optional.
     * @param {string} businessDomain - Website domain associated with the business (e.g., "serviceobjects.com"). Optional.
     * @param {string} businessEIN - Company Tax Number for US leads. Optional.
     * @param {string} address1 - Address line 1 of the contact or business address. Optional.
     * @param {string} address2 - Address line 2 of the contact or business address. Optional.
     * @param {string} address3 - Address line 3 of the contact or business address. Optional.
     * @param {string} address4 - Address line 4 of the contact or business address. Optional.
     * @param {string} address5 - Address line 5 of the contact or business address. Optional.
     * @param {string} locality - The city of the contacts postal address. Optional.
     * @param {string} adminArea - The state or province of the contacts postal address. Optional.
     * @param {string} postalCode - The zip or postal code of the contacts postal address. Optional.
     * @param {string} country - The country of the contacts postal address (e.g., "United States", "US"). Optional.
     * @param {string} phone1 - The contacts primary phone number. Optional.
     * @param {string} phone2 - The contacts secondary phone number. Optional.
     * @param {string} email - The contacts email address. Optional.
     * @param {string} ipAddress - The contacts IP address in IPv4. Optional.
     * @param {string} gender - The contacts gender ("Male", "Female", "Neutral"). Optional.
     * @param {string} dateOfBirth - The contacts date of birth. Optional.
     * @param {string} utcCaptureTime - The time the lead was submitted. Optional.
     * @param {string} outputLanguage - Language for some output information. Optional.
     * @param {string} testType - The type of validation to perform. Required.
     * @param {string} licenseKey - Your license key to use the service.
     * @param {boolean} isLive - Value to determine whether to use the live or trial servers.
     * @param {number} timeoutSeconds - Timeout, in seconds, for the call to the service.
     * @throws {Error} Thrown if LicenseKey is empty or null.
     */
    constructor(fullName, salutation, firstName, lastName, businessName, businessDomain, businessEIN,
        address1, address2, address3, address4, address5, locality, adminArea, postalCode, country,
        phone1, phone2, email, ipAddress, gender, dateOfBirth, utcCaptureTime, outputLanguage, testType, licenseKey,
        isLive = true, timeoutSeconds = 15) {

        this.args = {
            fullName, salutation, firstName, lastName, businessName, businessDomain, businessEIN,
            address1, address2, address3, address4, address5, locality, adminArea, postalCode, country,
            phone1, phone2, email, ipAddress, gender, dateOfBirth, utcCaptureTime, outputLanguage, testType, licenseKey
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