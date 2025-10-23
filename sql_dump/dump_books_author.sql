-- Datenbank anlegen (optional)
-- CREATE DATABASE IF NOT EXISTS library;
-- USE library;

-- Tabelle "authors" (1-Seite der Beziehung)
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100),
    birth_year INT
);

-- Tabelle "books" (N-Seite der Beziehung)
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    publication_year INT,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Autoren einfügen
INSERT INTO authors (name, country, birth_year) VALUES
('George Orwell', 'UK', 1903),
('Jane Austen', 'UK', 1775),
('Mark Twain', 'USA', 1835),
('Haruki Murakami', 'Japan', 1949),
('Isabel Allende', 'Chile', 1942),
('Franz Kafka', 'Austria-Hungary', 1883),
('Toni Morrison', 'USA', 1931),
('Gabriel García Márquez', 'Colombia', 1927),
('J.K. Rowling', 'UK', 1965),
('Stephen King', 'USA', 1947);

-- Bücher einfügen (50 Stück)
INSERT INTO books (title, publication_year, author_id) VALUES
('1984', 1949, 1),
('Animal Farm', 1945, 1),
('Pride and Prejudice', 1813, 2),
('Emma', 1815, 2),
('Sense and Sensibility', 1811, 2),
('Adventures of Huckleberry Finn', 1884, 3),
('The Adventures of Tom Sawyer', 1876, 3),
('Norwegian Wood', 1987, 4),
('Kafka on the Shore', 2002, 4),
('1Q84', 2009, 4),
('The Wind-Up Bird Chronicle', 1994, 4),
('The House of the Spirits', 1982, 5),
('Portrait in Sepia', 2000, 5),
('Zorro', 2005, 5),
('The Trial', 1925, 6),
('The Castle', 1926, 6),
('Metamorphosis', 1915, 6),
('Beloved', 1987, 7),
('Song of Solomon', 1977, 7),
('Sula', 1973, 7),
('One Hundred Years of Solitude', 1967, 8),
('Love in the Time of Cholera', 1985, 8),
('Chronicle of a Death Foretold', 1981, 8),
('Leaf Storm', 1955, 8),
('Harry Potter and the Philosopher\'s Stone', 1997, 9),
('Harry Potter and the Chamber of Secrets', 1998, 9),
('Harry Potter and the Prisoner of Azkaban', 1999, 9),
('Harry Potter and the Goblet of Fire', 2000, 9),
('Harry Potter and the Order of the Phoenix', 2003, 9),
('Harry Potter and the Half-Blood Prince', 2005, 9),
('Harry Potter and the Deathly Hallows', 2007, 9),
('Carrie', 1974, 10),
('The Shining', 1977, 10),
('It', 1986, 10),
('Misery', 1987, 10),
('The Stand', 1978, 10),
('Doctor Sleep', 2013, 10),
('The Institute', 2019, 10),
('Lisey\'s Story', 2006, 10),
('Duma Key', 2008, 10),
('Revival', 2014, 10),
('Under the Dome', 2009, 10),
('The Outsider', 2018, 10),
('Fairy Tale', 2022, 10),
('Billy Summers', 2021, 10),
('Later', 2021, 10),
('If It Bleeds', 2020, 10),
('The Colorado Kid', 2005, 10),
('Elevation', 2018, 10),
('Blaze', 2007, 10);
