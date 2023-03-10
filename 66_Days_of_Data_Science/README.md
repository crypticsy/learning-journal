# Journey of 66 Days of Data Science

<br/>

#### Resources

<details>
    <summary> &nbsp; Coursera </summary> 

- [Applied Data Science Specialization](https://www.coursera.org/specializations/applied-data-science) by IBM

</details>
<details>
    <summary> &nbsp; Datacamp </summary> 

- [Data Analyst in SQL](https://app.datacamp.com/learn/career-tracks/data-analyst-in-sql) : Career track

</details>
<details>
    <summary> &nbsp; Kaggle Learn </summary> 

- [Intro to Programming](https://www.kaggle.com/learn/intro-to-programming)
- [Intro to SQL](https://www.kaggle.com/learn/intro-to-sql)
- [Advanced SQL](https://www.kaggle.com/learn/advanced-sql)
- [Pandas](https://www.kaggle.com/learn/pandas)
- [Intro to AI Ethics](https://www.kaggle.com/learn/intro-to-ai-ethics)

</details>
<details>
    <summary> &nbsp; LinkedIn learing </summary> 

- [Become a Data Scientist](https://www.linkedin.com/learning/paths/become-a-data-scientist)

</details>
<details>
    <summary> &nbsp; Youtube Playlist </summary> 

- [Discrete Probability Distributions](https://youtube.com/playlist?list=PLvxOuBpazmsNIHP5cz37oOPZx0JKyNszN)

</details>



<br/>
<hr/>
</br/>



#### Daily Logs



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 1 - Revision of Statistics and Basic SQL </summary>

    🗓️ Date: 2023-02-15

##### Resources : 

Course
- <a href="https://app.datacamp.com/learn/courses/introduction-to-statistics">Introduction to Statistics (Datacamp)</a>
- <a href="https://app.datacamp.com/learn/courses/introduction-to-sql">Introduction to SQL (Datacamp)</a>

<center>
    <hr style="border: 0; height: 3px; width: 70%; text-align: center;">
</center>

##### Summary:

<p align="justify">
    While taking the course <a href="https://app.datacamp.com/learn/courses/introduction-to-statistics" target="_blank">Introduction to Statistics</a> as part of the track <a href="https://app.datacamp.com/learn/career-tracks/data-analyst-in-sql" target="_blank">Data Analyst in SQL,</a> I had the chance to review probability, distributions, the central limit theorem, correlation, and hypothesis testing. While revising the dependence and conditional probabilities, I was also able to recall the normal and poisson distributions (k = * n). 
</p>

<p align="justify">
    I also took <a href="https://app.datacamp.com/learn/courses/introduction-to-sql" target="_blank">Introduction to SQL</a> as part of the same curriculum, which helped me revise the basic sql queries to read and view data from tables. Because of this revision, I learned about "VIEW," a concept I was never aware of before. To summarize, views are virtual tables whose contents are determined by queries. It only allows you to restrict access to the database and does not significantly increase the performance of SQL queries. Nonetheless, it was a useful trick to have in my SQL toolbox for increasing readability.
</p>

---

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 2 - Revision of Intermediate SQL Queries </summary>

    🗓️ Date: 2023-02-16

##### Resources : 

Course
- <a href="https://app.datacamp.com/learn/courses/intermediate-sql">Intermediate SQL (Datacamp)</a>

<center>
    <hr style="border: 0; height: 3px; width: 70%; text-align: center;">
</center>

##### Summary:

<p align="justify">
    Continuing on from Day 1, I chose the <a href="https://app.datacamp.com/learn/courses/intermediate-sql" target="_blank">Intermediate SQL</a> course from the same track, which included queries for selecting, filtering, aggregating, sorting, and grouping. Unlike the previous time, I did not get to learn a new concept, but it was a good recollection of all these principles, particularly concerning conventions for writing SQL to promote readability, as I had become a little sloopy regarding this.
</p>

----

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 3 - Revision of Joins, Set theory & Subqueries in SQL </summary>

    🗓️ Date: 2023-02-17

##### Resources : 

Course
- <a href="https://app.datacamp.com/learn/courses/joining-data-in-sql">Joining Data in SQL (Datacamp)</a>

<center>
    <hr style="border: 0; height: 3px; width: 70%; text-align: center;">
</center>

##### Summary:

<p align="justify">
    I took the course <a href="https://app.datacamp.com/learn/courses/joining-data-in-sql" target="_blank">Joining Data in SQL</a>, the fifth Course under the track <a href="https://app.datacamp.com/learn/career-tracks/data-analyst-in-sql" target="_blank">Data Analyst in SQL</a>. It included an introduction to various types of joins (inner, outer, cross & self) as well as set theory (union, intersect & except) joins. The cross joins and set theory section was incredibly beneficial as my perspective on desiging tables using minimal readable query was expanded due to these concepts.  While I recall reading about it in my undergrad curriculum, putting it into practice has helped me comprehend it much better. In addition, subqueries in the "WHERE", "FROM" and "SELECT" keywords were covered in the course. I had never used subqueries in the "SELECT" & "FROM" section before, hence I learned some cool tricks up my sleeves. I have added some syntaxes that I learned as follows:
</p>

<center>
    <hr style="border: 0; height: 3px; width: 70%; text-align: center;">
</center>

##### Notes:

<details>
  <summary> &nbsp; Cross Join Query</summary>

```
--- Creates all possible combinations
SELECT column_name(s)
FROM table1
CROSS JOIN table2;
```

</details>

<details>
  <summary> &nbsp; Operators</summary>

```
--- UNION Operator : shows unique rows
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;

--- UNION ALL Operator : shows duplicate rows
SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2;

--- EXCEPT Operator : shows rows not present in the table
SELECT column_name(s) FROM table1
EXCEPT
SELECT column_name(s) FROM table2;
```

</details>

<details>
  <summary> &nbsp; Subquery</summary>

```
--- Example 1: Sub query with in WHERE

SELECT name, country_code
FROM cities
WHERE name in (
    SELECT capital
    FROM countries
)


--- Example 2: Sub query with in SELECT

SELECT countries.name AS country_name, (
        SELECT COUNT(*)
        FROM cities
        WHERE cities.country_code = country.code
    ) AS cities_num
FROM countries


--- Example 3: Sub query with in FROM

SELECT coutries.name AS country_name, lang_num
FROM countries,
    (SELECT code, COUNT(*) AS lang_num
    FROM languages
    GROUP BY code) AS sub
WHERE countries.code = sub.code
ORDER BY lang_num DESC;
```

</details>

----

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 4 - Exploring Data Manipulation in SQL </summary>

    🗓️ Date: 2023-02-20

##### Resources : 

Course
- <a href="https://app.datacamp.com/learn/courses/data-manipulation-in-sql">Data Manipulation in SQL (Datacamp)</a>

<center>
    <hr style="border: 0; height: 3px; width: 70%; text-align: center;">
</center>

##### Summary:

<p align="justify">
    Machine learning, the most trending topic in today's generation is nothing more than a series of if and else statements. With SQL, a similar scenario occurs when you use the CASE statement to insert new values into a table based on existing records. To be more specific, the first module in <a href="https://app.datacamp.com/learn/courses/data-manipulation-in-sql" target="_blank">Data Manipulation in SQL</a> that I took,' 'We'll Take the CASE' module focused on using case statements to generate labels, probability, and percentage based on supplied criteria. While accounting for only one-quarter of the course, this subject proved useful in a variety of ways. The following are some examples of the statement:
</p>

<center>
    <hr style="border: 0; height: 3px; width: 70%; text-align: center;">
</center>

##### Notes:

<details>
  <summary> &nbsp; CASE Statement</summary>

```
--- Example 1 : Basic

SELECT title,
    length,
    CASE
        WHEN length> 0 AND length <= 50
            THEN 'Short'
        WHEN length > 50 AND length <= 120
            THEN 'Medium'
        WHEN length> 120
            THEN 'Long'
        ELSE
            'Outlier'
    END AS duration
FROM film
ORDER BY title;


--- Example 2 : Count

SELECT
    c.name AS country,
    -- Count games from the 2012/2013 season
    count(CASE WHEN m.season = '2012/2013'
            THEN m.id ELSE NULL end) AS matches_2012_2013
FROM country AS c
LEFT JOIN match AS m
ON c.id = m.country_id
-- Group by country name alias
GROUP BY country;


--- Example 3 : Percentage

SELECT
    c.name AS country,
    -- Round the percentage of tied games to 2 decimal points
    ROUND(AVG(CASE WHEN m.season='2013/2014' AND m.home_goal = m.away_goal THEN 1
            WHEN m.season='2013/2014' AND m.home_goal != m.away_goal THEN 0
            END),2) AS pct_ties_2013_2014,
    ROUND(AVG(CASE WHEN m.season='2014/2015' AND m.home_goal = m.away_goal THEN 1
            WHEN m.season='2014/2015' AND m.home_goal != m.away_goal THEN 0
            END),2) AS pct_ties_2014_2015
FROM country AS c
LEFT JOIN matches AS m
ON c.id = m.country_id
    GROUP BY country;
```

</details>

----

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 5 - (Continued) Data Manipulation in SQL</summary>

    🗓️ Date: 2023-02-21

##### Resources : 

Course
- <a href="https://app.datacamp.com/learn/courses/data-manipulation-in-sql">Data Manipulation in SQL (Datacamp)</a>

<center>
    <hr style="border: 0; height: 3px; width: 70%; text-align: center;">
</center>

##### Summary:

<p align="justify">
    Continuing the remaining modules <a href="https://app.datacamp.com/learn/courses/data-manipulation-in-sql" target="_blank">Data Manipulation in SQL</a> course, I was able to gain insights on Simple Subqueires Joins, Correlated Subqueries (takes higher processing time), Multiple/Nested Subqueries, and Common Table Expressions (CTE). These concepts were handful in allowing to perform complex actions within SQL and gain data points that I once thought were only possible through pandas (a python library).
</p>

<p align="justify">
    However, more significantly, I learned about window functions and the various types, such as Over, Rank, Partition, and Slide, throughout this course. While I had seen it before, I had never utilized it in practice, and I am pleased that this course allowed me to do so. Aggregating on columns that aren't in the grouping columns is likely the most useful skill to have, especially when doing comparative analysis.
</p>

<center>
    <hr style="border: 0; height: 3px; width: 70%; text-align: center;">
</center>

##### Notes:

<details>
  <summary> &nbsp; Correlated subquery with multiple conditions</summary>

```
SELECT
    -- Select country ID, date, home, and away goals from match
    main.country_id,
    main.date,
    main.home_goal,
    main.away_goal
FROM match AS main
WHERE
    -- Filter for matches with the highest number of goals scored
    (home_goal + away_goal) >
        (SELECT MAX(home_goal + sub.away_goal)
        FROM match AS sub
        WHERE main.country_id = sub.country_id
            AND main.season = sub.season);
```

</details>

<details>
  <summary> &nbsp; Common Table Expressions</summary>

````
WITH match_list AS (
    SELECT
        country_id,
        id
    FROM match
-- Select league and count of matches from the CTE
SELECT
    l.name AS league,
    COUNT(match_list.id) AS matches
FROM league AS l
-- Join the CTE to the league table
LEFT JOIN match_list ON l.id = match_list.country_id
GROUP BY l.name;
````

</details>

<details>
  <summary> &nbsp; Window Function</summary>

```
-- Example 1 : Over function

SELECT
    m.id,
    c.name AS country,
    m.season,
    m.home_goal,
    m.away_goal,
    -- Use a window to include the aggregate average in each row
    AVG(m.home_goal + m.away_goal) OVER() AS overall_avg
FROM match AS m
LEFT JOIN country AS c ON m.country_id = c.id;


-- Example 2 : Rank function

SELECT
    l.name AS league,
    AVG(m.home_goal + m.away_goal) AS avg_goals,
    -- Rank each league according to the average goals
    RANK() OVER(ORDER BY AVG(m.home_goal + m.away_goal) DESC) AS league_rank
FROM league AS l
LEFT JOIN match AS m
ON l.id = m.country_id
WHERE m.season = '2011/2012'
GROUP BY l.name
ORDER BY league_rank;


-- Example 3 : Partition function

SELECT
    c.name,
    m.season,
    (home_goal + away_goal) AS goals,
    AVG(home_goal + away_goal)
        OVER(PARTITION BY m.season, c.name) AS season_country_avg
FROM country AS c
LEFT JOIN match AS m
ON c.id = m.country_id;


-- Example 4 : Sliding Function

SELECT
    date,
    home_goal,
    away_goal,
    -- Create a running total and running average of home goals
    SUM(home_goal) OVER(ORDER BY date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total,
    AVG(home_goal) OVER(ORDER BY date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_avg
FROM match
WHERE
    hometeam_id = 9908
    AND season = '2011/2012';
```

</details>

----

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 6 - Understanding PostgreSQL Summary Stats </summary>

    🗓️ Date: 2023-02-22

##### Resources : 

Course
- <a href="https://www.kaggle.com/learn/advanced-sql">Advanced SQL (Kaggle)</a>
- <a href="https://app.datacamp.com/learn/courses/postgresql-summary-stats-and-window-functions">PostgreSQL Summary Stats and Window Functions  (Datacamp)</a>

Articles
- <a href="https://medium.com/yavar/window-functions-in-sql-a7239bb97104">Window functions in SQL (Medium)</a>

----

##### Summary:

<p align="justify">
With the continuation of window functions, I have gotten slightly familiar with the notion of window function types, particularly fetching, framing, and ranking functions, which I had practiced today. While these functions seemed intimidating at first, they turned out to be considerably easy than I had anticipated.
</p>

<p align="justify">
Beside this,  I attempted to put my knowledge into practice by answering practice questions in the "Advanced sql" section of kaggle. It was a valuable experience since I was able to accurately utilize window functions and also learn about the 'UNNEST' function to load nested and repeated data from the tables.
</p>

----

##### Notes:

<details>
  <summary> &nbsp; Fetching functions</summary>

| Operator | Description 
| --- | ----------- 
| `LAG(column, n)` | Returns column's value at the row  `n` rows before the current row
| `LEAD(column, n)` | Returns column's value at the row `n` rows after the current row
| `FIRST_VALUE(column)` | Returns the first value in table or partition
| `LAST_VALUE(column)` | Returns the last value in table or partition

</details>

<details>
  <summary> &nbsp; Framing functions</summary>

| Operator | Description 
| --- | ----------- 
| ROW/RANGE | Uses the given row or range as a frame.
| PRECEDING | Rows before the current row.
| UNBOUNDED PRECEDING | Return all rows before the current row.
| UNBOUNDED FOLLOWING | Return all rows after the current row.
| CURRENT ROW | Current row of query execution.

</details>

<details>
  <summary> &nbsp; Ranking Functions</summary>

| Operator | Description 
| --- | ----------- 
| ROW_NUMBER | Unique sequential number for each row in the specified partition
| RANK | Unique rank number for the each distinct row within the specified partition, but equal values share same rank
| DENSE_RANK | Unique rank number for the each distinct row within the specified partition without skipping any duplicate values
| NTILE | Distribute the rows in to the rows set with a specific `n` number of groups.

</details>

----

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 7 - Understanding Data Scientist Fundamentals</summary>

    🗓️ Date: 2023-02-23

##### Resources : 

Course
- <a href="https://www.linkedin.com/learning/a-day-in-the-life-of-a-data-scientist/serving-the-client/">A Day In The Life of a Data Scientist (Linkedin Learning)</a>
- <a href="https://www.linkedin.com/learning/the-non-technical-skills-of-effective-data-scientists/">The Non-Technical Skills of Effective Data Scientists (Linkedin Learning)</a>
- <a href="https://www.kaggle.com/learn/pandas">Pandas (Kaggle)</a>

----

##### Summary:

<p align="justify">
Taking a break from the regular SQL courses, I delved into the everyday life of a data scientist, complete with current data science issues and how data scientists manage themselves and the organizations for which they operate. I was also able to take the following course on the non-technical abilities of a successful data scientist, which addressed not just the attributes that a person should have but also the role diplomacy plays while working in a professional setting. In addition, to polish my pandas abilities, I completed a Kaggle Learn course that served as a refresher on the techniques I use on a daily basis.
</p>

----

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 8 - Exploring PostgreSQL Window Functions</summary>

    🗓️ Date: 2023-02-24

##### Resources : 

Course
- <a href="https://www.kaggle.com/learn/intro-to-programming">Intro to Programming (Kaggle)</a>
- <a href="https://app.datacamp.com/learn/courses/postgresql-summary-stats-and-window-functions">PostgreSQL Summary Stats and Window Functions  (Datacamp)</a>

----

##### Summary:

<p align="justify">
Leveraging the same elements in different ways has always lit up the neurons in my brain, allowing me to perceive the world in new ways. This occurred when learning how to use the aggregrate functions within the window functions to obtain new results. In fact, utilizing the same `SUM` and `AVG` functions to deliver moving totals and averages within sql itself with the assistance of frames and aggregrate functions made me leap on top of my bed.  There were so many things that sql could do that I had always assumed only pandas could accomplish. While creating sophisticated queries in pandas is faster, the execution time would be much faster if same queries were implemented directly in SQL without loading the dataset into memory.
</p>

<p align="justify">
Continuing this discovery, pivoting tables in SQL was also conceivable with `CROSSTAB`, as well as other beneficial functions like `ROLLUP`, `CUBE`, `COALESCE`, and `STRING AGG`, which would come in handy when relying only on SQL.
</p>

----

##### Notes:

<details>
  <summary> &nbsp; ROW BETWEEN</summary>

Syntax
`ROWS BETWEEN [start] AND [finish]`
- `n PRECEDING` : `n` rows before the current row
- `CURRENT ROW` : the current row
- `n FOLLOWING` : `n` rows after the current row

Examples
- `ROWS BETWEEN 3 PRECEDING AND CURRENT ROW`
- `ROWS BETWEEN 4 PRECEDING AND 4 FOLLOWING`
- `ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING`

</details>

<details>
  <summary> &nbsp; CROSSTAB</summary>

```
-- Before using crosstab, use the to create an extension
CREATE EXTENSION IF NOT EXISTS tablefunc;

SELECT * FROM CROSSTAB($$
    source_sql TEXT
$$) AS ct(
    column_1 DATA_TYPE_1,
    column_2 DATA_TYPE_2,
    ...,
    column_n DATA_TYPE_N
);
```

</details>

<details>
  <summary> &nbsp; ROLLUP and CUBE</summary>

The `ROLLUP` option allows to include extra rows that represent the subtotals, which are commonly referred to as super-aggregate rows, along with the grand total row. 
```
SELECT 
    country, warehouse, SUM(quantity)
FROM
    inventory
GROUP BY ROLLUP (country, warehouse);
```
`ROLLUP` is hierarchical, de-aggregrating from the leftmost provided column to the right-most. 
```
ROLLUP (country, warehouse)     -- includes country level totals
ROLLUP (warehouse, country)     -- includes warehouse level totals
```

However, when we need all possible group-level aggregrations, we use `CUBE` which shares similar properties to `ROLLUP`.
```
CUBE (country, warehouse)       -- country country level and warehouse level, and grand total
```

</details>

<details>
  <summary> &nbsp; Useful Functions</summary>

- COALESCE

`COALESCE()` takes a list of values and returns the first non-null value, going from left to right
```
COALESCE(null, null, 1, null, 2)        -- returns 1
```

- STRING_AGG

`STRING_AGG(column, separator)` takes all the values of a column and concatenates them, with `separator` in between each value.

</details>

---

</details>

<br/>



<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 9 - Exploring Functions for Data manipulation in SQL</summary>

    🗓️ Date: 2023-02-25

##### Resources : 

Course
- <a href="https://app.datacamp.com/learn/courses/functions-for-manipulating-data-in-postgresql">Functions for Manipulating Data in PostgreSQL (Datacamp)</a>

----

##### Summary:

<p align="justify">
The focus of today's course was on data manipulation in PostgreSQL utilizing both built-in and user-defined functions. The built-in functions of PostgreSQL included common data types and their casts, date/time functions and operators, and string parsing and manipulation functions. While the most of the operators were familiar, I learned about several new ones, such as `INTERVAL` and `INITCAP`. Nevertheless, the postgreSQL extensions and full-text search capabilities were entirely new subjects, particularly `tsvector` (text search vector) to execute a full text search beyond the scope of the 'LIKE' operator. Knowing that PostgreSQL offers built-in extensions such as fuzzy string matching through 'levenshtein' and'similarity' blew my mind as I had previously only used it in Python. Learning the syntax to develop my own functions was also quite instructive. Overall, it was a productive weekend spent learning more about PostgreSQL.
</p>

----

##### Notes:

<details>
  <summary> &nbsp; INFORMATION_SCHEMA</summary>

`INFORMATION_SCHEMA` provides access to database metadata, information about the MySQL server such as the name of a database or table, the data type of a column, or access privileges. 

```
-- Example 1 : Extracting all table names from system database
SELECT table_name, table_type
FROM INFORMATION_SCHEMA.TABLES
WHERE table_schema = 'public';

-- Example 2 : Extracting column data types from table
SELECT
    column_name,
    data_type
FROM INFORMATION_SCHEMA.COLUMNS
WHERE table_name = 'actor';
```

</details>

<details>
  <summary> &nbsp; INTERVAL </summary>

`INTERVAL` data type allows to store and manipulate a period of time in years, months, days, hours, minutes, seconds, etc. 

```
INTERVAL '3 days'                       -- goes forward in time
INTERVAL '2 months ago';                -- goes back in time due to the keyword 'ago'
INTERVAL '3 hours 20 minutes';

-- Example 1 : Addition of timeframe
SELECT rental_date + INTERVAL '2 days' as expected_return
FROM rental;

-- Example 2: Conversion of column to interval
SELECT INTERVAL '1' day * rental_duration
FROM rental
```

</details>

<details>
  <summary> &nbsp; DATETIME Operators </summary>

| Operator | Description 
| --- | ----------- 
| AGE() | Subtract with current_date (at midnight) when empty and with the other arguments when two values are provided
| NOW() | Get current timestamp with microsecond precision
| CURRENT_TIMESTAMP() | Gets similar timestamp to now but allows precision parameter to round off seconds
| CURRENT_DATE/CURRENT_TIME | Get current date and time
| EXTRACT(`field` from `source`) | Get subfield
| DATE_PART('`field`', `source`) | Get subfield (equivalent to extract)
| DATE_TRUNC('`field`', `source`) | Truncate timestamp or interval data types with precision
| ISFINITE() | Test for finite date, time and interval (not +/-infinity)

</details>

<details>
  <summary> &nbsp; STRING Operators </summary>

| Operator | Description 
| --- | ----------- 
| UPPER/LOWER(`source`) | Converts column to upper or lower case
| INITCAP(`source`) | Converts column to title case
| REPLACE(`source`, '`find_string`', '`replace_string`') | Replaces the source string with the replacement string
| REVERSE(`source`) | Reverses the string
| LENGTH(`source`) | Extract the length of the string
| POSITION('`char`' IN `source`) | Extract the first position of a character in a string
| LEFT(`source`, `n`) | Extract the `n` number of characters from left side of the given source
| RIGHT(`source`, `n`) | Extract the `n` number of characters from right side of the given source
| SUBSTRING(`source`, `start`, `length`) | Extract a string containing a specific number of characters from a particular position of a given string
| TIRM([leading|trailing|both] [characters] FROM `source`) | Removes characters from source
| LPAD(`source`, `n`, `char`) | Left-pads a string with another string, to a certain length
| RPAD(`source`, `n`, `char`) | Right-pads a string with another string, to a certain length

</details>

<details>
  <summary> &nbsp; FULL TEXT Search </summary>

- Basic Search
`to_tsvector(text)` : performs normalization and creates a list of tokens
`to_tsquery(string)` : accepts a list of words that will be checked against the normalized vector
`@@` : check if `tsquery` matches `tsvector`

```
-- Example 1 : Check if the title contains 'elf'
SELECT title, description
FROM film
WHERE to_tsvector(title) @@ to_tsquery('elf');
```

- Fuzzystring
```
-- Enable the fuzzystrmatch extension
CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;
-- Confirm that fuzzystrmatch has been enabled
SELECT extname FROM pg_extension;

SELECT levenshtein('hello', 'jelly');       -- number of edits required to be a perfect match
SELECT similarity('hello', 'jelly');        -- similarity between two strings from 0 to 1
```

</details>

<details>
  <summary> &nbsp; User Defined Data Types </summary>

Enumerated Data Types 
- Allows to create list of values that will not change 
```
CREATE TYPE dayofweek AS 
ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday');

-- Check
SELECT typname, typcategory
FROM pg_type
WHERE typname='dayofweek';
```

</details>

<details>
  <summary> &nbsp; User Defined Functions </summary>

```
CREATE FUNCTION squared(i integer) RETURNS integer AS $$ 
    BEGIN
        RETURN i * i;
    END;
$$ LANGUAGE plpgsql;
```

</details>

---

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 10 - Exploratory Data Analysis in SQL</summary>

    🗓️ Date: 2023-02-27

##### Resources : 

Course
- <a href="https://app.datacamp.com/learn/courses/exploratory-data-analysis-in-sql">Exploratory Data Analysis in SQL (Datacamp)</a>

----

##### Summary:

<p align="justify">
Breaking the usual heavy dosage of study sessions, this particular course covered about the usage of relationship diagrams, constraints (primary key, foreign key, unique and not null), and data types for the columns. The most significant functions from this course are 'corr' and 'percentile desc,' which allow you to get correlation and discrete value from a percentile. Moreover, temporary tables were a notion I had heard of but had never used in practice, and this course was a huge help in reinforcing the concept of breaking large queries into smaller chunks.
</p>

----

##### Notes:

<details>
  <summary> &nbsp; CAST Function</summary>

```
-- Cast Function syntax
SELECT CAST (value AS value_type);

-- Alternate Cast Function with :: notation  
SELECT value::new_type;

--  Example 1 : Casting float to integer
SELECT CAST (3.7 AS integer); 
```

</details>

<details>
  <summary> &nbsp; Series</summary>

```
-- Example 1 : Basic series
SELECT generate_series(1, 10, 2);

-- Example 2 : Float series
SELECT generate_series(0, 1, 0.1);
```

</details>

<details>
  <summary> &nbsp; Summary functions</summary>

| Function | Description 
| --- | ----------- 
| CORR(`source1`,`source2`) | Returns the correlation between two columns
| percentile_disc(`percentile`) WITHIN GROUP (ORDER BY `column_name`) | Returns the value representing the percentile of the column using discrete method

</details>

<details>
  <summary> &nbsp; Temporary Tables</summary>

```
-- Dropping the table
DROP TABLE IF EXISTS table_name

-- Create a temporary table
CREATE TEMP TABLE table_name AS
SELECT column1, column2
FROM table;
```

</details>

----

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 11 - (Continued) Exploratory Data Analysis in SQL</summary>

    🗓️ Date: 2023-02-28

##### Resources : 

Course
- <a href="https://app.datacamp.com/learn/courses/exploratory-data-analysis-in-sql">Exploratory Data Analysis in SQL (Datacamp)</a>

----

##### Summary:

<p align="justify">
The remaining modules of the course delved into the topic of character types in PostgreSQL, specifically character, varchar, and text. It also covered common challenges that arise when grouping categorical variables and dealing with unstructured text data. The modules included exercises on data cleaning such as dealing with cases and white spaces, as well as data manipulation techniques such as splitting strings using delimiters and concatenating multiple strings. Additionally, the course covered working with date and timestamps to create complex queries through series.
</p>

----

##### Notes:

<details>
  <summary> &nbsp; Series Generation</summary>

```
-- Syntax
SELECT generate_series(from, to, interval);

-- Example 1
SELECT generate_series('2018-01-01', '2018-01-15', '2 days'::interval)
```

</details>

----

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 12 - Data-Driven Decision Making using SQL</summary>

    🗓️ Date: 2023-03-01

##### Resources : 

Course
- <a href="https://app.datacamp.com/learn/courses/data-driven-decision-making-in-sql">Data-Driven Decision Making in SQL(Datacamp)</a>

Project
- <a href="https://app.datacamp.com/learn/projects/1413">When Was the Golden Age of Video Games?(Datacamp)</a>

----

##### Summary:

<p align="justify">
With all the skills that I had accumilated so far, it was only about implementing them. While a proper implementation is yet to come, I could still practice within a real evironment through the course "Data-Driven Decision Making in SQL" and the project "When Was the Golden Age of Video Games?". These allowed me to use all of the concepts from data cleaning, manipulation to aggregration and concentrated on using groupings, joins and pivots to create complex tables. Today marks the end of the career track, and I'm over the moon with all the knowledge I've gained in these 12 days. Yay for learning!
</p>

----

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 13 - Understanding Data Science & Analytics Career Paths</summary>

    🗓️ Date: 2023-03-02

##### Resources : 

Course
- <a href="https://www.linkedin.com/learning/data-science-analytics-career-paths-certifications-first-steps-2018/welcome">Data Science & Analytics Career Paths & Certifications: First Steps (LinkedIn Learning)</a>

----

##### Summary:

<p align="justify">
Before diving into the world of mathematica, I needed to grasp the foundations that I would need to build as a Data Analyst. Attending the LinkedIn Learning career course "Data Science & Analytics Career Pathways & Certifications" was quite beneficial in this regard. It began by discussing the applications of data science, such as fraud detection, social media analytics, disease control, dating services, simulations, climate research, and network security. It also discussed the abilities required to be relevant in the sector. Data mining, machine learning, natural language processing, statistics, and visualization were among the crucial skills mentioned. It also discussed certificates that can help advance one's career and establish one as a specialist in a particular subject. Overall, the course was beneficial in aiding comprehension of the principles of being relevant in the ever-changing world of data science.
</p>

----

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 14 - Exploring Data Visualization through Storytelling</summary>

    🗓️ Date: 2023-03-03

##### Resources : 

Course
- <a href="https://www.linkedin.com/learning/data-visualization-storytelling/the-art-of-storytelling">Data Visualization: Storytelling (LinkedIn Learning)</a>

----

##### Summary:
    
<p align="justify">
As visualizing data through narrative storytelling is one of the most crucial skills for a data analyst to have,  which sets them apart from their colleagues. I took a data visualization course that included story structure and its components (begining, middle, end, plot, protagonist, problem and transformation). It also demonstrated the use of flow diagrams to successfully represent linear data flow for effective story telling.

Most notably, the course taught the principles of learning to demonstrate your analytic abilities utilizing the 4x4 progressive depth model:

- The watercooler moment 
    - The initial attention grabber determines whether or not individuals are interested in learning more.
    - Example: Image or headline.

- The cafe content
    - Example : Blog post or short article

- The research library
    - Research portion, such as a PDF document.

- The Lab Experience
    - Interactive dashboard where data aficionados can examine the content and tinker to answer their in-depth questions

</p>

----

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 15 - Setup for IBM Watson and SpaceX Rest API</summary>

    🗓️ Date: 2023-03-05

##### Resources : 

Course
- <a href="https://www.coursera.org/learn/applied-data-science-capstone/">Applied Data Science Capstone: Week 1 (Coursera)</a>

----

##### Summary:
    
<p align="justify">
I took a break from learning today to prepare for the journey ahead! I made my own IBM account and configured Watson Studio to publish notebooks directly to my GitHub repository. I also explored in the world of SpaceX's rest API in order to extract useful data for future projects. We can get so enthused in learning new things that we forget to take a deep breath and get organized. However, not today.
</p>

----

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 16 - Analyzing SpaceX Data and AI ethics</summary>

    🗓️ Date: 2023-03-06

##### Resources : 

Course
- <a href="https://www.kaggle.com/learn/intro-to-ai-ethics">Intro to AI Ethics (Kaggle)</a>
- <a href="https://www.coursera.org/learn/applied-data-science-capstone/">Applied Data Science Capstone: Week 1 & 2 (Coursera)</a>

----

##### Summary:

<p align="justify">
Building on yesterday's exploration, today was all about extracting launch data from SpaceX using requests and beautiful soup. The objective was to determine the fruitfulness of starting a new business for a hypothetical company, SpaceY. During the course, I delved into the concepts of Exploratory Data Analysis and Feature Engineering, utilizing both python and SQL to analyze the data. Wrapping up with data science, I visually represented our findings using scatterplots and barplots to identify factors such as landing site, booster, and payload mass that can contribute to a higher success rate.
</p>

<p align="justify">
Aside from that, I took an AI ethics course and was introduced to Human-Centered-Design for AI and its significance. It not only helped me assess whether a project is worth transitioning to be done under AI, but it also helped me grasp that AI systems are more effective when they work alongside people rather than independently. Also, I learned about the numerous types of biases and fairness that can emerge in an ML model when biased data/model is used, as garbage in, garbage out.
</p>

----

##### Notes:

<details>
  <summary> &nbsp; Six Types of Bias</summary>

<br/>

- Historical Bias
    - Occurs when the state of the world in which the data was generated is flawed. 
- Representation bias
    - Occurs when building datasets for training a model, if those datasets poorly represent the people that the model will serve.
    - Example : if the dataset used to train the models exclude darker skin tones.
- Measurement bias 
    - Occurs when the accuracy of the data varies across groups. 
    - This can happen when working with proxy variables (variables that take the place of a variable that cannot be directly measured), if the quality of the proxy varies in different groups.
    - Example : if the measurement apparatus shows reduced performance with dark skin tones.
- Aggregation bias 
    - Occurs when groups are inappropriately combined, resulting in a model that does not perform well for any group or only performs well for the majority group. 
    - This is often not an issue, but most commonly arises in medical applications.
- Evaluation bias 
    - Occurs when evaluating a model.
    - If the benchmark data (used to compare the model to other models that perform similar tasks) does not represent the population that the model will serve.
    - Example : if the dataset used to benchmark the model excludes darker skin tones.
- Deployment bias 
    - Occurs when the problem the model is intended to solve is different from the way it is actually used. 
    - If the end users don’t use the model in the way it is intended, there is no guarantee that the model will perform well.

</details>

<img src="./images/bias.png" alt="types of bias">
<br/>

<details>
  <summary> &nbsp; Four fairness criteria</summary>

<br/>

- Demographic parity / statistical parity
    - It says the model is fair if the composition of people who are selected by the model matches the group membership percentages of the applicants.
- Equal opportunity fairness 
    - It ensures that the proportion of people who should be selected by the model ("positives") that are correctly selected by the model is the same for each group. 
    - We refer to this proportion as the true positive rate (TPR) or sensitivity of the model.
-  Equal accuracy
    - It is the percentage of correct classifications (people who should be denied and are denied, and people who should be approved who are approved) should be the same for each group. 
    - If the model is 98% accurate for individuals in one group, it should be 98% accurate for other groups.
- Group unaware / Fairness through unawareness
    - Group unaware fairness removes all group membership information from the dataset. 
    - For instance, we can remove gender data to try to make the model fair to different gender groups. 
    - Similarly, we can remove information about race or age.

</details>

----

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 17 - Interactive Dashboard, Predective Analysis & Reporting</summary>

    🗓️ Date: 2023-03-07

##### Resources : 

Course
- <a href="https://www.coursera.org/learn/applied-data-science-capstone/">Applied Data Science Capstone: Week 3, 4 & 5 (Coursera)</a>

----

##### Summary:

<p align="justify">
After completing exploratory data analysis, I delved into creating an interactive dashboard with plolty dash and folium to facilitate in real-time data analysis. It was a good refresher on the concept of dash callbacks to help translate user inputs and update existing charts based on those inputs. In addition, as part of the course, I touched on predictive analysis to determine the optimum model and hyperparameters needed to develop a model capable of predicting the launch's success rate. To do this, I used Preprocessing, GridSearchCV, LogisticRegression, DecisionTreeClassifier, and KNeighborsClassifier to help automate model selection, as well as a confusion matrix to evaluate true accuracy much more clearly.
</p>

<p align="justify">
With plenty of time left in the day, I investigated the creation of an effective data analysis report and its components. While data reports vary depending on the use and data included, I was able to get a general idea of how a data report should look through the course.
</p>

----

##### Notes:

<details>
  <summary> &nbsp; Elements of Data Finding Report</summary>

<br/>

- Cover Page
    - Contains: Title, Date and Name of the presenter
- Executive Summary
    - Briefly explain the details
    - Considered a stand-alone document
    - No new information should be presented except from the main points
- Table of Contents
- Introduction
    - Nature of the analysis
    - States the problem
    - States questions for analysis
- Methodology
    - Explains the data sources
    - Outlines the plan for the collected data
- Results
    - Deatils of data collection
    - How data was organized?
    - How data was analyzed?
    - Charts and graphs to show crucial finding
- Discussion
    - Engage the audience
- Conclusion
    - Conclusion of the report finding, reiterating the problem given in introduction
    - Overall summary of the findings
    - Outcome of the analysis
    - Any steps taken in future
- Appendix 
    - Information that didn't fit in the report
    - Resources and references

</details>

----

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 18 - Using Powerpoint to Communicate Finding from Space X Launch Data </summary>

    🗓️ Date: 2023-03-08

##### Resources : 

Course
- <a href="https://www.coursera.org/learn/applied-data-science-capstone/">Applied Data Science Capstone: Week 5 (Coursera)</a>

----

##### Summary:

<p align="justify">
After a thorough analysis of Space X's launches, it was time to predict the first stage's successful landing to give competition to the likes of Space X with the assistance of Company Y. Armed with a lengthy 50-page presentation, a combination of online resources and a dash of personal passion was instrumental in completing the task, and in the process, honed valuable presentation creation skills. In addition, the power of context cannot be overstated, as it aided in comprehending the insights more easily, with an executive summary for those uninterested in the subject matter. All in all, it was a remarkable learning experience that showcased the importance of a compelling narrative and a comprehensive overview for maximum impact.  
</p>

----

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📖 &nbsp; Day 19 - Understanding Data Governance </summary>

    🗓️ Date: 2023-03-09

##### Resources : 

Course
- <a href="https://www.linkedin.com/learning/learning-data-governance-14224082/data-governance-affects-everyone">Learning Data Governance (LinkedInLearning)</a>

----

##### Summary:

<p align="justify">
In the data governance course, I gained insights into the significance of efficient data management in organizations. The course taught me that data governance involves creating and enforcing policies, procedures, and standards to manage data assets of an organization, which includes data privacy, quality, security, and access. A crucial lesson that I learned was how data governance plays a critical role in ensuring the trustworthiness and correctness of an organization's data. It enables high-quality data that can be relied upon to drive decision-making processes. Moreover, data governance can also aid organizations in complying with regulatory obligations related to data privacy and security.
</p>

----

##### Notes:

<details>
  <summary> &nbsp; Principles of Data Governance</summary>

<br/>

- Transparency
    - All data governance processes implemented throughout your organisation should exhibit the utmost transparency.
- Accountability
    - Ownership and accountability has to be applied across the organisation for the data being collected and stored by the individuals.
- Standardization
    - Any successful data governance process will need to define and abide by standardised rules and regulations to protect their data and to ensure it is used in accordance with all relevant external regulations (such as the GDPR).

</details>

----

</details>