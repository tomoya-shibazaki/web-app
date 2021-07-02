-- ---
-- Insert Table 'users'
-- 
-- ---
INSERT INTO users (name, email) VALUES ("admin", "admin@gmail.com");
INSERT INTO users (name, email) VALUES ("student", "student@gmail.com");

-- ---
-- Insert Table 'courses'
-- 
-- ---

INSERT INTO courses (name) VALUES ("programming");


-- ---
-- Insert Table 'courses'
-- 
-- ---
INSERT INTO users_courses (user_id, course_id, status) VALUES (1, 1, "done");