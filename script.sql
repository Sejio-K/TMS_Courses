create database sheltor

CREATE TABLE animal (
    id INT,
    animal_name VARCHAR(50),
    animal_type VARCHAR(50),
    age INT,
    male ENUM('male', 'female'),
    weight DECIMAL(8,2),
    PRIMARY KEY (id)
);

INSERT INTO animal (id, animal_name, animal_type, age, male, weight)
VALUES
  (1, 'Мурзик', 'кот', 3, 'male', 4.5),
  (2, 'Барсик', 'кот', 2, 'male', 5.2),
  (3, 'Люси', 'собака', 4, 'female', 8.7),
  (4, 'Шарик', 'собака', 2, 'male', 10.5),
  (5, 'Том', 'кот', 2, 'male', 3.8),
  (6, 'Луна', 'собака', 5, 'female', 12.1),
  (7, 'Макс', 'кот', 4, 'male', 4.2);

SELECT COUNT(*) AS total_animals FROM animal;

SELECT COUNT(*) AS total_dogs FROM animal WHERE animal_type = 'собака';

SELECT AVG(weight) AS average_weight FROM animal WHERE animal_type = 'собака';

SELECT DISTINCT animal_type FROM animal;

SELECT COUNT(*) AS total_willies FROM animal WHERE animal_name = 'Вилли';

SELECT male, COUNT(*) AS total FROM animal WHERE animal_type = 'собака' GROUP BY male;

SELECT DISTINCT animal_name FROM animal WHERE animal_type = 'кот' ORDER BY animal_name;

SELECT * FROM animal WHERE animal_name LIKE '%ик';

UPDATE animal SET animal_name = 'Монти' WHERE animal_name = 'Барсик';

