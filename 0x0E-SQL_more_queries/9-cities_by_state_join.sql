-- Using join to display the info about two tables
-- Statement to do the join query
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC;
