export default function CommandCenterPage() {
  return (
    <div className="max-w-container-max mx-auto flex flex-col gap-stack-lg p-margin-page">
      {/* Header */}
      <div>
        <h1 className="font-display-xl text-display-xl text-on-surface">Command Center</h1>
      </div>
      
      {/* Top Section: Recipes & Quick Start (Bento-ish) */}
      <section className="grid grid-cols-1 lg:grid-cols-3 gap-gutter">
        {/* Primary Action Card */}
        <div className="bg-surface-container-lowest border border-outline-variant rounded p-stack-lg shadow-sm flex flex-col justify-between col-span-1 lg:col-span-1 relative overflow-hidden">
          <div className="absolute -right-10 -top-10 w-40 h-40 bg-secondary-container/10 rounded-full blur-2xl pointer-events-none"></div>
          <div>
            <h3 className="font-heading-md text-heading-md text-on-surface mb-2">Automate Outreach</h3>
            <p className="font-body-sm text-body-sm text-on-surface-variant mb-6">Deploy high-converting sequences instantly based on your industry benchmarks.</p>
          </div>
          <button className="w-full bg-secondary text-on-secondary font-body-base text-body-base font-semibold py-3 rounded hover:bg-on-secondary-fixed-variant transition-colors flex items-center justify-center gap-2 shadow-[inset_0_-1px_0_rgba(0,0,0,0.2)]">
            <span className="material-symbols-outlined">rocket_launch</span>
            Start New Campaign
          </button>
        </div>
        
        {/* Suggested Recipes List */}
        <div className="bg-surface-container-lowest border border-outline-variant rounded p-stack-lg shadow-sm col-span-1 lg:col-span-2 flex flex-col">
          <div className="flex justify-between items-center mb-4 pb-2 border-b border-surface-container-high">
            <h3 className="font-heading-md text-heading-md text-on-surface">Suggested Recipes</h3>
            <a className="text-secondary font-body-sm text-body-sm font-semibold hover:underline" href="#">View All</a>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 flex-1">
            <div className="group border border-surface-container-high rounded p-4 hover:border-secondary hover:bg-surface-container-low transition-colors cursor-pointer flex items-start gap-4">
              <div className="w-10 h-10 rounded bg-primary-fixed flex items-center justify-center text-on-primary-fixed shrink-0">
                <span className="material-symbols-outlined">engineering</span>
              </div>
              <div>
                <h4 className="font-body-base text-body-base font-semibold text-on-surface group-hover:text-secondary transition-colors">SaaS Founder Warm-Up</h4>
                <p className="font-body-sm text-body-sm text-outline mt-1 line-clamp-2">Multi-channel touch sequence designed for B2B tech founders.</p>
              </div>
            </div>
            <div className="group border border-surface-container-high rounded p-4 hover:border-secondary hover:bg-surface-container-low transition-colors cursor-pointer flex items-start gap-4">
              <div className="w-10 h-10 rounded bg-tertiary-fixed flex items-center justify-center text-on-tertiary-fixed shrink-0">
                <span className="material-symbols-outlined">local_hospital</span>
              </div>
              <div>
                <h4 className="font-body-base text-body-base font-semibold text-on-surface group-hover:text-secondary transition-colors">Healthcare Enterprise Pitch</h4>
                <p className="font-body-sm text-body-sm text-outline mt-1 line-clamp-2">Compliance-first outreach pattern with high trust signals.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Middle & Right Section: Metrics & Urgent Actions */}
      <section className="grid grid-cols-1 lg:grid-cols-3 gap-gutter">
        {/* Metrics Cards (Left Span) */}
        <div className="lg:col-span-2 grid grid-cols-1 md:grid-cols-2 gap-gutter">
          {/* Metric 1 */}
          <div className="bg-surface-container-lowest border border-outline-variant rounded p-stack-lg shadow-sm flex flex-col">
            <div className="flex items-center justify-between mb-4">
              <span className="font-body-sm text-body-sm font-semibold text-on-surface-variant uppercase tracking-wider">Leads Found Today</span>
              <span className="material-symbols-outlined text-outline-variant">person_search</span>
            </div>
            <div className="flex items-end gap-3">
              <span className="font-metric-lg text-metric-lg text-on-surface">1,248</span>
              <span className="font-body-sm text-body-sm text-on-tertiary-container bg-tertiary-fixed-dim/20 px-2 py-0.5 rounded font-medium mb-1">+12%</span>
            </div>
          </div>
          {/* Metric 2 */}
          <div className="bg-surface-container-lowest border border-outline-variant rounded p-stack-lg shadow-sm flex flex-col">
            <div className="flex items-center justify-between mb-4">
              <span className="font-body-sm text-body-sm font-semibold text-on-surface-variant uppercase tracking-wider">Emails Sent</span>
              <span className="material-symbols-outlined text-outline-variant">forward_to_inbox</span>
            </div>
            <div className="flex items-end gap-3">
              <span className="font-metric-lg text-metric-lg text-on-surface">8,902</span>
              <span className="font-body-sm text-body-sm text-on-surface-variant mb-1">this week</span>
            </div>
          </div>
          {/* Metric 3 */}
          <div className="bg-surface-container-lowest border border-outline-variant rounded p-stack-lg shadow-sm flex flex-col">
            <div className="flex items-center justify-between mb-4">
              <span className="font-body-sm text-body-sm font-semibold text-on-surface-variant uppercase tracking-wider">Replies Received</span>
              <span className="material-symbols-outlined text-outline-variant">forum</span>
            </div>
            <div className="flex items-end gap-3">
              <span className="font-metric-lg text-metric-lg text-on-surface">342</span>
              <span className="font-body-sm text-body-sm text-on-tertiary-container bg-tertiary-fixed-dim/20 px-2 py-0.5 rounded font-medium mb-1">4.2% rate</span>
            </div>
          </div>
          {/* Metric 4 */}
          <div className="bg-surface-container-lowest border border-outline-variant rounded p-stack-lg shadow-sm flex flex-col border-l-4 border-l-tertiary-fixed-dim">
            <div className="flex items-center justify-between mb-4">
              <span className="font-body-sm text-body-sm font-semibold text-on-surface-variant uppercase tracking-wider">Interested Leads</span>
              <span className="material-symbols-outlined text-tertiary-fixed-dim">verified</span>
            </div>
            <div className="flex items-end gap-3">
              <span className="font-metric-lg text-metric-lg text-on-surface">89</span>
              <span className="font-body-sm text-body-sm text-on-surface-variant mb-1">awaiting action</span>
            </div>
          </div>
        </div>

        {/* Urgent Actions Sidebar */}
        <div className="lg:col-span-1 bg-surface-container-lowest border border-error/20 rounded p-stack-lg shadow-sm flex flex-col">
          <div className="flex items-center gap-2 mb-6 pb-2 border-b border-surface-container-high">
            <span className="material-symbols-outlined text-error">warning</span>
            <h3 className="font-heading-md text-heading-md text-on-surface">Urgent Actions</h3>
          </div>
          <div className="flex flex-col gap-4">
            <div className="group flex items-start gap-3 cursor-pointer hover:bg-surface-container-low p-2 -mx-2 rounded transition-colors">
              <div className="w-2 h-2 rounded-full bg-error mt-2 shrink-0"></div>
              <div className="flex-1">
                <p className="font-body-base text-body-base font-semibold text-on-surface">5 leads need follow-up</p>
                <p className="font-body-sm text-body-sm text-outline">SLA breached. Contact immediately.</p>
              </div>
              <span className="material-symbols-outlined text-outline-variant group-hover:text-secondary opacity-0 group-hover:opacity-100 transition-all">chevron_right</span>
            </div>
            <div className="group flex items-start gap-3 cursor-pointer hover:bg-surface-container-low p-2 -mx-2 rounded transition-colors">
              <div className="w-2 h-2 rounded-full bg-[#f59e0b] mt-2 shrink-0"></div>
              <div className="flex-1">
                <p className="font-body-base text-body-base font-semibold text-on-surface">2 replies need response</p>
                <p className="font-body-sm text-body-sm text-outline">From 'Enterprise Q3' campaign.</p>
              </div>
              <span className="material-symbols-outlined text-outline-variant group-hover:text-secondary opacity-0 group-hover:opacity-100 transition-all">chevron_right</span>
            </div>
            <div className="group flex items-start gap-3 cursor-pointer hover:bg-surface-container-low p-2 -mx-2 rounded transition-colors">
              <div className="w-2 h-2 rounded-full bg-tertiary-fixed-dim mt-2 shrink-0"></div>
              <div className="flex-1">
                <p className="font-body-base text-body-base font-semibold text-on-surface">3 high-quality leads waiting</p>
                <p className="font-body-sm text-body-sm text-outline">Manual review requested.</p>
              </div>
              <span className="material-symbols-outlined text-outline-variant group-hover:text-secondary opacity-0 group-hover:opacity-100 transition-all">chevron_right</span>
            </div>
          </div>
        </div>
      </section>

      {/* Bottom Section: Pipeline Snapshot */}
      <section className="bg-surface-container-lowest border border-outline-variant rounded p-stack-lg shadow-sm">
        <h3 className="font-heading-md text-heading-md text-on-surface mb-6">Pipeline Snapshot</h3>
        <div className="flex flex-col md:flex-row items-center justify-between gap-4">
          {/* Stage 1 */}
          <div className="flex-1 w-full bg-surface-container-low border border-outline-variant rounded p-4 text-center">
            <span className="font-label-caps text-label-caps text-on-surface-variant block mb-2">New</span>
            <span className="font-metric-lg text-metric-lg text-on-surface">1,420</span>
          </div>
          <span className="material-symbols-outlined text-outline-variant hidden md:block">arrow_forward</span>
          {/* Stage 2 */}
          <div className="flex-1 w-full bg-surface-container-low border border-outline-variant rounded p-4 text-center">
            <span className="font-label-caps text-label-caps text-on-surface-variant block mb-2">Contacted</span>
            <span className="font-metric-lg text-metric-lg text-on-surface">890</span>
          </div>
          <span className="material-symbols-outlined text-outline-variant hidden md:block">arrow_forward</span>
          {/* Stage 3 */}
          <div className="flex-1 w-full bg-primary-fixed border border-primary-fixed-dim rounded p-4 text-center">
            <span className="font-label-caps text-label-caps text-on-primary-fixed-variant block mb-2">Replied</span>
            <span className="font-metric-lg text-metric-lg text-on-primary-fixed">342</span>
          </div>
          <span className="material-symbols-outlined text-outline-variant hidden md:block">arrow_forward</span>
          {/* Stage 4 */}
          <div className="flex-1 w-full bg-tertiary-fixed-dim/20 border border-tertiary-fixed-dim/50 rounded p-4 text-center">
            <span className="font-label-caps text-label-caps text-on-tertiary-fixed block mb-2">Closed</span>
            <span className="font-metric-lg text-metric-lg text-on-tertiary-fixed">45</span>
          </div>
        </div>
      </section>
    </div>
  );
}
