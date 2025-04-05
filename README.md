# TributeTracker

This project is a Discord bot that tracks the total value of items and categorical totals. It supports both manual and external inputs for updating item values.

## Features

- **Manual Input**: Users can manually input item values, which will be processed and updated in the system.
- **External Input**: The bot can also handle data from external sources to update item values.
- **Total Value Calculation**: The bot calculates the total value of all items and provides categorical totals.

## Project Structure

```
discord-bot-project
├── bot
│   ├── __init__.py
│   ├── main.py
│   ├── commands
│   │   ├── __init__.py
│   │   ├── manual_input.py
│   │   └── external_input.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── calculations.py
│   │   └── data_handler.py
│   └── config
│       ├── __init__.py
│       └── settings.py
├── requirements.txt
├── .env
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd discord-bot-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Discord bot token:
   ```
   DISCORD_TOKEN=your_token_here
   ```

4. Run the bot:
   ```
   python bot/main.py
   ```

## Usage Guidelines

- Use the command prefix defined in `settings.py` to interact with the bot.
- For manual input, use the designated command to submit item values.
- For external input, ensure the data format matches the expected structure.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the bot!