show databases;
drop database if exists `DBProject`;
create database `DBProject`;
use `DBProject`;
show tables;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `UID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(32) NOT NULL,
  `E-mail` varchar(64) NOT NULL,
  `Account` varchar(16) NOT NULL,
  `Password` varchar(16) NOT NULL,
  `Role` varchar(16) NOT NULL,
  `Phone` varchar(16) NOT NULL,
  `Gender` varchar(16) NOT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
INSERT INTO `user` VALUES (1,'Tom','Tom0001@gmail.com','Tom0001','Tom0001','member','0900000000','F'),(2,'An','An0002@gmail.com','An0002','An0002','member','0900000001','M'),(3,'aaa','aaa@gmail.com','aaa','aaa','member','0900000002','M'),(4,'bbb','bbb@gmail.com','b','b','member','0900000003','M'),(5,'ccc','c@gmail.com','c','c','member','0900000004','F');
UNLOCK TABLES;

--
-- Table structure for table `communicate`
--

DROP TABLE IF EXISTS `communicate`;
CREATE TABLE `communicate` (
  `Sender` int NOT NULL,
  `Receiver` int NOT NULL,
  `Message` varchar(100) DEFAULT NULL,
  `Time` datetime DEFAULT NULL,
  KEY `Sender` (`Sender`),
  KEY `Receiver` (`Receiver`),
  CONSTRAINT `communicate_ibfk_1` FOREIGN KEY (`Sender`) REFERENCES `user` (`UID`) ON DELETE CASCADE,
  CONSTRAINT `communicate_ibfk_2` FOREIGN KEY (`Receiver`) REFERENCES `user` (`UID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `communicate`
--

LOCK TABLES `communicate` WRITE;
UNLOCK TABLES;

--
-- Table structure for table `manager`
--

DROP TABLE IF EXISTS `manager`;
CREATE TABLE `manager` (
  `Manager_ID` int NOT NULL,
  PRIMARY KEY (`Manager_ID`),
  CONSTRAINT `manager_ibfk_1` FOREIGN KEY (`Manager_ID`) REFERENCES `user` (`UID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `manager`
--

LOCK TABLES `manager` WRITE;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
CREATE TABLE `member` (
  `Member_ID` int NOT NULL,
  `Address` varchar(256) NOT NULL,
  PRIMARY KEY (`Member_ID`),
  CONSTRAINT `member_ibfk_1` FOREIGN KEY (`Member_ID`) REFERENCES `user` (`UID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
CREATE TABLE `department` (
  `Name` varchar(16) NOT NULL,
  `Manager_ID` int NOT NULL,
  PRIMARY KEY (`Name`),
  KEY `Manager_ID` (`Manager_ID`),
  CONSTRAINT `department_ibfk_1` FOREIGN KEY (`Manager_ID`) REFERENCES `manager` (`Manager_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee` (
  `Employee_ID` int NOT NULL,
  `Department` varchar(16) NOT NULL,
  PRIMARY KEY (`Employee_ID`),
  KEY `Department` (`Department`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `user` (`UID`) ON DELETE CASCADE,
  CONSTRAINT `employee_ibfk_2` FOREIGN KEY (`Department`) REFERENCES `department` (`Name`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `PID` int NOT NULL AUTO_INCREMENT,
  `Image` blob,
  `Manager_ID` int NOT NULL,
  `Type` varchar(16) NOT NULL,
  `Describe` varchar(256) NOT NULL,
  `Quantity` int NOT NULL,
  `Price` int NOT NULL,
  `Discount` decimal(3,2) NOT NULL,
  `Discount_period` datetime DEFAULT NULL,
  PRIMARY KEY (`PID`),
  KEY `Manager_ID` (`Manager_ID`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`Manager_ID`) REFERENCES `manager` (`Manager_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
UNLOCK TABLES;

--
-- Table structure for table `works_on`
--

DROP TABLE IF EXISTS `works_on`;
CREATE TABLE `works_on` (
  `Employee_ID` int NOT NULL,
  `OID` int NOT NULL,
  PRIMARY KEY (`Employee_ID`),
  KEY `OID` (`OID`),
  CONSTRAINT `works_on_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `employee` (`Employee_ID`) ON DELETE CASCADE,
  CONSTRAINT `works_on_ibfk_2` FOREIGN KEY (`OID`) REFERENCES `order` (`OID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `works_on`
--

LOCK TABLES `works_on` WRITE;
UNLOCK TABLES;

select * from `user`; 
select * from `communicate`;
select * from `manager`;
select * from `member`;
select * from `department`;
select * from `employee`;
select * from `works_on`;
select * from `product`;
select * from `order`;