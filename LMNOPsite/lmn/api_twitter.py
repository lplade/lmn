import os
import twitter
import logging

logger = logging.getLogger(__name__)

try:
    api = twitter.Api(
        consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
        consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
        access_token_key=os.environ['TWITTER_ACCESS_TOKEN'],
        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    )
except KeyError:
    logger.warning("Twitter API keys not set! Tweeting disabled.")


def tweet(status_string, status_url=None):
    # Slice string if it's longer than a legal tweet
    if status_url:
        status_string = status_string[:(140 - 23)]
        status_string += status_url
    else:
        status_string = status_string[:140]

    try:
        status = api.PostUpdate(status=status_string)
        logger.debug("Tweeting: " + status.text)
        # TODO geocode based on venue?

        # TODO return false on any kind of failure
        return True
    except NameError:  # if api is not initialized
        logger.debug("Not tweeting. Set environment variables to enable.")
        return False


# TODO Do stuff with any attached images. Twitter lets us use pictures.
