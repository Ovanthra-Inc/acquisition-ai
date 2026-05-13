import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
import { Sparkles, TrendingUp } from "lucide-react"

export function StyleIntelligence() {
  const stats = [
    { type: "Tone: Authoritative", success: 88, color: "bg-blue-500" },
    { type: "Hook: Question-based", success: 72, color: "bg-emerald-500" },
    { type: "Closing: Low-friction", success: 94, color: "bg-purple-500" },
  ];

  return (
    <Card className="h-full">
      <CardHeader>
        <div className="flex items-center justify-between">
          <div className="space-y-1">
            <CardTitle className="text-lg flex items-center gap-2">
              <Sparkles className="size-5 text-yellow-500" />
              Style Intelligence
            </CardTitle>
            <CardDescription>Winning patterns from the Personalization Vault.</CardDescription>
          </div>
          <TrendingUp className="size-5 text-muted-foreground" />
        </div>
      </CardHeader>
      <CardContent className="space-y-6">
        {stats.map((stat) => (
          <div key={stat.type} className="space-y-2">
            <div className="flex items-center justify-between text-sm">
              <span className="font-medium">{stat.type}</span>
              <span className="font-bold text-primary">{stat.success}% success</span>
            </div>
            <div className="flex items-center gap-4">
              <Progress value={stat.success} className={`h-2 flex-1`} />
            </div>
          </div>
        ))}
        <div className="mt-4 pt-4 border-t">
          <p className="text-[10px] uppercase font-bold text-muted-foreground tracking-widest mb-2">AI Recommendation</p>
          <div className="p-3 rounded-lg bg-primary/5 border border-primary/10">
            <p className="text-xs italic text-foreground/80">
              "Switch to 'Direct Value' hooks for the SaaS sector; they currently outperform 'Question' hooks by 14%."
            </p>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
