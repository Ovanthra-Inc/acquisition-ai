"use client"

import * as React from "react"
import {
  LayoutDashboard,
  Users,
  Search,
  Mail,
  Zap,
  BarChart3,
  Settings,
  ShieldCheck,
  ChevronRight,
} from "lucide-react"

import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarGroup,
  SidebarGroupLabel,
  SidebarGroupContent,
} from "@/components/ui/sidebar"

const items = [
  {
    title: "Command Center",
    url: "/dashboard",
    icon: LayoutDashboard,
  },
  {
    title: "Intelligence",
    url: "/dashboard/intelligence",
    icon: Zap,
  },
  {
    title: "Outreach",
    url: "/dashboard/outreach",
    icon: Mail,
  },
  {
    title: "Leads",
    url: "/dashboard/leads",
    icon: Search,
  },
  {
    title: "Analytics",
    url: "/dashboard/analytics",
    icon: BarChart3,
  },
]

const adminItems = [
  {
    title: "Users",
    url: "/dashboard/admin/users",
    icon: Users,
  },
  {
    title: "Settings",
    url: "/dashboard/settings",
    icon: Settings,
  },
]

export function DashboardSidebar() {
  return (
    <Sidebar variant="inset">
      <SidebarHeader className="flex h-16 items-center px-6">
        <div className="flex items-center gap-2 font-bold text-xl tracking-tight">
          <div className="bg-primary text-primary-foreground p-1 rounded-md">
            <Zap className="size-5" />
          </div>
          <span>Ovanthra</span>
        </div>
      </SidebarHeader>
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Platform</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {items.map((item) => (
                <SidebarMenuItem key={item.title}>
                  <SidebarMenuButton asChild tooltip={item.title}>
                    <a href={item.url}>
                      <item.icon />
                      <span>{item.title}</span>
                    </a>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>

        <SidebarGroup>
          <SidebarGroupLabel>Management</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {adminItems.map((item) => (
                <SidebarMenuItem key={item.title}>
                  <SidebarMenuButton asChild tooltip={item.title}>
                    <a href={item.url}>
                      <item.icon />
                      <span>{item.title}</span>
                    </a>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
      <SidebarFooter className="p-4 border-t">
        <div className="flex items-center gap-3 px-2">
          <div className="size-8 rounded-full bg-muted flex items-center justify-center text-xs font-bold">
            JD
          </div>
          <div className="flex-1 overflow-hidden">
            <p className="text-sm font-medium truncate">John Doe</p>
            <p className="text-xs text-muted-foreground truncate">john@example.com</p>
          </div>
          <Settings className="size-4 text-muted-foreground cursor-pointer hover:text-foreground" />
        </div>
      </SidebarFooter>
    </Sidebar>
  )
}
