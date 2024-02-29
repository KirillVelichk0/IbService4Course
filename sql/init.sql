CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    login VARCHAR,
    password VARCHAR,
    w VARCHAR,
    t TIMESTAMP
);
 
CREATE TABLE RSA (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(id),
    p NUMERIC(500, 0),
    q NUMERIC(500, 0),
    n NUMERIC(500, 0),
    phi NUMERIC(500, 0),
    e NUMERIC(500, 0),
    d NUMERIC(500, 0)
);
