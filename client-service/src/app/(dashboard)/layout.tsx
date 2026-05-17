import { AppHeader } from "@/components/layout/AppHeader";
import { AppSidebar } from "@/components/layout/AppSidebar";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex h-screen overflow-hidden">
      <AppSidebar />
      <main className="ml-sidebar-width flex-1 flex flex-col h-screen overflow-hidden">
        <AppHeader />
        <div className="flex-1 overflow-y-auto bg-surface">
          {children}
        </div>
      </main>
    </div>
  );
}
