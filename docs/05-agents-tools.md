# 🧠 1. Tool Design Principle

Every tool should be:

* Atomic (one job)
* Reusable
* Stateless (as much as possible)
* Backed by a service/API

---

# 🧩 2. COMPLETE TOOL LIST (Grouped Properly)

---

# 🔍 A. LEAD DISCOVERY TOOLS

---

## 1. `search_leads`

* Input:

  * keyword
  * domain (websites/local/etc.)
* Output:

  * list of potential leads

---

## 2. `crawl_website`

* Input:

  * URL
* Output:

  * raw HTML / text content

---

## 3. `extract_contact_info`

* Input:

  * website content
* Output:

  * emails
  * phone
  * social links

---

## 4. `get_company_data`

* Input:

  * domain
* Output:

  * company name
  * description
  * industry

---

---

# 🧠 B. ENRICHMENT & INTELLIGENCE TOOLS

---

## 5. `enrich_lead`

* Adds:

  * company size
  * type
  * metadata

---

## 6. `analyze_website`

* Extract:

  * product type
  * features
  * positioning

---

## 7. `detect_pain_points`

* Output:

  * potential problems
  * opportunities

---

## 8. `score_lead`

* Output:

  * score (0–100)
  * label (high/medium/low)

---

## 9. `match_icp`

* Matches:

  * lead vs user profile

---

---

# ✍️ C. PERSONALIZATION TOOLS

---

## 10. `generate_email`

* Input:

  * lead data
  * user profile
* Output:

  * personalized email

---

## 11. `generate_followup`

* Input:

  * previous message
  * context
* Output:

  * follow-up message

---

## 12. `generate_subject_line`

* Output:

  * optimized subject

---

## 13. `select_message_strategy`

* Output:

  * problem-based / value-based / insight-based

---

---

# 📩 D. CAMPAIGN & OUTREACH TOOLS

---

## 14. `create_campaign`

* Creates campaign object

---

## 15. `add_leads_to_campaign`

* Assign leads

---

## 16. `schedule_email`

* Schedule sending

---

## 17. `send_email`

* Actually send email

---

## 18. `schedule_followup`

* Add follow-up step

---

---

# 📬 E. EMAIL INFRASTRUCTURE TOOLS

---

## 19. `validate_email`

* Check if email is valid

---

## 20. `check_deliverability`

* Spam risk

---

## 21. `rotate_domain`

* Switch sending domain

---

## 22. `track_email_event`

* open / click / bounce

---

---

# 💬 F. CONVERSATION TOOLS

---

## 23. `fetch_replies`

* Get incoming replies

---

## 24. `classify_reply`

* interested / not now / etc.

---

## 25. `generate_reply`

* Draft response

---

## 26. `update_conversation`

* Store thread

---

---

# 📊 G. PIPELINE / CRM TOOLS

---

## 27. `update_lead_status`

* Move lead in pipeline

---

## 28. `create_deal`

* Create opportunity

---

## 29. `update_deal_stage`

* Move deal stage

---

## 30. `add_note`

* Add notes/logs

---

---

# 🔄 H. WORKFLOW / AUTOMATION TOOLS

---

## 31. `run_recipe`

* Trigger workflow

---

## 32. `get_recipe_steps`

* Retrieve steps

---

## 33. `execute_step`

* Execute one step

---

## 34. `schedule_job`

* Add to queue

---

## 35. `retry_job`

* Retry failed job

---

---

# 🔔 I. NOTIFICATION TOOLS

---

## 36. `send_notification`

* In-app alert

---

## 37. `send_email_notification`

* Notify user

---

---

# 👤 J. USER CONTEXT TOOLS

---

## 38. `get_user_profile`

* Fetch onboarding data

---

## 39. `update_user_settings`

* Save preferences

---

## 40. `get_user_limits`

* Plan/tier limits

---

---

# 📈 K. ANALYTICS TOOLS

---

## 41. `track_event`

* Log user/system action

---

## 42. `get_metrics`

* Campaign performance

---

## 43. `analyze_performance`

* Suggest improvements

---

---

# 🔌 L. INTEGRATION TOOLS

---

## 44. `connect_email_account`

* Gmail integration

---

## 45. `fetch_external_data`

* APIs (future sources)

---

---

# 🧠 3. Tool Flow Example (Real Execution)

User:

> “Get me SaaS leads and contact them”

---

### Tools used:

1. `search_leads`
2. `crawl_website`
3. `extract_contact_info`
4. `enrich_lead`
5. `score_lead`
6. `generate_email`
7. `create_campaign`
8. `send_email`
9. `schedule_followup`

---

---

# ⚠️ 4. Reality Check

You don’t need 45 tools on day 1.

---

# 🚀 5. Starter Tool Set (Build First)

Start with:

* `search_leads`
* `crawl_website`
* `extract_contact_info`
* `enrich_lead`
* `generate_email`
* `send_email`
* `fetch_replies`
* `classify_reply`

---

👉 This is enough for a working system.

---

# 🔥 6. Critical Insight

Your success depends on:

👉 Tool quality, not quantity

---

# 🧠 Final Mental Model

* Agents = decision makers
* Tools = execution layer
* Services = infrastructure