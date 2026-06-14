import requests
from config import PROSPEO_API_KEY

def find_decision_makers(domain):
    headers = {
        "X-KEY": PROSPEO_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "page": 1,
        "filters": {
            "company": {
                "websites": {
                    "include": [domain]
                }
            }
        }
    }
    try:
        response = requests.post(
            "https://api.prospeo.io/search-person",
            json=payload,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        contacts = []
        for result in data.get("results", []):
            person = result.get("person", {})
            contacts.append({
                "name": person.get("full_name", "Unknown"),
                "title": person.get("current_job_title", ""),
                "linkedin_url": person.get("linkedin_url", ""),
                "person_id": person.get("person_id", ""),
                "domain": domain
            })
        print("[Prospeo] Found " + str(len(contacts)) + " contacts at " + domain)
        return contacts
    except requests.exceptions.Timeout:
        print("[Prospeo] Timeout for " + domain)
        return []
    except requests.exceptions.HTTPError as e:
        print("[Prospeo] HTTP error for " + domain + ": " + str(e))
        return []
    except Exception as e:
        print("[Prospeo] Error for " + domain + ": " + str(e))
        return []
