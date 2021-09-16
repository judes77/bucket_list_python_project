DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    continent VARCHAR(255),
    language VARCHAR(255)
);

CREATE TABLE cities (
   id SERIAL PRIMARY KEY,
   name VARCHAR(255), 
   visited BOOLEAN,
   country_id INT REFERENCES countries(id)
);

INSERT INTO countries (name, continent, language) VALUES ('Spain', 'Europe', 'Spanish');
INSERT INTO countries (name, continent, language) VALUES ('France', 'Europe', 'French');
INSERT INTO countries (name, continent, language) VALUES ('Australia', 'Australia', 'English');
INSERT INTO countries (name, continent, language) VALUES ('Czech Republic', 'Europe', 'Czech');
INSERT INTO countries (name, continent, language) VALUES ('New Zealand', 'Oceania', 'English');
INSERT INTO countries (name, continent, language) VALUES ('Poland', 'Europe', 'Polish');
INSERT INTO countries (name, continent, language) VALUES ('Belguim', 'Europe', 'Dutch and French');
INSERT INTO countries (name, continent, language) VALUES ('Scotland', 'Europe', 'English');
INSERT INTO countries (name, continent, language) VALUES ('England', 'Europe', 'English');
INSERT INTO countries (name, continent, language) VALUES ('Usa', 'Europe', 'Americas');
INSERT INTO countries (name, continent, language) VALUES ('Finland', 'Europe', 'Finnish');
INSERT INTO countries (name, continent, language) VALUES ('Denmark', 'Europe', 'Danish');
INSERT INTO countries (name, continent, language) VALUES ('Portugal', 'Europe', 'Portuguese');




INSERT INTO cities (name, visited, country_id) VALUES ('Barcelona', 'True', 1);
INSERT INTO cities (name, visited, country_id) VALUES ('Edinburgh', 'True', 8);
INSERT INTO cities (name, visited, country_id) VALUES ('London', 'True', 9);
INSERT INTO cities (name, visited, country_id) VALUES ('Paris', 'True', 2);
INSERT INTO cities (name, visited, country_id) VALUES ('Brussels', 'True', 7);
INSERT INTO cities (name, visited, country_id) VALUES ('New York', 'True', 10);
INSERT INTO cities (name, visited, country_id) VALUES ('Chicago', 'True', 10);
INSERT INTO cities (name, visited, country_id) VALUES ('Washington', 'True', 10);
INSERT INTO cities (name, visited, country_id) VALUES ('Prague', 'True', 4);
INSERT INTO cities (name, visited, country_id) VALUES ('Javier', 'True', 1);
INSERT INTO cities (name, visited, country_id) VALUES ('Copenhagen', 'True', 12);
INSERT INTO cities (name, visited, country_id) VALUES ('Helsinki', 'True', 11);
INSERT INTO cities (name, visited, country_id) VALUES ('Warsaw', 'True', 6);
INSERT INTO cities (name, visited, country_id) VALUES ('Boston', 'True', 10);
INSERT INTO cities (name, visited, country_id) VALUES ('Nairn', 'True', 8);
INSERT INTO cities (name, visited, country_id) VALUES ('Newcastle', 'True', 9);
INSERT INTO cities (name, visited, country_id) VALUES ('Lagos', 'True', 13);
INSERT INTO cities (name, visited, country_id) VALUES ('Lisbon', 'True', 13);

SELECT * FROM countries


