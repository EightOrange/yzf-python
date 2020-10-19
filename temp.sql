/*
 Navicat Premium Data Transfer

 Source Server         : mysql_JavaEE
 Source Server Type    : MySQL
 Source Server Version : 80021
 Source Host           : localhost:3306
 Source Schema         : for_python

 Target Server Type    : MySQL
 Target Server Version : 80021
 File Encoding         : 65001

 Date: 10/10/2020 20:31:48
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for temp
-- ----------------------------
DROP TABLE IF EXISTS `temp`;
CREATE TABLE `temp`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `temperature` float(255, 1) NULL DEFAULT NULL,
  `Humidity` float(255, 1) NULL DEFAULT NULL,
  `time` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of temp
-- ----------------------------
INSERT INTO `temp` VALUES (1, 27.0, 74.0, '2020-10-09 16:26:12');
INSERT INTO `temp` VALUES (4, 11.0, 12.0, '2020-10-09 17:22:25');
INSERT INTO `temp` VALUES (5, 233.0, 333.0, '2020-10-10 08:40:32');
INSERT INTO `temp` VALUES (9, 123.1, 321.2, '2020-10-10 10:46:20');
INSERT INTO `temp` VALUES (10, 123.1, 321.2, '2020-10-10 11:13:05');
INSERT INTO `temp` VALUES (11, NULL, 74.2, '2020-10-10 11:31:41');
INSERT INTO `temp` VALUES (12, NULL, 74.2, '2020-10-10 11:31:44');
INSERT INTO `temp` VALUES (13, 123.1, 74.2, '2020-10-10 11:34:37');
INSERT INTO `temp` VALUES (14, 123.1, 74.2, '2020-10-10 11:34:37');
INSERT INTO `temp` VALUES (15, 123.1, 74.2, '2020-10-10 11:34:37');

SET FOREIGN_KEY_CHECKS = 1;
