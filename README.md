# Instahyre E2E Automation Framework 🚀

This is a PyTest-based automation framework for End-to-End (E2E) testing of the [Instahyre](https://www.instahyre.com) platform using Selenium WebDriver and the Page Object Model (POM) architecture.

---

## 📁 Project Structure
├── conftest.py  # PyTest fixtures (e.g., browser setup)
├── pages/ # Page Object Model classes
│ ├── base_page.py
│ ├── home_page.py
│ ├── login_page.py
│ └── opportunities_page.py
│
├── secure_store/ # Encrypted credential storage
│ ├── credentials.properties
│ └── secret.key
│
├── tests/
│ └── instahyre_flow.py # Test cases
│
├── utils/
│ ├── cred_utils.py # Decryption utility for credentials
│ └── feret_key_generator.py
│
├── .gitignore
└── README.md # You're here!



---

## ⚙️ Tech Stack

- 🐍 Python 3.10+
- 🧪 PyTest
- 🌐 Selenium WebDriver
- 🔐 AES-Encrypted Credential Management
- 📦 Page Object Model (POM) design

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/instahyre-e2e-pytest.git
cd instahyre-e2e-pytest


2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate     # On Windows
source .venv/bin/activate  # On Unix/macOS


3. Install dependencies
pip install -r requirements.txt

🔐 Secure Credential Setup
Add your Instahyre credentials in a credentials.properties file:
instahyre_email=your_email@example.com
instahyre_password=your_secure_password


Encrypt it using feret_key_generator.py (one-time):
python utils/feret_key_generator.py
  This will:
    Encrypt the credentials into credentials.properties
    Generate a new encryption key as secret.key

🧪 Running Tests
Run all tests:
PYTHONPATH=. pytest tests/

OR

Run a specific test file:
PYTHONPATH=. pytest tests/instahyre_flow.py


🧩 Features Implemented
      URL validation
      Secure login with encrypted credentials
      Apply to jobs under “Opportunities” based on availability
      Conditional handling for multiple apply buttons
      Modular & scalable with POM structure

🧼 Best Practices Followed
      Page Object Model for maintainability
      PyTest fixtures for shared browser sessions
      Secure credential handling using AES encryption
      Clean logging and error handling

🤝 Contributing
Pull requests are welcome! Please follow the structure and naming conventions used.

🛡️ License
This project is licensed under the MIT License - see the LICENSE file for details.

📬 Contact
Developer:Sagar Soni
Email: sagarsony5222@gmail.com
LinkedIn: https://www.linkedin.com/in/sagarsony/
