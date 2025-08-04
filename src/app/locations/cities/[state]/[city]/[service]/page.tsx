import { notFound } from 'next/navigation'
import type { Metadata } from 'next'

// Define service types
const SERVICES = [
  'forensic-economist',
  'business-valuation-analyst',
  'life-care-planner',
  'vocational-expert'
] as const

type Service = typeof SERVICES[number]

interface PageProps {
  params: {
    state: string
    city: string
    service: Service
  }
}

// Generate metadata for SEO
export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const cityName = params.city.split('-').map(word => 
    word.charAt(0).toUpperCase() + word.slice(1)
  ).join(' ')
  
  const stateName = params.state.toUpperCase()
  const serviceName = params.service.split('-').map(word => 
    word.charAt(0).toUpperCase() + word.slice(1)
  ).join(' ')

  return {
    title: `${serviceName} in ${cityName}, ${stateName} | Skerritt Economics`,
    description: `Expert ${serviceName.toLowerCase()} services in ${cityName}, ${stateName}. Trusted by attorneys for accurate economic analysis and expert witness testimony.`,
    openGraph: {
      title: `${serviceName} - ${cityName}, ${stateName}`,
      description: `Professional ${serviceName.toLowerCase()} services in ${cityName}`,
    },
  }
}

export default function CityServicePage({ params }: PageProps) {
  const cityName = params.city.split('-').map(word => 
    word.charAt(0).toUpperCase() + word.slice(1)
  ).join(' ')
  
  const stateName = params.state.toUpperCase()
  const serviceName = params.service.split('-').map(word => 
    word.charAt(0).toUpperCase() + word.slice(1)
  ).join(' ')

  // Validate service type
  if (!SERVICES.includes(params.service)) {
    notFound()
  }

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-blue-900 via-blue-800 to-blue-700 text-white py-20">
        <div className="container">
          <h1 className="text-4xl md:text-5xl font-bold mb-4">
            {serviceName} in {cityName}, {stateName}
          </h1>
          <p className="text-xl text-blue-100 max-w-3xl">
            Providing expert {serviceName.toLowerCase()} services to attorneys and law firms 
            throughout {cityName} and the greater {stateName} area.
          </p>
        </div>
      </section>

      {/* Services Section */}
      <section className="py-16 bg-gray-50">
        <div className="container">
          <h2 className="text-3xl font-bold mb-8 text-center">
            Our {serviceName} Services in {cityName}
          </h2>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div className="bg-white p-6 rounded-lg shadow-lg">
              <h3 className="text-xl font-semibold mb-3">Economic Analysis</h3>
              <p className="text-gray-600">
                Comprehensive economic damage calculations for cases in {cityName} courts.
              </p>
            </div>
            
            <div className="bg-white p-6 rounded-lg shadow-lg">
              <h3 className="text-xl font-semibold mb-3">Expert Testimony</h3>
              <p className="text-gray-600">
                Court-qualified expert witness services for {stateName} state and federal courts.
              </p>
            </div>
            
            <div className="bg-white p-6 rounded-lg shadow-lg">
              <h3 className="text-xl font-semibold mb-3">Case Consultation</h3>
              <p className="text-gray-600">
                Free initial consultation for attorneys in the {cityName} area.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 bg-blue-900 text-white">
        <div className="container text-center">
          <h2 className="text-3xl font-bold mb-4">
            Need a {serviceName} in {cityName}?
          </h2>
          <p className="text-xl mb-8 text-blue-100">
            Contact us today for a free consultation
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <a href="/contact" className="btn btn-primary bg-white text-blue-900 hover:bg-gray-100">
              Get Free Consultation
            </a>
            <a href="tel:+12036052814" className="btn btn-secondary border-white text-white hover:bg-blue-800">
              Call (203) 605-2814
            </a>
          </div>
        </div>
      </section>
    </div>
  )
}

// Generate static paths for all city/service combinations
export async function generateStaticParams() {
  // This would normally read from a database or JSON file
  // For now, returning empty array means pages are generated on-demand
  return []
}