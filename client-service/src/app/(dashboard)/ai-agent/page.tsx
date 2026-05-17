export default function AIAgentWorkspacePage() {
  return (
    <div className="flex-1 overflow-hidden flex flex-col md:flex-row bg-surface-container-low p-margin-page gap-gutter h-[calc(100vh-65px)]">
      {/* Chat History Sidebar */}
      <aside className="hidden md:flex w-[300px] bg-surface-container-lowest rounded-lg border border-outline-variant shadow-sm flex-col overflow-hidden shrink-0 h-full">
        <div className="p-4 border-b border-outline-variant bg-surface-bright">
          <h2 className="font-heading-md text-heading-md text-on-surface flex items-center gap-2">
            <span className="material-symbols-outlined text-secondary">history</span>
            Recent Threads
          </h2>
        </div>
        <div className="flex-1 overflow-y-auto p-2 space-y-1">
          <button className="w-full text-left p-3 rounded bg-surface-container-high hover:bg-surface-variant transition-colors group">
            <p className="font-label-caps text-label-caps text-secondary mb-1">Today, 9:41 AM</p>
            <p className="font-body-sm text-body-sm text-on-surface truncate group-hover:text-primary transition-colors">Find 50 leads in fintech...</p>
          </button>
          <button className="w-full text-left p-3 rounded hover:bg-surface-container transition-colors group">
            <p className="font-label-caps text-label-caps text-outline-variant mb-1">Yesterday</p>
            <p className="font-body-sm text-body-sm text-on-surface-variant truncate group-hover:text-on-surface transition-colors">Draft sequence for SaaS founders</p>
          </button>
          <button className="w-full text-left p-3 rounded hover:bg-surface-container transition-colors group">
            <p className="font-label-caps text-label-caps text-outline-variant mb-1">Oct 12</p>
            <p className="font-body-sm text-body-sm text-on-surface-variant truncate group-hover:text-on-surface transition-colors">Analyze Q3 conversion rates</p>
          </button>
          <button className="w-full text-left p-3 rounded hover:bg-surface-container transition-colors group">
            <p className="font-label-caps text-label-caps text-outline-variant mb-1">Oct 10</p>
            <p className="font-body-sm text-body-sm text-on-surface-variant truncate group-hover:text-on-surface transition-colors">Cleanse bouncing emails</p>
          </button>
        </div>
        <div className="p-4 border-t border-outline-variant mt-auto">
          <button className="w-full font-label-caps text-label-caps text-secondary flex items-center justify-center gap-2 hover:text-on-secondary-fixed-variant transition-colors">
            <span className="material-symbols-outlined text-[16px]">add</span>
            New Thread
          </button>
        </div>
      </aside>

      {/* Active Workspace */}
      <section className="flex-1 flex flex-col min-w-0 bg-surface-container-lowest rounded-lg border border-outline-variant shadow-sm overflow-hidden relative h-full">
        {/* Chat Feed */}
        <div className="flex-1 overflow-y-auto p-margin-page pb-[200px] flex flex-col gap-stack-lg">
          {/* System Greeting */}
          <div className="flex gap-4 max-w-3xl">
            <div className="w-10 h-10 rounded bg-primary-container text-on-primary-container flex items-center justify-center shrink-0">
              <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>smart_toy</span>
            </div>
            <div className="flex flex-col gap-2 pt-1">
              <span className="font-label-caps text-label-caps text-outline-variant">Agent</span>
              <div className="bg-surface-bright border border-outline-variant rounded-lg rounded-tl-none p-4 font-body-base text-on-surface shadow-sm">
                Hello. I am ready to execute your acquisition recipes. What are we building today?
              </div>
            </div>
          </div>

          {/* User Intent */}
          <div className="flex gap-4 max-w-3xl self-end flex-row-reverse">
            <div className="w-10 h-10 rounded overflow-hidden border border-outline-variant shrink-0">
              <img alt="User" className="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuA1qxhqDKwRsIc_I755IiHL-oF-bTgQCaQawrBWKb3YziJRbctMkP7wtMiJXIbUWJTIIZR-dyALV1zcOaL7ltYH0OTfVWadV64LHnNdxZtz32DK9AgnE0Vz-qYa2S9s0HtvT-8mLIqlLbBXkfNd3pjuoq5bz_Oeu-tuIcodfKHmKj6IUgUEBPdGy1BTKGAGIuVxGHAHdWm5dSSfVQVC2UrE_nqmEgvBJbrKzq5p9tSPqL6rkAfzlqxZFPffLSBUrE5uvzhiYmR_FrE" />
            </div>
            <div className="flex flex-col gap-2 pt-1 items-end">
              <span className="font-label-caps text-label-caps text-outline-variant">You</span>
              <div className="bg-secondary text-on-secondary rounded-lg rounded-tr-none p-4 font-body-base shadow-[inset_0_-1px_0_0_rgba(0,0,0,0.1)]">
                Find 50 leads in the fintech space and draft personalized emails emphasizing our new API integration features.
              </div>
            </div>
          </div>

          {/* Agent Reasoning & Response */}
          <div className="flex gap-4 max-w-4xl w-full">
            <div className="w-10 h-10 rounded bg-primary-container text-on-primary-container flex items-center justify-center shrink-0 mt-1">
              <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>smart_toy</span>
            </div>
            <div className="flex flex-col gap-3 pt-1 w-full">
              <span className="font-label-caps text-label-caps text-outline-variant">Agent Execution</span>
              
              {/* Reasoning Block Bento */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-2">
                <div className="bg-surface-container-low border-l-2 border-secondary rounded-r p-3 flex items-start gap-3">
                  <span className="material-symbols-outlined text-secondary shrink-0">check_circle</span>
                  <div>
                    <p className="font-label-caps text-label-caps text-on-surface mb-0.5">Step 1: Analyzing Intent</p>
                    <p className="font-body-sm text-body-sm text-on-surface-variant">Extracted target: "Fintech", quantity: 50, objective: "Draft emails (API focus)".</p>
                  </div>
                </div>
                <div className="bg-surface-container-low border-l-2 border-secondary rounded-r p-3 flex items-start gap-3">
                  <span className="material-symbols-outlined text-secondary shrink-0">database</span>
                  <div>
                    <p className="font-label-caps text-label-caps text-on-surface mb-0.5">Step 2: Searching Databases</p>
                    <p className="font-body-sm text-body-sm text-on-surface-variant">Querying Apollo &amp; LinkedIn for VP Engineering/CTO titles in NA Fintech sector.</p>
                  </div>
                </div>
                <div className="bg-surface-container border border-outline-variant rounded p-3 flex items-start gap-3 relative overflow-hidden">
                  <div className="absolute inset-y-0 left-0 bg-secondary/10 w-[60%] transition-all"></div>
                  <span className="material-symbols-outlined text-secondary animate-pulse shrink-0 relative z-10">sync</span>
                  <div className="relative z-10">
                    <p className="font-label-caps text-label-caps text-on-surface mb-0.5">Step 3: Verifying Deliverability</p>
                    <p className="font-body-sm text-body-sm text-on-surface-variant">Validating 64 raw emails found. 38/50 confirmed so far...</p>
                  </div>
                </div>
                <div className="bg-surface-bright border border-outline-variant border-dashed rounded p-3 flex items-start gap-3 opacity-60">
                  <span className="material-symbols-outlined text-outline-variant shrink-0">edit_document</span>
                  <div>
                    <p className="font-label-caps text-label-caps text-on-surface-variant mb-0.5">Step 4: Drafting Copy</p>
                    <p className="font-body-sm text-body-sm text-outline-variant">Awaiting final validated lead list to generate personalized variables.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Input Area Docked to Bottom */}
        <div className="absolute bottom-0 left-0 w-full bg-gradient-to-t from-surface-container-lowest via-surface-container-lowest to-transparent pt-8 pb-6 px-margin-page">
          <div className="max-w-4xl mx-auto">
            <div className="bg-surface-bright border-2 border-surface-variant focus-within:border-secondary rounded-lg shadow-sm transition-colors flex flex-col overflow-hidden">
              <textarea className="w-full bg-transparent border-none focus:ring-0 resize-none p-4 font-body-base text-on-surface placeholder:text-outline-variant outline-none" placeholder="Describe your acquisition goal or type a command..." rows={3}></textarea>
              <div className="bg-surface border-t border-surface-variant px-4 py-3 flex justify-between items-center">
                <div className="flex items-center gap-2">
                  <button className="p-1.5 text-on-surface-variant hover:text-secondary hover:bg-secondary/10 rounded transition-colors" title="Attach List">
                    <span className="material-symbols-outlined text-[20px]">attach_file</span>
                  </button>
                  <button className="p-1.5 text-on-surface-variant hover:text-secondary hover:bg-secondary/10 rounded transition-colors" title="Use Recipe">
                    <span className="material-symbols-outlined text-[20px]">auto_awesome</span>
                  </button>
                  <div className="h-4 w-[1px] bg-outline-variant mx-1"></div>
                  <span className="font-label-caps text-label-caps text-outline-variant flex items-center gap-1">
                    <span className="material-symbols-outlined text-[14px]">keyboard_return</span> to send
                  </span>
                </div>
                <button className="bg-secondary text-on-secondary px-4 py-2 rounded font-label-caps text-label-caps shadow-[inset_0_-1px_0_0_rgba(0,0,0,0.2)] hover:bg-on-secondary-fixed-variant transition-colors flex items-center gap-2">
                  Execute
                  <span className="material-symbols-outlined text-[16px]">send</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
