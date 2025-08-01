import requests
import json
import hmac
import hashlib


def generate_signature(secret_key, message):
    """
    Generate HMAC-SHA-256 signature.

    Args:
        secret_key (str): The secret key for HMAC.
        message (str): The message to sign.

    Returns:
        str: The generated signature.
    """
    return hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()


def get_ads(base_url, session_token, publisher_id, customer_id, secret_key, **optional_params):
    """
    Retrieve personalized offers by calling the /v2/ads/getAds endpoint.

    Args:
        base_url (str): Base API URL from documentation.
        session_token (str): JWT session token for authentication.
        publisher_id (str): Publisher ID required for the request.
        customer_id (str): Customer ID required for the request.
        secret_key (str): Secret key for generating the HMAC signature.
        **optional_params: Optional fields such as customer location, placement types, and ranking preferences.

    Returns:
        dict: API response containing ad groups and metadata.
    """
    url = f'{base_url}/v2/ads/getAds'

    headers = {
        'Authorization': f'Bearer {session_token}',
        'Content-Type': 'application/json',
        'x-sdk-info': 'your-sdk-info'  # Replace with actual SDK info if needed
    }

    payload = {
        'publisherId': publisher_id,
        'customerId': customer_id,
        **optional_params
    }

    # Generate signature
    message = json.dumps(payload, separators=(',', ':'))
    signature = generate_signature(secret_key, message)
    headers['x-signature'] = signature

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f'API call failed: {e}')

# Example usage
# base_url = 'https://platform.cardlytics.com'
# session_token = 'your-session-token'
# publisher_id = 'your-publisher-id'
# customer_id = 'your-customer-id'
# secret_key = 'your-secret-key'
# ads = get_ads(base_url, session_token, publisher_id, customer_id, secret_key, location='NY', placementType='banner')
# print(ads)