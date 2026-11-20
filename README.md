# From Records to Royalties

**Find the right release. Recover its songs. Show why we should trust the result.**

A four-hour hackathon for master's students, working in approximately four teams of four to five people.

[Challenge](#the-challenge) · [Data](#the-data) · [Schedule](#four-hour-workshop) · [Pitch](#your-ten-minute-pitch) · [Getting started](#getting-started-get-the-repository) · [Python setup](#optional-python-and-gemini) · [Frameworks](#optional-use-a-framework) · [Slides](#slides-and-organizer-checklist)

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
- Its ordered tracklist with song titles and performing artists, including disc numbers where available.
- Source links that support the release match and tracklist.
- A clear outcome: a supported match, a case needing review or no match found. Keep technical failures visible too.

**The tools are your choice.** Catalog APIs, automated web search, AI, scripts, no-code workflows or combinations are all welcome. There is no required language, framework or architecture. This repository provides the CSV file and an optional Python/Gemini starting point; use other tools you can access.

Manual checks help you understand the records and evaluate your results. The solution itself must automate discovery. A slide describing a future system or five manually researched tracklists is not the target.

### Optional bonus: enrich each track

Once your tracklist discovery works, extend your automated workflow to collect more information for each track:

- **Track length:** duration in `mm:ss` or seconds, for the recording on the matched release.
- **Credits:** lyricists, composers and producers, where available. Keep these roles separate from the performing artists; do not assume the performer wrote the song.
- **Other useful metadata:** for example featured artists, recording/version details or an ISRC, where supported by a source.

Include source links for the added information and mark missing or conflicting values explicitly. Do not guess credits or durations. Explain how you checked that the information belongs to the correct track and version.

This is a bonus, not a prerequisite for a good pitch. Prioritize a working discovery workflow before adding enrichment.

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
| 03:50–04:00 | Discuss |

Take a short break during the working session when needed. The pitch session starts at 03:10.

## Your ten-minute pitch

**Make us want to take your approach further—and give us evidence that it deserves it.**

Spend most of your time showing the workflow and its results. Slides, a live demo, a workflow view or a combination are fine. A saved run is useful if a live service fails.

1. **The opportunity:** Briefly explain the problem and the value of solving it.
2. **The demonstration:** Summarize the outcomes of all five cases, then demonstrate a selected case: how did you check the edition and songs? Try the same workflow on one additional record you have not prepared by hand. Run this check before your pitch if needed and save its output; do not tune the workflow specifically for that record. Show its actual outcome, including a failure if that happens. Distinguish observed results from assumptions.
3. **The choices:** Explain why you chose this method, its strengths and weaknesses, and where human review is needed.
4. **The economics and next step:** Estimate the cost of processing 1,000 records. Include relevant API/search fees, runtime, setup effort and human review. A rough estimate with stated assumptions is enough. What would you improve next?

Each team has the same 10 minutes in front of all participants. Questions follow in the joint discussion.

### What we will discuss

We will use the same three questions for every team:

- **Does the evidence hold up?** Correct editions and tracklists, useful sources, and an honest account of all five cases.
- **Can the approach repeat?** A demonstrated automated workflow and a credible path to processing 1,000 records.
- **Are the decisions convincing?** Clear reasoning about value, alternatives, limitations, costs and the next step.

Presentation polish is secondary to evidence and judgment. We will share feedback and learn from the choices each team made.

## Start here

1. Get a local copy using [Getting started](#getting-started-get-the-repository), then open `data/releases.csv` and read [the data section](#the-data). Preserve leading zeros in barcodes.
2. Choose your five records, agree what a correct result would look like and divide the work. Copying these input rows into your tool is fine; automating CSV import is optional.
3. Get the smallest end-to-end workflow running. Use `work/` for experiments, or your preferred tools.
4. Capture outputs, sources, failures and rough costs as you go. They are your pitch evidence.

The examples below are optional connection checks. They do not search for tracklists or solve the challenge for you.

## Getting started: get the repository

New to these tools? **Git** downloads the repository and tracks changes. **Python** runs Python scripts. **uv** installs Python and the packages those scripts need. Git and the Python setup are optional if you use a no-code tool; you still need the workshop data.

### 1. Install Git and uv

Choose your operating system below. Run commands one line at a time in the indicated terminal, pressing Enter after each line. Skip tools you already have. Install uv only if you want to use the Python examples.

<details>
<summary><strong>Windows — PowerShell</strong></summary>

Open **PowerShell** from the Start menu.

Install Git using the [official Git for Windows installer](https://git-scm.com/install/win), or run:

```powershell
winget install --id Git.Git -e --source winget
```

Install uv:

```powershell
winget install --id=astral-sh.uv -e
```

If `winget` is unavailable, use the Git installer and the Windows instructions in the [official uv installation guide](https://docs.astral.sh/uv/getting-started/installation/).

Close PowerShell and open it again after installation so it can find the new commands.

</details>

<details>
<summary><strong>macOS — Terminal</strong></summary>

Open **Terminal** using Spotlight (Command + Space, then type “Terminal”).

Install Git through Apple's Command Line Tools and finish the installation dialog:

```bash
xcode-select --install
```

If the tools are already installed, continue. Other options are listed in the [official Git installation guide for macOS](https://git-scm.com/install/mac).

Install uv using its [official installer](https://docs.astral.sh/uv/getting-started/installation/):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close Terminal and open it again after installation.

</details>

<details>
<summary><strong>Linux — Terminal</strong></summary>

Open your terminal. On Ubuntu or Debian, install Git with:

```bash
sudo apt update
sudo apt install git
```

On Fedora, use `sudo dnf install git`. For other distributions, see the [official Git installation guide for Linux](https://git-scm.com/install/linux). Your package manager may ask for your computer password.

Install uv using its [official installer](https://docs.astral.sh/uv/getting-started/installation/):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

If `curl` is missing, install it with your distribution's package manager first. Close your terminal and open it again after installation.

</details>

Check the installation in your new terminal (skip the uv check if you are not using Python):

```bash
git --version
uv --version
```

Each command should print a version number. If a command is not found, restart your terminal first; if it still fails, ask the organizer.

### 2. Download your copy (clone)

Open the [workshop repository on GitHub](https://github.com/cloudIT4IPM/ai4-lmu-hackathon) and confirm you can access it. Then run these commands in your terminal (the same commands work in PowerShell):

```bash
git clone https://github.com/cloudIT4IPM/ai4-lmu-hackathon.git
cd ai4-lmu-hackathon
```

`git clone` creates a folder with the workshop files. `cd` moves your terminal into that folder. This is the **repository root**: you should see `README.md`, `data/` and `pyproject.toml` when you open it in your file manager or editor. Keep this terminal open for the setup below.

If Git asks you to sign in, use the GitHub account that has repository access. A “Repository not found” or permission error can mean that access has not been granted; ask the organizer.

**Without Git:** on the repository page, choose **Code → Download ZIP**, extract it, and open the extracted folder. If you cannot access GitHub, ask the organizer for the workshop ZIP or CSV. To run the Python commands, open a terminal in the extracted folder containing `pyproject.toml`. ZIP downloads do not include Git history; you can skip the Git collaboration instructions.

### 3. Install Python with uv (optional)

For the Python examples, run this from the repository root on **any of the three operating systems**:

```bash
uv python install 3.12
```

You do not need to install Python separately before installing uv. The [uv Python installation guide](https://docs.astral.sh/uv/guides/install-python/) explains how it manages Python for you.

If you want a separate Python installation for other work, the [official Python downloads](https://www.python.org/downloads/) provide platform links. For this workshop, use the uv command above so everyone uses the version specified by the repository.

Continue with the environment setup below. If you use another language or a no-code tool, return to [Start here](#start-here).

## Optional: Python and Gemini

Run **all commands from the repository root**—the folder containing this README and `pyproject.toml`.

### 1. Install the environment

After completing [Getting started](#getting-started-get-the-repository), run:

```bash
uv sync --locked
uv run python --version
```

This creates the project environment and installs the Google Gen AI SDK and `python-dotenv`. The final command should print `Python 3.12.x`. No manual environment activation is needed; use `uv run` for the examples below.

### 2. Choose your access method

**Start with the Gemini API key unless your team needs Google Cloud access.** Both options below call Gemini; you only need one. The organizer supplies the credentials. You do not need to create a Google Cloud project or service account yourself.

| | Gemini API key — easiest start | Vertex AI — service account |
| --- | --- | --- |
| What you receive | A secret API key (text) | A temporary JSON key file |
| What it connects to | Gemini Developer API | Vertex AI in the workshop Google Cloud project |
| What to configure | API key and model | Key file path, project, location and model |

These credentials are for different services and are not interchangeable. A Gemini API key does not give you access to the whole Vertex AI Model Garden. Other models on Vertex AI may require separate enablement and their own integration; ask the organizer before relying on them.

Create a file named **`.env`** in the repository root (next to this README). You can copy [`.env.example`](.env.example) and fill in the section you need. Keep the filename exactly `.env`, not `.env.txt`. Both examples explicitly load it with `python-dotenv`, so no terminal `export` commands are needed.

### Option A: Gemini API key

Put these settings in `.env`, replacing the placeholder with the key supplied by the organizer:

```dotenv
GEMINI_API_KEY="PASTE_YOUR_API_KEY_HERE"
GOOGLE_GENAI_MODEL="gemini-3.8-flash"
```

Create `work/your_script.py` and paste:

```python
import os

from dotenv import load_dotenv
from google import genai

load_dotenv(".env", override=True)

with genai.Client(
    vertexai=False,
    api_key=os.environ["GEMINI_API_KEY"],
) as client:
    response = client.models.generate_content(
        model=os.environ["GOOGLE_GENAI_MODEL"],
        contents="Reply with exactly OK.",
    )
    print(response.text)
```

Run it from the repository root:

```bash
uv run python work/your_script.py
```

You should see `OK`. You can now replace the prompt with your own question.

### Option B: Vertex AI with a service-account key

A **service account** is an identity for software. Its JSON key lets your script use the permissions the organizer has assigned to it in the workshop project. You do not need to sign in with your personal Google account or install the Google Cloud CLI.

Save the supplied JSON file **outside the repository**. Put these settings in `.env`, replacing the example path with the full path to your file:

```dotenv
GOOGLE_CLOUD_PROJECT="lmu-hackathon-dev-2926"
GOOGLE_CLOUD_LOCATION="global"
GOOGLE_GENAI_MODEL="gemini-3.8-flash"
GOOGLE_APPLICATION_CREDENTIALS="/absolute/path/outside/this/repo/key.json"
```

Example paths:

- macOS: `/Users/YourName/Downloads/key.json`
- Windows: `C:/Users/YourName/Downloads/key.json` (use forward slashes)
- Linux: `/home/YourName/Downloads/key.json`

Use the filename you actually received. The value is a **local file path**, not a web link or the JSON contents. If an earlier setup uses `SA_KEY_FILE`, rename that setting to `GOOGLE_APPLICATION_CREDENTIALS`.

Paste this alternative into `work/your_script.py`:

```python
import os

from dotenv import load_dotenv
from google import genai
from google.oauth2 import service_account

load_dotenv(".env", override=True)

credentials = service_account.Credentials.from_service_account_file(
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

with genai.Client(
    vertexai=True,
    project=os.environ["GOOGLE_CLOUD_PROJECT"],
    location=os.environ["GOOGLE_CLOUD_LOCATION"],
    credentials=credentials,
) as client:
    response = client.models.generate_content(
        model=os.environ["GOOGLE_GENAI_MODEL"],
        contents="Reply with exactly OK.",
    )
    print(response.text)
```

Run it with the same command:

```bash
uv run python work/your_script.py
```

You should see `OK`. This example explicitly uses the JSON credentials, even if your `.env` also contains a Gemini API key. The required packages are already installed by `uv sync --locked`.

### If something goes wrong

| Symptom | What to check |
| --- | --- |
| `KeyError` for a setting | Check its spelling and value in `.env`. Run the script from the repository root. |
| Key file not found | Use the full local path and the actual JSON filename. |
| Invalid API key / unauthenticated | Check that you copied the correct credential for your chosen option; ask the organizer if it has expired or been revoked. |
| `403` / permission denied | Ask the organizer to check the service account's project permissions and that the Vertex AI API is enabled. |
| `404` / model not found | Check the model, project and location against the settings above; availability can differ between the two services. |
| `429` / quota exceeded | Slow down your requests and ask the organizer about the workshop limits. |

Both examples are **connection checks without web search**. A generated answer is not source evidence for a tracklist. Calls consume the workshop API/cloud budget; start small.

Keep API keys, JSON keys and `.env` out of commits, screenshots and presentations. `.env` is ignored by Git. Do not share credentials outside the workshop. The organizer will revoke the workshop credentials after the event; delete your local copies too.

[Google Gen AI SDK documentation](https://googleapis.github.io/python-genai/)

## Optional: use a framework

The Google SDK examples above are enough to start. If your team prefers a framework, choose one and follow its setup guide:

- **[LangChain Google integration](https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai):** model calls and workflows in LangChain.
- **[Pydantic AI Google models](https://ai.pydantic.dev/models/google/):** agents and structured outputs.

Select the same backend as your chosen option: Gemini Developer API with an API key, or Vertex AI with service-account credentials. Framework configuration differs, so follow the relevant provider instructions. If you use Python, keep `load_dotenv(".env", override=True)` before creating the provider. Search tools are not added automatically.

Other frameworks, languages and no-code tools are equally welcome. Use their credential settings instead of the Python examples, and check that they support your chosen backend.

## Slides and organizer checklist

The presentation uses **Slidev**. Its editable source is [slides/slides.md](slides/slides.md), with the layout styles in [slides/style.css](slides/style.css).

Install [Node.js 24](https://nodejs.org/en/download), then run from the repository root:

```bash
cd slides
npm ci
npm run dev
```

Open **http://localhost:3030** for the slides or **http://localhost:3030/presenter** for presenter view with speaker notes and the next slide. Use the arrow keys to navigate. Stop the server with Ctrl+C. Use this same start command on Windows, macOS and Linux; no global Slidev installation is needed.

**Alternative: start Slidev directly from the repository root.** After installing the slide dependencies with `npm ci` in `slides/`, if the `slidev` command is already installed globally, run:

```bash
slidev slides/slides.md
```

This starts the same presentation on the default port 3030. Choose either this command or `npm run dev`; do not run both servers at once.

To build the browser presentation and preview that build, run these commands from the `slides/` folder:

```bash
npm run build
npm run preview
```

The build is written to `slides/dist/`. Serve this folder over HTTP; do not open its `index.html` directly as a local file. GitHub Actions builds and uploads the complete folder as the `workshop-slides` artifact when slide files change. It does not publish a website.

Before the workshop, the organizer should:

- Confirm participants can obtain the repository and data. If GitHub access is unavailable, provide a workshop ZIP or CSV before the session.

- Test both connection examples with the credentials participants will receive: Gemini API key and Vertex AI service-account key. For Vertex AI, enable the API and grant the service account `roles/aiplatform.user` on the workshop project. Access is ready only after the calls succeed; installing dependencies alone does not confirm it.
- Confirm the cloud budget and usage limits, and explain them to participants.
- Explain that other tools, including no-code services, require participants' own access. Before the event, check at least one accessible no-code route if participants need it. Help teams check authentication and connections early; do not assume licenses or integrations are available.
- Be available during the build session to help teams narrow their scope and resolve access blockers.
- Arrange credential deletion after the workshop and remind participants to remove local key copies.

## Repository and Git

```text
README.md          Workshop brief and optional setup examples
data/              CSV release data
work/              Space for your experiments
slides/            Slidev source, styles and presentation tooling
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
