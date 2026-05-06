# newsforge

A small autonomous agent that wakes up every morning, scans the web for the latest AI and tech news, and sends you a clean digest directly to your email or WhatsApp. No dashboards, no feeds to check, no manual work.

---

## what it does

Every day at 7am IST, a GitHub Actions workflow kicks off a LangGraph pipeline that:

1. Searches the web for fresh AI and tech news using Tavily
2. Filters out noise and low-signal content using GPT-4o-mini
3. Categorizes each article into advancements, risks, or major news
4. Writes a sharp 2-sentence summary for each one
5. Delivers the digest to your email (SendGrid) and/or WhatsApp (Twilio)

Total running cost: under $0.20 a month.

---

## sample output

```
Your Daily AI Digest — Tuesday, May 6, 2026

🚀 ADVANCEMENTS
• Meta releases open-source Llama 4 Scout
  Beats GPT-4o on most coding benchmarks and runs on a single A100.
  Released under a permissive license, it's already shipping in VS Code extensions.

⚠️ RISKS & BAD NEWS
• EU AI Act enforcement begins with first formal warnings
  Three companies flagged for non-compliant hiring tools, facing fines up to 3% of global revenue.
  This marks the first real teeth of the Act being used in practice.

📰 MAJOR NEWS
• Anthropic closes $3B Series F
  Round led by Google at a $40B valuation, funding enterprise expansion.
  Capital will go toward infrastructure and continued safety research.
```

---

## tech stack

| piece | what it does |
|---|---|
| Python 3.12 | runtime |
| LangGraph | agent state machine |
| LangChain + langchain-openai | LLM abstraction |
| GPT-4o-mini | filtering, categorizing, summarizing |
| Tavily | real-time news search |
| Jinja2 | HTML email templating |
| SendGrid | email delivery |
| Twilio | WhatsApp delivery |
| GitHub Actions | daily cron scheduling |

---

## setup

**1. Clone and install**

```bash
git clone https://github.com/LordAizen1/newsforge.git
cd newsforge
pip install -r requirements.txt
```

**2. Set up your environment**

```bash
cp .env.example .env
```

Fill in `.env` with your API keys:

```
OPENAI_API_KEY=sk-...
TAVILY_API_KEY=tvly-...
SENDGRID_API_KEY=SG...
SENDER_EMAIL=you@gmail.com
RECIPIENT_EMAIL=you@gmail.com
TWILIO_ACCOUNT_SID=AC...
TWILIO_AUTH_TOKEN=...
TWILIO_WHATSAPP_FROM=+14155238886
WHATSAPP_RECIPIENT=+91XXXXXXXXXX
DELIVERY_CHANNEL=email
```

Set `DELIVERY_CHANNEL` to `email`, `whatsapp`, or `both`.

**3. Run it once to test**

```bash
python -m agent.graph
```

---

## where to get the keys

| key | where |
|---|---|
| `OPENAI_API_KEY` | platform.openai.com/api-keys |
| `TAVILY_API_KEY` | tavily.com (free tier: 1000 searches/month) |
| `SENDGRID_API_KEY` | sendgrid.com, then verify a sender email |
| Twilio keys | twilio.com, enable WhatsApp sandbox under Messaging |

---

## deploy to GitHub Actions

Push the repo to GitHub, then go to Settings → Secrets and variables → Actions and add all the keys from your `.env` as repository secrets.

The workflow at `.github/workflows/daily_digest.yml` will run automatically at 7am IST every day. You can also trigger it manually from the Actions tab anytime.

---

## project structure

```
newsforge/
├── agent/
│   ├── graph.py          # pipeline definition
│   ├── state.py          # shared state schema
│   ├── nodes/            # one file per pipeline step
│   └── prompts/          # system prompts for each LLM node
├── templates/
│   └── email.html        # HTML email template
├── tests/
│   └── test_nodes.py
├── .github/workflows/
│   └── daily_digest.yml
└── .env.example
```

---

## extending it

A few ideas if you want to take it further:

- **Custom topics**: add a config file to define your own search queries (biotech, fintech, robotics)
- **Slack delivery**: swap or add a Slack node using the Bolt SDK
- **Preference memory**: store which articles you found useful and re-rank future digests
- **Observability**: wire in LangSmith to trace each node's timing and output

---

made with curiosity · runs on ~$0.15/month
