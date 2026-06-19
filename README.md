#  Musical Time Machine

Musical Time Machine is a Python app that lets you travel back in time and generate a YouTube Music playlist based on the Billboard Hot 100 songs from any selected date.

It scrapes historical chart data and automatically creates a playlist of top songs from that day.

---

##  Features

- Scrapes Billboard Hot 100 songs for any date
- Extracts song titles automatically
- Searches songs on YouTube Music
- Creates playlists in your YouTube Music library
- Fully automated music discovery tool

---

##  Technologies Used

- Python
- Requests
- BeautifulSoup
- ytmusicapi
- python-dotenv

---

##  Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/musical-time-machine.git
cd musical-time-machine
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

---

##  YouTube Music Authentication Setup

This project requires YouTube Music authentication.

---

### Step 1: Open YouTube Music
Go to:
https://music.youtube.com

Log in to your Google account.

---

### Step 2: Open Developer Tools
- Press `F12`
- Go to the **Network** tab
- Refresh the page

---

### Step 3: Copy Request Headers
1. Click on a request named **browse**
2. Right-click it
3. Click:
   ```
   Copy → Copy request headers
   ```

---

### Step 4: Save headers locally

Create a file in your project folder:

```
headers.txt
```

Paste the copied request headers inside it.

---

### Step 5: Generate `browser.json`

Create and run a Python file (e.g. `auth.py`):

```python
from ytmusicapi import setup

with open("headers.txt", "r", encoding="utf-8") as f:
    headers = f.read()

setup(filepath="browser.json", headers_raw=headers)
```

This will generate:

```
browser.json
```

---

##  Run the Project

```bash
python main.py
```

Then enter a date in this format:

```
YYYY-MM-DD
```

Example:

```
2010-07-10
```

---

##  Project Structure

```
musical-time-machine/
│
├── main.py
├── auth.py
├── headers.txt
├── browser.json
├── requirements.txt
└── README.md
```

---

##  Important Notes

- Keep `browser.json` private (do NOT upload to GitHub)
- Regenerate headers if authentication expires
- You must be logged into YouTube Music for setup to work

---

##  License

This project is for educational purposes only.
