CREATE TABLE IF NOT EXISTS paitent (
   id INTEGER PRIMARY KEY,
   first_name VARCHAR(200),
   middle_name VARCHAR(200),
   last_name VARCHAR(200),
   dob VARCHAR(10),
   gender VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS user (
   id INTEGER PRIMARY KEY,
   username VARCHAR(200),
   passwd VARCHAR(200),
   role_id INTEGER,
   FOREIGN KEY (role_id) 
      REFERENCES roles (id)
);

CREATE TABLE IF NOT EXISTS roles (
   id INTEGER PRIMARY KEY,
   roles VARCHAR(200)
);