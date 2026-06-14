import requests
from config import BREVO_API_KEY, SENDER_EMAIL, SENDER_NAME

def send_outreach(contact):
    """Sends a personalized cold email to one contact"""
    
    if not contact.get("email"):
        print(f"[Brevo] Skipping {contact['name']} — no email found")
        return False
    
    first_name = contact['name'].split()[0]
    company = contact['domain'].replace('.com', '').replace('.io', '').title()
    
    subject = f"Quick question for {first_name} at {company}"
    
    body = f"""Hi {first_name},

I came across {company} and was genuinely impressed by what your team is building.

We help companies like yours streamline their outreach and lead generation — saving hours of manual work every week.

Would you be open to a quick 15-minute call this week to explore if there's a fit?

Best regards,
{SENDER_NAME}
Ideal Solution
{SENDER_EMAIL}
"""
    
    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }
    
    payload = {
        "sender": {"name": SENDER_NAME, "email": SENDER_EMAIL},
        "to": [{"email": contact["email"], "name": contact["name"]}],
        "subject": subject,
        "textContent": body
    }
    
    try:
        response = requests.post(
            "https://api.brevo.com/v3/smtp/email",
            json=payload,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        print(f"[Brevo] ✅ Email sent to {contact['name']} ({contact['email']})")
        return True
    
    except requests.exceptions.HTTPError as e:
        print(f"[Brevo] ❌ Failed for {contact['email']}: {e}")
        return False
    except Exception as e:
        print(f"[Brevo] ❌ Error: {e}")
        return False