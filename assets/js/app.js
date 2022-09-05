import '../styles/main.scss';
import Alpine from 'alpinejs';
import $ from 'jquery';

import landingScript from './landing';

window.Alpine = Alpine;
window.jQuery = $;
window.$ = $;

$(document).ready(() => {
  console.log(`this script is running on app.js`);
});

landingScript();

Alpine.start();

console.log('APP: webpack starterkit');
