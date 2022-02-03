const path = require('path');

module.exports = {
  entry: './sppr/frontend/index.js',  // path to our input file
  output: {
    filename: 'sppr_script_bundled.js',  // output bundle file name
    path: path.resolve(__dirname, './sppr/static/javascript'),  // path to our Django static directory
  },
};