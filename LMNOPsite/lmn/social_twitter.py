import os
import twitter
from django.conf import settings
from django.contrib.sites.models import Site


# TODO fail silently if these aren't set and continue (KeyError)
api = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
                  consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                  access_token_key=os.environ['TWITTER_ACCESS_TOKEN'],
                  access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

