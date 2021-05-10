# BIO539_Exam4
# Finding The linguistic complexity of the string

## What Is This?
  This is a simple Python/Flask application intended to provide a working example of Uber's external API. The goal of these endpoints is to be simple, well-documented and to    provide a base for developers to develop other applications off of.
## Instruction steps

This repository represents the steps followed to write the linguistic complexity of the string(sequence).

**1 step,** Created a function that calculates observed k-mers (unique k_mers) taking read(string) and K(int) values as an argument.\
**2 step,** Created a function calculates all the possible k-mers also taking read and K values as an argument.\
**3 step,** Created a data frame function with index, observed k-mers and possible k-mers columns.\
**4 step,** Created a function that calculates linguistic complexity taking dataframe as an argument.\
**5 step,** Created a main function that reads any string given by user and calculates the lingustic complexity.\
**6 step,** Created separate python test script to test the written python script.\

**Note** string.csv is an excel file with some sequence examples.
Example Uber app for developers
TravisCI Coverage Status

https://developer.uber.com/

What Is This?
This is a simple Python/Flask application intended to provide a working example of Uber's external API. The goal of these endpoints is to be simple, well-documented and to provide a base for developers to develop other applications off of.

How To Use This
Navigate over to https://developer.uber.com/, and sign up for an Uber developer account.
Register a new Uber application and make your Redirect URI http://localhost:7000/submit - ensure that both the profile and history OAuth scopes are checked.
Fill in the relevant information in the config.json file in the root folder and add your client id and secret as the environment variables UBER_CLIENT_ID and UBER_CLIENT_SECRET.
Run export UBER_CLIENT_ID="{your client id}"&&export UBER_CLIENT_SECRET="{your client secret}"
Run pip install -r requirements.txt to install dependencies
Run python app.py
Navigate to http://localhost:7000 in your browser
Testing
Install the dependencies with make bootstrap
Run the command make test
If you delete the fixtures, or decide to add some of your own, you’ll have to re-generate them, and the way this is done is by running the app, getting an auth_token from the main page of the app. Paste that token in place of the test_auth_token at the top of the test_endpoints.py file, then run the tests.
Development
If you want to work on this application we’d love your pull requests and tickets on GitHub!

If you open up a ticket, please make sure it describes the problem or feature request fully.
If you send us a pull request, make sure you add a test for what you added, and make sure the full test suite runs with make test.
Deploy to Heroku
Click the button below to set up this sample app on Heroku:

Deploy

After creating your app on Heroku, you have to configure the redirect URL for your Uber OAuth app. Use a https://{your-app-name}.herokuapp.com/submit URL. You will also want to configure the heroku environment variable FLASK_DEBUG=False in order to properly serve SSL traffic.

Making Requests
The base for all requests is https://api.uber.com/v1/, to find a list of all available endpoints, please visit: https://developer.uber.com/v1/endpoints/
