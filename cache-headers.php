<?php
// Cache headers for static assets
// This file handles cache headers dynamically to ensure they're properly set

$file = $_GET['file'] ?? '';
$type = $_GET['type'] ?? '';

// Security check - only allow specific file types and paths
if (!preg_match('/^(css|js)\/([\w\-]+\.min\.(css|js))(\?v=\d+)?$/', $file)) {
    header('HTTP/1.0 404 Not Found');
    exit;
}

// Get the actual file path
$filePath = __DIR__ . '/' . preg_replace('/\?.*$/', '', $file);

if (!file_exists($filePath)) {
    header('HTTP/1.0 404 Not Found');
    exit;
}

// Set appropriate content type
$extension = pathinfo($filePath, PATHINFO_EXTENSION);
$contentType = $extension === 'css' ? 'text/css' : 'application/javascript';
header('Content-Type: ' . $contentType);

// Set cache headers for 1 year
header('Cache-Control: public, max-age=31536000, immutable');
header('Expires: ' . gmdate('D, d M Y H:i:s', time() + 31536000) . ' GMT');

// Remove ETags
header_remove('ETag');

// Enable compression
if (extension_loaded('zlib') && !ini_get('zlib.output_compression')) {
    ob_start('ob_gzhandler');
}

// Output the file
readfile($filePath);
?>