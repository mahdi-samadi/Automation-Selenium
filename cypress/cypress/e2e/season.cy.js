/// <reference types = "cypress"/>
describe("sutite1", () => {
  it("Google Search", function () {
    cy.visit("https://google.com");
    cy.get('input[name="btnK"]').click();
  });

  it("2-Cypress website", () => {
    cy.visit("https://cypress.io");
    cy.title().should("include", "Cypress");
  });
});
