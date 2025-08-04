<?php
/**
 * Skerritt Economics functions and definitions
 *
 * @package Skerritt_Economics
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly.
}

/**
 * Sets up theme defaults and registers support for various WordPress features.
 */
function skerritt_economics_setup() {
    // Add default posts and comments RSS feed links to head.
    add_theme_support( 'automatic-feed-links' );

    // Let WordPress manage the document title.
    add_theme_support( 'title-tag' );

    // Enable support for Post Thumbnails on posts and pages.
    add_theme_support( 'post-thumbnails' );

    // Add theme support for custom logo.
    add_theme_support( 'custom-logo', array(
        'height'      => 100,
        'width'       => 400,
        'flex-height' => true,
        'flex-width'  => true,
    ) );

    // This theme uses wp_nav_menu() in multiple locations.
    register_nav_menus(
        array(
            'primary'              => esc_html__( 'Primary Menu', 'skerritt-economics' ),
            'footer-services'      => esc_html__( 'Footer Services Menu', 'skerritt-economics' ),
            'footer-practice-areas' => esc_html__( 'Footer Practice Areas Menu', 'skerritt-economics' ),
            'footer-resources'     => esc_html__( 'Footer Resources Menu', 'skerritt-economics' ),
        )
    );

    // Switch default core markup to output valid HTML5.
    add_theme_support(
        'html5',
        array(
            'search-form',
            'comment-form',
            'comment-list',
            'gallery',
            'caption',
            'style',
            'script',
        )
    );

    // Add theme support for selective refresh for widgets.
    add_theme_support( 'customize-selective-refresh-widgets' );
}
add_action( 'after_setup_theme', 'skerritt_economics_setup' );

/**
 * Enqueue scripts and styles.
 */
function skerritt_economics_scripts() {
    // Enqueue main stylesheet
    wp_enqueue_style( 'skerritt-economics-style', get_stylesheet_uri(), array(), '1.0.0' );

    // Enqueue main JavaScript
    wp_enqueue_script( 'skerritt-economics-main', get_template_directory_uri() . '/assets/js/main.js', array(), '1.0.0', true );

    // Add inline CSS for critical styles
    $critical_css = file_get_contents( get_template_directory() . '/assets/css/critical.min.css' );
    wp_add_inline_style( 'skerritt-economics-style', $critical_css );
}
add_action( 'wp_enqueue_scripts', 'skerritt_economics_scripts' );

/**
 * Register widget area.
 */
function skerritt_economics_widgets_init() {
    register_sidebar(
        array(
            'name'          => esc_html__( 'Sidebar', 'skerritt-economics' ),
            'id'            => 'sidebar-1',
            'description'   => esc_html__( 'Add widgets here.', 'skerritt-economics' ),
            'before_widget' => '<section id="%1$s" class="widget %2$s">',
            'after_widget'  => '</section>',
            'before_title'  => '<h2 class="widget-title">',
            'after_title'   => '</h2>',
        )
    );
}
add_action( 'widgets_init', 'skerritt_economics_widgets_init' );

/**
 * Custom post types for Services and Practice Areas
 */
function skerritt_economics_register_post_types() {
    // Register Services post type
    register_post_type( 'service',
        array(
            'labels' => array(
                'name'               => __( 'Services' ),
                'singular_name'      => __( 'Service' ),
                'add_new'            => __( 'Add New Service' ),
                'add_new_item'       => __( 'Add New Service' ),
                'edit_item'          => __( 'Edit Service' ),
                'new_item'           => __( 'New Service' ),
                'view_item'          => __( 'View Service' ),
                'search_items'       => __( 'Search Services' ),
                'not_found'          => __( 'No services found' ),
                'not_found_in_trash' => __( 'No services found in trash' ),
            ),
            'public'             => true,
            'has_archive'        => true,
            'rewrite'            => array( 'slug' => 'services' ),
            'supports'           => array( 'title', 'editor', 'thumbnail', 'excerpt' ),
            'menu_icon'          => 'dashicons-portfolio',
            'show_in_rest'       => true,
        )
    );

    // Register Practice Areas post type
    register_post_type( 'practice-area',
        array(
            'labels' => array(
                'name'               => __( 'Practice Areas' ),
                'singular_name'      => __( 'Practice Area' ),
                'add_new'            => __( 'Add New Practice Area' ),
                'add_new_item'       => __( 'Add New Practice Area' ),
                'edit_item'          => __( 'Edit Practice Area' ),
                'new_item'           => __( 'New Practice Area' ),
                'view_item'          => __( 'View Practice Area' ),
                'search_items'       => __( 'Search Practice Areas' ),
                'not_found'          => __( 'No practice areas found' ),
                'not_found_in_trash' => __( 'No practice areas found in trash' ),
            ),
            'public'             => true,
            'has_archive'        => true,
            'rewrite'            => array( 'slug' => 'practice-areas' ),
            'supports'           => array( 'title', 'editor', 'thumbnail', 'excerpt' ),
            'menu_icon'          => 'dashicons-hammer',
            'show_in_rest'       => true,
        )
    );
}
add_action( 'init', 'skerritt_economics_register_post_types' );

/**
 * Add custom image sizes
 */
function skerritt_economics_add_image_sizes() {
    add_image_size( 'hero-image', 1920, 800, true );
    add_image_size( 'service-thumbnail', 400, 300, true );
}
add_action( 'after_setup_theme', 'skerritt_economics_add_image_sizes' );

/**
 * Disable WordPress emojis
 */
function skerritt_economics_disable_emojis() {
    remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
    remove_action( 'admin_print_scripts', 'print_emoji_detection_script' );
    remove_action( 'wp_print_styles', 'print_emoji_styles' );
    remove_action( 'admin_print_styles', 'print_emoji_styles' );
    remove_filter( 'the_content_feed', 'wp_staticize_emoji' );
    remove_filter( 'comment_text_rss', 'wp_staticize_emoji' );
    remove_filter( 'wp_mail', 'wp_staticize_emoji_for_email' );
}
add_action( 'init', 'skerritt_economics_disable_emojis' );

/**
 * Custom excerpt length
 */
function skerritt_economics_excerpt_length( $length ) {
    return 30;
}
add_filter( 'excerpt_length', 'skerritt_economics_excerpt_length', 999 );

/**
 * Custom excerpt more
 */
function skerritt_economics_excerpt_more( $more ) {
    return '...';
}
add_filter( 'excerpt_more', 'skerritt_economics_excerpt_more' );