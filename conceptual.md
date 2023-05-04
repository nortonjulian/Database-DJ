### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
PostgreSQL is a relational database. It stores data in rows with the columns serving as different titles. The tables can have many related rows.

- What is the difference between SQL and PostgreSQL?
The difference is in the languages each supports. PostgreSQL supports: Python, PHP, Perl, Net, Java, Javascript. In contrast SQL
is more limited. It offers support for Java, Javascript, C#, PHP, Pyhton and Ruby.

- In `psql`, how do you connect to a database?
\c DB_NAME

- What is the difference between `HAVING` and `WHERE`?
"HAVING" decides which groups to keep whereas "WHERE" filters rows.

- What is the difference between an `INNER` and `OUTER` join?
"INNER" are the rows the match the condition in both tables and "OUTER" could be left or right but it's combining the entirety of one table to either the left or right of another.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

A "LEFT OUTER" returns all records from the left table matched with all records from the right table. A "RIGHT OUTER" returns all records from the right table matched with all records from the left table.

- What is an ORM? What do they do?
An "object relational mapper" is a technique used to create a bridge between object oriented programs and relational databases.

- What are some differences between making HTTP requests using AJAX
  and from the server side using a library like `requests`?
HTTP allows a user to post forms to the server. While AJAX is a way of using HTTP where parts of a website don't change.


- What is CSRF? What is the purpose of the CSRF token?
CSRF stands for "Cross-site request forgery". A CSRF is a random token used to prevent CSRF attacks. The token should be unique per person and random value making it difficult to guess.

- What is the purpose of `form.hidden_tag()`?
This is used to include data that needs to be submitted with the form but not be displayed to the user.
