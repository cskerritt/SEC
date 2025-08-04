import type { Metadata } from 'next'
import Image from 'next/image'

export const metadata: Metadata = {
  title: 'About Christopher Skerritt - Forensic Economist & Business Valuation Expert | Skerritt Economics',
  description: 'Meet Christopher T. Skerritt, CRC, CLCP - Expert forensic economist and business valuator serving legal professionals throughout New England.',
}

export default function AboutPage() {
  return (
    <div className="min-h-screen">
      {/* About Hero */}
      <section className="bg-gradient-to-br from-blue-900 via-blue-800 to-blue-700 text-white py-20">
        <div className="container">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div>
              <h1 className="text-4xl md:text-5xl font-bold mb-4">
                Christopher Skerritt, M.Ed, MBA, CRC, CLCP
              </h1>
              <p className="text-2xl text-blue-100 mb-4">Principal Economic Consultant</p>
              <p className="text-lg text-blue-100">
                Experienced professional providing expert economic analysis and business valuation 
                services to attorneys and businesses throughout New England. Court-tested professional expertise.
              </p>
            </div>
            <div className="bg-white/10 rounded-lg p-8 text-center">
              <div className="text-6xl mb-4">👨‍💼</div>
              <p className="text-lg">Christopher Skerritt</p>
            </div>
          </div>
        </div>
      </section>

      {/* Professional Summary */}
      <section className="py-16 bg-white">
        <div className="container">
          <h2 className="text-3xl font-bold mb-8">Professional Summary</h2>
          <div className="prose max-w-none text-gray-600 space-y-4">
            <p>
              Christopher Skerritt brings extensive experience in vocational rehabilitation, 
              forensic economics, and business valuation to the legal community. As Principal 
              Economist at Skerritt Economics and Consulting, he provides comprehensive economic 
              analysis, vocational assessment, and life care planning services.
            </p>
            <p>
              Based in Smithfield, Rhode Island (400 Putnam Pike Ste J, Smithfield, RI 02917), 
              Chris serves as a vocational counselor, economist, and consultant evaluator. His 
              expertise spans labor market analysis, transferable skills evaluation, economic 
              loss assessments, business valuation, and expert witness testimony across multiple 
              jurisdictions.
            </p>
          </div>
        </div>
      </section>

      {/* Education & Credentials */}
      <section className="py-16 bg-gray-50">
        <div className="container">
          <h2 className="text-3xl font-bold mb-12 text-center">Education & Professional Credentials</h2>
          
          <div className="grid md:grid-cols-2 gap-12">
            <div>
              <h3 className="text-2xl font-semibold mb-6">Education</h3>
              <ul className="space-y-4">
                <li className="bg-white p-4 rounded-lg shadow">
                  <strong className="text-blue-900">Master of Business Administration (MBA)</strong>
                  <br />Bryant University, Smithfield, Rhode Island, 2024
                </li>
                <li className="bg-white p-4 rounded-lg shadow">
                  <strong className="text-blue-900">Master of Education in Rehabilitation Counseling</strong>
                  <br />Springfield College, Springfield, Massachusetts, 2016
                </li>
                <li className="bg-white p-4 rounded-lg shadow">
                  <strong className="text-blue-900">Bachelor of Science in Communication Disorders</strong>
                  <br />Springfield College, Springfield, Massachusetts, 2015
                </li>
              </ul>
            </div>
            
            <div>
              <h3 className="text-2xl font-semibold mb-6">Key Certifications</h3>
              <ul className="space-y-3">
                <li className="bg-white p-3 rounded-lg shadow">
                  <strong>CRC</strong> - Certified Rehabilitation Counselor
                </li>
                <li className="bg-white p-3 rounded-lg shadow">
                  <strong>CLCP</strong> - Certified Life Care Planner
                </li>
                <li className="bg-white p-3 rounded-lg shadow">
                  <strong>FVE</strong> - Forensic Vocational Expert
                </li>
                <li className="bg-white p-3 rounded-lg shadow">
                  <strong>CVE</strong> - Certified Vocational Evaluator
                </li>
                <li className="bg-white p-3 rounded-lg shadow">
                  <strong>ABVE/F</strong> - Fellow of American Board of Vocational Experts
                </li>
                <li className="bg-white p-3 rounded-lg shadow">
                  <strong>MSCC</strong> - Medicare Set Aside Certified Consultant
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Court Experience */}
      <section className="py-16 bg-white">
        <div className="container">
          <h2 className="text-3xl font-bold mb-12 text-center">Court Experience & Jurisdictions</h2>
          
          <div className="grid md:grid-cols-2 gap-12">
            <div className="bg-gray-50 p-8 rounded-lg">
              <h3 className="text-2xl font-semibold mb-6">State Courts</h3>
              <ul className="space-y-2 text-gray-600">
                <li>• Rhode Island Superior Court</li>
                <li>• Massachusetts Superior Court</li>
                <li>• Connecticut Superior Court</li>
                <li>• New Hampshire Superior Court</li>
                <li>• Workers&apos; Compensation Courts (RI, MA)</li>
              </ul>
            </div>
            
            <div className="bg-gray-50 p-8 rounded-lg">
              <h3 className="text-2xl font-semibold mb-6">Federal Courts</h3>
              <ul className="space-y-2 text-gray-600">
                <li>• U.S. District Court for Rhode Island</li>
                <li>• U.S. District Court for Massachusetts</li>
                <li>• U.S. District Court for Connecticut</li>
                <li>• U.S. District Court for New Hampshire</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-blue-900 text-white">
        <div className="container text-center">
          <h2 className="text-3xl font-bold mb-4">Ready to Discuss Your Case?</h2>
          <p className="text-xl mb-8 text-blue-100">
            Contact Christopher Skerritt for expert economic analysis and testimony support.
          </p>
          <a href="/contact" className="btn btn-primary bg-white text-blue-900 hover:bg-gray-100">
            Schedule Consultation
          </a>
        </div>
      </section>
    </div>
  )
}