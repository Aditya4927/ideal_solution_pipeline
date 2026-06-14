import requests
from config import EAZYREACH_API_KEY

def resolve_email(contact):
    if not contact.get("linkedin_url"):
        print(f"[Eazyreach] No LinkedIn URL for {contact['name']}, skipping")
        contact["email"] = None
        return contact
    try:
        headers = {"Authorization": f"Bearer {EAZYREACH_API_KEY}"}
        payload = {"linkedin_url": contact["linkedin_url"]}
        response = requests.post(
            "https://api.eazyreach.app/v1/email",
            json=payload,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        contact["email"] = data.get("email")
        print(f"[Eazyreach] Resolved email for {contact['name']}: {contact['email']}")
        return contact
    except requests.exceptions.Timeout:
        print(f"[Eazyreach] Timeout for {contact['name']}")
        contact["email"] = None
        return contact
    except requests.exceptions.HTTPError as e:
        print(f"[Eazyreach] HTTP error for {contact['name']}: {e}")
        contact["email"] = None
        return contact
    except Exception as e:
        print(f"[Eazyreach] Error for {contact['name']}: {e}")
        contact["email"] = None
        return contact
