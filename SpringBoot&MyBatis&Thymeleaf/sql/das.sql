# 数据库脚本文件
SET NAMES utf8mb4;
-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
                          `id` int(11) NOT NULL AUTO_INCREMENT,
                          `name` varchar(255) NOT NULL,
                          `email` varchar(255) DEFAULT NULL,
                          PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
# 插入数据
INSERT INTO `user`(name, email) VALUES ('张三', 'zhangsan@deer.com');
INSERT INTO `user`(name, email) VALUES ( '李四', 'lisi@deer.com');
INSERT INTO `user` (name, email) VALUES ('王五', 'wangwu@deer.com');