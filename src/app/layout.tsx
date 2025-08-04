import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Skerritt Economics & Consulting',
  description: 'Expert forensic economics and business valuation services for legal professionals throughout New England. Specializing in personal injury, employment litigation, and commercial disputes.',
  keywords: 'forensic economics, business valuation, expert witness, litigation support, personal injury economics, employment litigation, commercial damages',
  authors: [{ name: 'Christopher C. Skerritt' }],
  openGraph: {
    title: 'Skerritt Economics & Consulting',
    description: 'Expert forensic economics and business valuation services',
    url: 'https://skerritteconomics.com',
    siteName: 'Skerritt Economics & Consulting',
    images: [
      {
        url: '/Christopher-Skerritt-1-636x960-1.jpg',
        width: 636,
        height: 960,
        alt: 'Christopher C. Skerritt',
      },
    ],
    locale: 'en_US',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Skerritt Economics & Consulting',
    description: 'Expert forensic economics and business valuation services',
    creator: '@SkerrittEcon',
    images: ['/Christopher-Skerritt-1-636x960-1.jpg'],
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  )
}