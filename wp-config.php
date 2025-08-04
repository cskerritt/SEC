<?php
/**
 * WordPress Configuration for MAMP
 */

// ** Database settings ** //
define( 'DB_NAME', 'skerritt_wp' );
define( 'DB_USER', 'wordpress' );
define( 'DB_PASSWORD', 'wordpress' );
define( 'DB_HOST', 'localhost' ); // Using local MySQL
define( 'DB_CHARSET', 'utf8' );
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 */
define('AUTH_KEY',         'oj8#M+P|<5B9WU~x%+N?vz7Y)Lq*!|h{T4,cRV=DU-+P#Mb3|&6WL+%5-YTnu2k');
define('SECURE_AUTH_KEY',  'W|E<4V%OqH*c+B[#Pvb8~+imJ#2MnQ==p+F6{D4M^-CY-+FVL?+w#hL5|r,+z|~R');
define('LOGGED_IN_KEY',    'O+1F|xp8BbW]+M)2+]|V+nJ3|+VH?#bX++6c|3W=D1uH++K7o1+pE~S1N&5QP+V|');
define('NONCE_KEY',        '#7|R+J_w/VQ|-U4&]xU+Y-|4*mY+PHkV]O7j+m|N6+8B<~K|E3t+Yd|u+V5b/v2&');
define('AUTH_SALT',        'x+~Zk|S8vR+|3M#a[+DW2|Y+p/J6|K+T8#vN+|G5oL+|U9#Qz+|F4wE+|H7mP+|C');
define('SECURE_AUTH_SALT', 'B+|9#Nx+|5Ks+|7Ju+|2Mw+|8Lp+|4Qt+|6Or+|3Vy+|1Uz+|0Xa+|Cb+|Ed+|Gf');
define('LOGGED_IN_SALT',   '+|Hi+|Jk+|Lm+|No+|Pq+|Rs+|Tu+|Vw+|Xy+|Zab+|cde+|fgh+|ijk+|lmn+|op');
define('NONCE_SALT',       'q+|rst+|uvw+|xyz+|123+|456+|789+|0AB+|CDE+|FGH+|IJK+|LMN+|OPQ+|RST');

/**#@-*/

/**
 * WordPress database table prefix.
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */
define('WP_MEMORY_LIMIT', '256M');
define('WP_MAX_MEMORY_LIMIT', '256M');
set_time_limit(300);

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
