// Step 1: Backend Setup to Retrieve Session Token
// File: backend.js

const express = require('express');
const axios = require('axios');
const router = express.Router();

router.post('/api/get_cardlytics_session', async (req, res) => {
    try {
        const payload = {
            client_id: process.env.CARDLYTICS_CLIENT_ID,
            client_secret: process.env.CARDLYTICS_CLIENT_SECRET
        };
        const response = await axios.post(
            'https://publisher-rewards-api.cardlytics.com/v2/session/startSession',
            payload,
            { headers: { 'Content-Type': 'application/json' } }
        );
        const sessionToken = response.data.sessionToken;
        res.json({ sessionToken, isLoggedIn: true });
    } catch (error) {
        console.error('Error retrieving session token:', error);
        res.status(500).json({ error: 'Failed to retrieve session token' });
    }
});

module.exports = router;

// Step 2: Frontend Setup to Initialize SDK
// File: frontend.js

<script src="https://publisher-cdn-us.cardlytics.com/linking-sdk/v1/cardlytics-embedding-sdk.js"></script>
<script>
    async function getSessionImplementation() {
        try {
            const response = await fetch('/api/get_cardlytics_session', { method: 'POST' });
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error fetching session token:', error);
            throw new Error('Failed to fetch session token');
        }
    }

    const { open, close } = CardlyticsEmbeddedSDK.create({
        applicationId: 'your_application_id', // Replace with your actual application ID
        getSession: getSessionImplementation,
    });

    document.getElementById('openBtn').addEventListener("click", function () {
        open(); // Attach `open` to a button on your page
    });
</script>

// Step 3: HTML Setup
// File: index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cardlytics Web SDK Integration</title>
</head>
<body>
    <button id="openBtn">Open Cardlytics Experience</button>
    <script src="frontend.js"></script>
</body>
</html>