# app.py
# Infobox Explorer: search a topic on Wikipedia and see its key facts as cards.

from flask import Flask, render_template, request  # Flask = tiny web framework
import requests                                     # to call Wikipedia's API
from bs4 import BeautifulSoup                       # to read the article's HTML

app = Flask(__name__)

# Wikipedia asks apps to identify themselves
HEADERS = {"User-Agent": "InfoboxExplorer/1.0 (student project)"}


def get_summary(topic):
    """Get title, description, short summary and image for a topic."""
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + topic.replace(" ", "_")
    response = requests.get(url, headers=HEADERS, timeout=10)
    if response.status_code != 200:   # 200 = success, anything else = not found
        return None
    return response.json()


# Emoji shown on each fact card, chosen by keywords in the label
ICONS = {
    "population": "👥", "capital": "🏛️", "born": "🎂", "died": "🕊️",
    "founder": "💡", "founded": "🏗️", "established": "🏗️", "area": "📐",
    "language": "🗣️", "currency": "💰", "gdp": "📈", "president": "🧑‍💼",
    "prime": "🧑‍💼", "ceo": "🧑‍💼", "headquarters": "🏢", "industry": "🏭",
    "revenue": "💵", "employees": "🤝", "website": "🌐", "occupation": "💼",
    "nationality": "🚩", "spouse": "💍", "education": "🎓", "government": "⚖️",
    "time zone": "🕐", "calling": "📞", "elevation": "⛰️", "coordinates": "📍",
    "location": "📍", "country": "🌍", "religion": "🙏", "height": "📏",
    "products": "📦", "genre": "🎵", "released": "📅", "date": "📅",
}


def pick_icon(label):
    """Return an emoji that matches the label (default: sparkle)."""
    text = label.lower()
    for keyword, icon in ICONS.items():
        if keyword in text:
            return icon
    return "✨"


def get_infobox(title):
    """Read the infobox (the box on the right side of a Wikipedia article)
    and return a list of (label, value) facts like ("Population", "1.4 billion")."""
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": title,
        "prop": "text",        # ask for the article's HTML
        "format": "json",
        "formatversion": 2,
        "redirects": 1,
    }
    response = requests.get(url, params=params, headers=HEADERS, timeout=10)
    data = response.json()

    if "parse" not in data:
        return []

    # Turn the HTML text into something we can search through
    soup = BeautifulSoup(data["parse"]["text"], "html.parser")
    table = soup.find("table", class_="infobox")   # the infobox is a <table>
    if table is None:
        return []                                  # this article has no infobox

    facts = []
    for row in table.find_all("tr"):               # go through each row
        label_cell = row.find("th")                # left side  = label
        value_cell = row.find("td")                # right side = value
        if label_cell and value_cell:
            # remove reference numbers like [1] and style blocks
            for junk in value_cell.find_all(["sup", "style"]):
                junk.decompose()
            label = label_cell.get_text(" ", strip=True)
            value = value_cell.get_text(" ", strip=True)
            if label and value:
                facts.append({"icon": pick_icon(label), "label": label,
                              "value": value[:150]})  # cut very long values

    return facts[:16]   # keep only the first 16 facts


@app.route("/")
def home():
    topic = request.args.get("q", "").strip()   # text typed in the search box
    summary = None
    facts = []
    error = None

    if topic:
        summary = get_summary(topic)
        if summary is None:
            error = "No article found. Try another topic."
        else:
            facts = get_infobox(summary["title"])

    return render_template("index.html", topic=topic, summary=summary,
                           facts=facts, error=error)


if __name__ == "__main__":
    app.run(debug=True)   # debug=True reloads the page when you edit code
