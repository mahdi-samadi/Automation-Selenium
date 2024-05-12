/// <reference types = "cypress"/>
describe("season2", () => {
  // it("test1", () => {
  // cy.visit("https://play2.automationcamp.ir/");
  // cy.get("#fname").type("mahdi");
  // });
  // it("scorll_check", () => {
  //   cy.visit("https://datatables.net/examples/basic_init/scroll_x.html");
  //   cy.get(":nth-child(9) > :nth-child(9)").click();
  // });
  it("test1", () => {
    cy.visit("https://play2.automationcamp.ir/");
    cy.get("label[for = moption]").contains("Option 2");
    cy.contains("label[for ='moption']", "Option 2");
  });
});
