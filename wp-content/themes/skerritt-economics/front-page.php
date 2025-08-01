<?php
/**
 * The front page template file
 *
 * @package Skerritt_Economics
 */

get_header(); ?>

<main>
    <!-- Hero Section -->
    <section class="hero" role="region" aria-label="Hero">
        <div class="container">
            <div class="hero-content">
                <h1><?php echo get_theme_mod( 'hero_title', 'Independent Economic Assessments for Litigation & Corporate Disputes' ); ?></h1>
                <p class="hero-subtitle"><?php echo get_theme_mod( 'hero_subtitle', 'Court-tested forensic economics and business valuation expertise for personal injury, medical malpractice, employment, and commercial litigation across Rhode Island, Massachusetts, and New England.' ); ?></p>
                <div class="hero-cta">
                    <a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" class="btn btn-primary">Schedule Consultation</a>
                    <a href="<?php echo esc_url( home_url( '/services/' ) ); ?>" class="btn btn-secondary">View Services</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Practice Areas Strip -->
    <section class="practice-areas-strip" role="region" aria-label="Practice Areas">
        <div class="container">
            <nav class="practice-areas-chips" aria-label="Practice area quick links">
                <?php
                $practice_areas = get_posts( array(
                    'post_type' => 'practice-area',
                    'posts_per_page' => 5,
                    'orderby' => 'menu_order',
                    'order' => 'ASC'
                ) );

                foreach ( $practice_areas as $area ) :
                    $icon = get_post_meta( $area->ID, 'practice_area_icon', true );
                ?>
                    <a href="<?php echo get_permalink( $area->ID ); ?>" class="practice-chip">
                        <span class="icon" aria-hidden="true"><?php echo esc_html( $icon ); ?></span>
                        <?php echo esc_html( $area->post_title ); ?>
                    </a>
                <?php endforeach; wp_reset_postdata(); ?>
            </nav>
        </div>
    </section>

    <!-- Expertise Section -->
    <section class="expertise" role="region" aria-label="Expertise">
        <div class="container">
            <div class="expertise-header">
                <h2>Expert Economic Analysis for Complex Legal Matters</h2>
                <p class="section-intro">With over 25 years of experience, Christopher Skerritt provides clear, defensible economic assessments that help attorneys achieve favorable outcomes for their clients.</p>
            </div>

            <div class="expertise-grid">
                <?php
                $services = get_posts( array(
                    'post_type' => 'service',
                    'posts_per_page' => 4,
                    'orderby' => 'menu_order',
                    'order' => 'ASC'
                ) );

                foreach ( $services as $service ) :
                    $icon = get_post_meta( $service->ID, 'service_icon', true );
                ?>
                    <article class="expertise-card">
                        <div class="expertise-icon" aria-hidden="true"><?php echo esc_html( $icon ); ?></div>
                        <h3><?php echo esc_html( $service->post_title ); ?></h3>
                        <p><?php echo wp_trim_words( $service->post_excerpt, 20 ); ?></p>
                        <a href="<?php echo get_permalink( $service->ID ); ?>" class="learn-more">
                            Learn More <span aria-hidden="true">→</span>
                        </a>
                    </article>
                <?php endforeach; wp_reset_postdata(); ?>
            </div>
        </div>
    </section>

    <!-- Professional Profile Section -->
    <section class="profile" role="region" aria-label="Professional Profile">
        <div class="container">
            <div class="profile-content">
                <div class="profile-image">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/christopher-skerritt.jpg" 
                         alt="Christopher C. Skerritt, MBA - Forensic Economist"
                         width="400" 
                         height="500"
                         loading="lazy">
                </div>
                <div class="profile-text">
                    <h2>Christopher C. Skerritt, MBA</h2>
                    <p class="profile-title">Forensic Economist & Business Valuation Expert</p>
                    <?php
                    $about_page = get_page_by_path( 'about' );
                    if ( $about_page ) {
                        echo '<div class="profile-bio">' . wp_trim_words( $about_page->post_content, 50 ) . '</div>';
                    }
                    ?>
                    <div class="profile-highlights">
                        <div class="highlight">
                            <strong>25+</strong>
                            <span>Years Experience</span>
                        </div>
                        <div class="highlight">
                            <strong>500+</strong>
                            <span>Cases Completed</span>
                        </div>
                        <div class="highlight">
                            <strong>100+</strong>
                            <span>Court Testimonies</span>
                        </div>
                    </div>
                    <a href="<?php echo esc_url( home_url( '/about/' ) ); ?>" class="btn btn-secondary">Read Full Bio</a>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="cta" role="region" aria-label="Call to Action">
        <div class="container">
            <div class="cta-content">
                <h2>Need an Economic Expert for Your Case?</h2>
                <p>Get a preliminary assessment of your economic damages or business valuation needs.</p>
                <div class="cta-buttons">
                    <a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" class="btn btn-primary btn-lg">Schedule Consultation</a>
                    <a href="tel:+12036052814" class="btn btn-outline btn-lg">
                        <svg class="icon-phone" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                        </svg>
                        Call (203) 605-2814
                    </a>
                </div>
            </div>
        </div>
    </section>
</main>

<?php get_footer();