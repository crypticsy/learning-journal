# Journey of 66 Days of Data Science

<br/>
<details> 
	<br/>
    <summary> &nbsp; 📝 &nbsp; Day 1 - Revision of Statistics and Basic SQL </summary>

    🗓️ Date: 2023-02-15

<blockquote>
    While taking the course "Introduction to Statistics" as part of the track "Data Analyst in SQL," I had the chance to review probability, distributions, the central limit theorem, correlation, and hypothesis testing. While revising the dependence and conditional probabilities, I was also able to recall the normal and poisson distributions (k = * n). 
</blockquote>

<blockquote>
    I also took "Introduction to SQL" as part of the same curriculum, which helped me revise the basic sql queries to read and view data from tables. Because of this revision, I learned about "VIEW," a concept I was never aware of before. To summarize, views are virtual tables whose contents are determined by queries. It only allows you to restrict access to the database and does not significantly increase the performance of SQL queries. Nonetheless, it was a useful trick to have in my SQL toolbox for increasing readability.
</blockquote>

</details>

<br/>
<details> 
	<br/>
    <summary> &nbsp; 📝 &nbsp; Day 2 - Revision of Intermediate SQL Queries </summary>

    🗓️ Date: 2023-02-16

<blockquote>
    Continuing on from Day 1, I chose the "Intermediate SQL" course from the same track, which included queries for selecting, filtering, aggregating, sorting, and grouping. Unlike the previous time, I did not get to learn a new concept, but it was a good recollection of all these principles, particularly concerning conventions for writing SQL to promote readability, as I had become a little sloopy regarding this.
</blockquote>

</details>

<br/>
<details> 
	<br/>
    <summary> &nbsp; 📝 &nbsp; Day 3 - Joins, Set theory & Subqueries in SQL </summary>

    🗓️ Date: 2023-02-17

<blockquote>
    I took the course "Joining Data in SQL", the fifth Course under the track Data Analyst in SQL. It included an introduction to various types of joins (inner, outer, cross & self) as well as set theory (union, intersect & except) joins. The cross joins and set theory section was incredibly beneficial as my perspective on desiging tables using minimal readable query was expanded due to these concepts.  While I recall reading about it in my undergrad curriculum, putting it into practice has helped me comprehend it much better. In addition, subqueries after the "WHERE", "FROM" and "SELECT" keywords were covered in the course. I had never used subqueries in the "SELECT" & "FROM" section before, hence I learned some cool tricks up my sleeves. I have added some syntaxes that I learned as follows:
</blockquote>

    --- Cross Join Query : creates all possible combinations
    SELECT column_name(s)
    FROM table1
    CROSS JOIN table2;


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


    --- SUBQUERY EXAMPLES
    
        --- Example 1:
        SELECT name, country_code
        FROM cities
        WHERE name in (
            SELECT capital
            FROM countries
        )

        --- Example 2:
        SELECT countries.name AS country_name, (
                SELECT COUNT(*)
                FROM cities
                WHERE cities.country_code = country.code 
            ) AS cities_num
        FROM countries

        --- Example 3:
        SELECT coutries.name AS country_name, lang_num
        FROM countries,
            (SELECT code, COUNT(*) AS lang_num
            FROM languages
            GROUP BY code) AS sub
        WHERE countries.code = sub.code
        ORDER BY lang_num DESC;

</details>


<br/>
<details> 
	<br/>
    <summary> &nbsp; 📝 &nbsp; Day 4 - Data Manipulation in SQL </summary>

    🗓️ Date: 2023-02-17

<blockquote>
    Machine learning, the most trending topic in today's generation is nothing more than a series of if and else statements. With SQL, a similar scenario occurs when you use the CASE statement to insert new values into a table based on existing records. To be more specific, the first module in 'Data Manipulation in SQL' that I took,' 'We'll Take the CASE,' focuses on using case statements to generate labels, probability, and percentage based on supplied criteria. While accounting for only one-quarter of the course, this subject proved useful in a variety of ways. The following are some examples of the statement:

</blockquote>

    --- CASE Statement Example
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


    --- CASE Statement : Count Example
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


    --- CASE Statement : Percentage Example
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
</details>
