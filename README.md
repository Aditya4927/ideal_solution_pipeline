# Automated Outreach Pipeline

A fully automated cold-outreach pipeline that takes one company domain as input and handles everything — from finding lookalike companies to sending personalized emails.

## How It Works

1. **Ocean.io** — Takes seed domain, finds 5 lookalike companies
2. **Prospeo** — Finds decision makers at each company
3. **Eazyreach** — Resolves LinkedIn profiles to work emails
4. **Brevo** — Sends personalized outreach emails

## Setup

1. Clone the repo
2. Install dependencies: `pip install requests`
3. Add your API keys in `config.py`
4. Run the pipeline: `python3 main.py`

## Usage

```bash
python3 main.py
# Enter seed domain (e.g. stripe.com): stripe.com
```

## Safety

A confirmation checkpoint is shown before any emails are sent. The user must type `yes` to proceed.

## Project Structure

```
ideal_solution_pipeline/
├── main.py
├── config.py
├── stages/
│   ├── ocean.py
│   ├── prospeo.py
│   ├── eazyreach.py
│   └── brevo.py
└── README.md
```
