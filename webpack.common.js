const Path = require("path");
const Webpack = require("webpack");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const CopyWebpackPlugin = require("copy-webpack-plugin");

module.exports = {
  entry: {
    app: Path.resolve(__dirname, "./assets/js/app.js"),
  },
  output: {
    path: Path.join(__dirname, "./static/"),
    filename: "js/[name].js",
  },
  optimization: {
    splitChunks: {
      chunks: "all",
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: "vendors",
        },
        jquery: {
          test: /[\\/]node_modules[\\/](jquery)[\\/]/,
          name: "jquery",
        },
      },
    },
  },
  plugins: [
    new Webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery",
    }),
    new CopyWebpackPlugin({
      patterns: [
        {
          from: Path.join(__dirname, "assets/images"),
          to: Path.join(__dirname, "static/images"),
        },
      ],
    }),
    new CleanWebpackPlugin(),
  ],
  resolve: {
    alias: {
      "~": Path.resolve(__dirname, "./assets"),
    },
  },
  module: {
    rules: [
      {
        test: /\.mjs$/,
        include: /node_modules/,
        type: "javascript/auto",
      },
      {
        test: require.resolve("jquery"),
        loader: "expose-loader",
        options: {
          exposes: ["$", "jQuery"],
        },
      },
      {
        test: /\.html$/i,
        loader: "html-loader",
      },
      {
        test: /\.(ico|jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2)(\?.*)?$/,
        type: "asset/resource",
      },
    ],
  },
};
