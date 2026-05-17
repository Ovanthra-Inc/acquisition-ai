"use client";

import { useTheme } from "next-themes";
import { useEffect, useState } from "react";

export function AppHeader() {
  const { theme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  return (
    <header className="bg-surface-container-lowest dark:bg-surface-container-low border-b border-outline-variant dark:border-outline shadow-sm flex justify-between items-center px-margin-page py-3 sticky top-0 z-40">
      {/* Left: Search */}
      <div className="flex-1 flex items-center">
        <div className="relative w-full max-w-md">
          <span className="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-outline-variant">
            search
          </span>
          <input
            type="text"
            className="w-full bg-surface-container-low border-none rounded py-2 pl-10 pr-4 text-body-sm font-body-sm focus:ring-1 focus:ring-secondary focus:bg-surface-container-lowest transition-colors"
            placeholder="Search leads, campaigns..."
          />
        </div>
      </div>

      {/* Right: Actions & Profile */}
      <div className="flex items-center gap-4">
        <button className="text-secondary font-body-base text-body-base font-semibold border border-secondary px-4 py-2 rounded hover:bg-surface-container-high transition-colors scale-95 active:scale-90 shadow-[inset_0_-1px_0_rgba(0,0,0,0.1)]">
          Add Leads
        </button>
        <button className="bg-secondary text-on-secondary font-body-base text-body-base font-semibold px-4 py-2 rounded hover:bg-on-secondary-fixed-variant transition-colors scale-95 active:scale-90 shadow-[inset_0_-1px_0_rgba(0,0,0,0.2)]">
          Run Recipe
        </button>
        <div className="h-6 w-[1px] bg-outline-variant mx-2"></div>
        
        {mounted && (
          <button
            onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
            className="text-on-surface-variant hover:bg-surface-container-high p-2 rounded-full transition-colors"
            aria-label="Toggle dark mode"
          >
            <span className="material-symbols-outlined">
              {theme === "dark" ? "light_mode" : "dark_mode"}
            </span>
          </button>
        )}

        <button className="text-on-surface-variant hover:bg-surface-container-high p-2 rounded-full transition-colors">
          <span className="material-symbols-outlined">notifications</span>
        </button>
        <button className="text-on-surface-variant hover:bg-surface-container-high p-2 rounded-full transition-colors">
          <span className="material-symbols-outlined">help</span>
        </button>
        <img
          src="https://lh3.googleusercontent.com/aida-public/AB6AXuD5VKqVx-lNY1GmxsLEdmmMl-BeCsINpbG85RKscnNCId6vU0_TQmULbmmmCVh3NGVGTuD0nG9Dmko_A1wcyyza1uadWsyfXitTltT06-QRgjYPTMFJ7n3MrlffHqKXBpIxAjQZS8RLXGPfToBXBUqD2TndFmW2NumunWuQn886gpR_faGhG-vm3LL-G4Z57Lt2efsPDiGqW5pm6lDJcdwxU-EBlDN5kEcdeA7jqaLuqXbtg9Sm3AdtiXdxDmTY9GfOPhO7jV8Zsd0"
          alt="User profile"
          className="w-8 h-8 rounded-full border border-outline-variant cursor-pointer ml-2"
        />
      </div>
    </header>
  );
}
