# copernicus

Simple javascript loader for NewsAPI.org news. Simple UX for quick news search.

The Twitter feed is via IFTTT but limited to 100 tweets per day and is
being quote-tweeted by @ParlRT twitter.com/ParlRT


## Set up development environment

    cd appengine


### Set up Google Cloud

(This is quite fiddly and the following probably works. But it might
not work (the order of things might be wrong) so be sure to fix the
instructions if needed.)

- [Install the Google Cloud SDK](https://cloud.google.com/sdk/install)
- Go through the documented setup (e.g. `gcloud init`)
- Set up a new App Engine project

    gcloud config set project copper-seeker-231313
    export GOOGLE_CLOUD_PROJECT=copper-seeker-231313

    # Connect your Google user to the project
    gcloud auth application-default login

Copy the `google-cloud.json.example` file to `google-cloud.json` and
change the ... bits. This file is not source controlled. You should
get the key details from someone, or generate your own key

    gcloud auth activate-service-account  --key-file=google-cloud.json
    export GOOGLE_APPLICATION_CREDENTIALS=google-cloud.json


### newsapi.org Credentials

In the below instructions you will need a valid API key for
[NewsAPI](https://newsapi.org), which can be obtained from the site,
or get the one we're using.

Copy the `creds.yaml.example` file to `creds.yaml` and change the
username/pass, and the api key. This file is not source controlled.


### Set up locally

You will need a valid Python 3 runtime environment in order for this
to work.

    # You can add the --user option for non-root installation:
    pip install -r requirements.txt

or

    pip3 install -r requirements.txt


### Run the web app

    export NEWSAPI_KEY=... insert valid API key here ...
    export BASIC_AUTH_USERNAME=hello
    export BASIC_AUTH_PASSWORD=there

    python main.py
    # or
    FLASK_APP=main.py flask run


### Run Google Cloud dev server

    dev_appserver.py --port=5000 app.yaml



# Deployment to Google App Engine

- Deploy the app:

        cd appengine
        gcloud app deploy
