/** @type {import('tailwindcss').Config} */
module.exports = {
  // manually list dj apps to exclude clientapps
  content: [
    "./templates/**/*.html",
    // "./artvendors/templates/**/*.html",
    "./washingtonsite/templates/**/*.html",
    "./website/templates/**/*.html",
    "./**/templates/**/*.html",
    // "../static_builds/assets/kjo/*.js",
  ],
  theme: {
    extend: {},
  },
  // plugins: [require("daisyui")],
  darkMode: "class",

  // daisyui: {
  //   themes: false, //[],
  //   logs: false,
  // },
};
