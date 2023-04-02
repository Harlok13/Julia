CREATE TABLE users (
    user_id BIGINT PRIMARY KEY,
    username VARCHAR(64) UNIQUE,
    user_nickname VARCHAR(64),
    admin BOOLEAN DEFAULT FALSE,
    register_date DATE DEFAULT CURRENT_DATE,
    update_date DATE DEFAULT CURRENT_DATE
);

-- TODO сделать декомпозицию таблицы
CREATE TABLE "books" (
    "book_id" SERIAL PRIMARY KEY,
    "title" VARCHAR(128) NOT NULL,
    "description" TEXT DEFAULT 'soon',
    "reviews" TEXT DEFAULT 'soon',
    "content" TEXT DEFAULT 'soon',
    "link" VARCHAR(128) NOT NULL,
    "cb_data" VARCHAR(32) NOT NULL
);

CREATE TABLE triggers_table (
    trigger_id SERIAL PRIMARY KEY,
    name_trigger TEXT,
    value_trigger TEXT,
    user_id BIGINT REFERENCES users(user_id)
);

COPY books FROM '/data/books.csv'
DELIMITER ',' CSV HEADER;