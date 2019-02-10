# copernicus

Simple javascript loader for NewsAPI.org news. Simple UX for quick news search.

The Twitter feed is via IFTTT but limited to 100 tweets per day and is
being quote-tweeted by @ParlRT twitter.com/ParlRT

## Deployment

In the below instructions you will need a valid API key for
[NewsAPI](https://newsapi.org), which can be obtained from the site.

Copy the `creds.yaml.example` to `creds.yaml` and change the
username/pass, and the api key. This file is not source controlled.



### Set up locally

    cd appengine

You will need a valid Python 3 runtime environment in order for this
to work.

    # You can add the --user option for non-root installation:
    pip install -r requirements.txt

or

    pip3 install -r requirements.txt


### Run the web app

    export NEWSAPI_KEY=... insert valid API key here ...
    python main.py


### Run Google Cloud dev server

    dev_appserver.py --port=5000 app.yaml



### Deployment to Google App Engine

- Copy `creds.yaml` to `creds.yaml.example` and populate with the
  NewsAPI key
- [Install the Google Cloud SDK](https://cloud.google.com/sdk/install)
- Go through the documented setup (e.g. `gcloud init`)
- Set up a new App Engine project
- Deploy the app:

        cd appengine
        gcloud app deploy
