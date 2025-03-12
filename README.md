# **📧 Email Spam Detection**  

> A Python-based spam detection system that identifies spam emails by analyzing predefined keyword patterns, hyperlinks, and excessive capitalization. The system integrates with Gmail to scan unread emails and move detected spam to the **Spam** folder.  

---

##  Table of Contents
- [Description](#description)
- [Technologies](#technologies)
- [How to Use](#how-to-use)
- [Gmail Integration](#gmail-integration)
- [Graphical Representations](#graphical-representations)
- [License](#license)
- [Author Info](#author-info) 

---

## Description  

This project is designed to detect spam emails by scanning the **subject and body** for specific spam-related patterns. It can detect:  
✅ **Spam keywords** (e.g., "earn money", "free gift")  
✅ **Suspicious hyperlinks**  
✅ **Excessive capitalization**  

Additionally, the script **integrates with Gmail** to:  
- Scan unread emails in the inbox  
- **Move detected spam emails** to the Spam folder  
- **Count** spam and non-spam emails  
- **Save the email analysis data to a CSV file** for further review  

---
 
##  Technologies  
- **Python**  
- **Google Gmail API**  
- **Regular Expressions (re module)**  
- **Google API Client Library**  

---

##  How To Use

### Installation  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/email-spam-detection.git
   cd email-spam-detection
   ```
2. **Install dependencies**  
   ```bash
   pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```
3. **Enable Gmail API**  
   - Visit the [Google Developer Console](https://console.cloud.google.com/)  
   - Enable **Gmail API**  
   - Download `credentials.json` and place it inside the project folder  

4. **Run the script**  
   ```bash
   python email_spam_detection.py
   ```

---

##  Gmail Integration

To integrate with Gmail, follow these steps:  

✅ **Enable the Gmail API** in Google Cloud Console  
✅ **Set up OAuth credentials** and download `credentials.json`  
✅ **Authenticate using OAuth** (only needed on first run)  
✅ The script will:  
   - **Scan unread emails**  
   - **Detect spam**  
   - **Move spam emails to the Spam folder**  

---

##  Saving Email Data  

The script will **count and log** all scanned emails.  

✔ **Spam Emails:** Moves detected spam to the Spam folder  
✔ **Non-Spam Emails:** Leaves them in the inbox  
✔ **Data Saved in `email_analysis.csv`**  

**Example CSV Output:**  
| Email Subject           | Classification |  
|-------------------------|---------------|  
| 50% off                 | Spam          |  
| Meeting at 10 AM        | Non-Spam      |  
| NPTEL News Letter       | Spam          |  
| Account Statement       | Non-Spam      |  

 **Location:** The file `email_analysis.csv` will be saved in the project folder.  

---
##  Graphical Representations
To help analyze the email spam trends, the script generates the following graphs:

Spam vs. Non-Spam (Pie Chart)
Shows the proportion of spam vs. non-spam emails detected.

![Pie Chart](https://private-user-images.githubusercontent.com/71929588/421852652-8bb6e615-57fa-48e8-b434-dbe0b3ddb90d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDE3NzkxMDMsIm5iZiI6MTc0MTc3ODgwMywicGF0aCI6Ii83MTkyOTU4OC80MjE4NTI2NTItOGJiNmU2MTUtNTdmYS00OGU4LWI0MzQtZGJlMGIzZGRiOTBkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMTIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzEyVDExMjY0M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdhMzA3OGQ4M2NmMGZmMmIxZmMwYmFhNTUwNjQxM2ZmZGY1MGM3Njg4MDE1YmJkM2EzMmNmZDUzNGFjMjgzMjEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.5D2NAEUKlggHSBP50uadBD2tvoCsJCLfh_3W2wpMD7I)

---

## License  

**MIT License**  

This project is open-source and free to use under the **MIT License**.  

---

##  Author Info  

- **GitHub** - [PB515](https://github.com/PB515)  
- **LinkedIn** - [Purven Bhavsar](https://linkedin.com/in/purvenbhavsar)  
- **Website** - [purvenbhavsar.com](https://pb515.github.io/Purven-Bhavsar/)  

---


