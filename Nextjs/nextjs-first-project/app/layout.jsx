import Navbar from "@/components/Navbar";
import "./globals.css";
import { Inter } from "next/font/google";

export const metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <Navbar />
        <main className="container mx-auto h-75 flex justify-center items-center">
          {children}
        </main>
      </body>
    </html>
  );
}