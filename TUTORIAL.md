## Step-by-step guide to building a Google Assistant 
action with Apprentice

### Our Goal 
Build a simple action that will respond with a dad joke of the day. 

Step 1 (setup development environment)
- Install Python and Apprentice
- Install ngrok
- run ngrok http 5000

Step 2 (setup the project)
- apprentice init
- export FLASK_APP=hello_world_agent.main.py
- apprentice run

Step 3 (setup the infrastructure)
- Sign into google cloud (link) and setup a Dialogflow (link) action
- Name it to factoid

Step 4 (setting up the action)
- Add the fulfillment endpoint
- add an entity (fact)
- add an intent with an action and parameter
- enable webhook for this intent

Step 5 (Testing)
- Google assistant console
- enable test app
- invoke the action
- see the call come in

Step 6 (Implementing our action)
- Write api call code
- implement intent response
- describe response and request from dialog flow

Step 7 (Testing again)
- With google assistant console.

Step 8 (Deploying to google cloud function)
- Now that it works with local setup, set it up with the gcloud function
- copy code and deploy function
- mention command

Step 9 (Deploying your action)
- walk through deployment of the action
- alpha, beta, production
