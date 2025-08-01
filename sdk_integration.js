// Include the SDK script in your HTML file
// <script src="https://platform.cardlytics.com/sdk.js?version=1.0.0"></script>

// Function to instantiate the SDK and configure it
function initializeCdlxSDK(elementId, placementType, callbackFunctions) {
    window.cdlxRewards.render({
        elementId: elementId,
        placementType: placementType,
        ...callbackFunctions
    });
}

// Example usage of the SDK initialization
initializeCdlxSDK('reward-container', 'banner', {
    onLoad: () => console.log('SDK Loaded'),
    onError: (error) => console.error('SDK Error:', error)
});

// Function to retrieve a customer's reward summary
async function getCustomerRewardSummary(baseUrl, sessionToken) {
    const url = `${baseUrl}/v2/customerProfile/getCustomerRewardSummary`;
    const headers = {
        'Authorization': `Bearer ${sessionToken}`,
        'Content-Type': 'application/json'
    };

    try {
        const response = await fetch(url, { headers });
        if (!response.ok) {
            throw new Error(`Error fetching reward summary: ${response.statusText}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Failed to retrieve reward summary:', error);
        throw error;
    }
}

// Example usage of retrieving reward summary
// getCustomerRewardSummary('https://platform.cardlytics.com', 'your-session-token')
//     .then(data => console.log('Reward Summary:', data))
//     .catch(error => console.error('Error:', error));