import type { Metadata } from "next";
import "./globals.css";
import { SocketProvider } from "../components/providers/SocketProvider";
import { AuthProvider } from "../contexts/AuthContext";
import { AppProvider } from "../contexts/AppContext";
import { ThemeProvider } from "../components/ThemeProvider";
import { NextAuthProvider } from "../components/providers/NextAuthProvider";

export const metadata: Metadata = {
  title: "MigrationStudio — MuleSoft to AWS Lambda Migration Editor",
  description: "Enterprise migration editor for converting MuleSoft applications to AWS Lambda, API Gateway, and Step Functions",
};

export default async function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="font-sans antialiased text-gray-900 dark:text-gray-100 bg-white dark:bg-gray-950 transition-colors duration-200">
        <NextAuthProvider>
          <ThemeProvider attribute="class" defaultTheme="light" enableSystem={false}>
            <SocketProvider>
              <AuthProvider>
                <AppProvider>
                  {children}
                </AppProvider>
              </AuthProvider>
            </SocketProvider>
          </ThemeProvider>
        </NextAuthProvider>
      </body>
    </html>
  );
}
