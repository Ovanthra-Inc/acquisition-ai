export default function CampaignsPage() {
  return (
    <div className="flex flex-col h-full w-full p-margin-page">
      <div className="max-w-container-max mx-auto space-y-stack-lg w-full">
        {/* Header Section */}
        <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-stack-sm">
          <div>
            <h2 className="font-display-xl text-display-xl text-on-surface">Active Campaigns</h2>
            <p className="font-body-base text-body-base text-on-surface-variant mt-1">Manage and monitor your outreach execution.</p>
          </div>
          <div className="flex gap-2">
            <button className="flex items-center gap-2 px-4 py-2 text-sm font-semibold text-on-surface bg-surface-container-lowest border border-outline-variant rounded-lg hover:bg-surface-container-high transition-colors">
              <span className="material-symbols-outlined text-[18px]">filter_list</span>
              Filter
            </button>
            <button className="flex items-center gap-2 px-4 py-2 text-sm font-semibold text-on-secondary bg-secondary rounded-lg hover:bg-on-secondary-fixed-variant transition-colors shadow-[0_1px_2px_rgba(0,0,0,0.1),inset_0_-1px_0_rgba(0,0,0,0.1)]">
              <span className="material-symbols-outlined text-[18px]">add</span>
              New Campaign
            </button>
          </div>
        </div>

        {/* Bento Grid for Campaigns */}
        <div className="grid grid-cols-1 xl:grid-cols-2 gap-gutter">
          {/* Campaign Card 1 */}
          <div className="bg-surface-container-lowest rounded-xl border border-outline-variant shadow-sm overflow-hidden flex flex-col">
            {/* Card Header */}
            <div className="p-stack-md border-b border-surface-container-highest flex justify-between items-center bg-surface-bright">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-lg bg-secondary-container/10 flex items-center justify-center text-secondary">
                  <span className="material-symbols-outlined fill-icon" style={{ fontVariationSettings: "'FILL' 1" }}>mail</span>
                </div>
                <div>
                  <h3 className="font-heading-md text-[18px] text-on-surface leading-snug">Q3 Enterprise Outreach</h3>
                  <div className="flex items-center gap-2 text-xs text-on-surface-variant mt-0.5">
                    <span className="flex items-center gap-1 text-on-tertiary-container bg-tertiary-fixed-dim/20 px-2 py-0.5 rounded-full font-semibold">
                      <span className="w-1.5 h-1.5 rounded-full bg-on-tertiary-container"></span>
                      Active
                    </span>
                    <span>• Started Sep 1</span>
                  </div>
                </div>
              </div>
              <div className="flex gap-1">
                <button className="p-1.5 text-on-surface-variant hover:text-secondary rounded-md hover:bg-surface-container-high transition-colors" title="Pause">
                  <span className="material-symbols-outlined text-[20px]">pause</span>
                </button>
                <button className="p-1.5 text-on-surface-variant hover:text-secondary rounded-md hover:bg-surface-container-high transition-colors" title="Edit">
                  <span className="material-symbols-outlined text-[20px]">edit</span>
                </button>
                <button className="p-1.5 text-on-surface-variant hover:text-secondary rounded-md hover:bg-surface-container-high transition-colors" title="More">
                  <span className="material-symbols-outlined text-[20px]">more_vert</span>
                </button>
              </div>
            </div>

            {/* Card Body - Metrics */}
            <div className="p-stack-md grid grid-cols-3 gap-4 bg-surface-container-lowest">
              <div className="flex flex-col">
                <span className="font-label-caps text-label-caps text-outline uppercase">Sent</span>
                <span className="font-metric-lg text-metric-lg text-on-surface">1,240</span>
              </div>
              <div className="flex flex-col border-l border-surface-container-highest pl-4">
                <span className="font-label-caps text-label-caps text-outline uppercase">Opened</span>
                <div className="flex items-baseline gap-2">
                  <span className="font-metric-lg text-metric-lg text-on-surface">862</span>
                  <span className="text-sm font-semibold text-on-tertiary-container">69%</span>
                </div>
              </div>
              <div className="flex flex-col border-l border-surface-container-highest pl-4">
                <span className="font-label-caps text-label-caps text-outline uppercase">Replied</span>
                <div className="flex items-baseline gap-2">
                  <span className="font-metric-lg text-metric-lg text-secondary">145</span>
                  <span className="text-sm font-semibold text-secondary">11%</span>
                </div>
              </div>
            </div>

            {/* Card Body - Sequence Visualizer */}
            <div className="p-stack-md pt-0 flex-1">
              <div className="bg-surface-container-low rounded-lg p-stack-sm flex items-center justify-between relative">
                {/* Sequence Line Background */}
                <div className="absolute left-6 right-6 top-1/2 -translate-y-1/2 h-0.5 bg-outline-variant/30 z-0"></div>
                {/* Steps */}
                <div className="relative z-10 flex flex-col items-center gap-1 group cursor-pointer">
                  <div className="w-8 h-8 rounded-full bg-secondary text-on-secondary flex items-center justify-center shadow-sm">
                    <span className="material-symbols-outlined text-[16px]">send</span>
                  </div>
                  <span className="text-[10px] font-semibold text-on-surface-variant">Step 1</span>
                </div>
                <div className="relative z-10 flex flex-col items-center gap-1 group cursor-pointer">
                  <span className="text-[10px] text-outline mb-1">Wait 3d</span>
                  <div className="w-8 h-8 rounded-full bg-surface-container-lowest border-2 border-secondary text-secondary flex items-center justify-center shadow-sm">
                    <span className="material-symbols-outlined text-[16px]">mark_email_read</span>
                  </div>
                  <span className="text-[10px] font-semibold text-on-surface-variant">Step 2</span>
                </div>
                <div className="relative z-10 flex flex-col items-center gap-1 group cursor-pointer">
                  <span className="text-[10px] text-outline mb-1">Wait 5d</span>
                  <div className="w-8 h-8 rounded-full bg-surface-container-highest border border-outline-variant text-outline flex items-center justify-center shadow-sm">
                    <span className="material-symbols-outlined text-[16px]">schedule</span>
                  </div>
                  <span className="text-[10px] font-semibold text-outline">Step 3</span>
                </div>
              </div>
            </div>
          </div>

          {/* Campaign Card 2 */}
          <div className="bg-surface-container-lowest rounded-xl border border-outline-variant shadow-sm overflow-hidden flex flex-col opacity-75">
            {/* Card Header */}
            <div className="p-stack-md border-b border-surface-container-highest flex justify-between items-center bg-surface-bright">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-lg bg-surface-container-highest flex items-center justify-center text-on-surface-variant">
                  <span className="material-symbols-outlined">pause_circle</span>
                </div>
                <div>
                  <h3 className="font-heading-md text-[18px] text-on-surface leading-snug">SaaS Founders Follow-up</h3>
                  <div className="flex items-center gap-2 text-xs text-on-surface-variant mt-0.5">
                    <span className="flex items-center gap-1 text-on-surface-variant bg-surface-container-high px-2 py-0.5 rounded-full font-semibold">
                      Paused
                    </span>
                    <span>• Last active Aug 28</span>
                  </div>
                </div>
              </div>
              <div className="flex gap-1">
                <button className="p-1.5 text-on-surface-variant hover:text-secondary rounded-md hover:bg-surface-container-high transition-colors" title="Resume">
                  <span className="material-symbols-outlined text-[20px]">play_arrow</span>
                </button>
                <button className="p-1.5 text-on-surface-variant hover:text-secondary rounded-md hover:bg-surface-container-high transition-colors" title="Edit">
                  <span className="material-symbols-outlined text-[20px]">edit</span>
                </button>
                <button className="p-1.5 text-on-surface-variant hover:text-secondary rounded-md hover:bg-surface-container-high transition-colors" title="More">
                  <span className="material-symbols-outlined text-[20px]">more_vert</span>
                </button>
              </div>
            </div>

            {/* Card Body - Metrics */}
            <div className="p-stack-md grid grid-cols-3 gap-4 bg-surface-container-lowest">
              <div className="flex flex-col">
                <span className="font-label-caps text-label-caps text-outline uppercase">Sent</span>
                <span className="font-metric-lg text-metric-lg text-on-surface">450</span>
              </div>
              <div className="flex flex-col border-l border-surface-container-highest pl-4">
                <span className="font-label-caps text-label-caps text-outline uppercase">Opened</span>
                <div className="flex items-baseline gap-2">
                  <span className="font-metric-lg text-metric-lg text-on-surface">210</span>
                  <span className="text-sm font-semibold text-on-surface-variant">46%</span>
                </div>
              </div>
              <div className="flex flex-col border-l border-surface-container-highest pl-4">
                <span className="font-label-caps text-label-caps text-outline uppercase">Replied</span>
                <div className="flex items-baseline gap-2">
                  <span className="font-metric-lg text-metric-lg text-on-surface">32</span>
                  <span className="text-sm font-semibold text-on-surface-variant">7%</span>
                </div>
              </div>
            </div>

            {/* Card Body - Sequence Visualizer */}
            <div className="p-stack-md pt-0 flex-1">
              <div className="bg-surface-container-low rounded-lg p-stack-sm flex items-center justify-between relative">
                {/* Sequence Line Background */}
                <div className="absolute left-6 right-6 top-1/2 -translate-y-1/2 h-0.5 bg-outline-variant/30 z-0"></div>
                {/* Steps */}
                <div className="relative z-10 flex flex-col items-center gap-1">
                  <div className="w-8 h-8 rounded-full bg-surface-container-highest text-on-surface-variant flex items-center justify-center shadow-sm">
                    <span className="material-symbols-outlined text-[16px]">send</span>
                  </div>
                  <span className="text-[10px] font-semibold text-on-surface-variant">Step 1</span>
                </div>
                <div className="relative z-10 flex flex-col items-center gap-1">
                  <span className="text-[10px] text-outline mb-1">Wait 2d</span>
                  <div className="w-8 h-8 rounded-full bg-surface-container-highest border border-outline-variant text-outline flex items-center justify-center shadow-sm">
                    <span className="material-symbols-outlined text-[16px]">schedule</span>
                  </div>
                  <span className="text-[10px] font-semibold text-outline">Step 2</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
