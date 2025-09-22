using System;
using System.Threading.Tasks;
using LVReference;

namespace lead_validation_dot_net.SOAP
{
    /// <summary>
    /// Provides functionality to call the ServiceObjects Lead Validation (LV) SOAP service's ValidateLead_V3 operation,
    /// retrieving lead validation information for a given US or Canada lead with fallback to a backup endpoint for reliability in live mode.
    /// </summary>
    public class ValidateLeadV3Validation
    {
        private const string LiveBaseUrl = "https://sws.serviceobjects.com/LV/soap.svc/SOAP";
        private const string BackupBaseUrl = "https://swsbackup.serviceobjects.com/LV/soap.svc/SOAP";
        private const string TrialBaseUrl = "https://trial.serviceobjects.com/LV/soap.svc/SOAP";

        private readonly string _primaryUrl;
        private readonly string _backupUrl;
        private readonly int _timeoutMs;
        private readonly bool _isLive;

        /// <summary>
        /// Initializes URLs, timeout, and IsLive.
        /// </summary>
        public ValidateLeadV3Validation(bool isLive)
        {
            _timeoutMs = 10000;
            _isLive = isLive;

            _primaryUrl = isLive ? LiveBaseUrl : TrialBaseUrl;
            _backupUrl = isLive ? BackupBaseUrl : TrialBaseUrl;

            if (string.IsNullOrWhiteSpace(_primaryUrl))
                throw new InvalidOperationException("Primary URL not set.");
            if (string.IsNullOrWhiteSpace(_backupUrl))
                throw new InvalidOperationException("Backup URL not set.");
        }

        /// <summary>
        /// Input parameters for the ValidateLead_V3 API call. Represents lead details for validation in the US or Canada.
        /// </summary>
        /// <param name="FullName">The contact’s full name. Optional.</param>
        /// <param name="Salutation">Salutation of the contact. Optional.</param>
        /// <param name="FirstName">First name of the contact. Optional.</param>
        /// <param name="LastName">Last name of the contact. Optional.</param>
        /// <param name="BusinessName">The contact’s company. Optional.</param>
        /// <param name="BusinessDomain">Website domain associated with the business. Optional.</param>
        /// <param name="BusinessEIN">Company Tax Number for US leads. Optional.</param>
        /// <param name="Address1">Address line 1 of the contact or business address. Optional.</param>
        /// <param name="Address2">Address line 2 of the contact or business address. Optional.</param>
        /// <param name="Address3">Address line 3 of the contact or business address. Optional.</param>
        /// <param name="Address4">Address line 4 of the contact or business address. Optional.</param>
        /// <param name="Address5">Address line 5 of the contact or business address. Optional.</param>
        /// <param name="Locality">The city of the contact’s postal address. Optional.</param>
        /// <param name="AdminArea">The state or province of the contact’s postal address. Optional.</param>
        /// <param name="PostalCode">The zip or postal code of the contact’s postal address. Optional.</param>
        /// <param name="Country">The country of the contact’s postal address. Optional.</param>
        /// <param name="Phone1">The contact’s primary phone number. Optional.</param>
        /// <param name="Phone2">The contact’s secondary phone number. Optional.</param>
        /// <param name="Email">The contact’s email address. Optional.</param>
        /// <param name="IPAddress">The contact’s IP address in IPv4. Optional.</param>
        /// <param name="Gender">The contact’s gender ("Male", "Female", "Neutral"). Optional.</param>
        /// <param name="DateOfBirth">The contact’s date of birth. Optional.</param>
        /// <param name="UTCCaptureTime">The time the lead was submitted. Optional.</param>
        /// <param name="OutputLanguage">Language for some output information. Optional.</param>
        /// <param name="TestType">The type of validation to perform. Required.</param>
        /// <param name="LicenseKey">The license key to authenticate the API request. Required.</param>
        public async Task<ContactInternational> ValidateLead_V3Async(
            string FullName, string Salutation, string FirstName, string LastName,
            string BusinessName, string BusinessDomain, string BusinessEIN,
            string Address1, string Address2, string Address3, string Address4, string Address5,
            string Locality, string AdminArea, string PostalCode, string Country,
            string Phone1, string Phone2, string Email, string IPAddress,
            string Gender, string DateOfBirth, string UTCCaptureTime,
            string OutputLanguage, string TestType, string LicenseKey)
        {
            LVSoapServiceClient clientPrimary = null;
            LVSoapServiceClient clientBackup = null;

            try
            {
                // Attempt Primary
                clientPrimary = new LVSoapServiceClient();
                clientPrimary.Endpoint.Address = new System.ServiceModel.EndpointAddress(_primaryUrl);
                clientPrimary.InnerChannel.OperationTimeout = TimeSpan.FromMilliseconds(_timeoutMs);

                ContactInternational response = await clientPrimary.ValidateLead_V3Async(
                    FullName, Salutation, FirstName, LastName, BusinessName, BusinessDomain, BusinessEIN,
                    Address1, Address2, Address3, Address4, Address5, Locality, AdminArea, PostalCode, Country,
                    Phone1, Phone2, Email, IPAddress, Gender, DateOfBirth, UTCCaptureTime, OutputLanguage, TestType, LicenseKey)
                    .ConfigureAwait(false);

                if (_isLive && !IsValid(response))
                {
                    throw new InvalidOperationException("Primary endpoint returned null or a fatal TypeCode=3 error for ValidateLead_V3");
                }
                return response;
            }
            catch (Exception primaryEx)
            {
                try
                {
                    clientBackup = new LVSoapServiceClient();
                    clientBackup.Endpoint.Address = new System.ServiceModel.EndpointAddress(_backupUrl);
                    clientBackup.InnerChannel.OperationTimeout = TimeSpan.FromMilliseconds(_timeoutMs);

                    return await clientBackup.ValidateLead_V3Async(
                        FullName, Salutation, FirstName, LastName, BusinessName, BusinessDomain, BusinessEIN,
                        Address1, Address2, Address3, Address4, Address5, Locality, AdminArea, PostalCode, Country,
                        Phone1, Phone2, Email, IPAddress, Gender, DateOfBirth, UTCCaptureTime, OutputLanguage, TestType, LicenseKey)
                        .ConfigureAwait(false);
                }
                catch (Exception backupEx)
                {
                    throw new InvalidOperationException(
                        $"Both primary and backup endpoints failed.\n" +
                        $"Primary error: {primaryEx.Message}\n" +
                        $"Backup error: {backupEx.Message}");
                }
                finally
                {
                    clientBackup?.Close();
                }
            }
            finally
            {
                clientPrimary?.Close();
            }
        }

        private static bool IsValid(ContactInternational response) => response?.Error == null || response.Error.TypeCode != "3";
    }
}