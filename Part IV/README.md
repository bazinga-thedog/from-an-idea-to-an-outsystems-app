In the end of Part IV, we'll have refactored the Padel Personal Coach application from a monolith to a group of modules with a well defined architecture, migrating all the data and with the supporting API and UI tests in cypress to assure that the refactor was successful.

The episode has already been uploaded in YT:
* [Part IV - Breaking the monolith - a tale of refactoring](https://youtu.be/iHhPsBWxQCE?feature=shared&t=10)

Sections in the video:
* Refactoring strategy
* Install and configure cypress
* Reset test user password
* Creating API Key for test user
* Import data for test user using a python script
* Creating a first UI test in cypress
* Running API tests with pytest
* Defining the final architecture
* Creating the Core Services module
* Creating a timer to migrate data
* Adding a "kill switch" to avoid infinite loops
* Running the timer to sync data
* Changing references for new Core Service module
* Creating the API Services module
* Creating the Roles module
* Testing the new API Service module
* Running the UI tests in cypress
* Fixing an error in the refactor activity
* Cleaning code after the successful refactor
* Running UI tests to make sure code clean didn't break production
