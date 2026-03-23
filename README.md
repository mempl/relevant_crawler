# AI Scraper

An AI-powered focused web crawler that uses Claude to intelligently scrape documentation into a single, clean markdown file.

Instead of blindly crawling everything, it asks Claude at every step:

- **"Should I follow this link?"** — only follows links relevant to your topic
- **"Is this content relevant?"** — strips ads, nav, boilerplate, and off-topic sections

The result is a focused, readable markdown document containing only the documentation you actually care about.

## How it works

```
Seed URLs → Fetch page → Clean HTML → Convert to markdown
                ↓                            ↓
        Extract links              AI judges content relevance
                ↓                            ↓
    AI picks relevant links        Keep or discard page
                ↓
        Add to queue → repeat until depth limit
                ↓
    Combine into one .md file + URL list
```

## Installation

**Requirements:** Python 3.11+, an [Anthropic API key](https://console.anthropic.com/)

```bash
# Clone the repo
git clone https://github.com/yourname/ai-scraper.git
cd ai-scraper

# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows

# Install
pip install -e .

# Or without editable install:
pip install -r requirements.txt
```

## Setup

Set your Anthropic API key as an environment variable:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

Or create a `.env` file and source it:

```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' > .env
source .env
```

## Usage

### Basic usage

```bash
ai-scraper \
    --urls "https://docs.databricks.com/en/genie/index.html" \
    --topic "Databricks Genie documentation and features" \
    --depth 3 \
    -o genie_docs.md
```

### Multiple seed URLs

```bash
ai-scraper \
    --urls "https://docs.example.com/intro" "https://docs.example.com/api" \
    --topic "Example SDK" \
    --depth 2
```

### Load seed URLs from a file

Create a text file with one URL per line (blank lines and `#` comments are supported):

```text
# seeds.txt
https://docs.databricks.com/en/genie/index.html
https://docs.databricks.com/en/genie/setup.html
```

Then:

```bash
ai-scraper \
    --urls-file seeds.txt \
    --topic "Databricks Genie" \
    -o genie_docs.md
```

You can combine `--urls` and `--urls-file` — all URLs are merged.

### List scraped URLs

Add `--list-urls` to print all scraped URLs to stdout after the crawl. A `<output>.urls.txt` file is always saved regardless.

```bash
ai-scraper \
    --urls "https://docs.example.com" \
    --topic "Example SDK" \
    --list-urls
```

### Running without installing

If you prefer not to install the package:

```bash
pip install -r requirements.txt
python -m ai_scraper.cli --urls "https://..." --topic "..."
```

## All options

| Flag | Default | Description |
|------|---------|-------------|
| `--urls` | — | One or more seed URLs |
| `--urls-file` | — | Path to a file of seed URLs (one per line) |
| `--topic` | *required* | Topic description for AI relevance judgment |
| `--depth` | `3` | Max crawl depth |
| `-o`, `--output` | `output.md` | Output markdown file |
| `--domains` | *auto* | Allowed domains (default: inferred from seed URLs) |
| `--max-pages` | `100` | Safety cap on total pages scraped |
| `--delay` | `1.0` | Seconds between HTTP requests |
| `--model` | `claude-sonnet-4-20250514` | Anthropic model to use |
| `--list-urls` | off | Print scraped URL list to stdout |
| `-v`, `--verbose` | off | Debug logging |

## Example: scraping Databricks Genie docs

```bash
ai-scraper \
    --urls-file examples/databricks_genie_seeds.txt \
    --topic "Databricks Genie: AI/BI dashboard assistant, setup, configuration, natural language querying, trusted assets, instructions, and administration" \
    --depth 3 \
    --max-pages 50 \
    -o genie_docs.md
```

This will:

1. Start from the Genie index page
2. Follow links that Claude thinks lead to more Genie documentation
3. On each page, Claude strips out irrelevant content (navigation, ads, unrelated docs)
4. Continue up to 3 levels deep, capping at 50 pages
5. Output `genie_docs.md` (the combined document) and `genie_docs.urls.txt` (list of all URLs scraped)

## Cost estimate

Each page requires ~2 API calls (one for content judgment, one for link judgment). With Sonnet at roughly $3/M input tokens and $15/M output tokens, a 50-page crawl typically costs under $1.

## Project structure

```
ai-scraper/
├── src/
│   └── ai_scraper/
│       ├── __init__.py      # Package metadata
│       ├── ai.py            # AI relevance judgment (links + content)
│       ├── cli.py           # CLI entrypoint & argument parsing
│       ├── crawler.py       # Core crawl loop
│       ├── fetcher.py       # HTML fetching, cleaning, markdown conversion
│       ├── models.py        # Data classes (Page, CrawlConfig, CrawlState)
│       └── output.py        # Output formatting (markdown + URL list)
├── examples/
│   └── databricks_genie_seeds.txt
├── pyproject.toml
├── requirements.txt
├── LICENSE
├── README.md
└── .gitignore
```

## Tips

- **Start small.** Use `--max-pages 10 --depth 1` for a test run before going deep.
- **Be specific with `--topic`.** The more descriptive your topic string, the better Claude can judge relevance. "Databricks Genie setup and natural language queries" works better than just "Genie".
- **Respect rate limits.** The default 1-second delay is polite. Increase with `--delay 2` if you're hitting a site that's sensitive.
- **Restrict domains.** By default the crawler stays on the same domain(s) as your seed URLs. Use `--domains` to override.

## License

MIT
