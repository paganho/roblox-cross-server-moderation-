# Roblox Cross-Server Moderation Engine 🛡️

A Python script designed for Roblox community managers and safety leads. It interfaces with Roblox Open Cloud APIs (MessagingService & Datastores) to broadcast real-time moderation actions (bans, kicks, warnings) across all active game instances.

## 🚀 Features
- **Global Ban Sync:** Instantly sync bans across running game servers without restarting instances.
- **Audit Logging:** Formats moderation actions for clean JSON export and webhook integration.
- **Batch Processing:** Handles multiple user IDs simultaneously for automated safety enforcement.

## 🛠️ Prerequisites
- Python 3.8+
- Roblox Open Cloud API Key (with MessagingService/Datastore permissions)
- `requests` library

## 📋 Quick Start
1. **Clone the repository:**
   ```bash
   git clone https://github.com/paganho/roblox-cross-server-moderation.git(https://github.com/paganho/roblox-cross-server-moderation.git)
   cd roblox-cross-server-moderation

