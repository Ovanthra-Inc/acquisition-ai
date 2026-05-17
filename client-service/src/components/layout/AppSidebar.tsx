"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { cn } from "@/lib/utils";

const NAV_ITEMS = [
  { href: "/command-center", icon: "dashboard", label: "Dashboard" },
  { href: "/recipes", icon: "auto_awesome", label: "Recipes" },
  { href: "/leads", icon: "person_search", label: "Leads" },
  { href: "/campaigns", icon: "campaign", label: "Campaigns" },
  { href: "/conversations", icon: "forum", label: "Conversations" },
  { href: "/pipeline", icon: "account_tree", label: "Pipeline" },
  { href: "/ai-agent", icon: "smart_toy", label: "AI Agent" },
  { href: "/analytics", icon: "analytics", label: "Analytics" },
  { href: "/settings", icon: "settings", label: "Settings" },
];

export function AppSidebar() {
  const pathname = usePathname();

  return (
    <aside className="bg-inverse-surface dark:bg-primary-container fixed left-0 top-0 h-screen w-sidebar-width flex flex-col py-stack-lg z-50">
      {/* Header */}
      <div className="px-6 pb-8">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded bg-surface-container-highest flex items-center justify-center text-on-surface">
            <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>
              corporate_fare
            </span>
          </div>
          <div>
            <h2 className="font-heading-md text-heading-md font-black text-secondary-fixed">Acquisition HQ</h2>
            <p className="font-body-sm text-body-sm text-outline-variant">Enterprise Plan</p>
          </div>
        </div>
      </div>

      {/* Navigation */}
      <nav className="flex-1 overflow-y-auto flex flex-col gap-1">
        {NAV_ITEMS.map((item) => {
          const isActive = pathname.startsWith(item.href);

          return (
            <Link
              key={item.href}
              href={item.href}
              className={cn(
                "py-3 px-4 flex items-center gap-3 transition-all duration-200 ease-in-out border-l-4",
                isActive
                  ? "bg-secondary-container/20 text-on-secondary-container border-secondary"
                  : "text-outline-variant hover:text-surface-bright hover:bg-on-primary-fixed-variant border-transparent"
              )}
            >
              <span
                className={cn("material-symbols-outlined", isActive && "text-secondary")}
                style={isActive ? { fontVariationSettings: "'FILL' 1" } : undefined}
              >
                {item.icon}
              </span>
              <span className={cn("font-body-base text-body-base", isActive && "font-semibold")}>
                {item.label}
              </span>
            </Link>
          );
        })}
      </nav>

      {/* Footer CTA */}
      <div className="px-6 pt-6 mt-auto">
        <button className="w-full bg-secondary text-on-secondary font-body-sm text-body-sm font-semibold py-2 rounded hover:bg-on-secondary-fixed-variant transition-colors shadow-[inset_0_-1px_0_rgba(0,0,0,0.2)]">
          Upgrade Power
        </button>
      </div>
    </aside>
  );
}
