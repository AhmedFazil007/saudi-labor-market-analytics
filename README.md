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

Once the report files are uploaded, the four final Power BI screenshots belong in `assets/screenshots/`:

- `01_Employment_Trends.png`
- `02_Sector_Demand.png`
- `03_Salary_Analysis.png`
- `04_Workforce_Demographics.png`

## Dataset and approach

The simulated dataset covers **28 quarters (2019 Q1–2025 Q4)**, with **8,960 records** across Saudi cities and economic sectors. I used Power BI, Power Query and DAX to build four report pages, alongside Python and SQL analysis files.

For **2025 Q4**, the synthetic data gives approximately **260,722 employed people**, **13,826 vacancies**, a **5.30% vacancy-to-employment ratio** and an **employment-weighted monthly salary of SAR 5,309**.

Employment and vacancy counts are **quarterly snapshots**. Adding them across quarters does **not** give a unique workforce or vacancy count. The latest-quarter KPI cards are intended to avoid that mistake.

The historical nationality and gender donut charts in the current report show aggregated quarterly observations (about 7M), whereas the employment KPI shows the latest-quarter snapshot (about 261K). **Those donuts should not be interpreted as latest-quarter headcounts.** They need a matching quarter filter or a clearer historical-aggregate label before being used as a current workforce comparison.

## Open the Power BI project

After the project files are uploaded:

1. Open `powerbi/Saudi_Labor_Market.pbip` in Power BI Desktop.
2. In **Transform data → Edit parameters**, set `CSVFilePath` to your local copy of `data/02_labor_market_quarterly_synthetic.csv`.
3. Select **Close & Apply**, refresh and review the four pages.
4. Save a `.pbix` copy if you want a single-file report.

The Power BI project is an editable **PBIP** folder structure. The screenshots show the report rendered in Power BI Desktop, but interactions and every filter combination have not been independently tested.

## What I would improve next

I would make the workforce donuts follow the selected quarter, then add a compact summary of which sectors have the highest vacancy ratios rather than only the most vacancies. If I were using this for real workforce planning, I'd validate the trends against official labor-market publications before drawing policy or hiring conclusions.

## Repository status

**Documentation initialized.** The Power BI project, dataset, scripts, analysis outputs and final PNG screenshots still need to be uploaded from the completed project package. This README is not a claim that those files are already present.
