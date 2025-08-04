import Image from 'next/image'
import Link from 'next/link'

export default function About() {
  return (
    <section className="py-20">
      <div className="container">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          <div>
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
              Christopher C. Skerritt, M.A.
            </h2>
            <div className="space-y-4 text-gray-600">
              <p>
                With over 30 years of experience, Christopher Skerritt is a leading forensic economist 
                serving attorneys throughout New England. His expertise spans personal injury, employment 
                litigation, and commercial disputes.
              </p>
              <p>
                As a court-qualified expert witness, Mr. Skerritt has provided testimony in numerous 
                high-stakes cases, delivering clear, defensible economic analyses that withstand scrutiny.
              </p>
              <p>
                Our team combines forensic economics with life care planning, vocational expertise, and 
                business valuation to provide comprehensive litigation support services.
              </p>
            </div>
            <div className="mt-8">
              <Link href="/about" className="btn btn-primary">
                Learn More About Us
              </Link>
            </div>
          </div>
          
          <div className="relative h-96 lg:h-full">
            <div className="bg-gradient-to-br from-blue-100 to-blue-200 rounded-lg h-full flex items-center justify-center">
              <span className="text-6xl">👨‍💼</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}