# 🔍 Price Monitor

Automated price monitor for Mac Mini M4 on MediaWorld.it

## What it does

- Scrapes daily price from MediaWorld
- Saves price history in SQLite database
- Sends Telegram notification when price drops

## Tech Stack

- Python
- Playwright
- SQLite
- Telegram Bot API
- Schedule

## Installation

```bash
pip install -r requirements.txt
playwright install chromium
```

## Configuration

Create `.env` file:

```
TELEGRAM_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat_id
```

## Usage

```bash
python scheduler.py
```

## Project Structure

```
price_monitor/
    main.py        → orchestrator
    scraper.py     → price scraping
    database.py    → SQLite operations
    notifier.py    → Telegram notifications
    scheduler.py   → automation
```
