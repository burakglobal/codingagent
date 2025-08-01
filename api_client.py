import requests
import json

class CardlyticsAPIClient:
    def __init__(self, base_url, auth_token, source_customer_id, mock_data=False):
        self.base_url = base_url
        self.auth_token = auth_token
        self.source_customer_id = source_customer_id
        self.mock_data = mock_data

    def send_client_event(self, client_event_id, client_event_type, client_event, client_event_timestamp, client_event_metadata=None):
        """
        Sends a client event to the Cardlytics API.

        Args:
            client_event_id (str): GUID assigned by client to associate with the event.
            client_event_type (str): Type of the event which took place.
            client_event (str): Event which took place.
            client_event_timestamp (str): ISO-8601 timestamp representing when the event took place.
            client_event_metadata (dict, optional): Metadata to associate with event, if applicable.

        Returns:
            dict: API response containing the requestId.
        """
        url = f'{self.base_url}/v2/events/clientEvent'

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.auth_token}',
            'x-source-customer-id': self.source_customer_id
        }

        if self.mock_data:
            headers['x-mock-data'] = 'true'

        payload = {
            "clientEvents": [
                {
                    "clientEventId": client_event_id,
                    "clientEventType": client_event_type,
                    "clientEvent": client_event,
                    "clientEventTimestamp": client_event_timestamp,
                    "clientEventMetadata": client_event_metadata or {}
                }
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f'Failed to send client event: {e}')

# Example usage:
# client = CardlyticsAPIClient(
#     base_url='https://publisher-rewards-api.cardlytics.com',
#     auth_token='your_auth_token',
#     source_customer_id='your_source_customer_id',
#     mock_data=True
# )
# response = client.send_client_event(
#     client_event_id='12395199-1565-4565-bf99-3f94ee505d12',
#     client_event_type='AdInteraction',
#     client_event='ActivateOffer',
#     client_event_timestamp='2024-10-01T07:00:00Z',
#     client_event_metadata={
#         "serveToken": "CiQ3MGU5ZjQzMy0xMjQxLTRlZTctOTZlZi02ZWM4MDQwZjg3MzgQqoTjo6syGgoxMDAwMDYyNzQwIgVFbWFpbA==",
#         "section": "Dashboard",
#         "channel": "OLB"
#     }
# )
# print(response)