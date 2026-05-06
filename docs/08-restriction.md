# 🧠 0. Core Principles (Non-Negotiable)

Every service must follow:

### 1. Single Responsibility

* One service = one domain

### 2. No Direct DB Sharing

* Services communicate via APIs/events only

### 3. Zero Trust Between Services

* Every request is authenticated + authorized

### 4. Async First

* Long tasks → queue

### 5. Rate Limited Everywhere

* Gateway + service-level protection

---

# 🌐 1. API GATEWAY SERVICE

## 🎯 Responsibility

* Single entry point for all clients

## 🔐 Security

* JWT validation
* API key validation (for integrations)
* IP filtering / geo rules

## ⚡ Control

* Global rate limiting (per user / IP / tier)
* Request validation
* Request size limits

## 🔄 Routing

* Route to correct microservice
* Versioning (/v1, /v2)

## 🚫 MUST NOT

* No business logic
* No DB access

---

# 🎯 2. BFF (Backend for Frontend)

## 🎯 Responsibility

* Shape data for UI
* Aggregate multiple services

## 🧠 Logic

* UI-specific transformations
* Combine:

  * leads + campaigns + analytics

## 🔐 Security

* Forward user context
* Never trust frontend directly

## 🚫 MUST NOT

* No core business logic
* No direct DB writes

---

# 🌐 3. NGINX PROXY

## 🎯 Responsibility

* Reverse proxy
* SSL termination
* Load balancing

## ⚡ Performance

* Caching (static assets)
* Compression

## 🔐 Security

* Basic DDoS protection
* Connection limits

---

# 🔐 4. AUTH SERVICE

## 🎯 Responsibility

* Authentication + identity

## Features:

* Login / Signup
* JWT issuing + refresh tokens
* OAuth (Google etc.)

## 🔐 Security:

* Password hashing (bcrypt/argon2)
* Token expiration + rotation
* Device/session tracking

## 🚫 MUST NOT

* No business logic
* No user profile data beyond auth

---

# 👤 5. USER / WORKSPACE SERVICE

## 🎯 Responsibility

* User profile
* Organizations / teams
* Roles & permissions

## 🔐 Security

* RBAC (role-based access control)
* Tenant isolation

## ⚡ Features

* User settings
* Preferences
* Team invites

---

# 💰 6. BILLING / TIER SERVICE

## 🎯 Responsibility

* Subscription management
* Usage tracking

## ⚡ Features

* Plan limits:

  * leads/month
  * emails/day
* Credit system

## 🔐 Enforcement

* Hard limits (block API calls)
* Soft limits (warnings)

---

# 🔍 7. LEAD SERVICE

## 🎯 Responsibility

* Source of truth for leads

## Features:

* Store leads
* Filter/search leads
* Tagging

## 🔐 Rules:

* Tenant isolation (no cross-user data)
* Input validation (avoid garbage data)

## 🚫 MUST NOT

* No scraping
* No AI logic

---

# 🧩 8. RECIPE SERVICE ⭐

## 🎯 Responsibility

* Define workflows (recipes)

## Features:

* Store recipe configs
* Manage steps

## 🔐 Rules:

* Validate recipe structure
* Prevent unsafe workflows

## 🚫 MUST NOT

* No execution logic

---

# 🤖 9. AGENT / WORKFLOW SERVICE ⭐

## 🎯 Responsibility

* Orchestrate execution

## Features:

* Plan → execute → monitor
* Call tools/services

## 🔐 Safety:

* Step limits (prevent infinite loops)
* Execution timeout
* Permission checks before actions

---

# 🧠 10. AI SERVICE

## 🎯 Responsibility

* Central LLM layer

## Features:

* Prompt templates
* Email generation
* Intent parsing

## 🔐 Controls:

* Token limits
* Cost tracking per user
* Prompt sanitization

---

# ⚙️ 11. ENRICHMENT SERVICE

## 🎯 Responsibility

* Enhance lead data

## Features:

* Company info
* Metadata extraction

## 🔐 Rules:

* Validate external data
* Rate limit external APIs

---

# 🕷️ 12. SCRAPER SERVICE

## 🎯 Responsibility

* Data collection

## Features:

* Crawl websites
* Extract content

## 🔐 Safety:

* Respect robots.txt
* Rate limiting per domain
* Proxy rotation

---

# 📩 13. CAMPAIGN SERVICE

## 🎯 Responsibility

* Manage outreach logic

## Features:

* Campaigns
* Sequences
* Follow-ups

## 🔐 Rules:

* Enforce sending limits
* Prevent spam bursts

---

# 📬 14. EMAIL SERVICE

## 🎯 Responsibility

* Email delivery layer

## Features:

* Send emails
* Track status

## 🔐 Deliverability:

* Domain warmup
* Bounce handling
* Spam detection

---

# 💬 15. CONVERSATION SERVICE

## 🎯 Responsibility

* Manage replies

## Features:

* Store threads
* Fetch replies

## 🔐 Rules:

* Thread integrity
* Deduplication

---

# 📊 16. PIPELINE SERVICE

## 🎯 Responsibility

* Deal tracking

## Features:

* Stages
* Status updates

---

# 📈 17. ANALYTICS SERVICE

## 🎯 Responsibility

* Metrics + insights

## Features:

* Track:

  * opens
  * replies
  * conversions

---

# 🔔 18. NOTIFICATION SERVICE

## 🎯 Responsibility

* User alerts

## Features:

* In-app notifications
* Email alerts

---

# 🔄 19. QUEUE / WORKER SERVICE

## 🎯 Responsibility

* Async execution

## Features:

* Job queue
* Retry mechanism
* Dead letter queue

---

# ⏱️ 20. SCHEDULER SERVICE

## 🎯 Responsibility

* Time-based tasks

## Features:

* Follow-ups
* recurring recipes

---

# 🔌 21. INTEGRATION SERVICE

## 🎯 Responsibility

* External APIs

## Features:

* Gmail
* Data providers

## 🔐 Rules:

* Token encryption
* API retry logic

---

# 🛡️ 22. SECURITY / ABUSE SERVICE

## 🎯 Responsibility

* Protect system

## Features:

* Spam detection
* Abuse monitoring
* anomaly detection

---

# 📊 23. LOGGING & MONITORING

## 🎯 Responsibility

* Observability

## Features:

* Logs
* Metrics
* Alerts

---

# 🧠 FINAL SYSTEM GOVERNANCE

---

## 🔐 Security Layers:

* Gateway → Auth → Service-level validation

---

## ⚡ Rate Limiting:

* Gateway level (global)
* Service level (critical endpoints)

---

## 🔄 Data Flow:

* Sync → lightweight
* Async → heavy workflows

---

## 🧩 Ownership Clarity:

* Each service owns:

  * its DB
  * its logic
  * its API

---

# ⚠️ FINAL WARNING

If you violate:

* service boundaries
* security rules
* async separation

👉 system will break at scale