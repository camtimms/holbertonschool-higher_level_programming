--
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.state_id
ORDER BY cities.id
