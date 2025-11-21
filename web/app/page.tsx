import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default function Home() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 dark:bg-black">
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
    </div>
  );
}
