module.exports = {
  mode: "jit",
  content: ["./sppr/dashboard/templates/**/*.{html, js}"],
  theme: {
    extend: {
      fontfamily: {
        regional: ["Philosopher"]
      },
      colors: {
        gray: {
          700: "#374151",
          800: "#1f2937",
          900: "#111827"
        }
      }
    }
  },
  plugins: [require("daisyui")],
  daisyui: {
    styled: true,
    themes: true,
    base: true,
    utils: true,
    logs: true,
    rtl: false,
    prefix: "",
    darkTheme: "dark",
  }
};
