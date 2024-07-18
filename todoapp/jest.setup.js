const { config } = require('@vue/test-utils');
const { createApp } = require('vue');
const Quasar = require('quasar').default;
const lang = require('quasar/lang/en-us').default;
require('@quasar/extras/material-icons/material-icons.css');
require('quasar/dist/quasar.css');

// Create a Vue app instance
const app = createApp({});

// Use Quasar plugin
app.use(Quasar, {
  config: {},
  lang: lang,
});

// Globally configure Vue Test Utils to use Quasar
config.global.plugins = [Quasar];
config.global.mocks = {
  $t: (msg) => msg, // Mock for translations
};

// Export the configured config object
module.exports = {
  config,
};
