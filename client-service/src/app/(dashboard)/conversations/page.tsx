export default function ConversationsPage() {
  return (
    <div className="flex-1 flex overflow-hidden h-[calc(100vh-65px)]">
      {/* Left Pane: Thread List */}
      <aside className="hidden md:flex w-[340px] border-r border-outline-variant bg-surface-container-lowest flex-col shrink-0 h-full">
        {/* Filters/Header */}
        <div className="p-4 border-b border-surface-container-highest flex justify-between items-center bg-surface-container-lowest">
          <div className="flex gap-2">
            <button className="px-3 py-1.5 rounded-full bg-secondary-container/10 text-secondary border border-secondary/20 font-body-sm text-[13px] font-semibold">Active</button>
            <button className="px-3 py-1.5 rounded-full text-on-surface-variant hover:bg-surface-container font-body-sm text-[13px] transition-colors">Unread</button>
          </div>
          <button className="text-on-surface-variant hover:text-on-surface p-1 rounded transition-colors">
            <span className="material-symbols-outlined text-[20px]">filter_list</span>
          </button>
        </div>

        {/* List Items (Scrollable) */}
        <div className="flex-1 overflow-y-auto">
          {/* Active Thread */}
          <div className="p-4 border-b border-surface-container-highest bg-secondary/5 border-l-2 border-l-secondary cursor-pointer">
            <div className="flex justify-between items-start mb-1">
              <h3 className="font-body-base text-body-base font-semibold text-on-surface">Sarah Jenkins</h3>
              <span className="font-body-sm text-[12px] text-on-surface-variant">10:42 AM</span>
            </div>
            <p className="font-body-sm text-body-sm text-on-surface-variant mb-2 truncate">Re: Enterprise Data Integration proposal</p>
            <div className="flex justify-between items-center">
              <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded text-[11px] font-semibold bg-tertiary-fixed text-on-tertiary-fixed uppercase tracking-wider">
                <span className="w-1.5 h-1.5 rounded-full bg-on-tertiary-fixed"></span> Interested
              </span>
              <div className="w-5 h-5 rounded-full bg-secondary flex items-center justify-center text-on-secondary text-[10px] font-bold shadow-sm">2</div>
            </div>
          </div>

          {/* Inactive Thread */}
          <div className="p-4 border-b border-surface-container-highest hover:bg-surface-container-low cursor-pointer transition-colors border-l-2 border-l-transparent">
            <div className="flex justify-between items-start mb-1">
              <h3 className="font-body-base text-body-base font-medium text-on-surface">Michael Chang</h3>
              <span className="font-body-sm text-[12px] text-outline-variant">Yesterday</span>
            </div>
            <p className="font-body-sm text-body-sm text-outline-variant mb-2 truncate">Question regarding the API rate limits...</p>
            <div className="flex justify-between items-center">
              <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded text-[11px] font-semibold bg-surface-container-high text-on-surface-variant uppercase tracking-wider">
                Follow-up
              </span>
            </div>
          </div>

          {/* Inactive Thread */}
          <div className="p-4 border-b border-surface-container-highest hover:bg-surface-container-low cursor-pointer transition-colors border-l-2 border-l-transparent">
            <div className="flex justify-between items-start mb-1">
              <h3 className="font-body-base text-body-base font-medium text-outline-variant">Elena Rodriguez</h3>
              <span className="font-body-sm text-[12px] text-outline-variant">Oct 12</span>
            </div>
            <p className="font-body-sm text-body-sm text-outline-variant mb-2 truncate">Not a good time right now, thanks.</p>
            <div className="flex justify-between items-center">
              <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded text-[11px] font-semibold bg-error-container/50 text-error uppercase tracking-wider">
                Not Interested
              </span>
            </div>
          </div>

          {/* Inactive Thread */}
          <div className="p-4 border-b border-surface-container-highest hover:bg-surface-container-low cursor-pointer transition-colors border-l-2 border-l-transparent">
            <div className="flex justify-between items-start mb-1">
              <h3 className="font-body-base text-body-base font-medium text-on-surface">David Kim</h3>
              <span className="font-body-sm text-[12px] text-outline-variant">Oct 10</span>
            </div>
            <p className="font-body-sm text-body-sm text-outline-variant mb-2 truncate">Let's schedule a call for next week.</p>
            <div className="flex justify-between items-center">
              <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded text-[11px] font-semibold bg-primary-fixed text-on-primary-fixed uppercase tracking-wider">
                Meeting Set
              </span>
            </div>
          </div>
        </div>
      </aside>

      {/* Right Pane: Conversation View */}
      <section className="flex-1 flex flex-col bg-surface h-full min-w-0">
        {/* Conversation Header */}
        <div className="px-6 py-4 bg-surface-container-lowest border-b border-outline-variant flex justify-between items-center shadow-sm z-10 shrink-0 overflow-x-auto">
          <div className="flex items-center gap-4 min-w-max">
            <div className="w-10 h-10 rounded bg-primary-fixed flex items-center justify-center text-on-primary-fixed font-bold text-heading-md shadow-sm">
              SJ
            </div>
            <div>
              <h2 className="font-heading-md text-[18px] font-bold text-on-surface leading-tight">Sarah Jenkins</h2>
              <p className="font-body-sm text-[13px] text-on-surface-variant flex items-center gap-1 mt-0.5">
                VP of Operations at TechFlow <span className="w-1 h-1 rounded-full bg-outline-variant mx-1"></span> sarah.j@techflow.io
              </p>
            </div>
          </div>
          <div className="flex gap-2 ml-4">
            <button className="px-3 py-1.5 rounded border border-outline-variant text-on-surface-variant font-body-sm text-[13px] font-semibold hover:bg-surface-container-low transition-colors shadow-sm bg-surface-container-lowest whitespace-nowrap">
              Mark Closed
            </button>
            <button className="px-3 py-1.5 rounded bg-secondary text-on-secondary font-body-sm text-[13px] font-semibold hover:bg-on-secondary-fixed-variant transition-colors shadow-sm shadow-[inset_0_-1px_0_rgba(0,0,0,0.1)] whitespace-nowrap">
              Move to Pipeline
            </button>
          </div>
        </div>

        {/* Messages Area (Scrollable) */}
        <div className="flex-1 overflow-y-auto p-6 flex flex-col gap-6">
          {/* System Action */}
          <div className="text-center font-body-sm text-[12px] text-outline-variant my-2 flex items-center justify-center gap-2">
            <span className="h-px w-8 bg-surface-container-highest block"></span>
            Automated Outreach Campaign Started • Oct 14, 9:00 AM
            <span className="h-px w-8 bg-surface-container-highest block"></span>
          </div>

          {/* Sent Message (Right aligned) */}
          <div className="flex flex-col items-end w-full">
            <div className="flex items-end gap-2 max-w-[80%]">
              <div className="bg-surface-container-highest text-on-surface p-4 rounded-xl rounded-br-sm shadow-sm border border-outline-variant/50">
                <p className="font-body-base text-[14px] leading-relaxed">
                  Hi Sarah,<br/><br/>
                  I noticed TechFlow has been scaling your operations team recently. As you handle more data sources, integration bottlenecks often slow down decision-making.<br/><br/>
                  Acquisition.ai can automate these workflows, typically saving teams 15 hours a week. Open to a brief 10-min chat to see if there's a fit?
                </p>
              </div>
            </div>
            <span className="font-body-sm text-[11px] text-outline-variant mt-1 mr-1">You • Oct 14, 9:02 AM</span>
          </div>

          {/* Received Message (Left aligned) */}
          <div className="flex flex-col items-start w-full">
            <div className="flex items-end gap-2 max-w-[80%]">
              <div className="w-8 h-8 rounded bg-primary-fixed flex items-center justify-center text-on-primary-fixed font-bold text-[12px] shrink-0 mb-1 shadow-sm">SJ</div>
              <div className="bg-surface-container-lowest text-on-surface p-4 rounded-xl rounded-bl-sm shadow-[0_4px_6px_-1px_rgba(0,0,0,0.05)] border border-[#E2E8F0]">
                <p className="font-body-base text-[14px] leading-relaxed">
                  Hi there,<br/><br/>
                  Timing is actually pretty good. We are struggling with siloed data right now. <br/><br/>
                  How does your platform handle custom API integrations with legacy CRMs? That's our biggest hurdle.
                </p>
              </div>
            </div>
            <span className="font-body-sm text-[11px] text-outline-variant mt-1 ml-10">Sarah Jenkins • Today, 10:42 AM</span>
          </div>
        </div>

        {/* AI Suggestions & Composer (Sticky Bottom) */}
        <div className="bg-surface-container-lowest border-t border-outline-variant p-4 shrink-0 shadow-[0_-4px_15px_-3px_rgba(0,0,0,0.05)]">
          {/* AI Suggestions */}
          <div className="mb-3">
            <div className="flex items-center gap-2 mb-2 px-1">
              <span className="material-symbols-outlined text-secondary text-[16px]">auto_awesome</span>
              <span className="font-label-caps text-label-caps text-secondary-container">Suggested Replies</span>
            </div>
            <div className="flex gap-2 overflow-x-auto pb-2 scrollbar-none">
              <button className="shrink-0 max-w-[280px] text-left p-3 rounded-lg border border-secondary/20 bg-secondary/5 hover:bg-secondary/10 transition-colors shadow-sm group">
                <h4 className="font-body-sm font-semibold text-on-surface mb-1 flex justify-between items-center">
                  Direct Answer
                  <span className="material-symbols-outlined text-[14px] text-secondary opacity-0 group-hover:opacity-100 transition-opacity">send</span>
                </h4>
                <p className="font-body-sm text-[12px] text-on-surface-variant truncate">"We offer a visual mapping tool specifically designed for legacy API endpoints..."</p>
              </button>
              <button className="shrink-0 max-w-[280px] text-left p-3 rounded-lg border border-outline-variant bg-surface-container-lowest hover:bg-surface-container-low transition-colors shadow-sm">
                <h4 className="font-body-sm font-semibold text-on-surface mb-1">Push to Meeting</h4>
                <p className="font-body-sm text-[12px] text-on-surface-variant truncate">"Great question. It's highly customizable. Can I show you a 5-min demo of how..."</p>
              </button>
            </div>
          </div>

          {/* Input Area */}
          <div className="bg-surface border border-outline-variant rounded-lg p-2 focus-within:border-secondary focus-within:ring-1 focus-within:ring-secondary transition-all shadow-[inset_0_1px_3px_rgba(0,0,0,0.02)]">
            <textarea className="w-full bg-transparent border-none outline-none focus:ring-0 text-on-surface resize-none p-2 font-body-base text-[14px] placeholder:text-outline-variant" placeholder="Type a reply or select a suggestion..." rows={3}></textarea>
            <div className="flex justify-between items-center mt-2 px-2 pb-1">
              <div className="flex gap-1 overflow-x-auto">
                <button className="p-1.5 text-on-surface-variant hover:text-secondary rounded transition-colors shrink-0">
                  <span className="material-symbols-outlined text-[20px]">format_bold</span>
                </button>
                <button className="p-1.5 text-on-surface-variant hover:text-secondary rounded transition-colors shrink-0">
                  <span className="material-symbols-outlined text-[20px]">attach_file</span>
                </button>
                <button className="p-1.5 text-on-surface-variant hover:text-secondary rounded transition-colors shrink-0">
                  <span className="material-symbols-outlined text-[20px]">link</span>
                </button>
                <div className="w-px h-5 bg-outline-variant mx-1 my-auto shrink-0"></div>
                <button className="p-1.5 text-on-surface-variant hover:text-secondary rounded transition-colors flex items-center gap-1 font-body-sm text-[12px] font-medium shrink-0">
                  <span className="material-symbols-outlined text-[16px]">event</span>
                  Insert Cal Link
                </button>
              </div>
              <button className="bg-secondary text-on-secondary px-5 py-2 rounded font-semibold text-body-sm flex items-center gap-2 hover:bg-on-secondary-fixed-variant transition-colors shadow-sm shadow-[inset_0_-1px_0_rgba(0,0,0,0.1)] shrink-0 ml-2">
                Send
                <span className="material-symbols-outlined text-[16px]">send</span>
              </button>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
