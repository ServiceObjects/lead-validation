using System.Web;

namespace lead_validation_dot_net.REST
{
    /// <summary>
    /// Provides functionality to call the ServiceObjects Lead Validation (LV) REST API's ValidateLead_V3 endpoint,
    /// retrieving lead validation information for a given US or Canada lead with fallback to a backup endpoint for reliability in live mode.
    /// </summary>
    public static class ValidateLeadV3Client
    {
        // Base URL constants: production, backup, and trial
        private const string LiveBaseUrl = "https://sws.serviceobjects.com/lv/api.svc/json/";
        private const string BackupBaseUrl = "https://swsbackup.serviceobjects.com/lv/api.svc/json/";
        private const string TrialBaseUrl = "https://trial.serviceobjects.com/lv/api.svc/json/";

        /// <summary>
        /// Synchronously calls the ValidateLead_V3 REST endpoint to retrieve lead validation information,
        /// attempting the primary endpoint first and falling back to the backup if the response is invalid
        /// (Error.TypeCode == "3") in live mode.
        /// </summary>
        /// <param name="input">The input parameters including name, address, phone, email, and other lead details.</param>
        /// <returns>Deserialized <see cref="LVResponse"/> containing lead validation data or an error.</returns>
        public static LVResponse Invoke(ValidateLeadV3Input input)
        {
            // Use query string parameters so missing/optional fields don't break the URL
            string url = BuildUrl(input, input.IsLive ? LiveBaseUrl : TrialBaseUrl);
            LVResponse response = Helper.HttpGet<LVResponse>(url, input.TimeoutSeconds);

            // Fallback on error in live mode
            if (input.IsLive && !IsValid(response))
            {
                string fallbackUrl = BuildUrl(input, BackupBaseUrl);
                LVResponse fallbackResponse = Helper.HttpGet<LVResponse>(fallbackUrl, input.TimeoutSeconds);
                return fallbackResponse;
            }

            return response;
        }

        /// <summary>
        /// Asynchronously calls the ValidateLead_V3 REST endpoint to retrieve lead validation information,
        /// attempting the primary endpoint first and falling back to the backup if the response is invalid
        /// (Error.TypeCode == "3") in live mode.
        /// </summary>
        /// <param name="input">The input parameters including name, address, phone, email, and other lead details.</param>
        /// <returns>Deserialized <see cref="LVResponse"/> containing lead validation data or an error.</returns>
        public static async Task<LVResponse> InvokeAsync(ValidateLeadV3Input input)
        {
            // Use query string parameters so missing/optional fields don't break the URL
            string url = BuildUrl(input, input.IsLive ? LiveBaseUrl : TrialBaseUrl);
            LVResponse response = await Helper.HttpGetAsync<LVResponse>(url, input.TimeoutSeconds).ConfigureAwait(false);

            // Fallback on error in live mode
            if (input.IsLive && !IsValid(response))
            {
                string fallbackUrl = BuildUrl(input, BackupBaseUrl);
                LVResponse fallbackResponse = await Helper.HttpGetAsync<LVResponse>(fallbackUrl, input.TimeoutSeconds).ConfigureAwait(false);
                return fallbackResponse;
            }

            return response;
        }

        // Build the full request URL, including URL-encoded query string
        public static string BuildUrl(ValidateLeadV3Input input, string baseUrl)
        {
            // Construct query string with URL-encoded parameters
            string qs = $"ValidateLead_V3?" +
                        $"FullName={Helper.UrlEncode(input.FullName)}" +
                        $"&Salutation={Helper.UrlEncode(input.Salutation)}" +
                        $"&FirstName={Helper.UrlEncode(input.FirstName)}" +
                        $"&LastName={Helper.UrlEncode(input.LastName)}" +
                        $"&BusinessName={Helper.UrlEncode(input.BusinessName)}" +
                        $"&BusinessDomain={Helper.UrlEncode(input.BusinessDomain)}" +
                        $"&BusinessEIN={Helper.UrlEncode(input.BusinessEIN)}" +
                        $"&Address1={Helper.UrlEncode(input.Address1)}" +
                        $"&Address2={Helper.UrlEncode(input.Address2)}" +
                        $"&Address3={Helper.UrlEncode(input.Address3)}" +
                        $"&Address4={Helper.UrlEncode(input.Address4)}" +
                        $"&Address5={Helper.UrlEncode(input.Address5)}" +
                        $"&Locality={Helper.UrlEncode(input.Locality)}" +
                        $"&AdminArea={Helper.UrlEncode(input.AdminArea)}" +
                        $"&PostalCode={Helper.UrlEncode(input.PostalCode)}" +
                        $"&Country={Helper.UrlEncode(input.Country)}" +
                        $"&Phone1={Helper.UrlEncode(input.Phone1)}" +
                        $"&Phone2={Helper.UrlEncode(input.Phone2)}" +
                        $"&Email={Helper.UrlEncode(input.Email)}" +
                        $"&IPAddress={Helper.UrlEncode(input.IPAddress)}" +
                        $"&Gender={Helper.UrlEncode(input.Gender)}" +
                        $"&DateOfBirth={Helper.UrlEncode(input.DateOfBirth)}" +
                        $"&UTCCaptureTime={Helper.UrlEncode(input.UTCCaptureTime)}" +
                        $"&OutputLanguage={Helper.UrlEncode(input.OutputLanguage)}" +
                        $"&TestType={Helper.UrlEncode(input.TestType)}" +
                        $"&LicenseKey={Helper.UrlEncode(input.LicenseKey)}";
            return baseUrl + qs;
        }

        private static bool IsValid(LVResponse response) => response?.Error == null || response.Error.TypeCode != "3";

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
        /// <param name="IsLive">Indicates whether to use the live service (true) or trial service (false).</param>
        /// <param name="TimeoutSeconds">Timeout duration for the API call, in seconds.</param>
        public record ValidateLeadV3Input(
            string FullName = "",
            string Salutation = "",
            string FirstName = "",
            string LastName = "",
            string BusinessName = "",
            string BusinessDomain = "",
            string BusinessEIN = "",
            string Address1 = "",
            string Address2 = "",
            string Address3 = "",
            string Address4 = "",
            string Address5 = "",
            string Locality = "",
            string AdminArea = "",
            string PostalCode = "",
            string Country = "",
            string Phone1 = "",
            string Phone2 = "",
            string Email = "",
            string IPAddress = "",
            string Gender = "",
            string DateOfBirth = "",
            string UTCCaptureTime = "",
            string OutputLanguage = "",
            string TestType = "",
            string LicenseKey = "",
            bool IsLive = true,
            int TimeoutSeconds = 15
        );
    }
}