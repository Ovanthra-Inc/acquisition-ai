import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { ChevronRight, MessageSquare } from "lucide-react"

export function InterestedLeads() {
  // In a real app, this would use useQuery to fetch from /api/v1/dashboard/interested
  const leads = [
    { id: 1, name: "Sarah Chen", company: "TechFlow", reason: "Asked for pricing and a demo next Tuesday.", time: "2h ago" },
    { id: 2, name: "Marcus Thorne", company: "Stellar AI", reason: "Interested in the enterprise plan for 50 seats.", time: "5h ago" },
  ];

  return (
    <Card className="border-emerald-200 dark:border-emerald-900/30">
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <div className="space-y-1">
          <CardTitle className="text-lg flex items-center gap-2">
            <MessageSquare className="size-5 text-emerald-500" />
            AI Classified: Interested
          </CardTitle>
          <CardDescription>High-intent leads found by the Closer agent.</CardDescription>
        </div>
        <Badge variant="outline" className="bg-emerald-500/10 text-emerald-600 border-emerald-500/20">
          {leads.length} New
        </Badge>
      </CardHeader>
      <CardContent className="pt-4">
        <div className="space-y-4">
          {leads.map((lead) => (
            <div key={lead.id} className="flex items-start gap-4 p-3 rounded-xl bg-muted/30 hover:bg-muted/50 transition-colors group cursor-pointer border border-transparent hover:border-emerald-500/20">
              <div className="flex-1">
                <div className="flex items-center justify-between mb-1">
                  <p className="text-sm font-bold">{lead.name}</p>
                  <p className="text-[10px] text-muted-foreground uppercase font-bold">{lead.time}</p>
                </div>
                <p className="text-xs text-muted-foreground mb-2">{lead.company}</p>
                <div className="bg-background/50 p-2 rounded-lg border border-emerald-500/10 italic text-[11px] text-foreground/80">
                  "{lead.reason}"
                </div>
              </div>
              <ChevronRight className="size-4 text-muted-foreground mt-1 group-hover:text-emerald-500 transition-colors" />
            </div>
          ))}
          <Button variant="ghost" className="w-full text-xs text-muted-foreground hover:text-primary">
            View All Interested Leads
          </Button>
        </div>
      </CardContent>
    </Card>
  )
}
