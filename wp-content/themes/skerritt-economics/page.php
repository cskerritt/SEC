<?php
/**
 * The template for displaying all pages
 *
 * @package Skerritt_Economics
 */

get_header(); ?>

<main id="primary" class="site-main">
    <?php
    while ( have_posts() ) :
        the_post();
    ?>
        <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
            <header class="page-header">
                <div class="container">
                    <?php the_title( '<h1 class="page-title">', '</h1>' ); ?>
                    <?php if ( function_exists( 'yoast_breadcrumb' ) ) {
                        yoast_breadcrumb( '<nav class="breadcrumb" aria-label="Breadcrumb">', '</nav>' );
                    } ?>
                </div>
            </header>

            <div class="page-content">
                <div class="container">
                    <?php the_content(); ?>
                </div>
            </div>
        </article>
    <?php
    endwhile;
    ?>
</main>

<?php get_footer();