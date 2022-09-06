module.exports = {
  mode: "jit",
  content: [
    "./templates/**/*.{html, js}",
    "./landing/templates/**/*.{html, js}",
  ],
  theme: {
    extend: {
      fontfamily: {
        regional: ["Philosopher"],
      },
      colors: {
        gray: {
          700: "#374151",
          800: "#1f2937",
          900: "#111827",
        },
      },
      animation: {
        "bounce-low": "bounce_low 1s infinite",
      },
      keyframes: {
        bounce_low: {
          "0%, 100%": {
            transform: "translateY(-5%)",
            "animation-timing-function": "cubic-bezier(0.6, 0, .75, .75)",
          },
          "50%": {
            transform: "translateY(0)",
            "animation-timing-function": "cubic-bezier(0, 0, 0.2, 1)",
          },
        },
      },
    },
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
  },
};
