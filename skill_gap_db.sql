-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: skill_gap
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `idemployees` int NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `age` varchar(45) NOT NULL,
  `department` varchar(45) NOT NULL,
  `skills_idskills` int NOT NULL,
  PRIMARY KEY (`idemployees`,`skills_idskills`),
  KEY `fk_employees_skills_idx` (`skills_idskills`),
  CONSTRAINT `fk_employees_skills` FOREIGN KEY (`skills_idskills`) REFERENCES `skills` (`idskills`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'Doe','John','25','Sales',1),(2,'Smith','Jane','30','Marketing',10),(3,'Johnson','Alice','28','HR',5),(4,'Brown','Bob','35','IT',3),(5,'Davis','Charlie','40','Finance',7),(6,'Wilson','David','32','Sales',2),(7,'Moore','Emma','29','Marketing',10),(8,'Taylor','Frank','31','HR',5),(9,'Anderson','Grace','26','IT',4),(10,'Thomas','Henry','37','Finance',7),(11,'Jackson','Ivy','27','Sales',2),(12,'White','Jack','33','Marketing',9),(13,'Harris','Karen','36','HR',6),(14,'Martin','Liam','24','IT',3),(15,'Thompson','Mia','38','Finance',8),(16,'Garcia','Noah','29','Sales',1),(17,'Martinez','Olivia','34','Marketing',9),(18,'Robinson','Paul','35','HR',6),(19,'Clark','Quinn','28','IT',3),(20,'Rodriguez','Rachel','31','Finance',7),(21,'Lewis','Steve','30','Sales',1),(22,'Lee','Tina','27','Marketing',9),(23,'Walker','Uma','33','HR',6),(24,'Hall','Victor','32','IT',4),(25,'Allen','Wendy','26','Finance',7),(26,'Young','Xander','28','Sales',1),(27,'Hernandez','Yara','31','Marketing',9),(28,'King','Zane','34','HR',5),(29,'Wright','Amy','36','IT',4),(30,'Lopez','Ben','25','Finance',8);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skills`
--

DROP TABLE IF EXISTS `skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skills` (
  `idskills` int NOT NULL,
  `skill_name` varchar(45) NOT NULL,
  PRIMARY KEY (`idskills`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skills`
--

LOCK TABLES `skills` WRITE;
/*!40000 ALTER TABLE `skills` DISABLE KEYS */;
INSERT INTO `skills` VALUES (1,'Customer Relationship Management'),(2,'Sales Forecasting'),(3,'Network Security'),(4,'Software Development'),(5,'Recruitment and Staffing'),(6,'Employee Relations'),(7,'Financial Analysis'),(8,'Budgeting and Forecasting'),(9,'Digital Marketing'),(10,'Market Research');
/*!40000 ALTER TABLE `skills` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-12  0:11:02
