<?php
/**
 * The template for displaying single service posts
 *
 * @package Skerritt_Economics
 */

get_header(); ?>

<main id="primary" class="site-main service-single">
    <?php while ( have_posts() ) : the_post(); ?>
        <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
            <header class="page-header">
                <div class="container">
                    <h1 class="page-title"><?php the_title(); ?></h1>
                    <nav class="breadcrumb" aria-label="Breadcrumb">
                        <a href="<?php echo esc_url( home_url( '/' ) ); ?>">Home</a>
                        <span aria-hidden="true">/</span>
                        <a href="<?php echo esc_url( home_url( '/services/' ) ); ?>">Services</a>
                        <span aria-hidden="true">/</span>
                        <span aria-current="page"><?php the_title(); ?></span>
                    </nav>
                </div>
            </header>

            <div class="service-content">
                <div class="container">
                    <div class="content-grid">
                        <div class="main-content">
                            <?php if ( has_post_thumbnail() ) : ?>
                                <div class="service-featured-image">
                                    <?php the_post_thumbnail( 'large' ); ?>
                                </div>
                            <?php endif; ?>

                            <?php the_content(); ?>

                            <?php
                            // Display related practice areas
                            $practice_areas = get_post_meta( get_the_ID(), 'related_practice_areas', true );
                            if ( $practice_areas ) : ?>
                                <div class="related-practice-areas">
                                    <h2>Related Practice Areas</h2>
                                    <div class="practice-area-links">
                                        <?php foreach ( $practice_areas as $area_id ) : 
                                            $area = get_post( $area_id );
                                            if ( $area ) : ?>
                                                <a href="<?php echo get_permalink( $area_id ); ?>" class="practice-area-link">
                                                    <?php echo esc_html( $area->post_title ); ?>
                                                </a>
                                            <?php endif;
                                        endforeach; ?>
                                    </div>
                                </div>
                            <?php endif; ?>
                        </div>

                        <aside class="service-sidebar">
                            <div class="sidebar-card cta-card">
                                <h3>Need <?php the_title(); ?> Services?</h3>
                                <p>Contact us for a confidential consultation about your case.</p>
                                <a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" class="btn btn-primary btn-block">Schedule Consultation</a>
                                <div class="contact-info">
                                    <p class="phone">
                                        <svg class="icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                                            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                                        </svg>
                                        <a href="tel:+12036052814">(203) 605-2814</a>
                                    </p>
                                </div>
                            </div>

                            <?php
                            // Display other services
                            $other_services = get_posts( array(
                                'post_type' => 'service',
                                'posts_per_page' => 5,
                                'post__not_in' => array( get_the_ID() ),
                                'orderby' => 'menu_order',
                                'order' => 'ASC'
                            ) );

                            if ( $other_services ) : ?>
                                <div class="sidebar-card">
                                    <h3>Other Services</h3>
                                    <ul class="service-list">
                                        <?php foreach ( $other_services as $service ) : ?>
                                            <li>
                                                <a href="<?php echo get_permalink( $service->ID ); ?>">
                                                    <?php echo esc_html( $service->post_title ); ?>
                                                </a>
                                            </li>
                                        <?php endforeach; ?>
                                    </ul>
                                </div>
                            <?php endif; wp_reset_postdata(); ?>

                            <div class="sidebar-card credentials-card">
                                <h3>Credentials</h3>
                                <ul class="credentials-list">
                                    <li>MBA, Finance</li>
                                    <li>25+ Years Experience</li>
                                    <li>Court-Qualified Expert</li>
                                    <li>500+ Cases Completed</li>
                                </ul>
                            </div>
                        </aside>
                    </div>
                </div>
            </div>
        </article>
    <?php endwhile; ?>
</main>

<?php get_footer();