These are NodeJS scripts to run the UI tests using cypress

In this folder, install cypress and make sure you configure

```powershell
npm install cypress

npx cypress open
```

Configure E2E tests in Cypress UI
add "scripts" to package.json:
```json
"scripts": {
    "cy:open:mobile" : "cypress open --config viewportWidth=375,viewportHeight=667",
    "cy:run:mobile" : "cypress run --browser chrome --config viewportWidth=375,viewportHeight=667"
}
```
add chromeWebSecurity: false in cypress.config.js

To open Cypress and watch tests running

```powershell
cy:open:mobile
```

To run Cypress in headless mode

```powershell
cy:run:mobile
```

