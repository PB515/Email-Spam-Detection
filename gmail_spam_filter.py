import re
import os
import base64
import csv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Spam detection patterns
spam_patterns = [
    r"\bearn money\b", r"\bmake money\b", r"\bget rich\b",
    r"\bwork from home\b", r"\bfree money\b", r"\bopportunity\b",
    r"\binvestment\b", r"\bcredit score\b", r"\bdebt relief\b",
    r"\bweight loss\b", r"\bdiet pill\b", r"\bviagra\b", r"\bCialis\b",
    r"\bonline pharmacy\b", r"\blottery\b", r"\bprize\b",
    r"\bfree gift\b", r"\bspecial offer\b", r"\blimited time\b",
    r"\bis live",r"\bwent live"
]

# Compile regex patterns
spam_regex = re.compile("|".join(spam_patterns), re.IGNORECASE)
hyperlink_pattern = re.compile(r'http[s]?://\S+', re.IGNORECASE)
capitalization_pattern = re.compile(r'[A-Z]{5,}')  # Detects 5+ consecutive uppercase letters

# Gmail API Authentication
SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]

def authenticate_gmail():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("gmail", "v1", credentials=creds)

# Track spam statistics
spam_count = 0
non_spam_count = 0
email_data = []  # Store email data

# Function to check if an email is spam
def is_spam(subject, body):
    global spam_count, non_spam_count

    if spam_regex.search(subject) or spam_regex.search(body):
        spam_count += 1
        return True

    if hyperlink_pattern.search(body):
        spam_count += 1
        return True

    if capitalization_pattern.search(subject) or capitalization_pattern.search(body):
        spam_count += 1
        return True

    non_spam_count += 1
    return False

# Function to read emails and detect spam
def check_emails():
    global spam_count, non_spam_count
    service = authenticate_gmail()
    results = service.users().messages().list(userId="me", labelIds=["INBOX"], q="is:unread").execute()
    messages = results.get("messages", [])

    if not messages:
        print("No unread emails found.")
        return

    for msg in messages:
        msg_id = msg["id"]
        msg_data = service.users().messages().get(userId="me", id=msg_id, format="full").execute()
        
        headers = msg_data["payload"]["headers"]
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "(No Subject)")
        body = ""

        if "parts" in msg_data["payload"]:
            for part in msg_data["payload"]["parts"]:
                if part["mimeType"] == "text/plain":
                    body = base64.urlsafe_b64decode(part["body"]["data"]).decode("utf-8", "ignore")

        is_spam_email = is_spam(subject, body)
        email_data.append([subject, "Spam" if is_spam_email else "Non-Spam"])

        if is_spam_email:
            print(f"Spam detected: {subject}")
            service.users().messages().modify(userId="me", id=msg_id, body={"addLabelIds": ["SPAM"], "removeLabelIds": ["INBOX"]}).execute()
        else:
            print(f"Not spam: {subject}")

# Function to save email data to CSV
def save_to_csv():
    with open("email_analysis.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Email Subject", "Classification"])  # Header
        writer.writerows(email_data)
    print("\n📊 Email analysis saved to email_analysis.csv")

if __name__ == "__main__":
    check_emails()  # Process emails
    print(f"\n📌 Spam Emails: {spam_count}")
    print(f"📌 Non-Spam Emails: {non_spam_count}")
    save_to_csv()  # Save results to CSV
