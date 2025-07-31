// Service Worker for Enhanced Caching
const CACHE_NAME = 'skerritt-economics-v1.0';
const STATIC_CACHE = 'static-v1.0';
const DYNAMIC_CACHE = 'dynamic-v1.0';

const STATIC_ASSETS = [
    '/',
    '/css/styles.min.css',
    '/css/mobile-optimized.min.css',
    '/js/mobile-performance.js',
    '/js/main.min.js',
    '/sec-logo.png',
    '/favicon.ico',
    '/offline.html'
];

const CACHE_STRATEGIES = {
    // Cache First - for static assets
    cacheFirst: ['/css/', '/js/', '/images/', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico'],
    // Network First - for HTML pages
    networkFirst: ['.html', '/'],
    // Stale While Revalidate - for API calls and dynamic content
    staleWhileRevalidate: ['/api/', '.json']
};

// Install event
self.addEventListener('install', event => {
    console.log('Service Worker: Installing...');
    event.waitUntil(
        caches.open(STATIC_CACHE)
            .then(cache => {
                console.log('Service Worker: Caching static assets');
                return cache.addAll(STATIC_ASSETS);
            })
            .then(() => self.skipWaiting())
    );
});

// Activate event
self.addEventListener('activate', event => {
    console.log('Service Worker: Activating...');
    event.waitUntil(
        caches.keys()
            .then(cacheNames => {
                return Promise.all(
                    cacheNames.map(cacheName => {
                        if (cacheName !== STATIC_CACHE && cacheName !== DYNAMIC_CACHE) {
                            console.log('Service Worker: Deleting old cache', cacheName);
                            return caches.delete(cacheName);
                        }
                    })
                );
            })
            .then(() => self.clients.claim())
    );
});

// Fetch event
self.addEventListener('fetch', event => {
    const url = event.request.url;
    
    // Skip non-GET requests
    if (event.request.method !== 'GET') {
        return;
    }
    
    // Skip external requests and specific paths
    if (!url.includes(self.location.origin) || 
        url.includes('/admin/') || 
        url.includes('formspree.io')) {
        return;
    }
    
    // Determine cache strategy
    let strategy = 'networkFirst'; // default
    
    for (const [strategyName, patterns] of Object.entries(CACHE_STRATEGIES)) {
        if (patterns.some(pattern => url.includes(pattern))) {
            strategy = strategyName;
            break;
        }
    }
    
    event.respondWith(handleRequest(event.request, strategy));
});

async function handleRequest(request, strategy) {
    switch (strategy) {
        case 'cacheFirst':
            return cacheFirst(request);
        case 'networkFirst':
            return networkFirst(request);
        case 'staleWhileRevalidate':
            return staleWhileRevalidate(request);
        default:
            return networkFirst(request);
    }
}

async function cacheFirst(request) {
    const cachedResponse = await caches.match(request);
    if (cachedResponse) {
        return cachedResponse;
    }
    
    try {
        const networkResponse = await fetch(request);
        if (networkResponse.ok) {
            const cache = await caches.open(DYNAMIC_CACHE);
            cache.put(request, networkResponse.clone());
        }
        return networkResponse;
    } catch (error) {
        console.log('Network request failed:', error);
        // Return offline fallback if available
        return new Response('Offline content not available', { status: 503 });
    }
}

async function networkFirst(request) {
    try {
        const networkResponse = await fetch(request);
        if (networkResponse.ok) {
            const cache = await caches.open(DYNAMIC_CACHE);
            cache.put(request, networkResponse.clone());
        }
        return networkResponse;
    } catch (error) {
        console.log('Network request failed, trying cache:', error);
        const cachedResponse = await caches.match(request);
        if (cachedResponse) {
            return cachedResponse;
        }
        return new Response('Offline and no cached version available', { status: 503 });
    }
}

async function staleWhileRevalidate(request) {
    const cachedResponse = await caches.match(request);
    
    const networkResponsePromise = fetch(request).then(response => {
        if (response.ok) {
            const cache = caches.open(DYNAMIC_CACHE);
            cache.then(c => c.put(request, response.clone()));
        }
        return response;
    }).catch(() => cachedResponse);
    
    return cachedResponse || networkResponsePromise;
}

// Background sync for form submissions
self.addEventListener('sync', event => {
    if (event.tag === 'background-sync') {
        event.waitUntil(handleBackgroundSync());
    }
});

async function handleBackgroundSync() {
    // Handle any queued form submissions when online
    console.log('Service Worker: Performing background sync');
}

// Push notifications (if needed)
self.addEventListener('push', event => {
    if (event.data) {
        const data = event.data.json();
        const options = {
            body: data.body,
            icon: '/sec-logo.png',
            badge: '/sec-logo.png',
            data: data.url
        };
        
        event.waitUntil(
            self.registration.showNotification(data.title, options)
        );
    }
});

self.addEventListener('notificationclick', event => {
    event.notification.close();
    if (event.notification.data) {
        event.waitUntil(
            clients.openWindow(event.notification.data)
        );
    }
});