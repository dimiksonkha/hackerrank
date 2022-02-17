-- student table 
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  marks INTEGER NOT NULL
);
-- insert some values
INSERT INTO students  (id, name, marks) VALUES (1, 'Ryan', 81);
INSERT INTO students  (id, name, marks) VALUES (2, 'Joanna', 75);

-- query
SELECT name FROM students order by marks asc order by right(name, 3) order by id asc;
