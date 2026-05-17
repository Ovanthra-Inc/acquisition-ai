export default function SettingsPage() {
  return (
    <div className="flex flex-col h-full w-full p-margin-page max-w-container-max mx-auto">
      {/* Page Header */}
      <div className="mb-stack-lg">
        <h1 className="font-display-xl text-display-xl text-on-surface">Organization Settings</h1>
        <p className="font-body-base text-body-base text-on-surface-variant mt-1">Manage your team preferences, connections, and security protocols.</p>
      </div>

      {/* Settings Layout Container */}
      <div className="flex flex-col md:flex-row gap-gutter items-start">
        {/* Inner Settings Navigation (Vertical Tabs) */}
        <nav className="w-full md:w-64 flex-shrink-0 sticky top-[80px]">
          <ul className="flex flex-col space-y-1 border border-outline-variant rounded-lg p-2 bg-surface-container-lowest shadow-sm">
            <li>
              <a className="block px-4 py-2.5 rounded-md font-body-sm text-body-sm text-on-surface-variant hover:bg-surface-container-high transition-colors" href="#">Profile</a>
            </li>
            <li>
              <a className="block px-4 py-2.5 rounded-md font-body-sm text-body-sm text-on-surface-variant hover:bg-surface-container-high transition-colors" href="#">Workspace</a>
            </li>
            {/* Active Sub-tab */}
            <li>
              <a className="block px-4 py-2.5 rounded-md font-body-sm text-body-sm font-semibold bg-surface text-secondary border border-outline-variant/50 shadow-sm transition-colors flex items-center justify-between group" href="#">
                Integrations
                <span className="material-symbols-outlined text-sm opacity-50 group-hover:opacity-100 transition-opacity">chevron_right</span>
              </a>
            </li>
            <li>
              <a className="block px-4 py-2.5 rounded-md font-body-sm text-body-sm text-on-surface-variant hover:bg-surface-container-high transition-colors" href="#">Billing</a>
            </li>
            <li>
              <a className="block px-4 py-2.5 rounded-md font-body-sm text-body-sm text-on-surface-variant hover:bg-surface-container-high transition-colors" href="#">Security</a>
            </li>
          </ul>
        </nav>

        {/* Settings Content Area (Integrations) */}
        <div className="flex-1 w-full">
          <div className="mb-stack-md flex justify-between items-end">
            <div>
              <h2 className="font-heading-md text-heading-md text-on-surface">Connected Services</h2>
              <p className="font-body-sm text-body-sm text-on-surface-variant">Link your external tools to automate workflows and sync data.</p>
            </div>
            <button className="font-body-sm text-body-sm text-secondary font-semibold hover:underline">View App Directory</button>
          </div>

          {/* Integrations Grid */}
          <div className="grid grid-cols-1 xl:grid-cols-2 gap-gutter">
            {/* Integration Card: Gmail */}
            <div className="bg-surface-container-lowest border border-outline-variant rounded-lg p-stack-lg shadow-sm flex flex-col hover:shadow-md transition-shadow">
              <div className="flex justify-between items-start mb-stack-md">
                <div className="flex items-center gap-4">
                  <div className="w-12 h-12 rounded bg-surface-container-low border border-outline-variant flex items-center justify-center text-error">
                    <span className="material-symbols-outlined text-2xl" style={{ fontVariationSettings: "'FILL' 1" }}>mail</span>
                  </div>
                  <div>
                    <h3 className="font-heading-md text-heading-md text-on-surface leading-tight">Gmail</h3>
                    <p className="font-body-sm text-body-sm text-outline">Email &amp; Calendar</p>
                  </div>
                </div>
                {/* Toggle */}
                <div className="relative inline-block w-12 mr-2 align-middle select-none transition duration-200 ease-in">
                  <input defaultChecked className="toggle-checkbox absolute block w-6 h-6 rounded-full bg-white border-4 appearance-none cursor-pointer transition-transform duration-200 ease-in-out border-surface-variant z-10 top-0 left-0 checked:right-0 checked:border-secondary-container" id="toggle-gmail" name="toggle" type="checkbox" />
                  <label className="toggle-label block overflow-hidden h-6 rounded-full bg-surface-variant cursor-pointer transition-colors duration-200 ease-in-out peer-checked:bg-secondary-container" htmlFor="toggle-gmail"></label>
                </div>
              </div>
              <p className="font-body-sm text-body-sm text-on-surface-variant mb-stack-lg flex-1">Sync your inbox to log client communications automatically and send campaigns directly from Acquisition.ai.</p>
              <div className="pt-stack-sm border-t border-surface-variant flex justify-between items-center">
                <span className="font-label-caps text-label-caps text-on-tertiary-container flex items-center gap-1"><span className="w-2 h-2 rounded-full bg-on-tertiary-container"></span> Connected</span>
                <button className="font-body-sm text-body-sm text-outline-variant hover:text-on-surface transition-colors">Configure</button>
              </div>
            </div>

            {/* Integration Card: Outlook */}
            <div className="bg-surface-container-lowest border border-outline-variant rounded-lg p-stack-lg shadow-sm flex flex-col hover:shadow-md transition-shadow">
              <div className="flex justify-between items-start mb-stack-md">
                <div className="flex items-center gap-4">
                  <div className="w-12 h-12 rounded bg-surface-container-low border border-outline-variant flex items-center justify-center text-secondary">
                    <span className="material-symbols-outlined text-2xl" style={{ fontVariationSettings: "'FILL' 1" }}>mark_email_unread</span>
                  </div>
                  <div>
                    <h3 className="font-heading-md text-heading-md text-on-surface leading-tight">Microsoft Outlook</h3>
                    <p className="font-body-sm text-body-sm text-outline">Email &amp; Calendar</p>
                  </div>
                </div>
                {/* Toggle */}
                <div className="relative inline-block w-12 mr-2 align-middle select-none transition duration-200 ease-in">
                  <input className="toggle-checkbox absolute block w-6 h-6 rounded-full bg-white border-4 appearance-none cursor-pointer transition-transform duration-200 ease-in-out border-surface-variant z-10 top-0 left-0 checked:right-0 checked:border-secondary-container" id="toggle-outlook" name="toggle" type="checkbox" />
                  <label className="toggle-label block overflow-hidden h-6 rounded-full bg-surface-variant cursor-pointer transition-colors duration-200 ease-in-out peer-checked:bg-secondary-container" htmlFor="toggle-outlook"></label>
                </div>
              </div>
              <p className="font-body-sm text-body-sm text-on-surface-variant mb-stack-lg flex-1">Connect your Exchange or Office 365 account to manage emails and meeting schedules seamlessly.</p>
              <div className="pt-stack-sm border-t border-surface-variant flex justify-between items-center">
                <span className="font-label-caps text-label-caps text-outline-variant">Not Connected</span>
              </div>
            </div>

            {/* Integration Card: Salesforce */}
            <div className="bg-surface-container-lowest border border-outline-variant rounded-lg p-stack-lg shadow-sm flex flex-col hover:shadow-md transition-shadow">
              <div className="flex justify-between items-start mb-stack-md">
                <div className="flex items-center gap-4">
                  <div className="w-12 h-12 rounded bg-surface-container-low border border-outline-variant flex items-center justify-center text-primary">
                    <span className="material-symbols-outlined text-2xl" style={{ fontVariationSettings: "'FILL' 1" }}>cloud</span>
                  </div>
                  <div>
                    <h3 className="font-heading-md text-heading-md text-on-surface leading-tight">Salesforce</h3>
                    <p className="font-body-sm text-body-sm text-outline">CRM</p>
                  </div>
                </div>
                {/* Toggle */}
                <div className="relative inline-block w-12 mr-2 align-middle select-none transition duration-200 ease-in">
                  <input defaultChecked className="toggle-checkbox absolute block w-6 h-6 rounded-full bg-white border-4 appearance-none cursor-pointer transition-transform duration-200 ease-in-out border-surface-variant z-10 top-0 left-0 checked:right-0 checked:border-secondary-container" id="toggle-sf" name="toggle" type="checkbox" />
                  <label className="toggle-label block overflow-hidden h-6 rounded-full bg-surface-variant cursor-pointer transition-colors duration-200 ease-in-out peer-checked:bg-secondary-container" htmlFor="toggle-sf"></label>
                </div>
              </div>
              <p className="font-body-sm text-body-sm text-on-surface-variant mb-stack-lg flex-1">Bi-directional sync for Leads, Contacts, and Opportunities. Keep your enterprise CRM as the source of truth.</p>
              <div className="pt-stack-sm border-t border-surface-variant flex justify-between items-center">
                <span className="font-label-caps text-label-caps text-on-tertiary-container flex items-center gap-1"><span className="w-2 h-2 rounded-full bg-on-tertiary-container"></span> Connected</span>
                <button className="font-body-sm text-body-sm text-outline-variant hover:text-on-surface transition-colors">Field Mapping</button>
              </div>
            </div>

            {/* Integration Card: HubSpot */}
            <div className="bg-surface-container-lowest border border-outline-variant rounded-lg p-stack-lg shadow-sm flex flex-col hover:shadow-md transition-shadow">
              <div className="flex justify-between items-start mb-stack-md">
                <div className="flex items-center gap-4">
                  <div className="w-12 h-12 rounded bg-surface-container-low border border-outline-variant flex items-center justify-center text-[#ff7a59]">
                    <span className="material-symbols-outlined text-2xl" style={{ fontVariationSettings: "'FILL' 1" }}>hub</span>
                  </div>
                  <div>
                    <h3 className="font-heading-md text-heading-md text-on-surface leading-tight">HubSpot</h3>
                    <p className="font-body-sm text-body-sm text-outline">CRM &amp; Marketing</p>
                  </div>
                </div>
                {/* Toggle */}
                <div className="relative inline-block w-12 mr-2 align-middle select-none transition duration-200 ease-in">
                  <input className="toggle-checkbox absolute block w-6 h-6 rounded-full bg-white border-4 appearance-none cursor-pointer transition-transform duration-200 ease-in-out border-surface-variant z-10 top-0 left-0 checked:right-0 checked:border-secondary-container" id="toggle-hubspot" name="toggle" type="checkbox" />
                  <label className="toggle-label block overflow-hidden h-6 rounded-full bg-surface-variant cursor-pointer transition-colors duration-200 ease-in-out peer-checked:bg-secondary-container" htmlFor="toggle-hubspot"></label>
                </div>
              </div>
              <p className="font-body-sm text-body-sm text-on-surface-variant mb-stack-lg flex-1">Push new generated leads directly into HubSpot workflows and track marketing attribution.</p>
              <div className="pt-stack-sm border-t border-surface-variant flex justify-between items-center">
                <span className="font-label-caps text-label-caps text-outline-variant">Not Connected</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
