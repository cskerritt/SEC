<?php
/**
 * The template for displaying the footer
 *
 * @package Skerritt_Economics
 */
?>

<footer class="site-footer" role="contentinfo">
    <div class="container">
        <div class="footer-content">
            <div class="footer-grid">
                <!-- Company Info -->
                <div class="footer-section">
                    <h3>Skerritt Economics & Consulting</h3>
                    <p>Court-tested forensic economics and business valuation expertise serving attorneys throughout New England.</p>
                    <address>
                        <p><strong>Christopher C. Skerritt, MBA</strong><br>
                        Forensic Economist & Business Valuation Expert</p>
                        <p>400 Putnam Pike, Suite J<br>
                        Smithfield, RI 02917</p>
                        <p><a href="tel:+12036052814">(203) 605-2814</a><br>
                        <a href="mailto:chris@skerritteconomics.com">chris@skerritteconomics.com</a></p>
                    </address>
                </div>

                <!-- Services -->
                <div class="footer-section">
                    <h3>Services</h3>
                    <?php
                    wp_nav_menu(
                        array(
                            'theme_location' => 'footer-services',
                            'menu_class'     => 'footer-links',
                            'container'      => false,
                            'fallback_cb'    => false,
                        )
                    );
                    ?>
                </div>

                <!-- Practice Areas -->
                <div class="footer-section">
                    <h3>Practice Areas</h3>
                    <?php
                    wp_nav_menu(
                        array(
                            'theme_location' => 'footer-practice-areas',
                            'menu_class'     => 'footer-links',
                            'container'      => false,
                            'fallback_cb'    => false,
                        )
                    );
                    ?>
                </div>

                <!-- Resources -->
                <div class="footer-section">
                    <h3>Resources</h3>
                    <?php
                    wp_nav_menu(
                        array(
                            'theme_location' => 'footer-resources',
                            'menu_class'     => 'footer-links',
                            'container'      => false,
                            'fallback_cb'    => false,
                        )
                    );
                    ?>
                </div>
            </div>

            <div class="footer-bottom">
                <p>&copy; <?php echo date('Y'); ?> Skerritt Economics & Consulting. All rights reserved.</p>
                <nav class="footer-legal-links" aria-label="Legal links">
                    <a href="<?php echo esc_url( home_url( '/privacy-policy/' ) ); ?>">Privacy Policy</a>
                    <span aria-hidden="true">|</span>
                    <a href="<?php echo esc_url( home_url( '/terms-of-service/' ) ); ?>">Terms of Service</a>
                    <span aria-hidden="true">|</span>
                    <a href="<?php echo esc_url( home_url( '/sitemap/' ) ); ?>">Sitemap</a>
                </nav>
            </div>
        </div>
    </div>
</footer>

<?php wp_footer(); ?>

</body>
</html>