import localFont from "next/font/local";
import "@/styles/globals.css";

const iransans = localFont({
  src: [
    {
      path: "../assets/fonts/iransans/woff2/IRANSansXFaNum-Light.woff2",
      weight: "300",
    },
    {
      path: "../assets/fonts/iransans/woff2/IRANSansXFaNum-Regular.woff2",
      weight: "400",
    },
    {
      path: "../assets/fonts/iransans/woff2/IRANSansXFaNum-Medium.woff2",
      weight: "500",
    },
    {
      path: "../assets/fonts/iransans/woff2/IRANSansXFaNum-Bold.woff2",
      weight: "700",
    },
    {
      path: "../assets/fonts/iransans/woff2/IRANSansXFaNum-Black.woff2",
      weight: "900",
    },
  ],
  variable: "--font-iransans",
});

export const metadata = {
  title: "Sofre | Online Restaurant Menu",
  description: "an online restaurant menu application",
};

export default function RootLayout({ children }) {
  return (
    <html lang="fa" dir="rtl">
      <body className={`${iransans.variable} font-sans`}>{children}</body>
    </html>
  );
}
