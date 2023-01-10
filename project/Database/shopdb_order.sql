-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: shopdb
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
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `OID` int NOT NULL AUTO_INCREMENT,
  `PID` int NOT NULL,
  `Manager_ID` int NOT NULL,
  `Member_ID` int NOT NULL,
  `Order_date` datetime NOT NULL,
  `Quantity` int NOT NULL,
  `Status` varchar(16) NOT NULL,
  `Payment_method` varchar(16) NOT NULL,
  `Delivery_method` varchar(16) NOT NULL,
  `Fee` int NOT NULL,
  `Other_request` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`OID`),
  KEY `PID` (`PID`),
  KEY `Manager_ID` (`Manager_ID`),
  KEY `Member_ID` (`Member_ID`),
  CONSTRAINT `order_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `product` (`PID`) ON DELETE CASCADE,
  CONSTRAINT `order_ibfk_2` FOREIGN KEY (`Manager_ID`) REFERENCES `manager` (`Manager_ID`) ON DELETE CASCADE,
  CONSTRAINT `order_ibfk_3` FOREIGN KEY (`Member_ID`) REFERENCES `member` (`Member_ID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (1,8,9,7,'2023-01-10 21:40:18',1,'剛剛成立','貨到付款','貨到付款',70,'mem1 black thin'),(2,11,9,7,'2023-01-10 21:40:18',2,'製作中','貨到付款','貨到付款',100,'mem1 white'),(3,9,9,7,'2023-01-10 21:40:18',2,'剛剛成立','貨到付款','貨到付款',180,'mem1 green fat'),(4,9,9,10,'2023-01-10 21:41:17',1,'剛剛成立','貨到付款','貨到付款',90,'mem2 black'),(5,9,9,11,'2023-01-10 21:42:35',6,'製作中','貨到付款','貨到付款',540,'mem3 blue thin'),(6,8,9,11,'2023-01-10 21:42:35',2,'已完成','貨到付款','貨到付款',140,'mem3 orange');
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-10 21:47:22
