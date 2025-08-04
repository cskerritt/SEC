import Link from 'next/link'

export default function CTA() {
  return (
    <section className="py-20 bg-blue-900 text-white">
      <div className="container text-center">
        <h2 className="text-3xl md:text-4xl font-bold mb-4">
          Need Expert Economic Analysis?
        </h2>
        <p className="text-xl mb-8 text-blue-100 max-w-2xl mx-auto">
          Get a free consultation to discuss your case and learn how our expertise can strengthen your litigation strategy
        </p>
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <Link href="/contact" className="btn btn-primary bg-white text-blue-900 hover:bg-gray-100">
            Schedule Consultation
          </Link>
          <a href="tel:+12036052814" className="btn btn-secondary border-white text-white hover:bg-blue-800">
            Call (203) 605-2814
          </a>
        </div>
      </div>
    </section>
  )
}