import time
from stages.ocean import find_lookalikes
from stages.prospeo import find_decision_makers
from stages.eazyreach import resolve_email
from stages.brevo import send_outreach

def run_pipeline(seed_domain):
    print(f"\n🚀 Starting pipeline for: {seed_domain}\n")
    print("--- STAGE 1: Finding lookalike companies ---")
    domains = find_lookalikes(seed_domain)
    if not domains:
        print("No lookalike companies found. Exiting.")
        return
    print("\n--- STAGE 2: Finding decision-makers ---")
    all_contacts = []
    for domain in domains:
        contacts = find_decision_makers(domain)
        all_contacts.extend(contacts)
        time.sleep(1)
    if not all_contacts:
        print("No contacts found. Exiting.")
        return
    print("\n--- STAGE 3: Resolving work emails ---")
    for i, contact in enumerate(all_contacts):
        all_contacts[i] = resolve_email(contact)
        time.sleep(1)
    seen_emails = set()
    contacts_with_email = []
    for c in all_contacts:
        if c.get("email") and c["email"] not in seen_emails:
            seen_emails.add(c["email"])
            contacts_with_email.append(c)
    print(f"\n{'='*50}")
    print(f"READY TO SEND — Summary:")
    print(f"  Companies found:  {len(domains)}")
    print(f"  Total contacts:   {len(all_contacts)}")
    print(f"  Valid emails:     {len(contacts_with_email)}")
    print(f"\nContacts to be emailed:")
    for c in contacts_with_email:
        print(f"  - {c['name']} ({c['title']}) at {c['domain']} → {c['email']}")
    print(f"{'='*50}")
    confirm = input("\nProceed and send emails? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Aborted. No emails sent.")
        return
    print("\n--- STAGE 4: Sending outreach emails ---")
    sent = 0
    for contact in contacts_with_email:
        if send_outreach(contact):
            sent += 1
        time.sleep(1)
    print(f"\n✅ Pipeline complete. Sent {sent}/{len(contacts_with_email)} emails.")

if __name__ == "__main__":
    domain = input("Enter seed domain (e.g. stripe.com): ").strip()
    run_pipeline(domain)
