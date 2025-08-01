import requests

class CardlyticsWebSDK:
    def __init__(self, base_url, api_key):
        """
        Initialize the Cardlytics Web SDK client.

        Args:
            base_url (str): The base URL for the Cardlytics API.
            api_key (str): The API key for authenticating requests.
        """
        self.base_url = base_url
        self.api_key = api_key

    def start_session(self, customer_id):
        """
        Start a session by obtaining a JWT token.

        Args:
            customer_id (str): The customer ID to start the session for.

        Returns:
            dict: The response containing the JWT token.

        Raises:
            Exception: If the API call fails.
        """
        url = f'{self.base_url}/v2/session/startSession'
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'customerId': customer_id
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f'Failed to start session: {e}')

# Example usage:
# sdk = CardlyticsWebSDK(base_url='https://platform.cardlytics.com', api_key='your_api_key')
# session_response = sdk.start_session(customer_id='customer123')
# print(session_response)