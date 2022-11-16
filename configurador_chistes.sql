/*
 Navicat Premium Data Transfer

 Source Server         : DB_LOCAL
 Source Server Type    : MySQL
 Source Server Version : 100420
 Source Host           : localhost:3306
 Source Schema         : configurador_chistes

 Target Server Type    : MySQL
 Target Server Version : 100420
 File Encoding         : 65001

 Date: 15/11/2022 18:12:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for chistes
-- ----------------------------
DROP TABLE IF EXISTS `chistes`;
CREATE TABLE `chistes`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `fecha_creacion` datetime(0) NULL DEFAULT NULL,
  `fecha_modificacion` datetime(0) NULL DEFAULT NULL,
  `vigente` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of chistes
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
