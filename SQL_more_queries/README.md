# SQL - More queries
## Amateur
**By:** Guillaume  
**Weight:** 1  
**Migrated to checker v2:** Your score will be updated as you progress.  
**Manual QA review must be done (request it when you are done with the project)**
****![image](https://github.com/ghinzuka/holbertonschool-higher_level_programming/assets/102736316/ed2ad640-6504-4bbf-bbdc-d9f4f11ffa63)

## Resources
Read or watch:
- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-grant.aspx)
- [MySQL constraints](https://dev.mysql.com/doc/refman/8.0/en/sql-syntax.html)
- [SQL technique: subqueries](https://www.w3resource.com/sql/subqueries/understanding-sql-subqueries.php)
- [Basic query operation: the join](https://www.w3schools.com/sql/sql_join.asp)
- [SQL technique: multiple joins and the distinct keyword](https://www.sqlshack.com/multiple-joins-work-sql/)
- [SQL technique: join types](https://www.datacamp.com/community/tutorials/sql-joins-tutorial)
- [SQL technique: union and minus](https://www.w3resource.com/sql/union-minus-intersect/union-minus-intersect.php)
- [MySQL Cheat Sheet](https://www.mysqltutorial.org/mysql-cheat-sheet.aspx)
- [The Seven Types of SQL Joins](https://www.essentialsql.com/what-are-the-seven-types-of-sql-joins/)
- [MySQL Tutorial](https://www.mysqltutorial.org/)
- [SQL Style Guide](https://www.sqlstyle.guide/)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-syntax.html)

Extra resources around relational database model design:
- [Design](https://www.oreilly.com/library/view/sql-and-relational/9781492051761/)
- [Normalization](https://www.studytonight.com/dbms/database-normalization.php)
- [ER Modeling](https://www.lucidchart.com/pages/er-diagrams)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a PRIMARY KEY
- What’s a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve data from multiple tables in one request
- What are subqueries
- What are JOIN and UNION

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## More Info
### Comments for your SQL file:
```sql
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
### Install MySQL 8.0 on Ubuntu 20.04 LTS
NOTE: If you’re using the provided sandbox you don’t need to install MySQL. Skip to the next section.

```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```
### Connect to your MySQL server:
```bash
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> quit
Bye
$
```
### Use the sandbox to run MySQL
In the container, credentials are root/root

Ask for container Ubuntu 20.04
Connect via SSH
OR connect via the Web terminal
In the container, you should start MySQL before playing with it:

```bash
$ service mysql start                                                   
* Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```
### How to import a SQL dump
```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
![image](https://github.com/ghinzuka/holbertonschool-higher_level_programming/assets/102736316/aead81d2-ef0e-45df-945d-6c0748fb6b0f)

| Task Number | Task Title                  | Description                                                                                                                                                                                                           |
|-------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0           | My privileges!              | Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in localhost).                                                                                                |
| 1           | Root user                   | Write a script that creates the MySQL server user `user_0d_1`. This user should have all privileges on your MySQL server, and the password should be set to `user_0d_1_pwd`.                                        |
| 2           | Read user                   | Write a script that creates the database `db_0d_2` and a user `user_0d_2`. This user should have only SELECT privileges on this database. The password should be set to `user_0d_2_pwd`.                            |
| 3           | Always a name               | Write a script that creates the table `name_0d_3` on database `db_0d_2`.                                                                                                                                            |
| 4           | ID can't be null            | Write a script that creates the table `id_not_null` on database `db_0d_2`. This table should have an `id` column that cannot be null.                                                                                |
| 5           | Unique ID                   | Write a script that creates the table `unique_id` on database `db_0d_2`. This table should have an `id` column that is unique.                                                                                       |
| 6           | Add data                    | Write a script that inserts some data into the table `name_0d_3`.                                                                                                                                                    |
| 7           | Count number of records     | Write a script that counts the number of records in the table `name_0d_3`.                                                                                                                                           |
| 8           | Sum                         | Write a script that calculates the sum of a column in the table `name_0d_3`.                                                                                                                                         |
| 9           | Join                        | Write a script that performs a join operation between the tables `name_0d_3` and `another_table`.                                                                                                                   |
| 10          | List users                  | Write a script that lists all MySQL users.                                                                                                                                                                           |
| 11          | Secure user creation        | Write a script that creates a user in a secure way, ensuring no SQL injection vulnerabilities are present.                                                                                                           |
| 12          | Backup                      | Write a script that backs up the database `db_0d_2`.                                                                                                                                                                 |
| 13          | Restore                     | Write a script that restores the database `db_0d_2` from a backup.                                                                                                                                                   |
| 14          | Script execution            | Write a script that runs an SQL script passed as an argument to the script.                                                                                                                                          |
| 15          | Setup replication           | Write a script that sets up MySQL replication between a master and a slave server.    