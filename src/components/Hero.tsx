import Link from 'next/link'

export default function Hero() {
  return (
    <section className="relative bg-gradient-to-br from-blue-900 via-blue-800 to-blue-700 text-white">
      <div className="container py-24 md:py-32">
        <div className="max-w-3xl">
          <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold mb-6">
            Expert Forensic Economics & Business Valuation
          </h1>
          <p className="text-xl md:text-2xl mb-8 text-blue-100">
            Trusted by attorneys throughout New England for accurate economic damage analysis and expert witness testimony
          </p>
          <div className="flex flex-col sm:flex-row gap-4">
            <Link href="/contact" className="btn btn-primary bg-white text-blue-900 hover:bg-gray-100">
              Get Free Consultation
            </Link>
            <Link href="/services" className="btn btn-secondary border-white text-white hover:bg-blue-800">
              View Services
            </Link>
          </div>
        </div>
      </div>
    </section>
  )
}