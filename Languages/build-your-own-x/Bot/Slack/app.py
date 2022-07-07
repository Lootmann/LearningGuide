# app.py
import logging

from slack_bolt import App
from slack_sdk.web import WebClient

from onboarding_tutorial import OnboardingTutorial

app = App()

onboarding_tutorials_sent = {}


def start_onboarding(user_id: str, channel: str, client: WebClient):
    onboarding_tutorial = OnboardingTutorial(channel)
    message = onboarding_tutorial.get_message_payload()
    response = client.chat_postMessage(**message)
    onboarding_tutorial.timestamp = response["ts"]

    if channel not in onboarding_tutorials_sent:
        onboarding_tutorials_sent[channel] = {}

    onboarding_tutorials_sent[channel][user_id] = onboarding_tutorial


# ================ Team Join Event =============== #
# When the user first joins a team, the type of the event will be 'team_join'.
# Here we'll link the onboarding_message callback to the 'team_join' event.

# Note: Bolt provides a WebClient instance as an argument to the listener function
# we've defined here, which we then use to access Slack Web API methods like conversations_open.
# For more info, checkout: https://slack.dev/bolt-python/concepts#message-listening
@app.event("team_join")
def onboarding_message(event, client):
    """Create and send an onboarding welcome message to new users. Save the
    time stamp of this message so we can update this message in the future.
    """
    user_id = event.get("user", {}).get("id")
    response = client.conversations_open(users=user_id)
    channel = response["channel"]["id"]

    start_onboarding(user_id, channel, client)


# ============= Reaction Added Events ============= #
# When a users adds an emoji reaction to the onboarding message,
# the type of the event will be 'reaction_added'.
# Here we'll link the update_emoji callback to the 'reaction_added' event.
@app.event("reaction_added")
def update_emoji(event, client):
    """Update the onboarding welcome message after receiving a "reaction_added"
    event from Slack. Update timestamp for welcome message as well.
    """
    channel_id = event.get("item", {}).get("channel")
    user_id = event.get("user")

    if channel_id not in onboarding_tutorials_sent:
        return

    onboarding_tutorial = onboarding_tutorials_sent[channel_id][user_id]
    onboarding_tutorial.reaction_task_completed = True
    message = onboarding_tutorial.get_message_payload()
    updated_message = client.chat_update(**message)


# =============== Pin Added Events ================ #
# When a users pins a message the type of the event will be 'pin_added'.
# Here we'll link the update_pin callback to the 'pin_added' event.
@app.event("pin_added")
def update_pin(event, client):
    """Update the onboarding welcome message after receiving a "pin_added"
    event from Slack. Update timestamp for welcome message as well.
    """
    # Get the ids of the Slack user and channel associated with the incoming event
    channel_id = event.get("channel_id")
    user_id = event.get("user")

    onboarding_tutorial = onboarding_tutorials_sent[channel_id][user_id]
    onboarding_tutorial.pin_task_completed = True
    message = onboarding_tutorial.get_message_payload()

    updated_message = client.chat_update(**message)


# ============== Message Events ============= #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the message callback to the 'message' event.
@app.event("message")
def message(event, client):
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")

    if text and text.lower() == "start":
        return start_onboarding(user_id, channel_id, client)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    app.start(3000)
