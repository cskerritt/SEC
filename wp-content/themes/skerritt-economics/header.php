<?php
/**
 * The header for our theme
 *
 * @package Skerritt_Economics
 */
?>
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="profile" href="https://gmpg.org/xfn/11">
    
    <?php wp_head(); ?>
</head>

<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<a class="skip-link screen-reader-text" href="#primary"><?php esc_html_e( 'Skip to content', 'skerritt-economics' ); ?></a>

<header class="site-header" role="banner">
    <div class="container">
        <div class="header-content">
            <div class="site-branding">
                <?php if ( has_custom_logo() ) : ?>
                    <?php the_custom_logo(); ?>
                <?php else : ?>
                    <a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home" class="site-title">
                        <?php bloginfo( 'name' ); ?>
                    </a>
                <?php endif; ?>
            </div>

            <nav id="site-navigation" class="main-navigation" role="navigation" aria-label="Primary Navigation">
                <button class="menu-toggle" aria-controls="primary-menu" aria-expanded="false">
                    <span class="menu-icon"></span>
                    <span class="screen-reader-text"><?php esc_html_e( 'Menu', 'skerritt-economics' ); ?></span>
                </button>
                <?php
                wp_nav_menu(
                    array(
                        'theme_location' => 'primary',
                        'menu_id'        => 'primary-menu',
                        'container'      => false,
                        'fallback_cb'    => false,
                    )
                );
                ?>
            </nav>

            <div class="header-cta">
                <span class="phone-number">
                    <a href="tel:+12036052814" aria-label="Call (203) 605-2814">
                        <svg class="icon-phone" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                        </svg>
                        (203) 605-2814
                    </a>
                </span>
                <a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" class="btn btn-primary">Get Started</a>
            </div>
        </div>
    </div>
</header>