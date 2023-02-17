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
    <summary> &nbsp; 📝 &nbsp; Day 3 - Joining Data in SQL with Set theory </summary>

    🗓️ Date: 2023-02-17

<blockquote>
    I took the course "Joining Data in SQL", the fifth Course under the track Data Analyst in SQL. It included an introduction to various types of joins (inner, outer, cross & self) as well as set theory (union, intersect & except) joins. The cross joins and set theory section was incredibly beneficial as my perspective on desiging tables using minimal readable query was expanded due to these concepts.  While I recall reading about it in my undergrad curriculum, putting it into practice has helped me comprehend it much better. In addition, subqueries within the "WHERE" and "SELECT" keywords were covered in the course. I had never used subqueries in the choose section before and learned some cool tricks up my sleeve. I have added some syntaxes that i learned as follows:
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
