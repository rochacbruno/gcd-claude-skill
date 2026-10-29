# GoogleSQL for Bigtable reference

Source: https://documentation.s3ns.fr/bigtable/docs/reference/sql/googlesql-reference-overview
Last updated: 2026-10-28

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/bigtable/docs/tpc-differences) for more details.














- 





[

Home

](https://documentation.s3ns.fr/)






- 








[

Documentation

](https://documentation.s3ns.fr/docs)






- 








[

Databases

](https://documentation.s3ns.fr/docs/databases)






- 








[

Bigtable

](https://documentation.s3ns.fr/bigtable/docs)






- 








[

Reference

](https://documentation.s3ns.fr/bigtable/docs/apis)

























# GoogleSQL for Bigtable reference



GoogleSQL for Bigtable is an ANSI compliant [Structured Query
Language (SQL)](https://en.wikipedia.org/wiki/SQL) that lets you run **query
statements** (also known as Data Query Language (DQL) statements) on
Bigtable tables. A query statement scans a table and returns
computed result rows. Query statements can include
[pipe syntax](/bigtable/docs/reference/sql/pipe-syntax).

GoogleSQL for Bigtable doesn't include support for some
common SQL constructs, including the following:

- Data Manipulation Language (DML) statements beyond `SELECT`, such as
`INSERT`, `UPDATE`, or `DELETE`

- Data Definition Language (DDL) expressions such as `CREATE`, `ALTER`, or
`DROP`

- Data Access Control statements

- Query syntax for subqueries, `JOIN`, `UNION`, and
`CTEs`

For information on where to run SQL queries on your Bigtable data,
as well examples of common Bigtable query patterns, see
[GoogleSQL for Bigtable
overview](/bigtable/docs/googlesql-overview).

## What's next

- [See all supported functions.](/bigtable/docs/reference/sql/functions-all)

- [See all supported operators.](/bigtable/docs/reference/sql/operators)

- [See all supported conditional expressions.](/bigtable/docs/reference/sql/conditional_expressions)

- [Learn about pipe syntax.](/bigtable/docs/reference/sql/pipe-syntax)

- [Review supported data types.](/bigtable/docs/reference/sql/data-types)