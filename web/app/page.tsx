import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Sidebar } from "@/components/sidebar";

export default function Home() {
  return (
    <div className="flex min-h-screen bg-zinc-50 dark:bg-black">
      <Sidebar />
      <main className="flex-1 flex items-center justify-center p-4">
        <Card className="w-full max-w-md">
          <CardHeader>
            <CardTitle>Hello World</CardTitle>
          </CardHeader>
          <CardContent>
            <p>
              This is a simple hello world message using NextJS, TypeScript,
              Shadcn, and TailwindCSS.
            </p>
          </CardContent>
        </Card>
      </main>
    </div>
  );
}
