CREATE TABLE Users (
    id INT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE Posts (
    id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE Comments (
    id INT PRIMARY KEY,
    content TEXT NOT NULL,
    post_id INT,
    user_id INT,
    FOREIGN KEY (post_id) REFERENCES Posts(id),
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE Tags (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Post_Tags (
    post_id INT,
    tag_id INT,
    PRIMARY KEY (post_id, tag_id),
    FOREIGN KEY (post_id) REFERENCES Posts(id),
    FOREIGN KEY (tag_id) REFERENCES Tags(id)
);

INSERT INTO Users (id, username, password) VALUES (1, 'admin', 'password123');
INSERT INTO Posts (id, title, content, user_id) VALUES (1, 'First Post', 'This is the first post', 1);
INSERT INTO Comments (id, content, post_id, user_id) VALUES (1, 'This is a comment', 1, 1);
INSERT INTO Tags (id, name) VALUES (1, 'tag1');
INSERT INTO Post_Tags (post_id, tag_id) VALUES (1, 1);

SELECT * FROM Users;
SELECT * FROM Posts;
SELECT * FROM Comments;
SELECT * FROM Tags;
SELECT * FROM Post_Tags;

CREATE VIEW UserPosts AS SELECT u.id, u.username, p.id, p.title FROM Users u JOIN Posts p ON u.id = p.user_id;
CREATE VIEW PostComments AS SELECT p.id, p.title, c.id, c.content FROM Posts p JOIN Comments c ON p.id = c.post_id;

SELECT * FROM UserPosts;
SELECT * FROM PostComments;

CREATE PROCEDURE GetUserPosts(@userId INT) AS BEGIN SELECT * FROM Posts WHERE user_id = @userId END;
CREATE PROCEDURE GetPostComments(@postId INT) AS BEGIN SELECT * FROM Comments WHERE post_id = @postId END;

EXEC GetUserPosts 1;
EXEC GetPostComments 1;