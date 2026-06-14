import requests
from config import OCEAN_API_KEY

def find_lookalikes(seed_domain):
    headers = {
        "X-Api-Token": OCEAN_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "size": 5,
        "companiesFilters": {
            "lookalikeDomains": [seed_domain]
        },
        "fields": ["domain", "name", "companySize", "industries"]
    }
    try:
        response = requests.post(
            "https://api.ocean.io/v3/search/companies",
            json=payload,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        domains = [company["company"]["domain"] for company in data.get("companies", [])]
        print("[Ocean.io] Found " + str(len(domains)) + " lookalike companies")
        return domains
    except requests.exceptions.Timeout:
        print("[Ocean.io] Request timed out")
        return []
    except requests.exceptions.HTTPError as e:
        print("[Ocean.io] HTTP error: " + str(e))
        print("[Ocean.io] Response: " + str(e.response.text[:200]))
        return []
    except Exception as e:
        print("[Ocean.io] Error: " + str(e))
        return []
