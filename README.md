# Email Spam Detection



> A Python-based spam detection system that identifies spam emails based on predefined keyword patterns and hyperlinks.

---

### Table of Contents

- [Description](#description)
- [Technologies](#technologies)
- [How To Use](#how-to-use)
- [Gmail Integration](#gmail-integration)
- [License](#license)
- [Author Info](#author-info)

---

## Description

This project is designed to detect spam emails by scanning the subject and body for specific patterns, including spam keywords, hyperlinks, and excessive capitalization. Additionally, it integrates with Gmail to automatically filter out spam messages from the inbox.

#### Features:

- Detects spam using regex-based keyword matching.
- Identifies spam emails containing suspicious links.
- Flags emails with excessive capitalization.
- Integrates with Gmail API to scan unread emails and move spam to the Spam folder.

[Back To The Top](#email-spam-detection)

---

## Technologies

- Python
- Google Gmail API
- Regular Expressions (re module)
- Google API Client Library

[Back To The Top](#email-spam-detection)

---

## How To Use

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/email-spam-detection.git
   cd email-spam-detection
   ```
2. Install dependencies:
   ```bash
   pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```
3. Enable Gmail API and download `credentials.json` from the [Google Developer Console](https://console.cloud.google.com/).
4. Place `credentials.json` in the project folder.
5. Run the script:
   ```bash
   python gmail_spam_filter.py
   ```

[Back To The Top](#email-spam-detection)

---

## Gmail Integration

To integrate with Gmail:

- Enable the **Gmail API** in Google Cloud Console.
- Set up OAuth credentials and download `credentials.json`.
- Authenticate using OAuth (first-time setup).
- The script will scan unread emails and move detected spam to the **Spam** folder.

[Back To The Top](#email-spam-detection)

---

## License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

[Back To The Top](#email-spam-detection)

---

## Author Info

- GitHub - [PB515](https://github.com/PB515)
- LinkedIn - [Purven Bhavsar](https://linkedin.com/in/purvenbhavsar)
- Website - [Purvenbhavsar.com](https://pb515.github.io/Purven-Bhavsar/)

[Back To The Top](#email-spam-detection)

