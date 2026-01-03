# Airbnb analytics — dbt + Snowflake

This repository contains a dbt project that implements an analytics pipeline for Airbnb data. It transforms raw source tables into cleansed dimensional models, fact tables, and a final mart used for analysis. The project includes a small seed (full moon dates), snapshot configurations, and tests to ensure data quality.

**Key points:**
- **Transforms**: source -> staging -> dimension/fact -> marts
- **Testing**: dbt tests and schema YAML enforce model expectations
- **Deployment-ready**: compiled SQL and run artifacts are available under `target/`

## What this project does

- Loads source data (see `models/src/`), applies cleansing and standardization.
- Builds dimension tables in `models/dim/` and fact tables in `models/fct/`.
- Produces a downstream mart in `models/mart/` (e.g., `mart_fullmoon_reviews`).
- Uses a seed (`seeds/seed_full_moon_dates.csv`) to enrich analysis with full-moon dates.
- Captures snapshots of raw data in `snapshots/`.

## Project structure

- **`models/`**: dbt models organized by purpose
  - `src/` — raw/source SQL selects
  - `dim/` — dimension models (cleansed host/listing tables)
  - `fct/` — fact tables (e.g., reviews)
  - `mart/` — business-ready marts
  - `schema.yml`, `sources.yml` — tests and source definitions
- **`seeds/`**: CSV seeds (e.g., `seed_full_moon_dates.csv`)
- **`snapshots/`**: snapshot definitions for slowly changing raw tables
- **`macros/`**: reusable SQL/Jinja helpers
- **`analyses/`**: ad-hoc analysis SQL for exploration
- **`target/`**: dbt's compiled SQL, run artifacts, and manifests (auto-generated)
- **`compiled/`** and **`run/`**: compiled and run-time artifacts produced by dbt
- **`logs/`**: dbt run logs

## Prerequisites

- Python 3.9+ (or your system Python)
- dbt (core and the Snowflake adapter) installed in a virtual environment
- A configured `profiles.yml` with your Snowflake (or other) connection details.

Recommended local setup commands:

```bash
# create + activate a venv (macOS / Linux)
python -m venv venv
source venv/bin/activate

# install dependencies (if you have a requirements file)
pip install -r requirements.txt || true

# or install dbt directly
pip install "dbt-core" "dbt-snowflake"
```

Note: Replace `dbt-snowflake` with the adapter you use. Do not store secrets in this repository — use environment variables or your CI/CD secret store.

## Common dbt commands

```bash
# verify connection and configuration
dbt debug

# load seed data (the full-moon dates seed)
dbt seed --select seed_full_moon_dates

# run models (example: run everything)
dbt run

# run a specific model or folder
dbt run --models mart

# run tests defined in schema.yml
dbt test

# execute snapshots
dbt snapshot

# generate and serve docs locally
dbt docs generate
dbt docs serve
```

## Where to find artifacts

- Compiled SQL: `target/compiled/<project_name>/models/` (or see `compiled/` and `run/` folders)
- Run artifacts and manifest: `target/manifest.json`, `target/run_results.json`

## Adding or modifying models

- Add new SQL models under `models/` in the appropriate folder and register tests/columns in `schema.yml`.
- Use `sources.yml` to declare and test raw tables.
- Re-run `dbt run` and `dbt test` locally before pushing changes.

## Contributing

- Follow the existing code organization and naming conventions.
- Keep tests up-to-date for any schema or logic changes.
- Open a PR with a clear description of the change and any required run steps.

## Troubleshooting

- If dbt cannot connect, run `dbt debug` and verify `profiles.yml` and environment variables.
- Look in `logs/` for detailed run logs.

## Security and secrets

Do not commit credentials, private keys, or other secrets. Store connection info in `~/.dbt/profiles.yml` or CI/CD secrets and use environment variables for runtime secrets.

## License

This project is provided as-is. Add a license file if you intend to publish or share it under a specific license.