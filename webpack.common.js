const Path = require('path');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
// const CopyWebpackPlugin = require('copy-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: {
    app: Path.resolve(__dirname, './assets/js/app.js'),
    vendor: Path.resolve(__dirname, './assets/js/vendor.js')
  },
  output: {
    path: Path.join(__dirname, './static/'),
    filename: 'js/[name].js',
  },
  optimization: {
    splitChunks: {
      chunks: 'all',
      name: false,
    },
  },
  plugins: [
    new CleanWebpackPlugin(),
    // * NOTE: USE THIS WHEN U WANT TO COPY THE BUILD FILE TO STATIC LOCATION ON THE SERVER
    // new CopyWebpackPlugin({
    //   patterns: [{ from: Path.resolve(__dirname, './static'), to: 'public' }],
    // }),
    new HtmlWebpackPlugin({
      template: Path.resolve(__dirname, './templates/index.html'),
    }),
  ],
  resolve: {
    alias: {
      '~': Path.resolve(__dirname, './assets'),
    },
  },
  module: {
    rules: [
      {
        test: /\.mjs$/,
        include: /node_modules/,
        type: 'javascript/auto',
      },
      {
        test: /\.html$/i,
        loader: 'html-loader',
      },
      {
        test: /\.(ico|jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2)(\?.*)?$/,
        type: 'asset'
      },
    ],
  },
};
