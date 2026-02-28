# Email Security Automation & Risk Intelligence Framework

Open-source platform for automated email analysis, risk scoring, and threat intelligence. Built with Python/FastAPI, Celery, Docker, and OSS tools.

## Features
- Email ingestion (IMAP/API/.eml/SMTP)
- Header/auth validation (SPF/DKIM/DMARC + Quantum-Resistant Checks)
- IOC extraction/enrichment (MISP/AbuseIPDB/Spamhaus/VirusTotal)
- Sandboxing (Cuckoo/YARA + Multi-Modal Analysis)
- ML risk scoring (with AI-Generated Phishing Detection + Predictive Forecasting)
- Decentralized intel sharing (IPFS)
- Automated responder for safe engagement
- Dashboards with visualizations and gamified analyst interface
- Integrations: TheHive/Cortex/Wazuh/ELK

## Installation
1. Clone repo: `git clone https://github.com/yourusername/email-security-framework.git`
2. Install deps: `pip install -r requirements.txt`
3. Set env vars in `.env` (e.g., DB URLs, API keys for VT/AbuseIPDB)
4. Run: `docker-compose up`
5. Access API: http://localhost:8000/docs
6. Frontend: http://localhost:3000

## Usage
- Upload email: POST /ingest/email with .eml file
- Get report: GET /analysis/{email_id}

## License
AGPL-3.0