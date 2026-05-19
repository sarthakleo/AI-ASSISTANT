# 🤖 AI Business Assistant - Codex Solutions

An intelligent, AI-powered business automation assistant built with **Streamlit** and powered by **Groq's LLaMA 3.3 70B model**. This application helps businesses automate customer inquiries, capture leads, and manage client interactions through a conversational AI interface.

---

## 🌟 Features

### 🎯 Main Features
- **AI-Powered Chat Interface**: Conversational assistant powered by LLaMA 3.3 70B for intelligent business automation
- **Lead Capture Form**: Multi-page form to collect customer inquiries and business requirements
- **Admin Dashboard**: Real-time analytics and lead management with KPIs and filtering
- **Multi-Page Streamlit Application**: Organized interface with dedicated pages for different functions
- **Database Persistence**: SQLite database for storing leads and conversation history
- **Email Notifications**: Automated email notifications for new leads
- **Quick Questions**: Pre-built question templates for faster interactions
- **Session Management**: Persistent conversation history with conversation reset capability

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Streamlit |
| **Backend** | Python 3.x |
| **AI Model** | Groq (LLaMA 3.3 70B) |
| **Database** | SQLite |
| **Email** | SMTP (Gmail-compatible) |
| **HTTP Server** | Flask |
| **Environment** | Python venv |

**Dependencies:**
- `streamlit` - Web UI framework
- `groq` - LLM API client
- `flask` - REST API server
- `flask-cors` - CORS support
- `python-dotenv` - Environment variables
- `pandas` - Data analysis (for dashboard)

---

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Setup Steps

1. **Clone the Repository**
```bash
git clone <repository-url>
cd AI-ASSITANCE
```

2. **Create Virtual Environment**
```bash
python -m venv .venv
```

3. **Activate Virtual Environment**

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

4. **Install Dependencies**
```bash
pip install -r requirements.txt
```

5. **Configure Environment Variables**

Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=recipient@example.com
```

**Get GROQ API Key:**
- Visit [console.groq.com](https://console.groq.com)
- Create an account and generate an API key

**Setup Gmail SMTP:**
- Enable 2-factor authentication on Gmail
- Generate an [App Password](https://myaccount.google.com/apppasswords)
- Use the app password in `.env`

---

## 🚀 Usage

### Run the Application

```bash
python -m streamlit run app.py
```

The application will be available at:
- **Local**: http://localhost:8501
- **Network**: http://192.168.0.x:8501

### Features Overview

#### 1. **Chat Page** (Main)
- Chat with the AI Business Assistant
- Quick question buttons for instant responses
- Clear conversation history option
- Sidebar navigation

#### 2. **Lead Form Page** (📝 Get a Free Consultation)
- Collect customer information
- Service selection dropdown
- Budget estimation
- Message/requirements input
- Automatic lead storage and email notification

#### 3. **Admin Dashboard** (📊 Admin Dashboard)
- View all leads with details
- KPI metrics:
  - Total leads count
  - Unique companies
  - Today's leads
  - High-budget leads
  - Average leads per day
- Lead filtering and analysis
- Export capabilities

---

## 📁 Project Structure

```
AI-ASSITANCE/
│
├── app.py                      # Main Streamlit application
├── bot.py                      # Chatbot logic & AI integration
├── chatbot.py                  # CLI chatbot interface
├── config.py                   # Configuration & constants
├── database.py                 # SQLite database operations
├── email_utils.py              # Email sending functionality
├── prompts.py                  # AI prompt templates
├── server.py                   # Flask API server
│
├── pages/                      # Streamlit multi-page apps
│   ├── 1_Lead_Form.py          # Lead capture form
│   └── 2_Admin_Dashboard.py    # Admin analytics dashboard
│
├── requirements.txt            # Python dependencies
├── leads.db                    # SQLite database (auto-generated)
├── .env                        # Environment variables (create manually)
└── README.md                   # This file
```

---

## ⚙️ Configuration

### Customize Services & Pricing

Edit `config.py` to modify:

```python
SERVICES = {
    'AI Chatbot Development': {'price': '₹ 49,999–1,49,999', 'weeks': '2–6'},
    'Business Process Automation': {'price': '₹ 29,999–99,999', 'weeks': '1–4'},
    # Add more services...
}
```

### Customize Business Info

Update company details in `config.py`:

```python
BUSINESS_INFO = {
    'company_name': 'Codex Solutions',
    'tagline': 'Automate. Innovate. Accelerate.',
    'website': 'codex.com',
    'email': 'hello@codex.com',
    'phone': '1800-COD-ENIX',
}
```

### Modify AI Behavior

Adjust LLM parameters in `config.py`:

```python
MODEL = 'llama-3.3-70b-versatile'
MAX_TOKENS = 1024
TEMPERATURE = 0.7  # 0=deterministic, 1=creative
```

---

## 📊 Database Schema

### Leads Table
```sql
CREATE TABLE leads (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT,
    company TEXT,
    service TEXT,
    budget TEXT,
    message TEXT,
    timestamp TEXT
)
```

---

## 🔌 API Endpoints

The Flask server (`server.py`) provides REST APIs:

- `POST /api/chat` - Send message to chatbot
- `GET /api/leads` - Retrieve all leads
- `POST /api/leads` - Create new lead
- `GET /api/health` - Health check

---

## 🐛 Troubleshooting

### Issue: `streamlit not recognized`
**Solution:**
```bash
python -m streamlit run app.py
```

### Issue: `GROQ_API_KEY not found`
**Solution:**
- Create `.env` file with proper API key
- Verify file is in project root directory
- Restart the application

### Issue: Email not sending
**Solution:**
- Verify Gmail 2FA is enabled
- Check if App Password is generated and correct
- Verify `EMAIL_SENDER` and `EMAIL_PASSWORD` in `.env`

### Issue: Database locked error
**Solution:**
```bash
rm leads.db  # Delete corrupted database
# Restart app - database will regenerate
```

---

## 👥 Team

**Codex Solutions**
- 🌐 Website: [codex.com](https://codex.com)
- 📧 Email: [hello@codex.com](mailto:hello@codex.com)
- ☎️ Phone: 1800-COD-ENIX
- ⏰ Support Hours: Mon–Sat, 9 AM – 7 PM IST

---

## 📝 License

This project is proprietary software by Codex Solutions. All rights reserved.

---

## 🚀 Future Enhancements

- [ ] User authentication & admin login
- [ ] Advanced lead scoring
- [ ] Integration with CRM systems
- [ ] Multiple language support
- [ ] Conversation analytics
- [ ] Custom AI model fine-tuning
- [ ] Webhook integrations
- [ ] Mobile app version

---

## 📞 Support

For issues, questions, or feature requests, contact:
- **Email**: hello@codex.com
- **Phone**: 1800-COD-ENIX
- **Hours**: Mon–Sat, 9 AM – 7 PM IST

---

**Tagline:** *Automate. Innovate. Accelerate.* ⚡


Updated AI Business Automation Assistant