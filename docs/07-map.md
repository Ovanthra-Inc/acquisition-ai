# 🧠 Mental Model (Keep in mind)

Every UI action =

👉 **UI → BFF → API Gateway → Service → Agent → Tool → Result**

---

# 🏠 1. DASHBOARD (HOME)

## 🔥 Run Recipe (CTA)

### Features Used:

* Recipe execution
* Lead generation
* Campaign trigger

### Services:

* Recipe Service
* Agent/Workflow Service
* Lead Service
* Campaign Service

### Agents:

* Master Agent
* Planner Agent
* Execution Agent
* Lead Finder Agent
* Email Generation Agent

### Tools:

* `run_recipe`
* `search_leads`
* `generate_email`
* `create_campaign`

### Recipes:

* SaaS Outreach
* Growth Gap Finder
* Hiring Conversion

---

---

## 📊 Metrics (Cards)

### Features:

* Performance tracking

### Services:

* Analytics Service
* Event Tracking Service

### Agents:

* Metrics Agent
* Insight Agent

### Tools:

* `get_metrics`
* `analyze_performance`

---

---

## ⚡ Action Items

(“Leads need follow-up”, “Replies pending”)

### Features:

* Task detection
* Follow-up alerts

### Services:

* Campaign Service
* Conversation Service
* Notification Service

### Agents:

* Follow-up Scheduler Agent
* Reply Detection Agent

### Tools:

* `fetch_replies`
* `schedule_followup`

---

---

# 📌 SIDEBAR MAPPING

---

# 1. 🏠 Dashboard

👉 Same as above (overview layer)

---

# 2. 🤖 Agent (Chatbot)

### Features:

* Natural language control
* Agent execution

### Services:

* AI Service
* Agent Service
* Context Service

### Agents:

* Chat Assistant Agent
* Master Agent
* Planner Agent

### Tools:

* ALL tools (this is universal interface)

### Recipes:

* Dynamically selected based on user prompt

---

---

# 3. 🧩 Recipes ⭐ (CORE)

### Features:

* View recipes
* Create/edit recipes
* Run recipes

### Services:

* Recipe Service
* Agent Service

### Agents:

* Planner Agent
* Execution Agent

### Tools:

* `get_recipe_steps`
* `run_recipe`
* `execute_step`

### Recipes:

* ALL recipes live here

---

---

# 4. 🔍 Leads

### Features:

* Lead viewing
* Filtering
* Lead insights

### Services:

* Lead Service
* Enrichment Service

### Agents:

* Lead Analyzer Agent
* Lead Scoring Agent

### Tools:

* `enrich_lead`
* `score_lead`
* `match_icp`

### Recipes:

* Output of recipes (this is result layer)

---

---

# 5. 📩 Campaigns

### Features:

* Email sequences
* Follow-ups
* Campaign tracking

### Services:

* Campaign Service
* Email Service

### Agents:

* Campaign Agent
* Sending Agent
* Deliverability Agent

### Tools:

* `create_campaign`
* `send_email`
* `schedule_followup`

### Recipes:

* Triggered from recipes

---

---

# 6. 💬 Conversations

### Features:

* Inbox
* Reply handling
* AI replies

### Services:

* Conversation Service
* AI Service

### Agents:

* Reply Detection Agent
* Reply Classification Agent
* Reply Generation Agent

### Tools:

* `fetch_replies`
* `classify_reply`
* `generate_reply`

### Recipes:

* Follow-up / conversion recipes

---

---

# 7. 📊 Pipeline (CRM)

### Features:

* Deal tracking
* Stage movement

### Services:

* Pipeline Service
* Lead Service

### Agents:

* Deal Tracking Agent
* Conversion Agent

### Tools:

* `update_lead_status`
* `update_deal_stage`

### Recipes:

* Conversion recipes

---

---

# 8. 📈 Analytics

### Features:

* Metrics
* Insights
* Optimization

### Services:

* Analytics Service
* Event Tracking Service

### Agents:

* Metrics Agent
* Insight Agent
* Optimization Agent

### Tools:

* `get_metrics`
* `analyze_performance`

### Recipes:

* Optimization recipes

---

---

# 9. ⚙️ Settings

### Features:

* Profile
* Email integration
* Limits

### Services:

* Auth Service
* User Service
* Integration Service
* Billing Service

### Agents:

* Context Agent

### Tools:

* `get_user_profile`
* `connect_email_account`

---

---

# 🔝 NAVBAR MAPPING

---

## 🔍 Search

### Features:

* Global search

### Services:

* Lead Service
* Campaign Service

### Tools:

* `search_leads`

---

---

## 🔔 Notifications

### Features:

* Alerts

### Services:

* Notification Service

### Agents:

* Notification Agent

### Tools:

* `send_notification`

---

---

## ⚡ Quick Actions (Run Recipe)

👉 Same as Dashboard CTA

---

---

## 👤 Profile

### Features:

* Account
* Billing

### Services:

* Auth
* User
* Billing

---

---

# 🔄 COMPLETE FLOW EXAMPLE

---

User clicks:
👉 “Run Recipe”

---

### Flow:

1. UI → BFF
2. BFF → API Gateway
3. Gateway → Recipe Service
4. Recipe → Agent Service

---

### Agent Flow:

* Master Agent
* Planner Agent
* Execution Agent

---

### Execution:

* Lead Finder Agent → `search_leads`
* Enrichment → `enrich_lead`
* AI → `generate_email`
* Campaign → `send_email`

---

### Async:

* Queue handles jobs
* Scheduler handles follow-ups

---

---

# 🧠 FINAL SYSTEM MAP (SIMPLE)

---

### UI Layer

Dashboard / Recipes / Chat

---

### Control Layer

BFF + API Gateway

---

### Brain Layer

Agents + AI Service

---

### Execution Layer

Lead / Campaign / Email services

---

### Data Layer

DB + Redis

---

---

# 🔥 Final Insight

Your strongest UX =

👉 **Everything can be done via:**

* UI (buttons)
* OR chatbot (agent)