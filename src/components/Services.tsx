import Link from 'next/link'

const services = [
  {
    title: 'Forensic Economics',
    description: 'Economic damage analysis for personal injury, wrongful death, and employment litigation cases',
    icon: '📊',
    href: '/services/forensic-economics',
  },
  {
    title: 'Business Valuation',
    description: 'Expert business appraisal for commercial litigation, divorce, and partnership disputes',
    icon: '💼',
    href: '/services/business-valuation',
  },
  {
    title: 'Life Care Planning',
    description: 'CLCP-certified future medical cost projections for catastrophic injury cases',
    icon: '🏥',
    href: '/services/life-care-planning',
  },
  {
    title: 'Vocational Expert',
    description: 'Professional vocational rehabilitation and employability assessments',
    icon: '👔',
    href: '/services/vocational-expert',
  },
]

export default function Services() {
  return (
    <section className="py-20 bg-gray-50">
      <div className="container">
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            Our Expert Services
          </h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Comprehensive litigation support services backed by decades of experience
          </p>
        </div>
        
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          {services.map((service) => (
            <div key={service.title} className="bg-white rounded-lg shadow-lg p-6 hover:shadow-xl transition-shadow">
              <div className="text-4xl mb-4">{service.icon}</div>
              <h3 className="text-xl font-semibold mb-3 text-gray-900">
                {service.title}
              </h3>
              <p className="text-gray-600 mb-4">
                {service.description}
              </p>
              <Link href={service.href} className="text-blue-600 font-semibold hover:text-blue-700">
                Learn More →
              </Link>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}