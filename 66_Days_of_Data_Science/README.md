# Journey of 66 Days of Data Science

<br>
##### Resources
<br>

Career Track
- [Data Analyst in SQL](https://app.datacamp.com/learn/career-tracks/data-analyst-in-sql) from Datacamp

---


##### Daily Logs

<br/>
<details> 
	<br/>
    <summary> &nbsp; 📝 &nbsp; Day 1 - Revision of Statistics and Basic SQL </summary>

    🗓️ Date: 2023-02-15

<br/>

##### Resources : 

Course
- <a href="https://app.datacamp.com/learn/courses/introduction-to-statistics">Introduction to Statistics (Datacamp)</a>
- <a href="https://app.datacamp.com/learn/courses/introduction-to-sql">Introduction to SQL (Datacamp)</a>

----

##### Summary:

<p align="justify">
    While taking the course <a href="https://app.datacamp.com/learn/courses/introduction-to-statistics" target="_blank">Introduction to Statistics</a> as part of the track <a href="https://app.datacamp.com/learn/career-tracks/data-analyst-in-sql" target="_blank">Data Analyst in SQL,</a> I had the chance to review probability, distributions, the central limit theorem, correlation, and hypothesis testing. While revising the dependence and conditional probabilities, I was also able to recall the normal and poisson distributions (k = * n). 
</p>

<p align="justify">
    I also took <a href="https://app.datacamp.com/learn/courses/introduction-to-sql" target="_blank">Introduction to SQL</a> as part of the same curriculum, which helped me revise the basic sql queries to read and view data from tables. Because of this revision, I learned about "VIEW," a concept I was never aware of before. To summarize, views are virtual tables whose contents are determined by queries. It only allows you to restrict access to the database and does not significantly increase the performance of SQL queries. Nonetheless, it was a useful trick to have in my SQL toolbox for increasing readability.
</p>

</details>



<br/>
<details> 
	<br/>
    <summary> &nbsp; 📝 &nbsp; Day 2 - Revision of Intermediate SQL Queries </summary>

    🗓️ Date: 2023-02-16

<br/>

##### Resources : 

Course
- <a href="https://app.datacamp.com/learn/courses/intermediate-sql">Intermediate SQL (Datacamp)</a>

----

##### Summary:

<p align="justify">
    Continuing on from Day 1, I chose the <a href="https://app.datacamp.com/learn/courses/intermediate-sql" target="_blank">Intermediate SQL</a> course from the same track, which included queries for selecting, filtering, aggregating, sorting, and grouping. Unlike the previous time, I did not get to learn a new concept, but it was a good recollection of all these principles, particularly concerning conventions for writing SQL to promote readability, as I had become a little sloopy regarding this.
</p>

</details>

<br/>
<details> 
	<br/>
    <summary> &nbsp; 📝 &nbsp; Day 3 - Joins, Set theory & Subqueries in SQL </summary>

    🗓️ Date: 2023-02-17

<br/>

##### Resources : 

Course
- <a href="https://app.datacamp.com/learn/courses/joining-data-in-sql">Joining Data in SQL (Datacamp)</a>

----

##### Summary:

<p align="justify">
    I took the course <a href="https://app.datacamp.com/learn/courses/joining-data-in-sql" target="_blank">Joining Data in SQL</a>, the fifth Course under the track <a href="https://app.datacamp.com/learn/career-tracks/data-analyst-in-sql" target="_blank">Data Analyst in SQL</a>. It included an introduction to various types of joins (inner, outer, cross & self) as well as set theory (union, intersect & except) joins. The cross joins and set theory section was incredibly beneficial as my perspective on desiging tables using minimal readable query was expanded due to these concepts.  While I recall reading about it in my undergrad curriculum, putting it into practice has helped me comprehend it much better. In addition, subqueries in the "WHERE", "FROM" and "SELECT" keywords were covered in the course. I had never used subqueries in the "SELECT" & "FROM" section before, hence I learned some cool tricks up my sleeves. I have added some syntaxes that I learned as follows:
</p>

----

##### Notes:

Cross Join Query
```
--- Creates all possible combinations
SELECT column_name(s)
FROM table1
CROSS JOIN table2;
```

</br>

Operators
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

</br>

Subquery

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

<br/>
<details> 
	<br/>
    <summary> &nbsp; 📝 &nbsp; Day 4 - Data Manipulation in SQL </summary>

    🗓️ Date: 2023-02-20

<br/>

##### Resources : 

Course
- <a href="https://app.datacamp.com/learn/courses/data-manipulation-in-sql">Data Manipulation in SQL (Datacamp)</a>

----

##### Summary:

<p align="justify">
    Machine learning, the most trending topic in today's generation is nothing more than a series of if and else statements. With SQL, a similar scenario occurs when you use the CASE statement to insert new values into a table based on existing records. To be more specific, the first module in <a href="https://app.datacamp.com/learn/courses/data-manipulation-in-sql" target="_blank">Data Manipulation in SQL</a> that I took,' 'We'll Take the CASE' module focused on using case statements to generate labels, probability, and percentage based on supplied criteria. While accounting for only one-quarter of the course, this subject proved useful in a variety of ways. The following are some examples of the statement:
</p>

----

##### Notes:

CASE Statement
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

<br/>
<details> 
	<br/>
    <summary> &nbsp; 📝 &nbsp; Day 5 - Data Manipulation in SQL (Continued)</summary>

    🗓️ Date: 2023-02-21

<br/>

##### Resources : 

Course
- <a href="https://app.datacamp.com/learn/courses/data-manipulation-in-sql">Data Manipulation in SQL (Datacamp)</a>

----

##### Summary:

<p align="justify">
    Continuing the remaining modules <a href="https://app.datacamp.com/learn/courses/data-manipulation-in-sql" target="_blank">Data Manipulation in SQL</a> course, I was able to gain insights on Simple Subqueires Joins, Correlated Subqueries (takes higher processing time), Multiple/Nested Subqueries, and Common Table Expressions (CTE). These concepts were handful in allowing to perform complex actions within SQL and gain data points that I once thought were only possible through pandas (a python library).
</p>

<p align="justify">
    However, more significantly, I learned about window functions and the various types, such as Over, Rank, Partition, and Slide, throughout this course. While I had seen it before, I had never utilized it in practice, and I am pleased that this course allowed me to do so. Aggregating on columns that aren't in the grouping columns is likely the most useful skill to have, especially when doing comparative analysis.
</p>

----

##### Notes:

Correlated subquery with multiple conditions
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

<br>

Common Table Expressions
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

<br/>

Window Function
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

<br/>
<details> 
	<br/>
    <summary> &nbsp; 📝 &nbsp; Day 6 - PostgreSQL Summary Stats and Window Functions</summary>

    🗓️ Date: 2023-02-22

<br/>

##### Resources : 

Course
- <a href="https://app.datacamp.com/learn/courses/postgresql-summary-stats-and-window-functions">PostgreSQL Summary Stats and Window Functions  (Datacamp)</a>

Articles
- <a href="https://medium.com/yavar/window-functions-in-sql-a7239bb97104">Window functions in SQL (Medium)</a>

----

##### Summary:

<p align="justify">
    I learnt  something today
</p>

----

##### Notes:

Fetching functions
| Syntax | Description 
| --- | ----------- 
| `LAG(column, n)` | Returns column's value at the row  `n` rows before the current row
| `LEAD(column, n)` | Returns column's value at the row `n` rows after the current row
| `FIRST_VALUE(column)` | Returns the first value in table or partition
| `LAST_VALUE(column)` | Returns the last value in table or partition

</br>

Framing functions
| Syntax | Description 
| --- | ----------- 
| `ROW/RANGE` | Uses the given row or range as a frame.
| `PRECEDING` | Rows before the current row.
| `UNBOUNDED PRECEDING` | Return all rows before the current row.
| `UNBOUNDED FOLLOWING` | Return all rows after the current row.
| `CURRENT ROW` | Current row of query execution.

</details>
