import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Resources for Attorneys | Skerritt Economics',
  description: 'Expert resources for attorneys including economic damage calculators, articles on forensic economics, and litigation support materials.',
}

export default function ResourcesPage() {
  return (
    <div className="min-h-screen">
      {/* Resources Hero */}
      <section className="bg-gradient-to-br from-blue-900 via-blue-800 to-blue-700 text-white py-20">
        <div className="container">
          <h1 className="text-4xl md:text-5xl font-bold mb-4">
            Resources for Legal Professionals
          </h1>
          <p className="text-xl text-blue-100">
            Tools, guides, and information to support your litigation strategy
          </p>
        </div>
      </section>

      {/* Resources Content */}
      <section className="py-16">
        <div className="container">
          <div className="grid lg:grid-cols-3 gap-8">
            {/* Economic Calculators */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-2xl font-bold mb-4 text-blue-900">Economic Calculators</h2>
              <ul className="space-y-3">
                <li>
                  <a href="#" className="text-blue-600 hover:text-blue-700 font-medium">
                    Present Value Calculator
                  </a>
                </li>
                <li>
                  <a href="#" className="text-blue-600 hover:text-blue-700 font-medium">
                    Lost Earnings Calculator
                  </a>
                </li>
                <li>
                  <a href="#" className="text-blue-600 hover:text-blue-700 font-medium">
                    Life Expectancy Tables
                  </a>
                </li>
                <li>
                  <a href="#" className="text-blue-600 hover:text-blue-700 font-medium">
                    Worklife Expectancy Calculator
                  </a>
                </li>
              </ul>
            </div>

            {/* Articles & Guides */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-2xl font-bold mb-4 text-blue-900">Articles & Guides</h2>
              <ul className="space-y-3">
                <li>
                  <a href="#" className="text-blue-600 hover:text-blue-700 font-medium">
                    Understanding Economic Damages
                  </a>
                </li>
                <li>
                  <a href="#" className="text-blue-600 hover:text-blue-700 font-medium">
                    Vocational Assessment in PI Cases
                  </a>
                </li>
                <li>
                  <a href="#" className="text-blue-600 hover:text-blue-700 font-medium">
                    Life Care Planning Basics
                  </a>
                </li>
                <li>
                  <a href="#" className="text-blue-600 hover:text-blue-700 font-medium">
                    Business Valuation Methods
                  </a>
                </li>
              </ul>
            </div>

            {/* Legal Resources */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-2xl font-bold mb-4 text-blue-900">Legal Resources</h2>
              <ul className="space-y-3">
                <li>
                  <a href="#" className="text-blue-600 hover:text-blue-700 font-medium">
                    Federal Court Rules
                  </a>
                </li>
                <li>
                  <a href="#" className="text-blue-600 hover:text-blue-700 font-medium">
                    State Court Guidelines
                  </a>
                </li>
                <li>
                  <a href="#" className="text-blue-600 hover:text-blue-700 font-medium">
                    Expert Witness Standards
                  </a>
                </li>
                <li>
                  <a href="#" className="text-blue-600 hover:text-blue-700 font-medium">
                    Daubert Standards Guide
                  </a>
                </li>
              </ul>
            </div>
          </div>

          {/* Publications Section */}
          <div className="mt-16">
            <h2 className="text-3xl font-bold mb-8 text-center">Recent Publications</h2>
            <div className="grid md:grid-cols-2 gap-8">
              <div className="bg-gray-50 p-6 rounded-lg">
                <h3 className="text-xl font-semibold mb-3">
                  Use of AI in Rehabilitation Counseling
                </h3>
                <p className="text-gray-600 mb-4">
                  Skerritt, C., & Wolstein, D. (2023). The Rehabilitation Professional, 31(2), pp. 19-26.
                </p>
                <a href="#" className="text-blue-600 hover:text-blue-700 font-medium">
                  Read Article →
                </a>
              </div>

              <div className="bg-gray-50 p-6 rounded-lg">
                <h3 className="text-xl font-semibold mb-3">
                  AI for Enhanced Life Care Planning
                </h3>
                <p className="text-gray-600 mb-4">
                  Bourgeois, P., Allison, A., & Skerritt, C. (2024). Journal of Life Care Planning, 22(1).
                </p>
                <a href="#" className="text-blue-600 hover:text-blue-700 font-medium">
                  Read Article →
                </a>
              </div>
            </div>
          </div>

          {/* Downloads Section */}
          <div className="mt-16">
            <h2 className="text-3xl font-bold mb-8 text-center">Downloadable Resources</h2>
            <div className="grid md:grid-cols-3 gap-6">
              <div className="bg-white border-2 border-gray-200 rounded-lg p-6 text-center">
                <div className="text-4xl mb-4">📄</div>
                <h3 className="font-semibold mb-2">CV & Qualifications</h3>
                <p className="text-gray-600 text-sm mb-4">Christopher Skerritt&apos;s complete CV</p>
                <a href="#" className="btn btn-primary text-sm">
                  Download PDF
                </a>
              </div>

              <div className="bg-white border-2 border-gray-200 rounded-lg p-6 text-center">
                <div className="text-4xl mb-4">📊</div>
                <h3 className="font-semibold mb-2">Fee Schedule</h3>
                <p className="text-gray-600 text-sm mb-4">Current rates and services</p>
                <a href="#" className="btn btn-primary text-sm">
                  Download PDF
                </a>
              </div>

              <div className="bg-white border-2 border-gray-200 rounded-lg p-6 text-center">
                <div className="text-4xl mb-4">📋</div>
                <h3 className="font-semibold mb-2">Retention Agreement</h3>
                <p className="text-gray-600 text-sm mb-4">Standard engagement terms</p>
                <a href="#" className="btn btn-primary text-sm">
                  Download PDF
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 bg-blue-900 text-white">
        <div className="container text-center">
          <h2 className="text-3xl font-bold mb-4">Need Expert Analysis?</h2>
          <p className="text-xl mb-8 text-blue-100">
            Contact us for a free consultation about your case
          </p>
          <a href="/contact" className="btn btn-primary bg-white text-blue-900 hover:bg-gray-100">
            Get Free Consultation
          </a>
        </div>
      </section>
    </div>
  )
}