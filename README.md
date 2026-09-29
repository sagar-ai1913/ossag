# Infobox Explorer

**Team Number:** [XX]
**Track:** Build with Open Source
**Event:** Open Source Day, Build with Wikimedia's Structured Wikipedia Dataset

## Team Members

| Name | GitHub Username | Contribution |
|------|-----------------|--------------|
| S J | @username | e.g. Backend: fetching and parsing infobox data (`app.py`) |
| Member 2 | @username | e.g. Frontend: page layout and styling (`index.html`) |
| Member 3 | @username | e.g. Testing, README, bonus features |
| Member 4 (if any) | @username | e.g. Dark mode / search improvements |

## About the Project

Infobox Explorer is a clean dashboard that pulls out just the hard facts
(country, population, founder, etc.) from a Wikipedia article and shows them
as simple cards, along with the article's title, short description, summary
and image.

## Features

- Search any Wikipedia topic
- Shows title, short description, summary and image
- Extracts infobox facts and displays them as cards
- Handles topics with no article or no infobox
- Animated glassmorphism UI with light and dark theme, live fact filter, click-to-copy cards, responsive layout

## Data Source

- Wikipedia data (article summaries, images, infobox facts)
- [Wikimedia Structured Wikipedia Dataset (Kaggle)](https://www.kaggle.com/)

## Tech Stack

- Python 3
- Flask (web framework)
- Requests (API calls)
- BeautifulSoup4 (reading the infobox)
- HTML and CSS

## How to Run

```bash
git clone https://github.com/USERNAME/REPO-NAME.git
cd REPO-NAME
python -m venv venv
venv\Scripts\activate        # Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Project Structure

```
app.py               # backend: fetches data and reads the infobox
templates/index.html # frontend: search box and fact cards
requirements.txt     # libraries needed
```

## Bonus Objectives Completed

- [x] Search functionality
- [x] External API usage
- [x] Dark-mode-friendly UI (light and dark toggle, animated design)
- [ ] Data visualization

## AI Usage Statement

We used AI tools (Claude) to help build this project. Every team member
understands the code and can explain how it works.

## Future Improvements

- Dark mode
- Compare infobox facts with article text to spot mismatches
- Support for Hindi and other languages
