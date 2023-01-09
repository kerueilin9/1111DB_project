-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: shopdb
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `PID` int NOT NULL AUTO_INCREMENT,
  `Image` varchar(256) DEFAULT NULL,
  `Manager_ID` int NOT NULL,
  `Type` varchar(16) NOT NULL,
  `Describe` varchar(256) NOT NULL,
  `Quantity` int NOT NULL,
  `Price` int NOT NULL,
  `Discount` decimal(3,2) NOT NULL,
  `Discount_period` datetime DEFAULT NULL,
  `productName` varchar(64) NOT NULL,
  PRIMARY KEY (`PID`),
  KEY `Manager_ID` (`Manager_ID`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`Manager_ID`) REFERENCES `manager` (`Manager_ID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES 
(1,'./productImage/P_20220810_235241.jpg',1,'block','This is a square',5,1200,1.00,'0000-00-00 00:00:00','BLock'),
(2,'./productImage/test.jpg',1,'block','This is a square',5,1200,1.00,'2023-01-01 01:01:01','square'),
(4,'./productImage/circle.jpg',1,'block','This is a circle',10,500,0.50,'2023-01-01 01:01:01','circle'),
(5,'./productImage/triangle.jpg',1,'block','This is a triangle',10,200,0.80,'2023-01-01 01:01:02','triangle'),
(6,'./productImage/test.jpg',1,'block','This is a rectangle',10,200,0.80,'2023-01-01 01:01:02','rectangle');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-09 16:30:49
