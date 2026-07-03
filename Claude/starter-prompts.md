# Starter Prompts — Option B: Data Analyst

These are **opening prompts** — one for each phase of the project. They are designed to get you started, not to do the work for you.

After running each starter prompt, you must **follow up**. Ask Claude Code to dig deeper, fix something that looks off, try a different approach, or explain what it found. The starter prompt is the door — you decide what's on the other side.

> **Reminder:** Adapt these prompts to your actual situation. If Claude Code produces something unexpected, say so. If a chart doesn't look right, describe what you wanted instead. If you want to explore something the prompt didn't ask for, ask.

---

## Phase 1 — Explore

> **Paste this at the start of your Claude Code session, after setting up your environment.**

```
I'm starting a data analysis project. The dataset is at data/latam_finanzas_2025.csv
and it contains survey responses from 500 young professionals across Latin America.

Before I touch the data, I need to understand what I'm working with. Please:

1. Read the file and print the number of rows and columns
2. List every column with its name and data type
3. Count the missing values in each column and show them sorted from most to least
4. Show the basic statistics for all numeric columns (min, max, mean, median, std)
5. For each categorical column (pais, industria, ocupacion, meta_financiera,
   tiene_tarjeta_credito, tiene_cuenta_ahorro, tiene_deuda), show the unique 
   values and how many times each appears

Save the script that does this to scripts/01_explore.py
```

**After the output, ask yourself:**
- Do the unique values look clean? Any typos or inconsistencies?
- Which columns have missing values and how many?
- Do the min/max values make sense for each column?

---

## Phase 2 — Clean

> **Run this after completing Phase 1 and reviewing the output.**

```
Based on the exploration, I've identified some data quality issues.
Please help me clean the dataset.

Using the original file data/latam_finanzas_2025.csv:

1. Check the 'industria' column for inconsistent values (spelling variations,
   different capitalizations, abbreviations for the same industry) and 
   standardize them. Show me all unique values before and after the fix.

2. For missing values in numeric columns: show me the percentage missing
   for each column and suggest whether to fill them with the median, 
   drop the rows, or leave them — then apply your recommendation.

3. Check 'ahorro_mensual_usd' for negative values. How many are there?
   These are valid (spending more than earning) — do NOT remove them,
   but flag them in a new boolean column called 'ahorro_negativo'.

4. Save the clean dataset to data/latam_finanzas_clean.csv
5. Print a summary: rows before vs. after, changes made

Save the script to scripts/02_clean.py
```

**After cleaning, add a "Data Quality Log" to your report with:**
- What problems you found
- How many rows were affected
- What you decided to do and why

---

## Phase 2.5 — Build Your Country Profiler Agent

> **Do this after Phase 2 is complete and `data/latam_finanzas_clean.csv` exists.**

**Step 1 — Create the agent file.**

In your project folder, create the directory `.claude/agents/` and save this content as `country-profiler.md` inside it:

```markdown
---
name: country-profiler
description: Generates a complete statistical profile for one Latin American country from the clean dataset
---

You are a data analyst assistant. When given a country name, read
`data/latam_finanzas_clean.csv` and produce a Markdown section with:

1. Sample size and age range for this country
2. Income: median, mean, min, max, standard deviation (USD)
3. Housing burden: average gasto_vivienda_usd as % of ingreso_mensual_usd
4. Spending breakdown: average % of income for each gasto_* column
5. Savings: average ahorro_mensual_usd and % of respondents with negative savings
6. AI tools: average horas_herramientas_ia_semana and average satisfaccion_financiera

Use the country name as the Markdown section header (## País: [name]).
Save the supporting Python script as scripts/country_[name].py.
```

**Step 2 — Invoke it for all 6 countries at once.**

```
I have a country-profiler agent defined in .claude/agents/country-profiler.md.
Please invoke it for all 6 countries in our dataset simultaneously:
México, Colombia, Argentina, Chile, Perú, Brasil.

Run all 6 profiles in parallel and collect the results into a single
Markdown file saved as scripts/country_profiles.md.
```

**After the profiles are generated, check:**
- Did all 6 country sections appear in `scripts/country_profiles.md`?
- Do the income numbers look plausible given what you saw in Phase 1?
- Which country has the highest housing burden? Does it match what you expected?

You will reference these profiles in Phase 3 — no need to recompute income by country or housing burden from scratch.

---

## Phase 3 — Analyse

> **Run this once you have the clean dataset and the country profiles from Phase 2.5.**

```
I now have a clean dataset at data/latam_finanzas_clean.csv and six country
profiles already generated in scripts/country_profiles.md.

Please run the following analyses and show the results as formatted tables.
For analyses 1 and 6, you may reference the country profiles already generated
rather than recomputing from scratch.

1. INCOME BY COUNTRY
   Reference the country profiles. Confirm and format the median income,
   mean income, min, max, and standard deviation for each country.
   Sort from highest to lowest median.

2. AGE VS. SAVINGS
   Create age groups: 18-22, 23-25, 26-28, 29-32.
   For each group: average monthly savings and average savings rate 
   (savings / income as a percentage).

3. SPENDING BREAKDOWN
   For the full sample, calculate the average percentage of income spent on:
   housing, food, transport, entertainment, education, and healthcare.
   Show as a table sorted from highest to lowest percentage.

4. CREDIT CARD HOLDERS VS NON-HOLDERS
   Compare the two groups on: average income, food spending, entertainment 
   spending, and savings. Calculate the percentage difference for each.

5. AI TOOL USAGE VS FINANCIAL SATISFACTION
   Create three groups: Low (0-3 hours/week), Medium (4-10), High (11+).
   For each group: count of respondents, average satisfaction score, 
   and average income. Also calculate the Pearson correlation between 
   horas_herramientas_ia_semana and satisfaccion_financiera.

6. HOUSING BURDEN BY COUNTRY
   Reference the country profiles. Confirm and format the average housing
   expense as % of income for each country, sorted from highest to lowest.

Save the script to scripts/03_analyse.py
```

**After reviewing the tables:** What surprises you? What confirms what you expected? Note at least 3 findings that you want to highlight in the report.

---

## Phase 4 — Visualise

> **Run this after Phase 3. Confirm your charts/ folder exists first.**

```
Using data/latam_finanzas_clean.csv, create the following 5 charts.
Save each as a PNG in the charts/ folder with the filenames shown.
Use a professional color palette (not the default matplotlib colors).
All charts must have: a clear title, labelled axes, and a source note 
"Source: Encuesta de Bienestar Financiero LatAm 2025, Futuro Digital LatAm".

1. charts/01_income_by_country.png
   Box plot showing the income distribution for each country.
   Sort countries by median income (highest on top for a horizontal box plot).

2. charts/02_age_vs_savings.png
   Scatter plot: age on x-axis, monthly savings on y-axis.
   Add a trend line (linear regression). Color points by country.

3. charts/03_spending_breakdown.png
   Horizontal bar chart showing the average % of income spent on each 
   expense category (housing, food, transport, entertainment, education, health).
   Sort from highest to lowest percentage.

4. charts/04_satisfaction_by_ai_usage.png
   Bar chart with three bars: Low / Medium / High AI tool users.
   Y-axis: average financial satisfaction score (1–5).
   Show the exact average value on top of each bar.

5. charts/05_housing_burden_by_country.png
   Horizontal bar chart: average housing cost as % of income, one bar per country.
   Sort from highest to lowest. Use a red-to-green color gradient 
   (high burden = red, low burden = green).

Save the script to scripts/04_visualise.py
```

**After generating the charts:** Open them and check — can you understand each chart in 5 seconds without reading the caption? If not, ask Claude Code to improve the labels, colors, or layout.

---

## Phase 5 — Interpret

> **Run this after reviewing all charts and tables from Phases 3 and 4.**

```
I have completed the statistical analysis and created the visualisations.
Now I need to translate the numbers into clear, actionable insights for 
a non-technical audience — specifically the leadership team of a nonprofit 
that designs financial literacy programmes.

For each of these 6 findings, write 3–4 sentences in plain language:
- What the data shows (the fact)
- Why it matters for a financial literacy programme (the implication)
- One specific programme recommendation based on this finding

Finding 1: Income differences across Latin American countries
Finding 2: The relationship between age and savings behaviour
Finding 3: Where the biggest expense categories are
Finding 4: How credit card holders differ from non-holders
Finding 5: The relationship between AI tool usage and financial satisfaction
Finding 6: Housing burden differences by country

Write these as they would appear in an executive report — professional,
concise, and evidence-based. Use specific numbers from the analysis.
```

**Review each paragraph:** Does it make a clear recommendation? Is it specific enough to act on? Would someone who has never seen the data understand it?

---

## Phase 6 — Report

> **Run this last, once all content is ready.**

```
I now have all the analysis, charts, and interpretations for the project.
Please write the complete executive report as a Markdown file.

Save it to analysis-report.md in the project root.

The report must include these sections exactly:

# Datos que Hablan: Bienestar Financiero de Jóvenes Profesionales en América Latina
## Informe Ejecutivo — Futuro Digital LatAm, 2025

### 1. Resumen Ejecutivo
A 200-word summary of the 3 most important findings and 2 key recommendations.
Written for a reader who will only read this section.

### 2. Metodología
- Dataset: Encuesta de Bienestar Financiero 2025
- Sample: 500 respondents, 6 countries, ages 18–32
- Data collection and processing approach
- Data quality issues found and how they were resolved (from Phase 2)

### 3. Perfil de la Muestra
Describe who the 500 respondents are: countries represented, age distribution,
industries, occupations. Use specific numbers. 

### 4. Hallazgos
One subsection per analysis from Phase 3.
Each subsection: the statistical finding + the plain-language interpretation
from Phase 5 + a reference to the relevant chart (e.g. "see Figure 1").

### 5. Recomendaciones
3–5 numbered recommendations for the financial literacy programme.
Each recommendation must cite at least one specific finding.

### 6. Conclusión
100 words. What does this data tell us about the state of financial wellness
among young Latin American professionals?

Use professional Markdown: headers, tables, bold for key numbers, 
chart references as image links where appropriate.
```

**Before submitting:** Read the report aloud. Does it tell a clear story? Are all 5 deliverable sections of the project present in the repo? Is the GitHub commit history clean?

---

## Tips for a Strong Analysis

**Ask follow-up questions.** The starter prompt is a door, not a destination.
- "That correlation looks low — is it statistically significant? Run a p-value test."
- "The box plot is hard to read. Can you try a violin plot instead?"
- "That insight feels vague. Can you rewrite it with the specific numbers from the table?"

**Delegate in parallel when it makes sense.** If you need country profiles for all 6 countries, you don't have to generate them one at a time.

**Monitor your session.** Data analysis fills context quickly — each script run adds output to the conversation. Check where you are periodically, and use `/compact` before heavy phases if needed.

**The data has surprises.** Some of the patterns in this dataset are not obvious until you look. The best teams will find more than the 6 required analyses. Bonus points go to teams that discover and present something unexpected.
