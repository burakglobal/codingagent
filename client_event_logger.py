import requests
import json
from datetime import datetime


def log_client_event(base_url, auth_token, event_type, ad_id, ad_group_id, placement):
    """
    Logs a client event to the Cardlytics API.

    Args:
        base_url (str): The base URL for the Cardlytics API.
        auth_token (str): The authentication token for API access.
        event_type (str): The type of event (e.g., 'impression').
        ad_id (str): The ID of the ad.
        ad_group_id (str): The ID of the ad group.
        placement (str): The placement of the ad.

    Returns:
        dict: The API response.
    """
    url = f'{base_url}/v2/events/clientEvent'
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'eventType': event_type,
        'adId': ad_id,
        'adGroupId': ad_group_id,
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'placement': placement
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f'Failed to log client event: {e}')

# Example usage
# response = log_client_event(
#     base_url='https://platform.cardlytics.com',
#     auth_token='your_auth_token',
#     event_type='impression',
#     ad_id='12345',
#     ad_group_id='67890',
#     placement='homepage'
# )
# print(response)