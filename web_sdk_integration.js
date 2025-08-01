// Import necessary modules
import axios from 'axios';

// Function to get session token
async function getSessionToken(clientId, clientSecret, customerId) {
    const url = 'https://publisher-rewards-api.cardlytics.com/v2/session/startSession';
    const headers = {
        'Content-Type': 'application/json',
        'x-source-customer-id': customerId
    };
    const payload = {
        clientId: clientId,
        secret: clientSecret
    };

    try {
        const response = await axios.post(url, payload, { headers });
        return response.data.sessionToken;
    } catch (error) {
        console.error('Error fetching session token:', error);
        throw new Error('Failed to get session token');
    }
}

// Function to initialize the Cardlytics Web SDK
async function initializeCardlyticsSDK(applicationId, clientId, clientSecret, customerId) {
    const sessionToken = await getSessionToken(clientId, clientSecret, customerId);

    const { open, close } = CardlyticsEmbeddedSDK.create({
        applicationId: applicationId,
        getSession: async () => ({ sessionToken, isLoggedIn: true })
    });

    document.getElementById('openBtn').addEventListener('click', function () {
        open();
    });
}

// Example usage
(async () => {
    const applicationId = 'your_application_id';
    const clientId = 'your_client_id';
    const clientSecret = 'your_client_secret';
    const customerId = 'hashed_customer_id'; // Use HMAC-SHA-256 to hash the customer ID

    try {
        await initializeCardlyticsSDK(applicationId, clientId, clientSecret, customerId);
        console.log('Cardlytics SDK initialized successfully');
    } catch (error) {
        console.error('Failed to initialize Cardlytics SDK:', error);
    }
})();