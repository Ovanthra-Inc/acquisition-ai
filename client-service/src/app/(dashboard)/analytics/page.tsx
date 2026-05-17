export default function AnalyticsPage() {
  return (
    <div className="flex flex-col h-full w-full p-margin-page overflow-x-hidden max-w-container-max mx-auto">
      {/* Top Row: Metric Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-gutter mb-stack-lg">
        {/* Total Leads Card */}
        <div className="bg-surface-container-lowest rounded-lg border border-surface-variant shadow-[0_4px_6px_-1px_rgba(0,0,0,0.05)] p-6 flex flex-col justify-between">
          <div className="flex justify-between items-start mb-4">
            <span className="font-label-caps text-label-caps text-on-surface-variant uppercase">Total Leads</span>
            <div className="bg-tertiary-fixed-dim/20 text-on-tertiary-fixed-variant px-2 py-0.5 rounded text-xs font-semibold flex items-center gap-1">
              <span className="material-symbols-outlined text-[14px]">trending_up</span> 12.5%
            </div>
          </div>
          <div>
            <div className="font-metric-lg text-metric-lg text-on-surface mb-2">24,592</div>
            {/* Simple CSS Sparkline representation */}
            <div className="h-10 w-full flex items-end gap-1 opacity-80">
              <div className="w-full bg-secondary-container h-[20%] rounded-t-sm"></div>
              <div className="w-full bg-secondary-container h-[35%] rounded-t-sm"></div>
              <div className="w-full bg-secondary-container h-[25%] rounded-t-sm"></div>
              <div className="w-full bg-secondary-container h-[50%] rounded-t-sm"></div>
              <div className="w-full bg-secondary-container h-[45%] rounded-t-sm"></div>
              <div className="w-full bg-secondary-container h-[70%] rounded-t-sm"></div>
              <div className="w-full bg-secondary-container h-[60%] rounded-t-sm"></div>
              <div className="w-full bg-secondary h-[90%] rounded-t-sm"></div>
            </div>
          </div>
        </div>

        {/* Email Open Rate */}
        <div className="bg-surface-container-lowest rounded-lg border border-surface-variant shadow-[0_4px_6px_-1px_rgba(0,0,0,0.05)] p-6 flex flex-col justify-between">
          <div className="flex justify-between items-start mb-4">
            <span className="font-label-caps text-label-caps text-on-surface-variant uppercase">Email Open Rate</span>
            <span className="material-symbols-outlined text-outline-variant">mail_lock</span>
          </div>
          <div>
            <div className="font-metric-lg text-metric-lg text-on-surface mb-1">42.8%</div>
            <p className="font-body-sm text-body-sm text-on-surface-variant">Avg. across all active campaigns</p>
          </div>
        </div>

        {/* Reply Rate */}
        <div className="bg-surface-container-lowest rounded-lg border border-surface-variant shadow-[0_4px_6px_-1px_rgba(0,0,0,0.05)] p-6 flex flex-col justify-between">
          <div className="flex justify-between items-start mb-4">
            <span className="font-label-caps text-label-caps text-on-surface-variant uppercase">Reply Rate</span>
            <span className="material-symbols-outlined text-outline-variant">forum</span>
          </div>
          <div>
            <div className="font-metric-lg text-metric-lg text-on-surface mb-1">8.4%</div>
            <p className="font-body-sm text-body-sm text-on-surface-variant">+1.2% from last month</p>
          </div>
        </div>

        {/* Revenue Generated */}
        <div className="bg-surface-container-lowest rounded-lg border border-surface-variant shadow-[0_4px_6px_-1px_rgba(0,0,0,0.05)] p-6 flex flex-col justify-between">
          <div className="flex justify-between items-start mb-4">
            <span className="font-label-caps text-label-caps text-on-surface-variant uppercase">Revenue Generated</span>
            <span className="material-symbols-outlined text-outline-variant">payments</span>
          </div>
          <div>
            <div className="font-metric-lg text-metric-lg text-on-surface mb-1">$1.2M</div>
            <p className="font-body-sm text-body-sm text-on-surface-variant">Estimated pipeline value</p>
          </div>
        </div>
      </div>

      {/* Middle Section: Large Line Chart (Acquisition over time) */}
      <div className="bg-surface-container-lowest rounded-lg border border-surface-variant shadow-[0_4px_6px_-1px_rgba(0,0,0,0.05)] mb-stack-lg flex flex-col h-96">
        <div className="p-6 border-b border-surface-variant flex justify-between items-center">
          <div>
            <h3 className="font-heading-md text-heading-md text-on-surface">Lead Acquisition Velocity</h3>
            <p className="font-body-sm text-body-sm text-on-surface-variant">Trailing 30 Days</p>
          </div>
          <div className="flex gap-2">
            <button className="px-3 py-1 text-sm bg-surface-container text-on-surface rounded font-medium">7D</button>
            <button className="px-3 py-1 text-sm bg-secondary text-on-primary rounded font-medium">30D</button>
            <button className="px-3 py-1 text-sm bg-surface-container text-on-surface rounded font-medium">90D</button>
          </div>
        </div>
        <div className="flex-1 p-6 relative">
          {/* Faux Line Chart Visualization */}
          <div className="absolute inset-0 p-6 flex items-end">
            <div className="w-full h-full relative border-l border-b border-outline-variant/30">
              {/* Grid lines */}
              <div className="absolute w-full h-px bg-outline-variant/20 bottom-1/4"></div>
              <div className="absolute w-full h-px bg-outline-variant/20 bottom-2/4"></div>
              <div className="absolute w-full h-px bg-outline-variant/20 bottom-3/4"></div>
              {/* Fake Line (SVG) */}
              <svg className="absolute w-full h-full" preserveAspectRatio="none" viewBox="0 0 100 100">
                <path className="vector-path" d="M0,80 Q10,70 20,60 T40,50 T60,30 T80,40 T100,10" fill="none" stroke="#0051d5" strokeWidth="2"></path>
                <path d="M0,100 L0,80 Q10,70 20,60 T40,50 T60,30 T80,40 T100,10 L100,100 Z" fill="url(#blue-gradient)" opacity="0.2"></path>
                <defs>
                  <linearGradient id="blue-gradient" x1="0" x2="0" y1="0" y2="1">
                    <stop offset="0%" stopColor="#0051d5"></stop>
                    <stop offset="100%" stopColor="#ffffff" stopOpacity="0"></stop>
                  </linearGradient>
                </defs>
              </svg>
            </div>
          </div>
        </div>
      </div>

      {/* Bottom Section: Bento Grid Layout */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-gutter">
        {/* Conversion by Channel (Bar Chart) */}
        <div className="bg-surface-container-lowest rounded-lg border border-surface-variant shadow-[0_4px_6px_-1px_rgba(0,0,0,0.05)] col-span-1 lg:col-span-2 flex flex-col">
          <div className="p-6 border-b border-surface-variant">
            <h3 className="font-heading-md text-heading-md text-on-surface">Conversion by Channel</h3>
          </div>
          <div className="p-6 flex-1 flex flex-col justify-end gap-4">
            {/* Horizontal Bar Items */}
            <div className="space-y-4">
              <div>
                <div className="flex justify-between font-body-sm text-body-sm mb-1">
                  <span className="text-on-surface font-semibold">Cold Email (Sequence A)</span>
                  <span className="text-on-surface-variant">45%</span>
                </div>
                <div className="w-full bg-surface-container h-2 rounded-full overflow-hidden">
                  <div className="bg-secondary h-full rounded-full" style={{ width: '45%' }}></div>
                </div>
              </div>
              <div>
                <div className="flex justify-between font-body-sm text-body-sm mb-1">
                  <span className="text-on-surface font-semibold">LinkedIn Outreach</span>
                  <span className="text-on-surface-variant">32%</span>
                </div>
                <div className="w-full bg-surface-container h-2 rounded-full overflow-hidden">
                  <div className="bg-secondary-container h-full rounded-full" style={{ width: '32%' }}></div>
                </div>
              </div>
              <div>
                <div className="flex justify-between font-body-sm text-body-sm mb-1">
                  <span className="text-on-surface font-semibold">Webinars (Organic)</span>
                  <span className="text-on-surface-variant">15%</span>
                </div>
                <div className="w-full bg-surface-container h-2 rounded-full overflow-hidden">
                  <div className="bg-primary-fixed-dim h-full rounded-full" style={{ width: '15%' }}></div>
                </div>
              </div>
              <div>
                <div className="flex justify-between font-body-sm text-body-sm mb-1">
                  <span className="text-on-surface font-semibold">Direct Mail</span>
                  <span className="text-on-surface-variant">8%</span>
                </div>
                <div className="w-full bg-surface-container h-2 rounded-full overflow-hidden">
                  <div className="bg-outline-variant h-full rounded-full" style={{ width: '8%' }}></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Top Performing Recipes List */}
        <div className="bg-surface-container-lowest rounded-lg border border-surface-variant shadow-[0_4px_6px_-1px_rgba(0,0,0,0.05)] col-span-1 flex flex-col">
          <div className="p-6 border-b border-surface-variant">
            <h3 className="font-heading-md text-heading-md text-on-surface">Top Recipes</h3>
          </div>
          <div className="p-0 flex-1 overflow-y-auto">
            <ul className="divide-y divide-surface-variant">
              <li className="p-4 hover:bg-surface-bright transition-colors flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded bg-primary-fixed flex items-center justify-center text-on-primary-fixed">
                    <span className="material-symbols-outlined text-sm">rocket_launch</span>
                  </div>
                  <div>
                    <p className="font-body-base text-body-base font-semibold text-on-surface">SaaS Founders Q3</p>
                    <p className="font-body-sm text-body-sm text-on-surface-variant">Auto-enrich &amp; Email</p>
                  </div>
                </div>
                <span className="font-body-sm text-body-sm font-semibold text-on-tertiary-container bg-tertiary-fixed-dim/20 px-2 py-1 rounded">18% Conv</span>
              </li>
              <li className="p-4 hover:bg-surface-bright transition-colors flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded bg-primary-fixed flex items-center justify-center text-on-primary-fixed">
                    <span className="material-symbols-outlined text-sm">precision_manufacturing</span>
                  </div>
                  <div>
                    <p className="font-body-base text-body-base font-semibold text-on-surface">Manufacturing Execs</p>
                    <p className="font-body-sm text-body-sm text-on-surface-variant">LinkedIn + Call</p>
                  </div>
                </div>
                <span className="font-body-sm text-body-sm font-semibold text-on-tertiary-container bg-tertiary-fixed-dim/20 px-2 py-1 rounded">12% Conv</span>
              </li>
              <li className="p-4 hover:bg-surface-bright transition-colors flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded bg-primary-fixed flex items-center justify-center text-on-primary-fixed">
                    <span className="material-symbols-outlined text-sm">storefront</span>
                  </div>
                  <div>
                    <p className="font-body-base text-body-base font-semibold text-on-surface">Retail Chains D2C</p>
                    <p className="font-body-sm text-body-sm text-on-surface-variant">Multi-channel drip</p>
                  </div>
                </div>
                <span className="font-body-sm text-body-sm font-semibold text-on-tertiary-container bg-tertiary-fixed-dim/20 px-2 py-1 rounded">9% Conv</span>
              </li>
              <li className="p-4 hover:bg-surface-bright transition-colors flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded bg-surface-container flex items-center justify-center text-on-surface-variant">
                    <span className="material-symbols-outlined text-sm">add</span>
                  </div>
                  <div>
                    <p className="font-body-base text-body-base font-medium text-secondary">Create New Recipe</p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
