-- SQLite queries for synthetic quarterly labor market observations.
-- Each row is a modeled city-sector-nationality-gender cohort.
-- Do not sum employment across quarters as unique individuals.

-- Quarterly estimates and employment-weighted salary
SELECT quarter, SUM(estimated_employed_people) AS employed,
 SUM(estimated_open_vacancies) AS vacancies,
 ROUND(100.0*SUM(estimated_open_vacancies)/SUM(estimated_employed_people),2) AS vacancy_ratio_pct,
 ROUND(SUM(estimated_average_monthly_salary_sar*estimated_employed_people)/SUM(estimated_employed_people),2) AS weighted_salary_sar
FROM labor_market GROUP BY quarter ORDER BY quarter;

-- Latest-quarter sector comparisons
SELECT economic_sector, SUM(estimated_employed_people) AS employed,
 SUM(estimated_open_vacancies) AS vacancies,
 ROUND(100.0*SUM(estimated_open_vacancies)/SUM(estimated_employed_people),2) AS vacancy_ratio_pct,
 ROUND(SUM(estimated_average_monthly_salary_sar*estimated_employed_people)/SUM(estimated_employed_people),2) AS weighted_salary_sar
FROM labor_market WHERE quarter=(SELECT MAX(quarter) FROM labor_market)
GROUP BY economic_sector ORDER BY vacancies DESC;

-- Latest-quarter city comparisons
SELECT city, SUM(estimated_employed_people) AS employed,
 SUM(estimated_open_vacancies) AS vacancies,
 ROUND(100.0*SUM(estimated_open_vacancies)/SUM(estimated_employed_people),2) AS vacancy_ratio_pct
FROM labor_market WHERE quarter=(SELECT MAX(quarter) FROM labor_market)
GROUP BY city ORDER BY vacancy_ratio_pct DESC;

-- Latest-quarter nationality shares
SELECT nationality_group, SUM(estimated_employed_people) AS employed,
 ROUND(100.0*SUM(estimated_employed_people)/(SELECT SUM(estimated_employed_people) FROM labor_market WHERE quarter=(SELECT MAX(quarter) FROM labor_market)),2) AS share_pct
FROM labor_market WHERE quarter=(SELECT MAX(quarter) FROM labor_market)
GROUP BY nationality_group ORDER BY employed DESC;

-- Latest-quarter gender shares
SELECT gender, SUM(estimated_employed_people) AS employed,
 ROUND(100.0*SUM(estimated_employed_people)/(SELECT SUM(estimated_employed_people) FROM labor_market WHERE quarter=(SELECT MAX(quarter) FROM labor_market)),2) AS share_pct
FROM labor_market WHERE quarter=(SELECT MAX(quarter) FROM labor_market)
GROUP BY gender ORDER BY employed DESC;
