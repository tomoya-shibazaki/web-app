-- ---
-- Table 'users'
-- 
-- ---

DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

-- ---
-- Table 'courses'
-- 
-- ---

DROP TABLE IF EXISTS courses;
		
CREATE TABLE courses (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

-- ---
-- Table 'users_courses'
-- 
-- ---

DROP TABLE IF EXISTS users_courses;
		
CREATE TABLE users_courses (
  id INT NOT NULL AUTO_INCREMENT,
  user_id INT NOT NULL,
  FOREIGN KEY (user_id)
    REFERENCES users(id)
    ON DELETE CASCADE,
  course_id INT NOT NULL,
  FOREIGN KEY (course_id)
    REFERENCES courses(id)
    ON DELETE CASCADE,
  status ENUM('todo', 'wip', 'done') DEFAULT 'todo',
  PRIMARY KEY (id)
);