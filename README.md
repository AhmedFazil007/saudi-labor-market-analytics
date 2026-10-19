# Saudi Labor Market Pulse | Power BI Analytics

I built this project to explore how modeled employment, job vacancies and monthly salaries vary across Saudi cities, industries and worker groups. I wanted to look beyond headline totals and compare how demand, pay and workforce composition change over time.

**Important:** This is a portfolio exercise using **synthetic data**, not official Saudi government labor-market statistics. The vacancies are simulated, not verified job openings, and salaries are not observed market benchmarks.

## Power BI report

| Page | What I explored |
| --- | --- |
| Employment Trends | Quarterly employment and vacancies, quarter-on-quarter changes and vacancy-to-employment ratio |
| Sector Demand | Vacancy counts versus vacancy ratios across economic sectors |
| Salary Analysis | Employment-weighted monthly salary trends and sector comparisons |
| Workforce Demographics | Separate nationality and gender distributions |

### Dashboard screenshots

The four final Power BI screenshots are available in `assets/screenshots/`:

- [Employment Trends](assets/screenshots/01_Employment_Trends.png)
- [Sector Demand](assets/screenshots/02_Sector_Demand.png)
- [Salary Analysis](assets/screenshots/03_Salary_Analysis.png)
- [Workforce Demographics](assets/screenshots/04_Workforce_Demographics.png)

## Dataset and approach

The simulated dataset covers **28 quarters (2019 Q1–2025 Q4)**, with **8,960 records** across Saudi cities and economic sectors. I used Power BI, Power Query and DAX to build four report pages. The repository also includes prepared analysis CSVs, a SQLite database, summary JSON, a [Python analysis script](python/analyze_labor.py) and [SQLite queries](sql/labor_market_analysis.sql).

For **2025 Q4**, the synthetic data gives approximately **260,722 employed people**, **13,826 vacancies**, a **5.30% vacancy-to-employment ratio** and an **employment-weighted monthly salary of SAR 5,309**.

Employment and vacancy counts are **quarterly snapshots**. Adding them across quarters does **not** give a unique workforce or vacancy count. The latest-quarter KPI cards are intended to avoid that mistake.

The historical nationality and gender donut charts in the current report show aggregated quarterly observations (about 7M), whereas the employment KPI shows the latest-quarter snapshot (about 261K). **Those donuts should not be interpreted as latest-quarter headcounts.** They need a matching quarter filter or a clearer historical-aggregate label before being used as a current workforce comparison.

## Open the Power BI project

To open the report:

1. Open [`Saudi_Labor_Market.pbix`](Saudi_Labor_Market.pbix) in Power BI Desktop, or open [`Saudi_Labor_Market.pbip`](Saudi_Labor_Market.pbip) for the editable Power BI project.
2. In **Transform data → Edit parameters**, set `CSVFilePath` to your local copy of `data/02_labor_market_quarterly_synthetic.csv`.
3. Select **Close & Apply**, refresh and review the four pages.
4. Save a `.pbix` copy if you want a single-file report.

The Power BI project is an editable **PBIP** folder structure with a separate report and semantic model. A **PBIX** copy is also included. The screenshots show the report rendered in Power BI Desktop, but interactions and every filter combination have not been independently tested.

## Reproduce the analysis

From the repository root, run `python python/analyze_labor.py` (Python standard library only). It reads the source CSV and writes analysis summaries and the SQLite database to `analysis/`. Open the database with a SQLite client to run the queries in `sql/labor_market_analysis.sql`.

## What I would improve next

I would make the workforce donuts follow the selected quarter, then add a compact summary of which sectors have the highest vacancy ratios rather than only the most vacancies. If I were using this for real workforce planning, I'd validate the trends against official labor-market publications before drawing policy or hiring conclusions.

## Repository status

**Published:** The PBIP project, PBIX report, source CSV, analysis outputs and four Power BI screenshots are in this repository. The Python and SQL analysis scripts are included in their respective folders.
