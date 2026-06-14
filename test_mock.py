from stages.brevo import send_outreach

# Fake data to test pipeline logic without using any credits
mock_domains = [
    "razorpay.com",
    "cashfree.com",
    "paytm.com"
]

mock_contacts = [
    {
        "name": "John Smith",
        "title": "CTO",
        "linkedin_url": "linkedin.com/in/johnsmith",
        "domain": "razorpay.com",
        "email": "adityasagar4927@gmail.com"
    }
]

# Test STAGE 4 only — sends a real email to YOUR gmail
print("--- Testing Brevo email sending ---")
result = send_outreach(mock_contacts[0])
if result:
    print("Success! Check your gmail inbox.")
else:
    print("Failed. Check your Brevo API key.")
