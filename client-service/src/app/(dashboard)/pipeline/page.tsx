export default function PipelinePage() {
  return (
    <div className="flex flex-col h-full w-full">
      {/* Pipeline Header & Actions */}
      <div className="px-margin-page py-stack-lg border-b border-surface-variant bg-surface-container-lowest">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 max-w-container-max mx-auto w-full">
          <div>
            <h2 className="font-display-xl text-display-xl text-on-surface">Sales Pipeline</h2>
            <p className="font-body-base text-body-base text-on-surface-variant mt-1">Manage and track your active deals across all stages.</p>
          </div>
          <div className="flex items-center gap-3">
            <div className="flex bg-surface-container-low rounded-lg p-1">
              <button className="px-3 py-1.5 rounded bg-surface-container-lowest text-on-surface shadow-sm font-label-caps text-label-caps">List</button>
              <button className="px-3 py-1.5 rounded text-on-surface-variant hover:text-on-surface font-label-caps text-label-caps">Board</button>
            </div>
            <button className="bg-secondary text-on-secondary px-4 py-2 rounded-lg font-label-caps text-label-caps flex items-center gap-2 hover:bg-secondary/90 transition-colors shadow-[inset_0_-1px_0_0_rgba(0,0,0,0.1)]">
              <span className="material-symbols-outlined text-[18px]">add</span>
              Add Deal
            </button>
          </div>
        </div>

        {/* Quick Filters */}
        <div className="flex gap-2 mt-stack-md overflow-x-auto pb-2 -mb-2 no-scrollbar max-w-container-max mx-auto w-full">
          <button className="border border-outline-variant bg-surface-container-lowest text-on-surface px-3 py-1 rounded-full font-body-sm text-body-sm whitespace-nowrap hover:bg-surface-container-low">All Deals</button>
          <button className="border border-transparent bg-secondary-fixed text-on-secondary-fixed px-3 py-1 rounded-full font-body-sm text-body-sm whitespace-nowrap">My Deals</button>
          <button className="border border-outline-variant bg-surface-container-lowest text-on-surface px-3 py-1 rounded-full font-body-sm text-body-sm whitespace-nowrap hover:bg-surface-container-low">High Value</button>
        </div>
      </div>

      {/* Kanban Board */}
      <div className="flex-1 overflow-x-auto overflow-y-hidden bg-background p-margin-page">
        <div className="flex gap-gutter h-full min-w-max pb-4 max-w-container-max mx-auto">
          {/* Stage: New */}
          <div className="w-[300px] flex flex-col bg-surface-container-low rounded-xl p-3 flex-shrink-0">
            <div className="flex items-center justify-between px-2 mb-3">
              <div className="flex items-center gap-2">
                <h3 className="font-heading-md text-heading-md text-on-surface">New</h3>
                <span className="bg-surface-variant text-on-surface-variant px-2 py-0.5 rounded-full font-label-caps text-label-caps">3</span>
              </div>
              <span className="font-body-sm text-body-sm text-on-surface-variant font-medium">$45k</span>
            </div>
            <div className="flex-1 overflow-y-auto kanban-col flex flex-col gap-3 pr-1">
              {/* Card 1 */}
              <div className="bg-surface-container-lowest rounded-lg p-4 border border-outline-variant/50 shadow-sm cursor-grab hover:border-secondary/50 transition-colors">
                <div className="flex justify-between items-start mb-2">
                  <span className="text-[10px] font-bold tracking-wider text-on-surface-variant uppercase bg-surface-container-high px-2 py-1 rounded">Inbound</span>
                  <button className="text-outline-variant hover:text-on-surface"><span className="material-symbols-outlined text-[18px]">more_horiz</span></button>
                </div>
                <h4 className="font-body-base text-body-base font-semibold text-on-surface mb-1">Acme Corp Redesign</h4>
                <p className="font-body-sm text-body-sm text-on-surface-variant mb-3">Acme Corporation</p>
                <div className="flex items-center justify-between pt-3 border-t border-surface-variant">
                  <div className="flex items-center gap-2">
                    <div className="w-6 h-6 rounded-full bg-secondary/10 flex items-center justify-center text-secondary font-label-caps text-[10px]">JD</div>
                    <span className="font-body-sm text-body-sm text-on-surface-variant">John Doe</span>
                  </div>
                  <span className="font-body-sm text-body-sm font-semibold text-on-surface">$15,000</span>
                </div>
              </div>
              {/* Card 2 */}
              <div className="bg-surface-container-lowest rounded-lg p-4 border border-outline-variant/50 shadow-sm cursor-grab hover:border-secondary/50 transition-colors">
                <div className="flex justify-between items-start mb-2">
                  <span className="text-[10px] font-bold tracking-wider text-on-surface-variant uppercase bg-surface-container-high px-2 py-1 rounded">Referral</span>
                </div>
                <h4 className="font-body-base text-body-base font-semibold text-on-surface mb-1">Q3 Enterprise License</h4>
                <p className="font-body-sm text-body-sm text-on-surface-variant mb-3">TechFlow Inc.</p>
                <div className="flex items-center justify-between pt-3 border-t border-surface-variant">
                  <div className="flex items-center gap-2">
                    <img alt="Sarah Smith" className="w-6 h-6 rounded-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAD-Sjtw9Q-bA5L0986TDVtc0Yw7Eg42mWhLJLgUixdgWKhpItK5cIC3QMeX3WaMk-aH_rVjtgdamymV6HUYBkzE-XB2syw-0uRmNYu19vb37Zl5vWrePzSJbSaxBiLLhvlCj3qjLsaFDUp6Xm1SOiTMC0n8HIu_6sveRwiTnKisRdnpOCWyvRhkfxae0bZ1sf-F8e7i5r6FDRk-cZNgxp77lRCIGDPpasfy--D3dCqMM1wPVFifisuWoHPsMFmqWSNPjmDE344Lzw" />
                    <span className="font-body-sm text-body-sm text-on-surface-variant">Sarah S.</span>
                  </div>
                  <span className="font-body-sm text-body-sm font-semibold text-on-surface">$22,500</span>
                </div>
              </div>
            </div>
            <button className="mt-3 flex items-center justify-center gap-1 py-2 text-on-surface-variant hover:text-on-surface hover:bg-surface-container-highest rounded-lg transition-colors w-full font-body-sm text-body-sm">
              <span className="material-symbols-outlined text-[18px]">add</span> Add Deal
            </button>
          </div>

          {/* Stage: Contacted */}
          <div className="w-[300px] flex flex-col bg-surface-container-low rounded-xl p-3 flex-shrink-0">
            <div className="flex items-center justify-between px-2 mb-3">
              <div className="flex items-center gap-2">
                <h3 className="font-heading-md text-heading-md text-on-surface">Contacted</h3>
                <span className="bg-surface-variant text-on-surface-variant px-2 py-0.5 rounded-full font-label-caps text-label-caps">1</span>
              </div>
              <span className="font-body-sm text-body-sm text-on-surface-variant font-medium">$8k</span>
            </div>
            <div className="flex-1 overflow-y-auto kanban-col flex flex-col gap-3 pr-1">
              {/* Card 3 */}
              <div className="bg-surface-container-lowest rounded-lg p-4 border border-outline-variant/50 shadow-sm cursor-grab hover:border-secondary/50 transition-colors">
                <div className="flex justify-between items-start mb-2">
                  <span className="text-[10px] font-bold tracking-wider text-on-surface-variant uppercase bg-surface-container-high px-2 py-1 rounded">Cold Outbound</span>
                </div>
                <h4 className="font-body-base text-body-base font-semibold text-on-surface mb-1">Starter Package</h4>
                <p className="font-body-sm text-body-sm text-on-surface-variant mb-3">Local Dynamics</p>
                <div className="flex items-center justify-between pt-3 border-t border-surface-variant">
                  <div className="flex items-center gap-2">
                    <div className="w-6 h-6 rounded-full bg-primary-container text-on-primary-container flex items-center justify-center font-label-caps text-[10px]">MK</div>
                    <span className="font-body-sm text-body-sm text-on-surface-variant">Mike K.</span>
                  </div>
                  <span className="font-body-sm text-body-sm font-semibold text-on-surface">$8,000</span>
                </div>
              </div>
            </div>
          </div>

          {/* Stage: Replied */}
          <div className="w-[300px] flex flex-col bg-surface-container-low rounded-xl p-3 flex-shrink-0">
            <div className="flex items-center justify-between px-2 mb-3">
              <div className="flex items-center gap-2">
                <h3 className="font-heading-md text-heading-md text-on-surface">Replied</h3>
                <span className="bg-surface-variant text-on-surface-variant px-2 py-0.5 rounded-full font-label-caps text-label-caps">0</span>
              </div>
              <span className="font-body-sm text-body-sm text-on-surface-variant font-medium">$0</span>
            </div>
            <div className="flex-1 overflow-y-auto kanban-col flex flex-col gap-3 pr-1">
              {/* Empty State */}
              <div className="flex-1 border-2 border-dashed border-outline-variant/30 rounded-lg flex flex-col items-center justify-center p-6 text-center">
                <span className="material-symbols-outlined text-outline-variant text-[32px] mb-2">inbox</span>
                <p className="font-body-sm text-body-sm text-on-surface-variant">No deals in this stage yet.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
