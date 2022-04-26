module.exports = {
  mode: "jit",
  content: ["./sppr/dashboard/templates/**/*.{html, js}"],
  theme: {
    extend: {
      fontfamily: {
        regional: ["Philosopher"]
      },
      colors: {}
    }
  },
  plugins: [require("daisyui")]
};
