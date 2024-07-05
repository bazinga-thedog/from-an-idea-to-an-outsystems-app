describe('Tests for assuring good refactor', () => {
  
  it('Should display all matches for test user', () => {
    cy.visit('https://bazinga-thedog.outsystemscloud.com/PadelPersonalCoach/Login')
    cy.get('#Input_UsernameVal', {timeout: 10000}).type('test_user')
    cy.get('#Input_PasswordVal').type('test123')
    cy.get('.btn').click()
    cy.get('.list').find('.list-item').should('have.length', 8)
  })
})