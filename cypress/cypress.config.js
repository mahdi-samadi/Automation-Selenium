const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});

// const { defineConfig } = require("cypress");

// module.exports = defineConfig({
//   e2e: {
//     baseUrl: "http://localhost:1234",
//     // سایر تنظیمات را اینجا اضافه کنید
//   },
//   // میتوانید تنظیمات جهانی را نیز اینجا اضافه کنید
// });
