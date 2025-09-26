import axios from 'axios';
import querystring from 'querystring';
import { LVResponse } from './lv_response.js';

/**
 * @constant
 * @type {string}
 * @description The base URL for the live ServiceObjects Lead Validation (LV) API service.
 */
const LiveBaseUrl = 'https://sws.serviceobjects.com/lv/api.svc/json/';

/**
 * @constant
 * @type {string}
 * @description The base URL for the backup ServiceObjects Lead Validation (LV) API service.
 */
const BackupBaseUrl = 'https://swsbackup.serviceobjects.com/lv/api.svc/json/';

/**
 * @constant
 * @type {string}
 * @description The base URL for the trial ServiceObjects Lead Validation (LV) API service.
 */
const TrialBaseUrl = 'https://trial.serviceobjects.com/lv/api.svc/json/';

/**
 * <summary>
 * Checks if a response from the API is valid by verifying that it either has no Error object
 * or the Error.TypeCode is not equal to '3'.
 * </summary>
 * <param name="response" type="Object">The API response object to validate.</param>
 * <returns type="boolean">True if the response is valid, false otherwise.</returns>
 */
const isValid = (response) => !response?.Error || response.Error.TypeCode !== '3';

/**
 * <summary>
 * Constructs a full URL for the ValidateLead_V3 API endpoint by combining the base URL
 * with query parameters derived from the input parameters.
 * </summary>
 * <param name="params" type="Object">An object containing all the input parameters.</param>
 * <param name="baseUrl" type="string">The base URL for the API service (live, backup, or trial).</param>
 * <returns type="string">The constructed URL with query parameters.</returns>
 */
const buildUrl = (params, baseUrl) =>
    `${baseUrl}ValidateLead_V3?${querystring.stringify(params)}`;

/**
 * <summary>
 * Performs an HTTP GET request to the specified URL with a given timeout.
 * </summary>
 * <param name="url" type="string">The URL to send the GET request to.</param>
 * <param name="timeoutSeconds" type="number">The timeout duration in seconds for the request.</param>
 * <returns type="Promise<LVResponse>">A promise that resolves to an LVResponse object containing the API response data.</returns>
 * <exception cref="Error">Thrown if the HTTP request fails, with a message detailing the error.</exception>
 */
const httpGet = async (url, timeoutSeconds) => {
    try {
        const response = await axios.get(url, { timeout: timeoutSeconds * 1000 });
        return new LVResponse(response.data);
    } catch (error) {
        throw new Error(`HTTP request failed: ${error.message}`);
    }
};

/**
 * <summary>
 * Provides functionality to call the ServiceObjects Lead Validation (LV) API's ValidateLead_V3 endpoint,
 * retrieving lead validation information for a given US or Canada lead with fallback to a backup endpoint for reliability in live mode.
 * </summary>
 */
const ValidateLeadV3Client = {
    /**
     * <summary>
     * Asynchronously invokes the ValidateLead_V3 API endpoint, attempting the primary endpoint
     * first and falling back to the backup if the response is invalid (Error.TypeCode == '3') in live mode.
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
     * @returns {Promise<LVResponse>} - A promise that resolves to an LVResponse object.
     */
    async invokeAsync(fullName, salutation, firstName, lastName, businessName, businessDomain, businessEIN,
        address1, address2, address3, address4, address5, locality, adminArea, postalCode, country,
        phone1, phone2, email, ipAddress, gender, dateOfBirth, utcCaptureTime, outputLanguage, testType, licenseKey,
        isLive = true, timeoutSeconds = 15) {
        const params = {
            fullName, salutation, firstName, lastName, businessName, businessDomain, businessEIN,
            address1, address2, address3, address4, address5, locality, adminArea, postalCode, country,
            phone1, phone2, email, ipAddress, gender, dateOfBirth, utcCaptureTime, outputLanguage, testType, licenseKey
        };

        const url = buildUrl(params, isLive ? LiveBaseUrl : TrialBaseUrl);
        let response = await httpGet(url, timeoutSeconds);

        if (isLive && !isValid(response)) {
            const fallbackUrl = buildUrl(params, BackupBaseUrl);
            const fallbackResponse = await httpGet(fallbackUrl, timeoutSeconds);
            return fallbackResponse;
        }
        return response;
    },

    /**
     * <summary>
     * Synchronously invokes the ValidateLead_V3 API endpoint by wrapping the async call
     * and awaiting its result immediately.
     * </summary>
     * @param {string} FullName - The contacts full name. Optional.
     * @param {string} Salutation - Salutation of the contact. Optional.
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
     * @returns {LVResponse} - An LVResponse object with lead validation details or an error.
     */
    invoke(fullName, salutation, firstName, lastName, businessName, businessDomain, businessEIN,
        address1, address2, address3, address4, address5, locality, adminArea, postalCode, country,
        phone1, phone2, email, ipAddress, gender, dateOfBirth, utcCaptureTime, outputLanguage, testType, licenseKey,
        isLive = true, timeoutSeconds = 15) {
        return (async () => await this.invokeAsync(
            fullName, salutation, firstName, lastName, businessName, businessDomain, businessEIN,
            address1, address2, address3, address4, address5, locality, adminArea, postalCode, country,
            phone1, phone2, email, ipAddress, gender, dateOfBirth, utcCaptureTime, outputLanguage, testType, licenseKey,
            isLive, timeoutSeconds
        ))();
    }
};

export { ValidateLeadV3Client, LVResponse };