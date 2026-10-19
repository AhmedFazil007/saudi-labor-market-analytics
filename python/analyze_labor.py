"""Reproduce quarterly Saudi labor-market descriptive analysis using standard Python."""
from pathlib import Path
from collections import defaultdict
import csv, json, sqlite3
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'data/02_labor_market_quarterly_synthetic.csv'
OUT=ROOT/'analysis';OUT.mkdir(exist_ok=True)
DASH=ROOT/'dashboard';DASH.mkdir(exist_ok=True)
with SOURCE.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
required=['quarter','city','region','economic_sector','nationality_group','gender','estimated_employed_people','estimated_average_monthly_salary_sar','estimated_open_vacancies','vacancy_to_employment_pct']
assert rows and set(required)<=set(rows[0]),'Missing required columns'
assert all(all(r[c].strip() for c in required) for r in rows),'Missing data'
keys=[tuple(r[c] for c in ('quarter','city','economic_sector','nationality_group','gender')) for r in rows]
assert len(keys)==len(set(keys)),'Duplicate quarter/city/sector/nationality/gender records'
for r in rows:
 for c in ['estimated_employed_people','estimated_open_vacancies']:r[c]=int(r[c])
 for c in ['estimated_average_monthly_salary_sar','vacancy_to_employment_pct']:r[c]=float(r[c])
 assert r['estimated_employed_people']>0 and r['estimated_open_vacancies']>=0
 assert abs(r['vacancy_to_employment_pct']-100*r['estimated_open_vacancies']/r['estimated_employed_people'])<=0.011
quarters=sorted({r['quarter'] for r in rows})
assert len(quarters)==28

def summary(records):
 emp=sum(r['estimated_employed_people'] for r in records)
 vac=sum(r['estimated_open_vacancies'] for r in records)
 payroll=sum(r['estimated_average_monthly_salary_sar']*r['estimated_employed_people'] for r in records)
 return {'employed':emp,'vacancies':vac,'weighted_salary_sar':round(payroll/emp,2) if emp else None,'vacancy_ratio_pct':round(100*vac/emp,2) if emp else None}

def write_csv(name, data):
 if not data:return
 with (OUT/name).open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)

quarterly=[{'quarter':q,**summary([r for r in rows if r['quarter']==q])} for q in quarters]
write_csv('quarterly.csv',quarterly)
latest=quarters[-1]
recent=[r for r in rows if r['quarter']==latest]
for name,field in [('latest_city.csv','city'),('latest_region.csv','region'),('latest_sector.csv','economic_sector'),('latest_nationality.csv','nationality_group'),('latest_gender.csv','gender')]:
 groups=sorted({r[field] for r in recent})
 write_csv(name,[{field:g,**summary([r for r in recent if r[field]==g])} for g in groups])
for name,fields in [('latest_city_sector.csv',('city','economic_sector')),('sector_nationality.csv',('economic_sector','nationality_group'))]:
 data=recent if name.startswith('latest') else rows
 groups=sorted({tuple(r[f] for f in fields) for r in data})
 write_csv(name,[{**dict(zip(fields,g)),**summary([r for r in data if tuple(r[f] for f in fields)==g])} for g in groups])
overview={'records':len(rows),'quarters':len(quarters),'latest_quarter':latest,**summary(recent)}
(OUT/'summary.json').write_text(json.dumps(overview,indent=2),encoding='utf-8')
db=sqlite3.connect(OUT/'labor_market.sqlite')
try:
 db.execute('DROP TABLE IF EXISTS labor_market')
 db.execute('CREATE TABLE labor_market (quarter TEXT, city TEXT, region TEXT, economic_sector TEXT, nationality_group TEXT, gender TEXT, estimated_employed_people INTEGER, estimated_average_monthly_salary_sar REAL, estimated_open_vacancies INTEGER, vacancy_to_employment_pct REAL)')
 db.executemany('INSERT INTO labor_market VALUES (?,?,?,?,?,?,?,?,?,?)',[tuple(r[c] for c in required) for r in rows])
 db.commit()
finally:db.close()
print(json.dumps(overview,indent=2))
