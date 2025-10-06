self.addEventListener('install', event => {
    console.log('Service Worker installert');
});

self.addEventListener('fetch', event => {
    console.log('Henter ressurs:', event.request.url);
});