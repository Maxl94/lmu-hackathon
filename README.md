# From Records to Royalties

**Find the right release. Recover its songs. Show why we should trust the result.**

A four-hour hackathon for master's students, working in approximately four teams of four to five people.

[Challenge](#the-challenge) · [Data](#the-data) · [Schedule](#four-hour-workshop) · [Pitch](#your-ten-minute-pitch) · [Python setup](#optional-python-and-gemini) · [Frameworks](#optional-use-a-framework) · [Slides](#slides-and-organizer-checklist)

## Why this matters

Music royalties help composers, lyricists and publishers earn money from the use of their works. At GEMA, knowing which songs appear on a record provides an essential input for the later allocation of royalties. A barcode, album title or artist name can identify a product while its tracklist is still missing.

Finding the songs sounds simple—until you encounter a deluxe edition, a regional release, a reissue or two albums with the same name. The first plausible result can be the wrong record. Useful information is spread across catalogs and websites, and manual research takes time.

Your work starts at this gap: **build a repeatable process that automatically discovers the tracklist of the correct edition, with evidence.** Linking the recordings to musical works and their rights holders, then calculating and paying royalties, comes later and is outside this workshop.

## The challenge

**Turn five records with missing tracklists into a small, runnable discovery workflow. Then show how you would take it to 1,000.**

Your input is [a CSV file with 1,000 records](data/releases.csv). It has three columns: `barcode`, `album_title` and `album_artist`. Some values may be missing or inconsistent. These are release metadata; the file contains no internal customer data. See [the data section](#the-data) for details.

Choose **five varied records** first: include barcode cases and title/artist-only cases where possible. Run the same workflow on these records to develop and evaluate it before attempting a larger batch. Keep track of all five outcomes, including unsuccessful or uncertain ones.

For each record, aim to return:

- The release and edition you matched, with enough detail to distinguish alternatives.
- Its ordered tracklist, including disc numbers and durations where available.
- Source links that support the release match and tracklist.
- A clear outcome: a supported match, a case needing review or no match found. Keep technical failures visible too.

**The tools are your choice.** Catalog APIs, automated web search, AI, scripts, no-code workflows or combinations are all welcome. There is no required language, framework or architecture. This repository provides the CSV file and an optional Python/Vertex AI starting point; use other tools you can access.

Manual checks help you understand the records and evaluate your results. The solution itself must automate discovery. A slide describing a future system or five manually researched tracklists is not the target.

## Build something small, early

Get one record through an end-to-end workflow early, then improve it on the other four. A runnable no-code workflow counts just as much as code. Entering a record or pressing Run manually is fine; finding the release and extracting its tracklist should run automatically. Choose the simplest approach your team can get working in the time available.

You will need to make decisions, not solve everything:

- How will you find candidate releases and choose between editions?
- What evidence is enough to accept a result, and when should a person review it?
- How will you check that the songs belong to this edition?
- What changes when the workflow runs on 1,000 records: coverage, fees, runtime, source limits or review effort?

Your five chosen cases show what happened in this experiment; they do not establish accuracy or coverage across the full dataset. You do not need a production system or all 1,000 results. A small prototype with honest evidence can teach us more than a large batch of unchecked answers. If the prototype stalls, show what you tried, the actual evidence and the specific blocker. An unsuccessful experiment is useful when you can explain what it rules out and what you would try next.

## The data

[`data/releases.csv`](data/releases.csv) contains **1,000 sampled records** whose track information was marked as missing in the source snapshot. This is a starting point for discovery, not a verified catalog or an answer key. The status may have changed since that snapshot.

The CSV uses UTF-8 encoding, commas as separators and a header row with three columns. Treat barcodes as text to preserve leading zeros. Empty fields mean information was not supplied.

| Field | Description |
| --- | --- |
| `barcode` | Supplied EAN/UPC/GTIN; may be missing or invalid |
| `album_title` | Supplied album or product title; may be incomplete |
| `album_artist` | Supplied artist credit; may be missing or inconsistent |

A reproducible random sample of 1,000 rows was selected from 8,970 distinct eligible metadata combinations, using random seed 42. Only rows marked as requiring track data were selected. Customer, invoice, financial, organizational and operational fields were excluded. Exact duplicate combinations of barcode, title and artist were collapsed. Rows containing explicit organization references, web links or email addresses in these fields were also excluded. Values were otherwise preserved apart from surrounding whitespace.

One row does not necessarily equal one unique release. The same album may appear with different identifiers or spellings, and one title can refer to several editions. The data contains real supplied music metadata; it is not synthetic. It is prepared for this workshop. Removing business fields does not establish permission for unrestricted public redistribution; confirm publication permission before making the repository public.

No verified tracklists are included. Your team decides how to check the results and demonstrate reliability. There is no prescribed output format: choose one that makes the matched release, songs, sources and uncertainty easy to inspect.

## Four-hour workshop

| Time | Activity |
| --- | --- |
| 00:00–00:20 | Introduction, dataset walkthrough and team formation |
| 00:20–00:40 | Choose five records, sketch the approach and agree how to check it |
| 00:40–02:50 | Build, run and evaluate your prototype |
| 02:50–03:10 | Prepare your pitch and demonstration |
| 03:10–03:50 | Each team presents to everyone for 10 minutes |
| 03:50–04:00 | Joint discussion, select the strongest project and share takeaways |

Take a short break during the working session when needed. The pitch session starts at 03:10.

## Your ten-minute pitch

**Make us want to take your approach further—and give us evidence that it deserves it.**

Spend most of your time showing the workflow and its results. Slides, a live demo, a workflow view or a combination are fine. A saved run is useful if a live service fails.

1. **The opportunity:** Briefly explain the problem and the value of solving it.
2. **The demonstration:** Summarize the outcomes of all five cases, then demonstrate a selected case: how did you check the edition and songs? Try the same workflow on one additional record you have not prepared by hand. Run this check before your pitch if needed and save its output; do not tune the workflow specifically for that record. Show its actual outcome, including a failure if that happens. Distinguish observed results from assumptions.
3. **The choices:** Explain why you chose this method, its strengths and weaknesses, and where human review is needed.
4. **The economics and next step:** Estimate the cost of processing 1,000 records. Include relevant API/search fees, runtime, setup effort and human review. A rough estimate with stated assumptions is enough. What would you improve next?

Each team has the same 10 minutes in front of all participants. Questions follow in the joint discussion.

### How we choose the winner

We will use the same three questions for every team:

- **Does the evidence hold up?** Correct editions and tracklists, useful sources, and an honest account of all five cases.
- **Can the approach repeat?** A demonstrated automated workflow and a credible path to processing 1,000 records.
- **Are the decisions convincing?** Clear reasoning about value, alternatives, limitations, costs and the next step.

The winner is the project that makes the strongest practical case across these questions. Presentation polish is secondary to evidence and judgment. We will recognize the strongest approach, share feedback and learn from the choices each team made.

## Start here

1. Open `data/releases.csv` and read [the data section](#the-data). Preserve leading zeros in barcodes.
2. Choose your five records, agree what a correct result would look like and divide the work. Copying these input rows into your tool is fine; automating CSV import is optional.
3. Get the smallest end-to-end workflow running. Use `work/` for experiments, or your preferred tools.
4. Capture outputs, sources, failures and rough costs as you go. They are your pitch evidence.

The examples below are optional connection checks. They do not search for tracklists or solve the challenge for you.

## Optional: Python and Gemini

Run **all commands from the repository root**—the folder containing this README and `pyproject.toml`.

### 1. Install the environment

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run:

```bash
uv sync --locked
```

This sets up Python 3.12, the Google Gen AI SDK and `python-dotenv`.

### 2. Configure workshop access

Copy [`.env.example`](.env.example) to `.env` in the repository root. Fill in the project, location and model supplied by the organizer:

```dotenv
GOOGLE_CLOUD_PROJECT="PROJECT_ID"
GOOGLE_CLOUD_LOCATION="LOCATION"
GOOGLE_GENAI_MODEL="MODEL_ID"
GOOGLE_APPLICATION_CREDENTIALS="/absolute/path/outside/this/repo/key.json"
```

The organizer supplies a temporary service-account JSON key for the workshop. Keep it **outside the repository** and enter its full path in `GOOGLE_APPLICATION_CREDENTIALS`. On Windows, use forward slashes, for example `C:/Users/YourName/Downloads/key.json`.

Python loads these settings from `.env`; no shell environment setup or separate API key is needed. `.env` is ignored by Git. Do not share or commit the key. Delete your local key after the workshop; the workshop credential will also be deleted after the event.

### 3. Make your first call

Create `work/your_script.py` and paste:

```python
import os

from dotenv import load_dotenv
from google import genai

load_dotenv(".env", override=True)

with genai.Client(
    vertexai=True,
    project=os.environ["GOOGLE_CLOUD_PROJECT"],
    location=os.environ["GOOGLE_CLOUD_LOCATION"],
) as client:
    response = client.models.generate_content(
        model=os.environ["GOOGLE_GENAI_MODEL"],
        contents="What information helps distinguish different editions of an album?",
    )
    print(response.text)
```

Run it from the repository root:

```bash
uv run python work/your_script.py
```

The SDK uses the key referenced by `GOOGLE_APPLICATION_CREDENTIALS`. If the call fails, check the four `.env` values and the key path, or ask the organizer.

This example calls Gemini **without web search**. A generated answer is not source evidence for a tracklist. Each call uses the workshop cloud budget.

[Google Gen AI SDK documentation](https://googleapis.github.io/python-genai/)

## Optional: use a framework

Choose one approach; there is no need to install every framework. The direct Google SDK example above is enough to get started. These alternatives make the same connection check using the same `.env` and service-account key. They do not add search tools automatically.

### LangChain

Install only if you choose this approach:

```bash
uv add "langchain-google-genai==4.3.7"
```

Use this in `work/your_script.py`:

```python
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(".env", override=True)

model = ChatGoogleGenerativeAI(
    model=os.environ["GOOGLE_GENAI_MODEL"],
    vertexai=True,
    project=os.environ["GOOGLE_CLOUD_PROJECT"],
    location=os.environ["GOOGLE_CLOUD_LOCATION"],
)
response = model.invoke("What information helps distinguish different editions of an album?")
print(response.content)
```

`vertexai=True` selects the cloud backend. The integration uses the key referenced by `GOOGLE_APPLICATION_CREDENTIALS`.

[LangChain Google integration documentation](https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai)

### Pydantic AI

Install only if you choose this approach:

```bash
uv add "pydantic-ai-slim[google]==2.31.1"
```

Use this in `work/your_script.py`:

```python
import os

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google_cloud import GoogleCloudProvider

load_dotenv(".env", override=True)

provider = GoogleCloudProvider(
    project=os.environ["GOOGLE_CLOUD_PROJECT"],
    location=os.environ["GOOGLE_CLOUD_LOCATION"],
)
model = GoogleModel(os.environ["GOOGLE_GENAI_MODEL"], provider=provider)
agent = Agent(model)
result = agent.run_sync("What information helps distinguish different editions of an album?")
print(result.output)
```

The cloud provider uses the key referenced by `GOOGLE_APPLICATION_CREDENTIALS`.

[Pydantic AI Google Cloud documentation](https://pydantic.dev/docs/ai/models/google-cloud/)

For either framework, run your chosen script from the repository root:

```bash
uv run python work/your_script.py
```

Search tools, structured outputs and further orchestration are choices for your team. Other frameworks and languages are equally welcome.

## Slides and organizer checklist

Open [slides/index.html](slides/index.html) in a browser to present offline; use the arrow keys to navigate. Its editable source is [slides/slides.md](slides/slides.md). To rebuild it, install Node.js 24 and run:

```bash
cd slides
npm ci
npm run build
```

For a live preview with speaker notes, use **Marp**, the renderer used by this deck:

```bash
cd slides
npm ci
PORT=3030 npm run dev
```

Open `http://localhost:3030/slides.md` and press **P** for presenter view (speaker notes and next slide). Use the arrow keys to navigate. The Markdown contains Marp-specific styles; running it with `slidev` ignores those styles and breaks the layout.

GitHub Actions builds the presentation and saves it as a downloadable artifact when slide files change. This runs after the repository is hosted on GitHub; it does not publish a website.

Before the workshop, the organizer should:

- Test a live Vertex AI call using the supplied project, model, location and temporary key. Access is ready only after this succeeds; installing dependencies alone does not confirm it.
- Confirm the cloud budget and usage limits, and explain them to participants.
- Explain that other tools, including no-code services, require participants' own access. Before the event, check at least one accessible no-code route if participants need it. Help teams check authentication and connections early; do not assume licenses or integrations are available.
- Be available during the build session to help teams narrow their scope and resolve access blockers.
- Arrange credential deletion after the workshop and remind participants to remove local key copies.

## Repository and Git

```text
README.md          Workshop brief and optional setup examples
data/              CSV release data
work/              Space for your experiments
slides/            Markdown source and offline browser presentation
.github/workflows/ Slide build for GitHub Actions
pyproject.toml     Optional Python dependencies
uv.lock            Reproducible dependency versions
.env.example       Configuration template; copy to .env
```

If you use a shared Git repository, create a branch for your team:

```bash
git switch -c group-1
git status
# Add only the files you intend to share.
git add work/
git diff --cached
git commit -m "Add group experiment"
```

Keep credentials and private configuration out of Git. `.env`, `credentials/` and `outputs/` are ignored. A key saved under another filename is not automatically protected: review staged files before committing. The dataset is prepared for this workshop; check [the data section](#the-data) before redistributing it.
