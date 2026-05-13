"use client"

import * as React from "react"
import { 
  Rocket, 
  Zap, 
  TrendingUp, 
  Users, 
  Mail, 
  MessageSquare, 
  AlertCircle,
  ChevronRight,
  Plus,
  Play,
  ShieldCheck,
  Sparkles
} from "lucide-react"

import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
import { InterestedLeads } from "@/components/dashboard/interested-leads"
import { StyleIntelligence } from "@/components/dashboard/style-intelligence"
import { useAuth } from "@/hooks/use-auth"
import { useEffect, useState } from "react"

export default function DashboardPage() {
  const { user } = useAuth();
  const [monologue, setMonologue] = useState<any[]>([]);

  useEffect(() => {
    if (user?.user_id) {
      const ws = new WebSocket(`ws://localhost/api/ws/${user.user_id}`);
      ws.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          if (data.type === 'agent_monologue') {
            setMonologue(prev => [data, ...prev].slice(0, 5));
          }
        } catch (e) {
          console.error("WS error", e);
        }
      };
      return () => ws.close();
    }
  }, [user]);

  return (
    <div className="space-y-8 animate-in fade-in duration-500 pb-10">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">Command Center</h1>
          <p className="text-muted-foreground">Orchestrating multi-channel acquisition and intent-based closing.</p>
        </div>
        <div className="flex gap-2">
          <Button variant="outline" size="sm">
            <Plus className="mr-2 h-4 w-4" /> Add Leads
          </Button>
          <Button size="sm">
            <Play className="mr-2 h-4 w-4" /> Run Recipe
          </Button>
        </div>
      </div>

      {/* Hero: Multi-Channel Status */}
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <Card className="bg-primary/5 border-primary/20">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Domain Health</CardTitle>
            <ShieldCheck className="h-4 w-4 text-emerald-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">98%</div>
            <p className="text-[10px] text-muted-foreground uppercase mt-1 tracking-wider font-bold">Excellent Reputation</p>
            <Progress value={98} className="h-1 mt-3" />
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">LinkedIn Outreach</CardTitle>
            <Users className="h-4 w-4 text-blue-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">45</div>
            <p className="text-xs text-muted-foreground">Requests sent today</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Email Velocity</CardTitle>
            <Mail className="h-4 w-4 text-primary" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">1.2k</div>
            <p className="text-xs text-muted-foreground">Active sequences</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">AI Conversions</CardTitle>
            <TrendingUp className="h-4 w-4 text-emerald-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">8.4%</div>
            <p className="text-xs text-muted-foreground">+2.1% from A/B tests</p>
          </CardContent>
        </Card>
      </div>

      <div className="grid gap-4 lg:grid-cols-7">
        {/* Pipeline & Agent Monologue */}
        <Card className="lg:col-span-4 overflow-hidden">
          <CardHeader className="border-b bg-muted/30">
            <CardTitle>Acquisition Intelligence</CardTitle>
            <CardDescription>Live feed and lead funnel metrics.</CardDescription>
          </CardHeader>
          <CardContent className="p-0">
            <div className="p-6 border-b">
              <div className="grid grid-cols-4 gap-4 text-center">
                <div className="space-y-1">
                  <p className="text-[10px] font-bold text-muted-foreground uppercase">Leads</p>
                  <p className="text-2xl font-bold">1,420</p>
                </div>
                <div className="space-y-1">
                  <p className="text-[10px] font-bold text-muted-foreground uppercase">Engaged</p>
                  <p className="text-2xl font-bold">890</p>
                </div>
                <div className="space-y-1 text-primary">
                  <p className="text-[10px] font-bold uppercase">Replies</p>
                  <p className="text-2xl font-bold">342</p>
                </div>
                <div className="space-y-1 text-emerald-500">
                  <p className="text-[10px] font-bold uppercase">Closed</p>
                  <p className="text-2xl font-bold">45</p>
                </div>
              </div>
            </div>
            
            <div className="p-6">
              <div className="flex items-center gap-2 mb-4">
                <span className="relative flex h-2 w-2">
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                  <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                </span>
                <h3 className="text-sm font-bold uppercase tracking-widest text-muted-foreground">Live Agent Feed</h3>
              </div>
              <div className="space-y-3">
                {monologue.length === 0 ? (
                  <p className="text-xs text-muted-foreground italic">Agent is currently idle. Waiting for next run...</p>
                ) : (
                  monologue.map((item, idx) => (
                    <div key={idx} className="flex items-start gap-3 animate-in slide-in-from-left duration-300">
                      <div className="size-1.5 mt-1.5 rounded-full bg-primary" />
                      <div>
                        <p className="text-xs font-medium leading-none">{item.message}</p>
                        <p className="text-[10px] text-muted-foreground mt-1">{new Date(item.timestamp).toLocaleTimeString()}</p>
                      </div>
                    </div>
                  ))
                )}
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Style Intelligence */}
        <div className="lg:col-span-3">
          <StyleIntelligence />
        </div>
      </div>

      <div className="grid gap-4 lg:grid-cols-7">
        {/* High-Intent "Interested" Leads */}
        <div className="lg:col-span-4">
          <InterestedLeads />
        </div>

        {/* Hero Section: Quick Actions */}
        <Card className="lg:col-span-3 bg-primary text-primary-foreground overflow-hidden relative">
          <div className="absolute top-0 right-0 p-8 opacity-10">
            <Rocket className="size-32 rotate-12" />
          </div>
          <CardHeader>
            <CardTitle className="text-2xl">Deploy Engine</CardTitle>
            <CardDescription className="text-primary-foreground/70">
              Start a new multi-channel acquisition campaign.
            </CardDescription>
          </CardHeader>
          <CardContent>
            <Button variant="secondary" className="w-full mt-4 font-bold shadow-lg">
              <Zap className="mr-2 h-4 w-4 fill-current" /> Launch Campaign
            </Button>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
