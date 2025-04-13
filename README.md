# TributeTracker

This project is a Discord bot that tracks the total value of items and categorical totals. 

## Features

- **Manual Input**: Users can manually input item values, which will be processed and updated in the system.
- **Currency Conversion**: Users can specify both their desired currency and total other compatible currencies as they go.
- **Total Value Calculation**: The bot calculates the total value of all items and provides monthly totals.

## Project Structure

```
TributeTracker
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
│   │   ├── currency_conversion.py
│   │   └── data_handler.py
│   └── config
│       ├── __init__.py
│       ├── settings.py
│       └── structures.py
├── requirements.txt
├── .env (REQUIRED BUT NOT INCLUDED IN REPO)
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd TributeTracker
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

## Future plans

- Categorical filtering of totals coming soon.
- External inputs (YouPay, Throne, etc.)

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the bot!