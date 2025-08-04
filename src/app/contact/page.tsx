import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Contact Skerritt Economics - Free Case Consultation | Skerritt Economics',
  description: 'Contact Christopher Skerritt for expert forensic economics and business valuation services. Free consultation for attorneys. Call (203) 605-2814.',
}

export default function ContactPage() {
  return (
    <div className="min-h-screen">
      {/* Contact Hero */}
      <section className="bg-gradient-to-br from-blue-900 via-blue-800 to-blue-700 text-white py-20">
        <div className="container">
          <h1 className="text-4xl md:text-5xl font-bold mb-4">
            Contact Skerritt Economics
          </h1>
          <p className="text-xl text-blue-100">
            Free Case Consultation for Attorneys
          </p>
        </div>
      </section>

      {/* Contact Content */}
      <section className="py-16">
        <div className="container">
          <div className="grid lg:grid-cols-2 gap-12">
            {/* Contact Form */}
            <div>
              <h2 className="text-3xl font-bold mb-6">Send Us a Message</h2>
              <form className="space-y-6">
                <div>
                  <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-2">
                    Your Name *
                  </label>
                  <input
                    type="text"
                    id="name"
                    name="name"
                    required
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
                
                <div>
                  <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-2">
                    Email Address *
                  </label>
                  <input
                    type="email"
                    id="email"
                    name="email"
                    required
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
                
                <div>
                  <label htmlFor="phone" className="block text-sm font-medium text-gray-700 mb-2">
                    Phone Number
                  </label>
                  <input
                    type="tel"
                    id="phone"
                    name="phone"
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
                
                <div>
                  <label htmlFor="caseType" className="block text-sm font-medium text-gray-700 mb-2">
                    Case Type
                  </label>
                  <select
                    id="caseType"
                    name="caseType"
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option value="">Select a case type...</option>
                    <option value="personal-injury">Personal Injury</option>
                    <option value="wrongful-death">Wrongful Death</option>
                    <option value="employment">Employment Litigation</option>
                    <option value="business">Business Valuation</option>
                    <option value="divorce">Divorce/Family Law</option>
                    <option value="other">Other</option>
                  </select>
                </div>
                
                <div>
                  <label htmlFor="message" className="block text-sm font-medium text-gray-700 mb-2">
                    Message *
                  </label>
                  <textarea
                    id="message"
                    name="message"
                    rows={5}
                    required
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="Please provide a brief description of your case..."
                  ></textarea>
                </div>
                
                <button
                  type="submit"
                  className="w-full btn btn-primary"
                >
                  Send Message
                </button>
              </form>
            </div>
            
            {/* Contact Information */}
            <div>
              <h2 className="text-3xl font-bold mb-6">Get in Touch</h2>
              
              <div className="space-y-6">
                <div className="bg-gray-50 p-6 rounded-lg">
                  <h3 className="text-xl font-semibold mb-3">Office Location</h3>
                  <p className="text-gray-600">
                    400 Putnam Pike Ste J<br />
                    Smithfield, RI 02917
                  </p>
                </div>
                
                <div className="bg-gray-50 p-6 rounded-lg">
                  <h3 className="text-xl font-semibold mb-3">Phone</h3>
                  <p className="text-gray-600">
                    <a href="tel:+12036052814" className="text-blue-600 hover:text-blue-700">
                      (203) 605-2814
                    </a>
                  </p>
                </div>
                
                <div className="bg-gray-50 p-6 rounded-lg">
                  <h3 className="text-xl font-semibold mb-3">Email</h3>
                  <p className="text-gray-600">
                    <a href="mailto:chris@skerritteconomics.com" className="text-blue-600 hover:text-blue-700">
                      chris@skerritteconomics.com
                    </a>
                  </p>
                </div>
                
                <div className="bg-gray-50 p-6 rounded-lg">
                  <h3 className="text-xl font-semibold mb-3">Office Hours</h3>
                  <p className="text-gray-600">
                    Monday - Friday: 9:00 AM - 5:00 PM<br />
                    Saturday - Sunday: By Appointment
                  </p>
                </div>
                
                <div className="bg-blue-50 border-2 border-blue-200 p-6 rounded-lg">
                  <h3 className="text-xl font-semibold mb-3 text-blue-900">Free Consultation</h3>
                  <p className="text-gray-700">
                    We offer free initial consultations for attorneys. Contact us to discuss 
                    your case and learn how our expertise can strengthen your litigation strategy.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Service Areas */}
      <section className="py-16 bg-gray-50">
        <div className="container">
          <h2 className="text-3xl font-bold mb-8 text-center">Service Areas</h2>
          <div className="grid md:grid-cols-3 gap-6 max-w-4xl mx-auto">
            <div className="text-center">
              <h3 className="font-semibold text-lg mb-2">Rhode Island</h3>
              <p className="text-gray-600">Providence, Warwick, Cranston, Pawtucket, Newport</p>
            </div>
            <div className="text-center">
              <h3 className="font-semibold text-lg mb-2">Massachusetts</h3>
              <p className="text-gray-600">Boston, Worcester, Springfield, Cambridge, Lowell</p>
            </div>
            <div className="text-center">
              <h3 className="font-semibold text-lg mb-2">Connecticut</h3>
              <p className="text-gray-600">Hartford, New Haven, Stamford, Bridgeport, Waterbury</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}