# 🤖 OpenAI-Discord-Chatbot
A simple Discord bot that utilizes the OpenAI API to provide chatbot functionality in a Discord server.

### ⚙️ Prerequisites

You will need the following API keys:

  * **[OpenAI API Key](https://openai.com/api/)**
  
  * **[Discord Bot Token](https://discord.com/developers/docs/reference)**

### 🛠️ Installation & Usage

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/cdmanning/OpenAI-Discord-Chatbot
    cd OpenAI-Discord-Chatbot
    ```

2.  **Install Dependencies:**
    ```bash
    pip install openai discord
    ```

3. **Configuration**
   
    For secure token managment this bot uses environment variables. Create a `.env` file and include the following:

    ```env
    OpenAIKey="YOUR_OPENAI_API_KEY_HERE"
    DiscordAPIKey="YOUR_DISCORD_BOT_TOKEN_HERE"
    ```

5.  **Running the Bot:**
    ```bash
    python main.py
    ```

6. **Use the Chatbot**
    Call the bot using the trigger `-gpt` for example:
    ```
     -gpt How many seconds are in a day?
    ```
