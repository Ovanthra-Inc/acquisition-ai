'use client';

import React from 'react';
import { useParams } from 'next/navigation';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, Cell } from 'recharts';
import { Badge } from "@/components/ui/badge";
import { TrendingUp, Users, MessageSquare, MousePointer2 } from 'lucide-react';

const mockData = [
  { name: 'Variant A', open_rate: 0.58, reply_rate: 0.08, opens: 145, replies: 12 },
  { name: 'Variant B', open_rate: 0.79, reply_rate: 0.04, opens: 198, replies: 8 },
];

export default function ABTestPage() {
  const params = useParams();
  const campaignId = params.id;

  return (
    <div className="p-8 space-y-8 animate-in fade-in duration-700">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">Campaign Intelligence</h1>
          <p className="text-muted-foreground">A/B Performance Analysis for Campaign {campaignId}</p>
        </div>
        <Badge variant="outline" className="px-4 py-1 text-sm bg-primary/10 text-primary border-primary/20">
          Winning: Variant B
        </Badge>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card className="bg-card/50 backdrop-blur-sm">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium flex items-center gap-2">
              <TrendingUp className="w-4 h-4 text-emerald-500" />
              Winning Variant
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-emerald-500">Variant B</div>
            <p className="text-xs text-muted-foreground">+36% Open Rate</p>
          </CardContent>
        </Card>
        <Card className="bg-card/50 backdrop-blur-sm">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium flex items-center gap-2">
              <Users className="w-4 h-4 text-blue-500" />
              Total Reach
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">432</div>
            <p className="text-xs text-muted-foreground">Across 2 variants</p>
          </CardContent>
        </Card>
        <Card className="bg-card/50 backdrop-blur-sm">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium flex items-center gap-2">
              <MousePointer2 className="w-4 h-4 text-purple-500" />
              Avg Open Rate
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">68.5%</div>
            <p className="text-xs text-muted-foreground">High Engagement</p>
          </CardContent>
        </Card>
        <Card className="bg-card/50 backdrop-blur-sm">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium flex items-center gap-2">
              <MessageSquare className="w-4 h-4 text-orange-500" />
              Avg Reply Rate
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">6.0%</div>
            <p className="text-xs text-muted-foreground">Needs Optimization</p>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <Card className="border-primary/10 shadow-lg shadow-primary/5">
          <CardHeader>
            <CardTitle>Open Rate Comparison</CardTitle>
            <CardDescription>Percentage of leads who opened the email</CardDescription>
          </CardHeader>
          <CardContent className="h-[300px]">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={mockData}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="rgba(255,255,255,0.05)" />
                <XAxis dataKey="name" stroke="#888888" fontSize={12} tickLine={false} axisLine={false} />
                <YAxis stroke="#888888" fontSize={12} tickLine={false} axisLine={false} tickFormatter={(value) => `${(value * 100).toFixed(0)}%`} />
                <Tooltip 
                  contentStyle={{ backgroundColor: 'hsl(var(--card))', borderColor: 'hsl(var(--border))', color: 'hsl(var(--foreground))' }}
                  itemStyle={{ color: 'hsl(var(--primary))' }}
                />
                <Bar dataKey="open_rate" radius={[4, 4, 0, 0]}>
                  {mockData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={index === 1 ? 'hsl(var(--primary))' : 'hsl(var(--muted-foreground)/0.3)'} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        <Card className="border-primary/10 shadow-lg shadow-primary/5">
          <CardHeader>
            <CardTitle>Reply Rate Comparison</CardTitle>
            <CardDescription>Percentage of leads who responded</CardDescription>
          </CardHeader>
          <CardContent className="h-[300px]">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={mockData}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="rgba(255,255,255,0.05)" />
                <XAxis dataKey="name" stroke="#888888" fontSize={12} tickLine={false} axisLine={false} />
                <YAxis stroke="#888888" fontSize={12} tickLine={false} axisLine={false} tickFormatter={(value) => `${(value * 100).toFixed(0)}%`} />
                <Tooltip 
                  contentStyle={{ backgroundColor: 'hsl(var(--card))', borderColor: 'hsl(var(--border))', color: 'hsl(var(--foreground))' }}
                  itemStyle={{ color: 'hsl(var(--orange-500))' }}
                />
                <Bar dataKey="reply_rate" radius={[4, 4, 0, 0]}>
                  {mockData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={index === 0 ? '#f97316' : 'hsl(var(--muted-foreground)/0.3)'} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>
      </div>

      <Card className="border-primary/10">
        <CardHeader>
          <CardTitle>Style Pattern Insights</CardTitle>
          <CardDescription>AI recommendations based on the winning variant</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div className="flex items-start gap-4 p-4 rounded-lg bg-emerald-500/5 border border-emerald-500/10">
              <div className="mt-1 p-2 rounded-full bg-emerald-500/20 text-emerald-500">
                <TrendingUp className="w-4 h-4" />
              </div>
              <div>
                <h4 className="font-semibold text-emerald-500">Pattern Detected: Curiosity Gap</h4>
                <p className="text-sm text-muted-foreground mt-1">
                  Subject lines that pose a question or leave information incomplete are performing 36% better in initial opens.
                </p>
              </div>
            </div>
            <div className="flex items-start gap-4 p-4 rounded-lg bg-orange-500/5 border border-orange-500/10">
              <div className="mt-1 p-2 rounded-full bg-orange-500/20 text-orange-500">
                <MessageSquare className="w-4 h-4" />
              </div>
              <div>
                <h4 className="font-semibold text-orange-500">Drop-off Warning: Reply friction</h4>
                <p className="text-sm text-muted-foreground mt-1">
                  While Variant B has higher opens, Variant A has 2x higher reply rates. The Curiosity Gap subject lines might be attracting the wrong audience or setting misaligned expectations.
                </p>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
