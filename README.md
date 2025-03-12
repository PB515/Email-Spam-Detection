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

![Pie Chart](https://drive.google.com/file/d/17R5-5Ie96NSU8CnOESzJbHLOQE12T486/view?usp=drive_link)

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


