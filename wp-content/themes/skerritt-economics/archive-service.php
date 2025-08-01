<?php
/**
 * The template for displaying service archive pages
 *
 * @package Skerritt_Economics
 */

get_header(); ?>

<main id="primary" class="site-main services-archive">
    <header class="page-header">
        <div class="container">
            <h1 class="page-title">Our Services</h1>
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <a href="<?php echo esc_url( home_url( '/' ) ); ?>">Home</a>
                <span aria-hidden="true">/</span>
                <span aria-current="page">Services</span>
            </nav>
            <p class="page-description">Comprehensive economic analysis and valuation services for legal professionals</p>
        </div>
    </header>

    <div class="services-content">
        <div class="container">
            <?php if ( have_posts() ) : ?>
                <div class="services-grid">
                    <?php while ( have_posts() ) : the_post(); ?>
                        <article class="service-card">
                            <?php if ( has_post_thumbnail() ) : ?>
                                <div class="service-image">
                                    <a href="<?php the_permalink(); ?>">
                                        <?php the_post_thumbnail( 'service-thumbnail' ); ?>
                                    </a>
                                </div>
                            <?php endif; ?>
                            
                            <div class="service-content">
                                <h2 class="service-title">
                                    <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
                                </h2>
                                
                                <div class="service-excerpt">
                                    <?php the_excerpt(); ?>
                                </div>
                                
                                <a href="<?php the_permalink(); ?>" class="btn btn-link">
                                    Learn More <span aria-hidden="true">→</span>
                                </a>
                            </div>
                        </article>
                    <?php endwhile; ?>
                </div>

                <?php the_posts_pagination(); ?>

            <?php else : ?>
                <p>No services found.</p>
            <?php endif; ?>

            <section class="services-cta">
                <div class="cta-content">
                    <h2>Need Expert Economic Analysis?</h2>
                    <p>Contact us to discuss how our services can support your case.</p>
                    <div class="cta-buttons">
                        <a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" class="btn btn-primary">Schedule Consultation</a>
                        <a href="tel:+12036052814" class="btn btn-outline">Call (203) 605-2814</a>
                    </div>
                </div>
            </section>
        </div>
    </div>
</main>

<?php get_footer();