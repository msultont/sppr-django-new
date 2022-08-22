import '../styles/main.scss';
import Alpine from 'alpinejs';
import $ from "jquery";

import LandingScript from "./landing";

window.Alpine = Alpine;
window.jQuery = $;
window.$ = $;

$(document).ready(() => {
  console.log(`this script is running on app.js`);
});

LandingScript();

Alpine.start();

console.log('APP: webpack starterkit');