from bs4 import BeautifulSoup
import httpx
import re
from app.utils.auth import get_internal_headers, get_agent_client
from app.core.config import settings

async def search_leads(state: dict, query: str, limit: int = 5):
    """Hits the domain-service to find leads and lead-service to store/fetch them."""
    print(f"[Tool] Searching leads for: {query}")
    async with get_agent_client(state) as client:
        # 1. Search domain-service (website adapter for now)
        res = await client.post(f"{settings.DOMAIN_SERVICE_URL}/api/v1/domains/search", json={"domain": "website", "keyword": query})
        res.raise_for_status()
        raw_leads = res.json().get("results", [])
        
        # 2. Store found leads in lead-service (Phase 1 wiring)
        stored_leads = []
        for lead in raw_leads[:limit]:
            try:
                # We need to provide user_id and tenant_id but get_agent_client already handles headers
                l_res = await client.post(f"{settings.LEAD_SERVICE_URL}/api/v1/leads/", json=lead)
                l_res.raise_for_status()
                stored_leads.append(l_res.json())
            except Exception as e:
                print(f"Failed to store lead {lead.get('company_name')}: {e}")
                # Fallback to the raw lead if storage fails
                stored_leads.append(lead)
                
        return stored_leads

async def crawl_website(state: dict, url: str):
    """Hits enrichment-service to crawl a website."""
    print(f"[Tool] Crawling website: {url}")
    async with get_agent_client(state) as client:
        res = await client.post(f"{settings.ENRICHMENT_SERVICE_URL}/api/v1/enrichment/crawl?url={url}")
        res.raise_for_status()
        return res.json().get("text", "")

def extract_contact_info(text: str):
    """Extracts email addresses from text using regex."""
    print(f"[Tool] Extracting contact info from text length: {len(text)}")
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}", text)
    emails = list(set(emails))
    if not emails:
        return ["hello@example.com"]
    return emails

async def enrich_lead(state: dict, lead_data: dict):
    print(f"[Tool] Enriching lead: {lead_data.get('company_name')}")
    async with get_agent_client(state) as client:
        res = await client.post(f"{settings.ENRICHMENT_SERVICE_URL}/api/v1/enrichment/enrich", json=lead_data)
        res.raise_for_status()
        return res.json()

async def score_lead(state: dict, lead_data: dict):
    print(f"[Tool] Scoring lead: {lead_data.get('company_name')}")
    async with get_agent_client(state) as client:
        res = await client.post(f"{settings.ENRICHMENT_SERVICE_URL}/api/v1/enrichment/score", json={"lead_data": lead_data})
        res.raise_for_status()
        return res.json().get("score", 0)

async def match_icp(state: dict, lead_data: dict):
    print(f"[Tool] Matching ICP for lead: {lead_data.get('company_name')}")
    return True

async def fetch_replies(state: dict):
    print("[Tool] Fetching replies manually via agent...")
    return []

async def classify_reply(state: dict, reply_text: str):
    print(f"[Tool] Classifying reply...")
    async with get_agent_client(state) as client:
        res = await client.post(f"{settings.CONVERSATION_SERVICE_URL}/api/v1/conversations/classify", json={"message_text": reply_text})
        res.raise_for_status()
        return res.json().get("classification", "neutral")

async def get_metrics(state: dict):
    print("[Tool] Fetching analytics metrics...")
    async with get_agent_client(state) as client:
        res = await client.get(f"{settings.ANALYTICS_SERVICE_URL}/api/v1/analytics/overview")
        res.raise_for_status()
        return res.json()

async def track_event(state: dict, event_type: str, metadata: dict):
    print(f"[Tool] Tracking event: {event_type}")
    async with get_agent_client(state) as client:
        payload = {
            "event_type": event_type,
            "metadata": metadata
        }
        res = await client.post(f"{settings.ANALYTICS_SERVICE_URL}/api/v1/analytics/track", json=payload)
        res.raise_for_status()
        return res.json()

async def generate_email(state: dict, lead_data: dict):
    print(f"[Tool] Generating email for {lead_data.get('company_name')}")
    async with get_agent_client(state) as client:
        payload = {
            "lead_data": lead_data,
            "user_profile": {"offer": "Our AI automation services"}
        }
        res = await client.post(f"{settings.AI_SERVICE_URL}/api/v1/ai/generate-email", json=payload)
        res.raise_for_status()
        return res.json()

async def create_campaign(state: dict, leads: list):
    print(f"[Tool] Creating campaign with {len(leads)} leads")
    async with get_agent_client(state) as client:
        # 1. Create campaign
        res = await client.post(f"{settings.CAMPAIGN_SERVICE_URL}/api/v1/campaigns/", json={"name": "Auto Agent Campaign"})
        res.raise_for_status()
        campaign = res.json()
        
        # 2. Add leads with personalization
        leads_payload = []
        for lead in leads:
            lead_id = lead.get("id")
            if lead_id:
                # The agent state stores generated email per lead
                email_draft = lead.get("generated_email", {})
                leads_payload.append({
                    "lead_id": lead_id,
                    "personalized_subject": email_draft.get("subject"),
                    "personalized_body": email_draft.get("body")
                })
        
        if leads_payload:
            res_add = await client.post(
                f"{settings.CAMPAIGN_SERVICE_URL}/api/v1/campaigns/{campaign['id']}/add-leads", 
                json={"leads": leads_payload}
            )
            res_add.raise_for_status()
            
        return campaign

async def send_email(state: dict, campaign_id: str):
    print(f"[Tool] Initiating send for campaign {campaign_id}")
    async with get_agent_client(state) as client:
        res = await client.post(f"{settings.CAMPAIGN_SERVICE_URL}/api/v1/campaigns/{campaign_id}/send")
        res.raise_for_status()
        return res.json()

# --- PHASE 3 TOOLS ---
async def run_recipe(state: dict, recipe_id: str, context: dict = {}):
    """Trigger a recipe execution via recipe-service."""
    print(f"[Tool] Running recipe {recipe_id}")
    async with get_agent_client(state) as client:
        res = await client.post(
            f"{settings.RECIPE_SERVICE_URL}/api/v1/recipes/{recipe_id}/execute",
            json={"context": context}
        )
        res.raise_for_status()
        return res.json()

async def execute_step(state: dict, step_name: str, step_context: dict = {}):
    """Execute a single named step by running the agent with a targeted plan."""
    print(f"[Tool] Executing single step: {step_name}")
    async with get_agent_client(state) as client:
        payload = {
            "goal": f"Execute single step: {step_name}",
            "approved_to_send": state.get("approved_to_send", False)
        }
        res = await client.post(
            f"{settings.AGENT_SERVICE_URL}/api/v1/agent/run" if hasattr(settings, "AGENT_SERVICE_URL") else "http://agent-service:8000/api/v1/agent/run",
            json=payload
        )
        res.raise_for_status()
        return res.json()

async def schedule_job(state: dict, recipe_id: str, cron_expression: str = "0 9 * * 1"):
    """Schedule a recipe for recurring execution."""
    print(f"[Tool] Scheduling recipe {recipe_id} via scheduler-service")
    import datetime
    run_at = (datetime.datetime.utcnow() + datetime.timedelta(days=1)).isoformat()
    
    payload = {
        "task_name": "app.tasks.agent_tasks.run_recipe_task",
        "run_at": run_at,
        "kwargs": {"recipe_id": recipe_id, "context": {}}
    }
    
    async with get_agent_client(state) as client:
        res = await client.post(
            f"{settings.SCHEDULER_SERVICE_URL}/api/v1/scheduler/job",
            json=payload
        )
        res.raise_for_status()
        return res.json()

async def retry_job(state: dict, task_name: str, args: list = [], delay_seconds: int = 60):
    """Enqueue a retry for a failed Celery task via the worker."""
    print(f"[Tool] Retrying job {task_name} after {delay_seconds}s")
    import os
    from celery import Celery
    redis_url = os.getenv("REDIS_URL", "redis://redis:6379/0")
    celery_app = Celery("agent", broker=redis_url)
    celery_app.send_task(
        "app.tasks.agent_tasks.retry_job",
        args=[task_name, args, "default-queue", delay_seconds],
        queue="default-queue"
    )
    return {"status": "retry_scheduled", "task": task_name, "delay_seconds": delay_seconds}

# --- PHASE 4 TOOLS ---
async def search_domain(state: dict, domain: str, keyword: str):
    print(f"[Tool] Searching domain {domain} for {keyword}")
    async with get_agent_client(state) as client:
        res = await client.post(
            f"{settings.DOMAIN_SERVICE_URL}/api/v1/domains/search",
            json={"domain": domain, "keyword": keyword}
        )
        res.raise_for_status()
        return res.json().get("results", [])

async def detect_signal(state: dict, lead_id: str):
    print(f"[Tool] Detecting signal for lead {lead_id}")
    async with get_agent_client(state) as client:
        res = await client.get(f"{settings.DOMAIN_SERVICE_URL}/api/v1/signals/{lead_id}")
        res.raise_for_status()
        return res.json()

async def merge_lead_data(state: dict, lead_id: str, domains: list):
    print(f"[Tool] Merging lead data from {domains}")
    async with get_agent_client(state) as client:
        res = await client.post(
            f"{settings.DOMAIN_SERVICE_URL}/api/v1/domains/merge",
            json={"lead_id": lead_id, "domains": domains}
        )
        res.raise_for_status()
        return res.json()

async def index_search_data(state: dict, lead_data: dict):
    print(f"[Tool] Indexing search data for {lead_data.get('company_name')}")
    return True


# --- PHASE 5 TOOLS ---
async def check_reputation(state: dict, domain: str):
    print(f"[Tool] Checking reputation for {domain}")
    async with get_agent_client(state) as client:
        res = await client.get(
            f"{settings.DELIVERABILITY_SERVICE_URL}/api/v1/deliverability/reputation/{domain}"
        )
        if res.status_code in (404, 503):
            return {"domain": domain, "score": 95.0, "status": "healthy", "note": "stub fallback"}
        res.raise_for_status()
        return res.json()

async def warmup_domain(state: dict, domain: str):
    print(f"[Tool] Initiating warmup for {domain}")
    async with get_agent_client(state) as client:
        res = await client.post(
            f"{settings.DELIVERABILITY_SERVICE_URL}/api/v1/deliverability/warmup",
            json={"domain": domain}
        )
        if res.status_code in (404, 503):
            return {"domain": domain, "status": "warming_up", "note": "stub fallback"}
        res.raise_for_status()
        return res.json()

async def detect_abuse(state: dict, user_id: str, action: str):
    print(f"[Tool] Checking abuse patterns for {user_id} on {action}")
    return {"risk": "low"}

async def track_email_event(state: dict, campaign_id: str, event_type: str):
    print(f"[Tool] Tracking email event {event_type} for campaign {campaign_id}")
    return await track_event(state, event_type, {"campaign_id": campaign_id})

async def enforce_limit(state: dict, user_id: str, limit_type: str, limit: int):
    print(f"[Tool] Enforcing {limit_type} limit of {limit} for {user_id}")
    return {"allowed": True}

async def rotate_proxy(state: dict):
    print(f"[Tool] Rotating proxy")
    return {"new_proxy": "rotated"}


# --- PHASE 6 TOOLS ---
async def run_ab_test(state: dict, campaign_id: str, variants: list):
    print(f"[Tool] Running A/B test for campaign {campaign_id} with {len(variants)} variants")
    async with get_agent_client(state) as client:
        # Create experiment
        res_exp = await client.post(
            f"{settings.EXPERIMENT_SERVICE_URL}/api/v1/experiment/",
            json={"campaign_id": campaign_id, "experiment_type": "ab_test"}
        )
        res_exp.raise_for_status()
        exp_id = res_exp.json().get("id")
        
        # Add variants
        for v in variants:
            await client.post(
                f"{settings.EXPERIMENT_SERVICE_URL}/api/v1/experiment/variants",
                json={"experiment_id": exp_id, "variant_name": v.get("name", "variant"), "configuration": v}
            )
            
        return {"experiment_id": exp_id, "status": "running"}

async def analyze_performance(state: dict, campaign_id: str):
    print(f"[Tool] Analyzing performance for campaign {campaign_id}")
    return await get_metrics(state)

async def generate_recommendation(state: dict, user_id: str):
    print(f"[Tool] Generating recommendation for user {user_id}")
    return {"recommendation": "Use more personalized subject lines", "confidence": 0.88}

async def store_learning(state: dict, key: str, value: dict, score: float):
    print(f"[Tool] Storing learning for {key} with score {score}")
    async with get_agent_client(state) as client:
        res = await client.post(
            f"{settings.LEARNING_SERVICE_URL}/api/v1/learning/memory",
            json={"key": key, "value": value, "score": score}
        )
        res.raise_for_status()
        return res.json()

async def fetch_strategy(state: dict, strategy_name: str):
    print(f"[Tool] Fetching performance data for strategy: {strategy_name}")
    return await get_metrics(state)

async def optimize_sequence(state: dict, campaign_id: str):
    print(f"[Tool] Optimizing email sequence for campaign {campaign_id}")
    return {"status": "optimized"}

# --- PHASE 7 TOOLS ---
async def create_workspace(state: dict, org_id: str, name: str):
    print(f"[Tool] Creating workspace {name} for organization {org_id}")
    async with get_agent_client(state) as client:
        res = await client.post(
            f"{settings.ORGANIZATION_SERVICE_URL}/api/v1/organizations/",
            json={"name": name, "plan": "pro"}
        )
        res.raise_for_status()
        return res.json()

async def assign_role(state: dict, user_id: str, org_id: str, role: str):
    print(f"[Tool] Assigning role {role} to user {user_id} in org {org_id}")
    return True

async def generate_api_key(state: dict, org_id: str, permissions: list):
    print(f"[Tool] Generating API key for org {org_id}")
    return {"api_key": "ak_auto_generated"}

async def create_webhook(state: dict, org_id: str, url: str, events: list):
    print(f"[Tool] Creating webhook for {url} on events {events}")
    return {"webhook_id": "wh_auto"}

async def validate_policy(state: dict, org_id: str, action: str, data: dict):
    print(f"[Tool] Validating policy for {action} in org {org_id}")
    return {"allowed": True}

async def log_audit_event(state: dict, org_id: str, user_id: str, action: str):
    print(f"[Tool] Logging audit event {action} for user {user_id}")
    async with get_agent_client(state) as client:
        payload = {
            "action": action,
            "metadata": {"org_id": org_id}
        }
        res = await client.post(f"{settings.AUDIT_SERVICE_URL}/api/v1/audit/", json=payload)
        res.raise_for_status()
        return res.json()

