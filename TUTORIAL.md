## Step-by-step guide to building a Dad Joke action with Apprentice

### Our Goal 
Build a simple action that will respond with a dad joke of the day. 

Step 1 (setup development environment)
- Install Python and Apprentice
- Install ngrok
- run `./ngrok http 5000`

Step 2 (setup the project)
- `apprentice init`
- `export FLASK_APP=main.py`
- `apprentice run`

Step 3 (setup the infrastructure)
- Sign into google cloud (link) and setup a Dialogflow (link) action
- Name it to Dad Joke

Step 4 (setting up the action)
- Add the fulfillment endpoint
- add an entity (joke, humor, dad)
- add an intent with an action and parameter
- enable webhook for this intent

Step 5 (Hello World)
- Google assistant console
- enable test app
- invoke the action
- see the call come in

---

Step 6 (Implementing our action)
- Write api call code
    - add requests to requirements
    - 
- implement intent response
- describe response and request from dialog flow

Step 7 (Testing again)
- With google assistant console.

---  

Step 8 (Deploying to google cloud function)
- Now that it works with local setup, set it up with the gcloud function
- console -> cloud functions -> enable billing -> enable api -> create function
- copy code and deploy function
- mention command
- change fulfillment endpoint to cloud function endpoint
- turn off ngrok and local server
- go to assistant console and run command

Step 9 (Deploying your action)
- walk through deployment of the action
- alpha, beta, production


Articles
1. Get going hello world response
1. implement api call
1. deploy to google cloud functions
1. Why dialogflow and serverless functions are like peas and carrots
