from app.core.state_manager import AgentState
from typing import Dict, Any
from app.utils.tools import (
    # Phase 1
    search_leads, crawl_website, extract_contact_info,
    generate_email, create_campaign, send_email,
    # Phase 2
    enrich_lead, score_lead, fetch_replies, classify_reply, get_metrics, track_event,
    # Phase 3
    run_recipe, execute_step, schedule_job, retry_job,
    # Phase 4
    search_domain, detect_signal, merge_lead_data, index_search_data,
    # Phase 5
    check_reputation, warmup_domain, detect_abuse, track_email_event, enforce_limit, rotate_proxy,
    # Phase 6
    run_ab_test, analyze_performance, generate_recommendation, store_learning, fetch_strategy, optimize_sequence,
    # Phase 7
    create_workspace, assign_role, generate_api_key, create_webhook, validate_policy, log_audit_event
)

async def _search_leads(state, context, results, step):
    leads = await search_leads(state, "software companies")
    context["leads"] = leads
    results[step] = f"Found {len(leads)} leads"

async def _enrich_lead(state, context, results, step):
    if "leads" in context:
        for lead in context["leads"]:
            text = await crawl_website(state, lead["website"])
            emails = extract_contact_info(text)
            lead["email"] = emails[0] if emails else None
            enrichment = await enrich_lead(state, lead)
            lead.update(enrichment)
        results[step] = "Enriched leads"

async def _score_lead(state, context, results, step):
    if "leads" in context:
        for lead in context["leads"]:
            lead["score"] = await score_lead(state, lead)
        results[step] = "Scored leads"

async def _generate_email(state, context, results, step):
    if "leads" in context:
        for lead in context["leads"]:
            email_copy = await generate_email(state, lead)
            lead["generated_email"] = email_copy
    results[step] = "Generated emails for leads"

async def _create_campaign(state, context, results, step):
    if "leads" in context:
        campaign = await create_campaign(state, context["leads"])
        context["campaign_id"] = campaign.get("id")
    results[step] = "Created campaign"

async def _send_email(state, context, results, step):
    # HUMAN IN THE LOOP: Check if approved
    if not state.get("approved_to_send", False):
        return {"status": "paused", "reason": "Awaiting human approval before sending emails."}
    
    campaign_id = context.get("campaign_id")
    if campaign_id:
        await send_email(state, campaign_id)
    results[step] = "Sent emails"

async def _fetch_replies(state, context, results, step):
    replies = await fetch_replies(state)
    context["replies"] = replies
    results[step] = f"Fetched {len(replies)} replies"

async def _classify_reply(state, context, results, step):
    if "replies" in context:
        for reply in context["replies"]:
            reply["classification"] = await classify_reply(state, reply.get("body", ""))
    results[step] = "Classified replies"

async def _get_metrics(state, context, results, step):
    metrics = await get_metrics(state)
    context["metrics"] = metrics
    results[step] = "Fetched metrics"

async def _track_event(state, context, results, step):
    event_type = context.get("event_type", "campaign_step")
    metadata = context.get("event_metadata", {})
    await track_event(state, event_type, metadata)
    results[step] = f"Tracked event: {event_type}"

async def _run_recipe(state, context, results, step):
    recipe_id = context.get("recipe_id", "")
    if not recipe_id:
        results[step] = "Skipped: no recipe_id in context"
    else:
        recipe_result = await run_recipe(state, recipe_id, context)
        context["recipe_execution"] = recipe_result
        results[step] = f"Recipe dispatched: {recipe_result.get('status')}"

async def _execute_step(state, context, results, step):
    step_name = context.get("target_step", "search_leads")
    step_result = await execute_step(state, step_name, context)
    results[step] = f"Step '{step_name}' result: {step_result.get('status')}"

async def _schedule_job(state, context, results, step):
    recipe_id = context.get("recipe_id", "")
    cron = context.get("cron_expression", "0 9 * * 1")
    if recipe_id:
        schedule_result = await schedule_job(state, recipe_id, cron)
        results[step] = f"Scheduled: {schedule_result.get('message')}"
    else:
        results[step] = "Skipped: no recipe_id in context"

async def _retry_job(state, context, results, step):
    task_name = context.get("retry_task_name", "")
    if task_name:
        retry_result = await retry_job(state, task_name, [], 60)
        results[step] = f"Retry scheduled for: {task_name}"
    else:
        results[step] = "Skipped: no retry_task_name in context"

async def _search_domain_hiring(state, context, results, step):
    leads = await search_domain(state, "hiring", "engineer")
    context["leads"] = leads
    results[step] = f"Found {len(leads)} leads from hiring domain"

async def _search_domain_local(state, context, results, step):
    leads = await search_domain(state, "local", "services")
    context["leads"] = leads
    results[step] = f"Found {len(leads)} leads from local domain"

async def _search_domain_website(state, context, results, step):
    leads = await search_domain(state, "website", "saas")
    context["leads"] = leads
    results[step] = f"Found {len(leads)} leads from website domain"

async def _detect_signal(state, context, results, step):
    if "leads" in context:
        for lead in context["leads"]:
            lead["signal_data"] = await detect_signal(state, lead.get("id", "123"))
    results[step] = "Detected signals for leads"

async def _merge_lead_data(state, context, results, step):
    if "leads" in context:
        for lead in context["leads"]:
            await merge_lead_data(state, lead.get("id", "123"), ["hiring", "local"])
    results[step] = "Merged cross-domain lead data"

async def _index_search_data(state, context, results, step):
    if "leads" in context:
        for lead in context["leads"]:
            await index_search_data(state, lead)
    results[step] = "Indexed leads for universal search"

async def _check_reputation(state, context, results, step):
    domain = context.get("domain", "example.com")
    results[step] = await check_reputation(state, domain)

async def _warmup_domain(state, context, results, step):
    domain = context.get("domain", "example.com")
    results[step] = await warmup_domain(state, domain)

async def _detect_abuse(state, context, results, step):
    user_id = state.get("user_id", "anon")
    results[step] = await detect_abuse(state, user_id, "mass_emailing")

async def _track_email_event(state, context, results, step):
    campaign_id = context.get("campaign_id", "camp123")
    results[step] = await track_email_event(state, campaign_id, "delivery")

async def _enforce_limit(state, context, results, step):
    user_id = state.get("user_id", "anon")
    results[step] = await enforce_limit(state, user_id, "daily_send", 100)

async def _rotate_proxy(state, context, results, step):
    results[step] = await rotate_proxy(state)

async def _run_ab_test(state, context, results, step):
    campaign_id = context.get("campaign_id", "camp123")
    variants = context.get("variants", [{"name": "A"}, {"name": "B"}])
    results[step] = await run_ab_test(state, campaign_id, variants)

async def _analyze_performance(state, context, results, step):
    campaign_id = context.get("campaign_id", "camp123")
    results[step] = await analyze_performance(state, campaign_id)

async def _generate_recommendation(state, context, results, step):
    user_id = state.get("user_id", "anon")
    results[step] = await generate_recommendation(state, user_id)

async def _store_learning(state, context, results, step):
    key = context.get("learning_key", "strategy_a")
    value = context.get("learning_value", {"pattern": "success"})
    score = context.get("learning_score", 0.9)
    results[step] = await store_learning(state, key, value, score)

async def _fetch_strategy(state, context, results, step):
    strategy_name = context.get("strategy_name", "cold_outreach")
    results[step] = await fetch_strategy(state, strategy_name)

async def _optimize_sequence(state, context, results, step):
    campaign_id = context.get("campaign_id", "camp123")
    results[step] = await optimize_sequence(state, campaign_id)

async def _create_workspace(state, context, results, step):
    org_id = context.get("org_id", "org123")
    name = context.get("workspace_name", "Acme Team")
    results[step] = await create_workspace(state, org_id, name)

async def _assign_role(state, context, results, step):
    user_id = context.get("target_user_id", "user456")
    org_id = context.get("org_id", "org123")
    role = context.get("role", "marketer")
    results[step] = await assign_role(state, user_id, org_id, role)

async def _generate_api_key(state, context, results, step):
    org_id = context.get("org_id", "org123")
    results[step] = await generate_api_key(state, org_id, ["read", "write"])

async def _create_webhook(state, context, results, step):
    org_id = context.get("org_id", "org123")
    url = context.get("webhook_url", "https://app.example.com/webhook")
    results[step] = await create_webhook(state, org_id, url, ["campaign.completed"])

async def _validate_policy(state, context, results, step):
    org_id = context.get("org_id", "org123")
    results[step] = await validate_policy(state, org_id, "sending", {})

async def _log_audit_event(state, context, results, step):
    org_id = context.get("org_id", "org123")
    user_id = state.get("user_id", "anon")
    action = context.get("audit_action", "view_campaign")
    results[step] = await log_audit_event(state, org_id, user_id, action)

TOOL_REGISTRY = {
    "search_leads": _search_leads,
    "enrich_lead": _enrich_lead,
    "score_lead": _score_lead,
    "generate_email": _generate_email,
    "create_campaign": _create_campaign,
    "send_email": _send_email,
    "fetch_replies": _fetch_replies,
    "classify_reply": _classify_reply,
    "get_metrics": _get_metrics,
    "track_event": _track_event,
    "run_recipe": _run_recipe,
    "execute_step": _execute_step,
    "schedule_job": _schedule_job,
    "retry_job": _retry_job,
    "search_domain_hiring": _search_domain_hiring,
    "search_domain_local": _search_domain_local,
    "search_domain_website": _search_domain_website,
    "detect_signal": _detect_signal,
    "merge_lead_data": _merge_lead_data,
    "index_search_data": _index_search_data,
    "check_reputation": _check_reputation,
    "warmup_domain": _warmup_domain,
    "detect_abuse": _detect_abuse,
    "track_email_event": _track_email_event,
    "enforce_limit": _enforce_limit,
    "rotate_proxy": _rotate_proxy,
    "run_ab_test": _run_ab_test,
    "analyze_performance": _analyze_performance,
    "generate_recommendation": _generate_recommendation,
    "store_learning": _store_learning,
    "fetch_strategy": _fetch_strategy,
    "optimize_sequence": _optimize_sequence,
    "create_workspace": _create_workspace,
    "assign_role": _assign_role,
    "generate_api_key": _generate_api_key,
    "create_webhook": _create_webhook,
    "validate_policy": _validate_policy,
    "log_audit_event": _log_audit_event,
}

class ExecutorNode:
    async def __call__(self, state: AgentState) -> Dict[str, Any]:
        steps = state.get("steps", [])
        idx = state.get("current_step_index", 0)
        context = state.get("context", {})
        results = state.get("results", {})
        
        if idx >= len(steps):
            return {"status": "completed"}
            
        step = steps[idx]
        
        handler = TOOL_REGISTRY.get(step)
        if not handler:
            return {"status": "failed", "error": f"Unknown step: {step}"}
            
        try:
            handler_result = await handler(state, context, results, step)
            # Check if handler explicitly requested a pause (e.g. human in the loop)
            if handler_result and isinstance(handler_result, dict) and handler_result.get("status") == "paused":
                return handler_result
                
            return {
                "current_step_index": idx + 1,
                "context": context,
                "results": results
            }
        except Exception as e:
            return {"status": "failed", "error": f"Execution failed at '{step}': {str(e)}"}

def should_continue(state: AgentState) -> str:
    if state.get("status") in ["failed", "completed", "paused"]:
        return "end"
    if state.get("current_step_index", 0) >= len(state.get("steps", [])):
        return "end"
    return "execute"
