<?php
/**
 * Template Name: Contact Page
 * 
 * @package Skerritt_Economics
 */

get_header(); ?>

<main id="primary" class="site-main contact-page">
    <?php while ( have_posts() ) : the_post(); ?>
        <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
            <header class="page-header">
                <div class="container">
                    <h1 class="page-title"><?php the_title(); ?></h1>
                    <?php if ( function_exists( 'yoast_breadcrumb' ) ) {
                        yoast_breadcrumb( '<nav class="breadcrumb" aria-label="Breadcrumb">', '</nav>' );
                    } ?>
                </div>
            </header>

            <div class="page-content">
                <div class="container">
                    <div class="contact-intro">
                        <?php the_content(); ?>
                    </div>

                    <div class="contact-grid">
                        <div class="contact-form-section">
                            <h2>Send a Message</h2>
                            <?php 
                            // Check if Contact Form 7 is active
                            if ( function_exists( 'wpcf7' ) && get_theme_mod( 'contact_form_shortcode' ) ) {
                                echo do_shortcode( get_theme_mod( 'contact_form_shortcode' ) );
                            } else {
                                // Fallback form
                                ?>
                                <form class="contact-form" action="<?php echo esc_url( admin_url('admin-post.php') ); ?>" method="post">
                                    <input type="hidden" name="action" value="contact_form_submission">
                                    <?php wp_nonce_field( 'contact_form_nonce', 'contact_nonce' ); ?>
                                    
                                    <div class="form-group">
                                        <label for="name">Name *</label>
                                        <input type="text" id="name" name="name" required>
                                    </div>

                                    <div class="form-group">
                                        <label for="email">Email *</label>
                                        <input type="email" id="email" name="email" required>
                                    </div>

                                    <div class="form-group">
                                        <label for="phone">Phone</label>
                                        <input type="tel" id="phone" name="phone">
                                    </div>

                                    <div class="form-group">
                                        <label for="case-type">Case Type</label>
                                        <select id="case-type" name="case_type">
                                            <option value="">Select a case type</option>
                                            <option value="personal-injury">Personal Injury</option>
                                            <option value="medical-malpractice">Medical Malpractice</option>
                                            <option value="employment">Employment Litigation</option>
                                            <option value="business-valuation">Business Valuation</option>
                                            <option value="other">Other</option>
                                        </select>
                                    </div>

                                    <div class="form-group">
                                        <label for="message">Message *</label>
                                        <textarea id="message" name="message" rows="5" required></textarea>
                                    </div>

                                    <button type="submit" class="btn btn-primary">Send Message</button>
                                </form>
                                <?php
                            }
                            ?>
                        </div>

                        <div class="contact-info-section">
                            <h2>Contact Information</h2>
                            
                            <div class="contact-card">
                                <h3>Office Location</h3>
                                <address>
                                    <p>
                                        Skerritt Economics & Consulting<br>
                                        400 Putnam Pike, Suite J<br>
                                        Smithfield, RI 02917
                                    </p>
                                </address>
                            </div>

                            <div class="contact-card">
                                <h3>Phone & Email</h3>
                                <p>
                                    <strong>Phone:</strong> <a href="tel:+12036052814">(203) 605-2814</a><br>
                                    <strong>Email:</strong> <a href="mailto:chris@skerritteconomics.com">chris@skerritteconomics.com</a>
                                </p>
                            </div>

                            <div class="contact-card">
                                <h3>Office Hours</h3>
                                <p>
                                    Monday - Friday: 9:00 AM - 5:00 PM<br>
                                    Saturday - Sunday: By appointment
                                </p>
                            </div>

                            <div class="contact-card">
                                <h3>Coverage Areas</h3>
                                <p>Serving attorneys throughout New England:</p>
                                <ul>
                                    <li>Rhode Island</li>
                                    <li>Massachusetts</li>
                                    <li>Connecticut</li>
                                    <li>New Hampshire</li>
                                    <li>Vermont</li>
                                    <li>Maine</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </article>
    <?php endwhile; ?>
</main>

<?php get_footer();