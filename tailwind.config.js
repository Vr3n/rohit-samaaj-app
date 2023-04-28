const tw_colors = require("tailwindcss/colors");

/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ["./templates/**/*.html", "./static/vendors/flowbite/**/*.js"],
  theme: {
    extend: {},
    colors: {
      primary: tw_colors.blue,
      secondary: tw_colors.pink,
    },
  },
  plugins: [require("flowbite/plugin")],
};
