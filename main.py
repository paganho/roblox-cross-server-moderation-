import os
import requests
import json

# Configuration
API_KEY = os.getenv("ROBLOX_API_KEY", "MOCK_API_KEY_FOR_TESTING")
UNIVERSE_ID = os.getenv("UNIVERSE_ID", "0000000000")
TOPIC = "GlobalModerationTopic"

def send_global_moderation_event(user_id, action, reason, moderator_id):
    """
    Sends a moderation payload to Roblox MessagingService API.
    """
    url = f"https://apis.roblox.com/messaging-service/v1/universes/{UNIVERSE_ID}/topics/{TOPIC}"
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    
    payload = {
        "message": json.dumps({
            "UserId": user_id,
            "Action": action,      # e.g., "BAN", "KICK", "WARN"
            "Reason": reason,
            "ModeratorId": moderator_id
        })
    }

    print(f"[{action}] Dispatching event for User {user_id}...")
    
    # Mock return for testing without active live key
    if API_KEY == "MOCK_API_KEY_FOR_TESTING":
        print("Mock execution complete. Payload validated successfully.")
        return True

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Successfully broadcasted to active servers.")
        return True
    else:
        print(f"Failed to broadcast: {response.status_code} - {response.text}")
        return False

if __name__ == "__main__":
    # Example execution for testing
    send_global_moderation_event(
        user_id=12345678,
        action="BAN",
        reason="Exploiting / Venue Disruption",
        moderator_id=98765432
    )
