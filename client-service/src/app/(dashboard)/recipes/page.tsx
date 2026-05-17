export default function RecipesPage() {
  return (
    <div className="flex flex-col h-full w-full">
      {/* Top Header Action Area */}
      <div className="px-margin-page py-8 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 max-w-container-max mx-auto w-full">
        <div>
          <h1 className="font-display-xl text-display-xl text-primary mb-1">Acquisition Recipes</h1>
          <p className="font-body-base text-body-base text-on-surface-variant">Deploy pre-configured client acquisition workflows.</p>
        </div>
        <div className="flex items-center gap-3">
          <button className="bg-surface-container-lowest border border-outline hover:bg-surface-container-low text-on-surface font-body-sm text-body-sm font-semibold py-2.5 px-4 rounded-lg transition-colors flex items-center gap-2">
            <span className="material-symbols-outlined text-[18px]">filter_list</span>
            Filter
          </button>
          <button className="bg-secondary hover:bg-on-secondary-fixed-variant text-on-secondary font-body-sm text-body-sm font-semibold py-2.5 px-4 rounded-lg transition-colors flex items-center gap-2 btn-shadow">
            <span className="material-symbols-outlined text-[18px]">add</span>
            Create Custom Recipe
          </button>
        </div>
      </div>

      {/* Recipes Grid */}
      <div className="px-margin-page pb-12 w-full max-w-container-max mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-gutter">
          {/* Recipe Card 1 */}
          <div className="bg-surface-container-lowest rounded-xl surface-1 flex flex-col overflow-hidden hover:surface-2 transition-shadow duration-300 group cursor-pointer h-full relative border border-outline-variant">
            <div className="p-5 border-b border-surface-variant flex justify-between items-start">
              <div>
                <div className="flex items-center gap-2 mb-2">
                  <span className="material-symbols-outlined text-secondary text-[20px]" style={{ fontVariationSettings: "'FILL' 1" }}>location_on</span>
                  <span className="font-label-caps text-label-caps text-on-surface-variant">LOCAL BUSINESS</span>
                </div>
                <h3 className="font-heading-md text-heading-md text-on-surface">Local SEO Outreach</h3>
              </div>
              <button className="text-outline hover:text-secondary transition-colors">
                <span className="material-symbols-outlined">more_vert</span>
              </button>
            </div>
            <div className="p-5 flex-1 bg-surface-bright flex flex-col justify-center">
              <div className="flex flex-col gap-4 relative">
                {/* Steps Connector Line */}
                <div className="absolute left-[11px] top-[14px] bottom-[14px] w-px bg-outline-variant"></div>
                {/* Step 1 */}
                <div className="flex items-start gap-3 relative z-10">
                  <div className="w-6 h-6 rounded-full bg-secondary-fixed text-secondary flex items-center justify-center shrink-0 border border-surface-container-lowest mt-0.5">
                    <span className="material-symbols-outlined text-[14px]" style={{ fontVariationSettings: "'FILL' 1" }}>language</span>
                  </div>
                  <div>
                    <div className="font-body-sm text-body-sm font-semibold text-on-surface">Target Domain</div>
                    <div className="font-body-sm text-body-sm text-on-surface-variant text-[13px]">Google Maps &amp; Directories</div>
                  </div>
                </div>
                {/* Step 2 */}
                <div className="flex items-start gap-3 relative z-10">
                  <div className="w-6 h-6 rounded-full bg-secondary-fixed text-secondary flex items-center justify-center shrink-0 border border-surface-container-lowest mt-0.5">
                    <span className="material-symbols-outlined text-[14px]" style={{ fontVariationSettings: "'FILL' 1" }}>tune</span>
                  </div>
                  <div>
                    <div className="font-body-sm text-body-sm font-semibold text-on-surface">Filters</div>
                    <div className="font-body-sm text-body-sm text-on-surface-variant text-[13px]">Low Reviews, Missing Website</div>
                  </div>
                </div>
                {/* Step 3 */}
                <div className="flex items-start gap-3 relative z-10">
                  <div className="w-6 h-6 rounded-full bg-secondary-fixed text-secondary flex items-center justify-center shrink-0 border border-surface-container-lowest mt-0.5">
                    <span className="material-symbols-outlined text-[14px]" style={{ fontVariationSettings: "'FILL' 1" }}>mail</span>
                  </div>
                  <div>
                    <div className="font-body-sm text-body-sm font-semibold text-on-surface">Outreach Style</div>
                    <div className="font-body-sm text-body-sm text-on-surface-variant text-[13px]">Value-first Email + SMS Drop</div>
                  </div>
                </div>
              </div>
            </div>
            <div className="p-4 bg-surface-container-lowest border-t border-surface-variant flex justify-between items-center mt-auto">
              <div className="flex -space-x-2">
                <div className="w-6 h-6 rounded-full bg-tertiary-fixed-dim border-2 border-surface-container-lowest"></div>
                <div className="w-6 h-6 rounded-full bg-secondary-fixed border-2 border-surface-container-lowest"></div>
              </div>
              <button className="text-secondary font-body-sm text-body-sm font-semibold hover:text-on-secondary-fixed-variant transition-colors flex items-center gap-1 group-hover:underline">
                Run Recipe <span className="material-symbols-outlined text-[18px]">arrow_forward</span>
              </button>
            </div>
          </div>

          {/* Recipe Card 2 */}
          <div className="bg-surface-container-lowest rounded-xl surface-1 flex flex-col overflow-hidden hover:surface-2 transition-shadow duration-300 group cursor-pointer h-full relative border border-outline-variant">
            <div className="p-5 border-b border-surface-variant flex justify-between items-start">
              <div>
                <div className="flex items-center gap-2 mb-2">
                  <span className="material-symbols-outlined text-secondary text-[20px]" style={{ fontVariationSettings: "'FILL' 1" }}>business</span>
                  <span className="font-label-caps text-label-caps text-on-surface-variant">B2B SAAS</span>
                </div>
                <h3 className="font-heading-md text-heading-md text-on-surface">SaaS Cold Email Engine</h3>
              </div>
              <button className="text-outline hover:text-secondary transition-colors">
                <span className="material-symbols-outlined">more_vert</span>
              </button>
            </div>
            <div className="p-5 flex-1 bg-surface-bright flex flex-col justify-center">
              <div className="flex flex-col gap-4 relative">
                <div className="absolute left-[11px] top-[14px] bottom-[14px] w-px bg-outline-variant"></div>
                <div className="flex items-start gap-3 relative z-10">
                  <div className="w-6 h-6 rounded-full bg-secondary-fixed text-secondary flex items-center justify-center shrink-0 border border-surface-container-lowest mt-0.5">
                    <span className="material-symbols-outlined text-[14px]" style={{ fontVariationSettings: "'FILL' 1" }}>groups</span>
                  </div>
                  <div>
                    <div className="font-body-sm text-body-sm font-semibold text-on-surface">Target Domain</div>
                    <div className="font-body-sm text-body-sm text-on-surface-variant text-[13px]">LinkedIn &amp; Tech Crunch</div>
                  </div>
                </div>
                <div className="flex items-start gap-3 relative z-10">
                  <div className="w-6 h-6 rounded-full bg-secondary-fixed text-secondary flex items-center justify-center shrink-0 border border-surface-container-lowest mt-0.5">
                    <span className="material-symbols-outlined text-[14px]" style={{ fontVariationSettings: "'FILL' 1" }}>tune</span>
                  </div>
                  <div>
                    <div className="font-body-sm text-body-sm font-semibold text-on-surface">Filters</div>
                    <div className="font-body-sm text-body-sm text-on-surface-variant text-[13px]">Recently Funded, Hiring Tech Roles</div>
                  </div>
                </div>
                <div className="flex items-start gap-3 relative z-10">
                  <div className="w-6 h-6 rounded-full bg-secondary-fixed text-secondary flex items-center justify-center shrink-0 border border-surface-container-lowest mt-0.5">
                    <span className="material-symbols-outlined text-[14px]" style={{ fontVariationSettings: "'FILL' 1" }}>send</span>
                  </div>
                  <div>
                    <div className="font-body-sm text-body-sm font-semibold text-on-surface">Outreach Style</div>
                    <div className="font-body-sm text-body-sm text-on-surface-variant text-[13px]">Direct Email sequence (4 touches)</div>
                  </div>
                </div>
              </div>
            </div>
            <div className="p-4 bg-surface-container-lowest border-t border-surface-variant flex justify-between items-center mt-auto">
              <div className="flex -space-x-2">
                <div className="w-6 h-6 rounded-full bg-primary-fixed-dim border-2 border-surface-container-lowest"></div>
                <div className="w-6 h-6 rounded-full bg-secondary-fixed border-2 border-surface-container-lowest"></div>
              </div>
              <button className="text-secondary font-body-sm text-body-sm font-semibold hover:text-on-secondary-fixed-variant transition-colors flex items-center gap-1 group-hover:underline">
                Run Recipe <span className="material-symbols-outlined text-[18px]">arrow_forward</span>
              </button>
            </div>
          </div>

          {/* Recipe Card 3 */}
          <div className="bg-surface-container-lowest rounded-xl surface-1 flex flex-col overflow-hidden hover:surface-2 transition-shadow duration-300 group cursor-pointer h-full relative border border-outline-variant">
            <div className="p-5 border-b border-surface-variant flex justify-between items-start">
              <div>
                <div className="flex items-center gap-2 mb-2">
                  <span className="material-symbols-outlined text-secondary text-[20px]" style={{ fontVariationSettings: "'FILL' 1" }}>storefront</span>
                  <span className="font-label-caps text-label-caps text-on-surface-variant">E-COMMERCE</span>
                </div>
                <h3 className="font-heading-md text-heading-md text-on-surface">DTC Retention Audit</h3>
              </div>
              <button className="text-outline hover:text-secondary transition-colors">
                <span className="material-symbols-outlined">more_vert</span>
              </button>
            </div>
            <div className="p-5 flex-1 bg-surface-bright flex flex-col justify-center">
              <div className="flex flex-col gap-4 relative">
                <div className="absolute left-[11px] top-[14px] bottom-[14px] w-px bg-outline-variant"></div>
                <div className="flex items-start gap-3 relative z-10">
                  <div className="w-6 h-6 rounded-full bg-secondary-fixed text-secondary flex items-center justify-center shrink-0 border border-surface-container-lowest mt-0.5">
                    <span className="material-symbols-outlined text-[14px]" style={{ fontVariationSettings: "'FILL' 1" }}>shopping_cart</span>
                  </div>
                  <div>
                    <div className="font-body-sm text-body-sm font-semibold text-on-surface">Target Domain</div>
                    <div className="font-body-sm text-body-sm text-on-surface-variant text-[13px]">Shopify Storefronts</div>
                  </div>
                </div>
                <div className="flex items-start gap-3 relative z-10">
                  <div className="w-6 h-6 rounded-full bg-secondary-fixed text-secondary flex items-center justify-center shrink-0 border border-surface-container-lowest mt-0.5">
                    <span className="material-symbols-outlined text-[14px]" style={{ fontVariationSettings: "'FILL' 1" }}>tune</span>
                  </div>
                  <div>
                    <div className="font-body-sm text-body-sm font-semibold text-on-surface">Filters</div>
                    <div className="font-body-sm text-body-sm text-on-surface-variant text-[13px]">$1M-$5M Rev, Missing Klaviyo</div>
                  </div>
                </div>
                <div className="flex items-start gap-3 relative z-10">
                  <div className="w-6 h-6 rounded-full bg-secondary-fixed text-secondary flex items-center justify-center shrink-0 border border-surface-container-lowest mt-0.5">
                    <span className="material-symbols-outlined text-[14px]" style={{ fontVariationSettings: "'FILL' 1" }}>video_camera_front</span>
                  </div>
                  <div>
                    <div className="font-body-sm text-body-sm font-semibold text-on-surface">Outreach Style</div>
                    <div className="font-body-sm text-body-sm text-on-surface-variant text-[13px]">Custom Loom Video Pitch</div>
                  </div>
                </div>
              </div>
            </div>
            <div className="p-4 bg-surface-container-lowest border-t border-surface-variant flex justify-between items-center mt-auto">
              <div className="flex -space-x-2">
                <div className="w-6 h-6 rounded-full bg-tertiary-fixed-dim border-2 border-surface-container-lowest"></div>
                <div className="w-6 h-6 rounded-full bg-primary-fixed-dim border-2 border-surface-container-lowest"></div>
              </div>
              <button className="text-secondary font-body-sm text-body-sm font-semibold hover:text-on-secondary-fixed-variant transition-colors flex items-center gap-1 group-hover:underline">
                Run Recipe <span className="material-symbols-outlined text-[18px]">arrow_forward</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
