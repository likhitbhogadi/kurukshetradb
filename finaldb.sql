-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: localhost    Database: ldb
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.24.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ARMY`
--

DROP TABLE IF EXISTS `ARMY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ARMY` (
  `ARMY_ID` int NOT NULL,
  `SIDE` varchar(255) NOT NULL,
  `KINGDOM_ID` int NOT NULL,
  PRIMARY KEY (`ARMY_ID`),
  KEY `KINGDOM_ID` (`KINGDOM_ID`),
  CONSTRAINT `ARMY_ibfk_1` FOREIGN KEY (`KINGDOM_ID`) REFERENCES `KINGDOM` (`KINGDOM_ID`),
  CHECK (`SIDE` IN ('Pandavas','Kauravas','Neutral'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ARMY`
--

LOCK TABLES `ARMY` WRITE;
/*!40000 ALTER TABLE `ARMY` DISABLE KEYS */;
INSERT INTO `ARMY` VALUES (1,'Pandavas',1),(2,'Pandavas',2),(3,'Pandavas',3),(4,'Pandavas',4),(5,'Kauravas',5),(6,'Kauravas',6),(7,'Kauravas',7),(8,'Kauravas',8);
/*!40000 ALTER TABLE `ARMY` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AYUDHA`
--

DROP TABLE IF EXISTS `AYUDHA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AYUDHA` (
  `ARMY_ID` int NOT NULL,
  `AYUDHA_NAME` varchar(255) NOT NULL,
  `QUANTITY` int NOT NULL,
  PRIMARY KEY (`ARMY_ID`,`AYUDHA_NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AYUDHA`
--

LOCK TABLES `AYUDHA` WRITE;
/*!40000 ALTER TABLE `AYUDHA` DISABLE KEYS */;
INSERT INTO `AYUDHA` VALUES (1,'Bow',1500),(1,'Spear',1000),(1,'Sword',500),(2,'Mace',800),(3,'Chariot',100),(5,'Bow',1600),(5,'Spear',1100),(6,'Sword',700),(7,'Mace',900),(8,'Chariot',120);
/*!40000 ALTER TABLE `AYUDHA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BATTLE_CONFRONTATION`
--

DROP TABLE IF EXISTS `BATTLE_CONFRONTATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BATTLE_CONFRONTATION` (
  `WARRIOR1_ID` int NOT NULL,
  `WARRIOR2_ID` int NOT NULL,
  `WEAPON1_ID` int NOT NULL,
  `WEAPON2_ID` int NOT NULL,
  `EVENT_ID` int DEFAULT NULL,
  PRIMARY KEY (`WARRIOR1_ID`,`WARRIOR2_ID`,`WEAPON1_ID`,`WEAPON2_ID`),
  KEY `WARRIOR2_ID` (`WARRIOR2_ID`),
  KEY `WEAPON1_ID` (`WEAPON1_ID`),
  KEY `WEAPON2_ID` (`WEAPON2_ID`),
  KEY `EVENT_ID` (`EVENT_ID`),
  CONSTRAINT `BATTLE_CONFRONTATION_ibfk_1` FOREIGN KEY (`WARRIOR1_ID`) REFERENCES `WARRIOR` (`WARRIOR_ID`),
  CONSTRAINT `BATTLE_CONFRONTATION_ibfk_2` FOREIGN KEY (`WARRIOR2_ID`) REFERENCES `WARRIOR` (`WARRIOR_ID`),
  CONSTRAINT `BATTLE_CONFRONTATION_ibfk_3` FOREIGN KEY (`WEAPON1_ID`) REFERENCES `DIVINE_WEAPON` (`WEAPON_ID`),
  CONSTRAINT `BATTLE_CONFRONTATION_ibfk_4` FOREIGN KEY (`WEAPON2_ID`) REFERENCES `DIVINE_WEAPON` (`WEAPON_ID`),
  CONSTRAINT `BATTLE_CONFRONTATION_ibfk_5` FOREIGN KEY (`EVENT_ID`) REFERENCES `BATTLE_EVENT` (`EVENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BATTLE_CONFRONTATION`
--

LOCK TABLES `BATTLE_CONFRONTATION` WRITE;
/*!40000 ALTER TABLE `BATTLE_CONFRONTATION` DISABLE KEYS */;
INSERT INTO `BATTLE_CONFRONTATION` VALUES (1,2,1,2,1),(1,4,3,7,2),(6,7,10,11,3),(7,8,11,12,4);
/*!40000 ALTER TABLE `BATTLE_CONFRONTATION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BATTLE_EVENT`
--

DROP TABLE IF EXISTS `BATTLE_EVENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BATTLE_EVENT` (
  `EVENT_ID` int NOT NULL,
  `DAY` int NOT NULL,
  `TIME` time NOT NULL,
  `LOCATION` varchar(255) NOT NULL,
  PRIMARY KEY (`EVENT_ID`),
  CHECK (`DAY` > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BATTLE_EVENT`
--

LOCK TABLES `BATTLE_EVENT` WRITE;
/*!40000 ALTER TABLE `BATTLE_EVENT` DISABLE KEYS */;
INSERT INTO `BATTLE_EVENT` VALUES (1,1,'09:00:00','East'),(2,1,'15:00:00','North'),(3,2,'19:00:00','South'),(4,3,'09:00:00','West'),(5,4,'15:00:00','North');
/*!40000 ALTER TABLE `BATTLE_EVENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BATTLE_EVENT_CONSEQUENCES`
--

DROP TABLE IF EXISTS `BATTLE_EVENT_CONSEQUENCES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BATTLE_EVENT_CONSEQUENCES` (
  `EVENT_ID` int NOT NULL,
  `CONSEQUENCES` varchar(255) NOT NULL,
  PRIMARY KEY (`EVENT_ID`,`CONSEQUENCES`),
  CONSTRAINT `BATTLE_EVENT_CONSEQUENCES_ibfk_1` FOREIGN KEY (`EVENT_ID`) REFERENCES `BATTLE_EVENT` (`EVENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BATTLE_EVENT_CONSEQUENCES`
--

LOCK TABLES `BATTLE_EVENT_CONSEQUENCES` WRITE;
/*!40000 ALTER TABLE `BATTLE_EVENT_CONSEQUENCES` DISABLE KEYS */;
INSERT INTO `BATTLE_EVENT_CONSEQUENCES` VALUES (1,'Arjuna defeats Karna in a fierce duel'),(2,'Duryodhana orders a retreat to regroup'),(3,'Bhima kills Dushasana in revenge for Draupadi'),(4,'Bhima kills Duryodhana by smashing his thighs'),(5,'Pandavas kill Shakuni after the war ends');
/*!40000 ALTER TABLE `BATTLE_EVENT_CONSEQUENCES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BATTLE_FORMATION`
--

DROP TABLE IF EXISTS `BATTLE_FORMATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BATTLE_FORMATION` (
  `ARMY_ID` int NOT NULL,
  `DAY` int NOT NULL,
  `FORMATION_NAME` varchar(255) NOT NULL,
  `COMMANDER_ID` int NOT NULL,
  PRIMARY KEY (`ARMY_ID`,`DAY`),
  KEY `COMMANDER_ID` (`COMMANDER_ID`),
  CONSTRAINT `BATTLE_FORMATION_ibfk_1` FOREIGN KEY (`ARMY_ID`) REFERENCES `ARMY` (`ARMY_ID`),
  CONSTRAINT `BATTLE_FORMATION_ibfk_2` FOREIGN KEY (`COMMANDER_ID`) REFERENCES `WARRIOR` (`WARRIOR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BATTLE_FORMATION`
--

LOCK TABLES `BATTLE_FORMATION` WRITE;
/*!40000 ALTER TABLE `BATTLE_FORMATION` DISABLE KEYS */;
INSERT INTO `BATTLE_FORMATION` VALUES (3,10,'Vajra',4),(4,10,'Kurukshetra',4),(5,10,'Chakravyuha',11),(6,10,'Padmavyuha',11),(8,10,'Sarvatobhadra',10);
/*!40000 ALTER TABLE `BATTLE_FORMATION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BOON`
--

DROP TABLE IF EXISTS `BOON`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BOON` (
  `WARRIOR_ID` int NOT NULL,
  `DESCRIPTION` varchar(255) NOT NULL,
  `GRANTED_BY` varchar(255) NOT NULL,
  PRIMARY KEY (`WARRIOR_ID`),
  CONSTRAINT `BOON_ibfk_1` FOREIGN KEY (`WARRIOR_ID`) REFERENCES `WARRIOR` (`WARRIOR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BOON`
--

LOCK TABLES `BOON` WRITE;
/*!40000 ALTER TABLE `BOON` DISABLE KEYS */;
INSERT INTO `BOON` VALUES (1,'Pasupatastra (destructive weapon)','Lord Shiva'),(2,'Divine strength and stamina','Vayu (Wind God)'),(3,'Sceptre of Justice','Yama (God of Death)'),(4,'Divine sword','Indra'),(5,'Divine sword','Indra'),(6,'Divine armor (Kavacha) and earrings (Kundalas)','Kunti');
/*!40000 ALTER TABLE `BOON` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CHARIOT`
--

DROP TABLE IF EXISTS `CHARIOT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CHARIOT` (
  `DHVAJA_NAMA` varchar(255) NOT NULL,
  `CHARIOT_NAME` varchar(255) NOT NULL,
  `SARATHI_ID` int NOT NULL,
  `WARRIOR_ID` int NOT NULL,
  PRIMARY KEY (`DHVAJA_NAMA`),
  KEY `WARRIOR_ID` (`WARRIOR_ID`),
  KEY `SARATHI_ID` (`SARATHI_ID`),
  CONSTRAINT `CHARIOT_ibfk_1` FOREIGN KEY (`WARRIOR_ID`) REFERENCES `WARRIOR` (`WARRIOR_ID`),
  CONSTRAINT `CHARIOT_ibfk_2` FOREIGN KEY (`SARATHI_ID`) REFERENCES `WARRIOR` (`WARRIOR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CHARIOT`
--

LOCK TABLES `CHARIOT` WRITE;
/*!40000 ALTER TABLE `CHARIOT` DISABLE KEYS */;
INSERT INTO `CHARIOT` VALUES ('Hastikashyamahar-ketu ','Vijaya',13,8),('Kapi Dhwaja','Nandaka',10,1);
/*!40000 ALTER TABLE `CHARIOT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CHATURANGA`
--

DROP TABLE IF EXISTS `CHATURANGA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CHATURANGA` (
  `ARMY_ID` int NOT NULL,
  `ANGA_NAMA` varchar(255) NOT NULL,
  `INITIAL_STRENGTH` int NOT NULL,
  `CASUALTIES` int NOT NULL,
  PRIMARY KEY (`ARMY_ID`),
  CONSTRAINT `CHATURANGA_ibfk_1` FOREIGN KEY (`ARMY_ID`) REFERENCES `ARMY` (`ARMY_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CHATURANGA`
--

LOCK TABLES `CHATURANGA` WRITE;
/*!40000 ALTER TABLE `CHATURANGA` DISABLE KEYS */;
INSERT INTO `CHATURANGA` VALUES (1,'Padati',5000,1200),(2,'Ashva',3000,800),(3,'Gaja',1500,300),(4,'Ratha',1000,200),(5,'Padati',6000,1300),(6,'Ashva',3500,900),(7,'Gaja',1800,400),(8,'Ratha',1200,250);
/*!40000 ALTER TABLE `CHATURANGA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CURSE`
--

DROP TABLE IF EXISTS `CURSE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CURSE` (
  `WARRIOR_ID` int NOT NULL,
  `DESCRIPTION` varchar(255) NOT NULL,
  `IMPOSED_BY` varchar(255) NOT NULL,
  PRIMARY KEY (`WARRIOR_ID`),
  CONSTRAINT `CURSE_ibfk_1` FOREIGN KEY (`WARRIOR_ID`) REFERENCES `WARRIOR` (`WARRIOR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CURSE`
--

LOCK TABLES `CURSE` WRITE;
/*!40000 ALTER TABLE `CURSE` DISABLE KEYS */;
INSERT INTO `CURSE` VALUES (7,'May you never be able to sleep','Draupadi'),(8,'May you forget the incantations of Brahmastra when you need it the most','Parashurama'),(9,'May you be the cause of the destruction of your clan','Gandhari'),(10,'May you never be able to marry','Ganga');
/*!40000 ALTER TABLE `CURSE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DIVINE_WEAPON`
--

DROP TABLE IF EXISTS `DIVINE_WEAPON`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DIVINE_WEAPON` (
  `WEAPON_ID` int NOT NULL,
  `NAME` varchar(255) NOT NULL,
  `TYPE` varchar(255) NOT NULL,
  `INVINCIBLE` varchar(255) NOT NULL,
  `ELEMENT` varchar(255) NOT NULL,
  `BLESSING` varchar(255) NOT NULL,
  `USAGE_LIMIT` int NOT NULL,
  `WARRIOR_ID` int NOT NULL,
  PRIMARY KEY (`WEAPON_ID`),
  CHECK (`INVINCIBLE` IN ('Yes','No'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DIVINE_WEAPON`
--

LOCK TABLES `DIVINE_WEAPON` WRITE;
/*!40000 ALTER TABLE `DIVINE_WEAPON` DISABLE KEYS */;
INSERT INTO `DIVINE_WEAPON` VALUES (1,'Gandiva','Bow','Yes','Fire','Divine Blessing from Lord Agni',1000,1),(2,'Vijaya','Bow','Yes','Wind','Divine Blessing from Lord Indra',1000,2),(3,'Pashupatastra','Weapon','Yes','Fire','Divine Blessing from Lord Shiva',1,1),(4,'Shakti','Weapon','Yes','Lightning','Divine Blessing from Lord Indra',1,2),(5,'Mace','Melee Weapon','No','None','Power of Bhima',1000,3),(6,'Gada','Melee Weapon','No','None','Power of Bhima',1000,3),(7,'Mace','Melee Weapon','No','Earth','Duryodhana’s Mace',1000,4),(8,'Sword','Melee Weapon','No','None','Shalya’s Sword',1000,5),(9,'Spear','Melee Weapon','No','Water','Shalya’s Spear',1000,5),(10,'Brahmastra','Weapon','Yes','Fire','Divine Weapon of Destruction',1,6),(11,'Conch','Weapon','No','Wind','Bhishma’s Conch',1000,7),(12,'Bow','Bow','No','None','Dronacharya’s Bow',1000,8);
/*!40000 ALTER TABLE `DIVINE_WEAPON` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GURU_SHISHYA`
--

DROP TABLE IF EXISTS `GURU_SHISHYA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `GURU_SHISHYA` (
  `GURU_ID` int DEFAULT NULL,
  `SHISHYA_ID` int DEFAULT NULL,
  KEY `GURU_ID` (`GURU_ID`),
  KEY `SHISHYA_ID` (`SHISHYA_ID`),
  CONSTRAINT `GURU_SHISHYA_ibfk_1` FOREIGN KEY (`GURU_ID`) REFERENCES `WARRIOR` (`WARRIOR_ID`),
  CONSTRAINT `GURU_SHISHYA_ibfk_2` FOREIGN KEY (`SHISHYA_ID`) REFERENCES `WARRIOR` (`WARRIOR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GURU_SHISHYA`
--

LOCK TABLES `GURU_SHISHYA` WRITE;
/*!40000 ALTER TABLE `GURU_SHISHYA` DISABLE KEYS */;
INSERT INTO `GURU_SHISHYA` VALUES (1,2),(1,3),(1,4),(2,5),(2,6),(3,7);
/*!40000 ALTER TABLE `GURU_SHISHYA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `KINGDOM`
--

DROP TABLE IF EXISTS `KINGDOM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `KINGDOM` (
  `KINGDOM_ID` int NOT NULL,
  `NAME` varchar(255) NOT NULL,
  `RULER` varchar(255) NOT NULL,
  `ALLIANCE` varchar(255) NOT NULL,
  `CAPITAL` varchar(255) NOT NULL,
  `COORDINATE1` varchar(255) NOT NULL,
  `COORDINATE2` varchar(255) NOT NULL,
  PRIMARY KEY (`KINGDOM_ID`),
  CHECK (`ALLIANCE` IN ('Pandavas','Kauravas','Neutral'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `KINGDOM`
--

LOCK TABLES `KINGDOM` WRITE;
/*!40000 ALTER TABLE `KINGDOM` DISABLE KEYS */;
INSERT INTO `KINGDOM` VALUES (1,'Hastinapura','Dhritarashtra','Pandavas','Hastinapura','29.0','77.0'),(2,'Hastinapura','Dhritarashtra','Kauravas','Hastinapura','29.0','77.0'),(3,'Matsya','Yudhishthira','Pandavas','Indraprastha','29.1','77.2'),(4,'Magadha','Jarasandha','Kauravas','Girivraja','24.0','85.0'),(5,'Gandhara','Shakuni','Kauravas','Gandhar','34.0','72.5'),(6,'Kashi','Viraat','Pandavas','Kashi','25.0','82.0'),(7,'Chedi','Sishupala','Kauravas','Kundinapura','24.5','80.5'),(8,'Vrishni','Vasudeva Krishna','Pandavas','Dwaraka','22.5','69.5'),(9,'Anga','Karna','Kauravas','Anga','25.5','88.0'),(10,'Kuru','Dhritarashtra','Neutral','Hastinapura','29.0','77.0'),(11,'Sindhu','King Shalva','Kauravas','Shalva','29.5','75.5');
/*!40000 ALTER TABLE `KINGDOM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `POSSESS`
--

DROP TABLE IF EXISTS `POSSESS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `POSSESS` (
  `WARRIOR_ID` int NOT NULL,
  `WEAPON_ID` int NOT NULL,
  PRIMARY KEY (`WARRIOR_ID`,`WEAPON_ID`),
  KEY `WEAPON_ID` (`WEAPON_ID`),
  CONSTRAINT `POSSESS_ibfk_1` FOREIGN KEY (`WARRIOR_ID`) REFERENCES `WARRIOR` (`WARRIOR_ID`),
  CONSTRAINT `POSSESS_ibfk_2` FOREIGN KEY (`WEAPON_ID`) REFERENCES `DIVINE_WEAPON` (`WEAPON_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `POSSESS`
--

LOCK TABLES `POSSESS` WRITE;
/*!40000 ALTER TABLE `POSSESS` DISABLE KEYS */;
INSERT INTO `POSSESS` VALUES (1,1),(2,2),(1,3),(2,4),(3,5),(3,6),(4,7),(5,8),(6,8),(5,9),(6,10),(8,10),(7,11),(8,12);
/*!40000 ALTER TABLE `POSSESS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SARATHI`
--

DROP TABLE IF EXISTS `SARATHI`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SARATHI` (
  `WARRIOR_ID` int NOT NULL,
  `RATHI_ID` int NOT NULL,
  `HORSES_MANAGED` int NOT NULL,
  `PREFERRED_FORMATION_NAME` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`WARRIOR_ID`),
  CONSTRAINT `SARATHI_ibfk_1` FOREIGN KEY (`WARRIOR_ID`) REFERENCES `WARRIOR` (`WARRIOR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SARATHI`
--

LOCK TABLES `SARATHI` WRITE;
/*!40000 ALTER TABLE `SARATHI` DISABLE KEYS */;
INSERT INTO `SARATHI` VALUES (1,10,4,'Chakravyuha'),(5,12,3,'sarvatobhadra');
/*!40000 ALTER TABLE `SARATHI` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SENAPATI`
--

DROP TABLE IF EXISTS `SENAPATI`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SENAPATI` (
  `WARRIOR_ID` int NOT NULL,
  `ARMY_SIZE` int NOT NULL,
  `YEARS_OF_EXPERIENCE` int NOT NULL,
  `ARMY_ID` int NOT NULL,
  PRIMARY KEY (`WARRIOR_ID`),
  KEY `ARMY_ID` (`ARMY_ID`),
  CONSTRAINT `SENAPATI_ibfk_1` FOREIGN KEY (`ARMY_ID`) REFERENCES `ARMY` (`ARMY_ID`),
  CONSTRAINT `SENAPATI_ibfk_2` FOREIGN KEY (`WARRIOR_ID`) REFERENCES `WARRIOR` (`WARRIOR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SENAPATI`
--

LOCK TABLES `SENAPATI` WRITE;
/*!40000 ALTER TABLE `SENAPATI` DISABLE KEYS */;
INSERT INTO `SENAPATI` VALUES (2,100000,70,1),(4,50000,60,2);
/*!40000 ALTER TABLE `SENAPATI` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WARRIOR`
--

DROP TABLE IF EXISTS `WARRIOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `WARRIOR` (
  `WARRIOR_ID` int NOT NULL,
  `DOB` varchar(20) NOT NULL,
  `RANK` varchar(255) NOT NULL,
  `BATTLE_STATUS` varchar(255) NOT NULL,
  `KINGDOM_ID` int DEFAULT NULL,
  PRIMARY KEY (`WARRIOR_ID`),
  KEY `KINGDOM_ID` (`KINGDOM_ID`),
  CONSTRAINT `WARRIOR_ibfk_1` FOREIGN KEY (`KINGDOM_ID`) REFERENCES `KINGDOM` (`KINGDOM_ID`),
  CHECK (`BATTLE_STATUS` IN ('Alive','Dceased'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WARRIOR`
--

LOCK TABLES `WARRIOR` WRITE;
/*!40000 ALTER TABLE `WARRIOR` DISABLE KEYS */;
INSERT INTO `WARRIOR` VALUES (1,'3190 B.C.','Atirathi','Alive',1),(2,'3190 B.C.','Mahamaharathi','Alive',1),(3,'3190 B.C.','Rathi','Alive',1),(4,'3190 B.C.','Rathi','Alive',1),(5,'3190 B.C.','Rathi','Alive',1),(6,'3190 B.C.','Rathi','Alive',2),(7,'3190 B.C.','Rathi','Alive',2),(8,'3170 B.C.','Atirathi','Alive',9),(9,'3190 B.C.',' Ardhrathi','Alive',5),(10,'3170 B.C.','Mahamaharathi','Alive',2),(11,'3185 B.C.','Rathi','Alive',2),(12,'3180 B.C.','Atirathi','Alive',2),(13,'3185 B.C.','Ardhrathi','Alive',7),(14,'3180 B.C.','Rathi','Alive',11),(15,'3190 B.C.','Rathi','Alive',1),(16,'3190 B.C.','Allmighty','Alive',8);
/*!40000 ALTER TABLE `WARRIOR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WARRIOR_NAME`
--

DROP TABLE IF EXISTS `WARRIOR_NAME`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `WARRIOR_NAME` (
  `WARRIOR_ID` int NOT NULL,
  `NAME` varchar(255) NOT NULL,
  PRIMARY KEY (`WARRIOR_ID`,`NAME`),
  CONSTRAINT `FK_WARRIOR_NAME_WARRIOR_ID` FOREIGN KEY (`WARRIOR_ID`) REFERENCES `WARRIOR` (`WARRIOR_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WARRIOR_NAME`
--

LOCK TABLES `WARRIOR_NAME` WRITE;
/*!40000 ALTER TABLE `WARRIOR_NAME` DISABLE KEYS */;
INSERT INTO `WARRIOR_NAME` VALUES (1,'Arjuna'),(1,'Kaunteya'),(1,'Partha'),(2,'Bhima'),(2,'Vrikodara'),(3,'Dharmaraja'),(3,'Yudhishthira'),(4,'Madhavendra'),(4,'Nakula'),(5,'Sahadeva'),(5,'Yajnaseni'),(6,'Duryodhana'),(6,'Suyodhana'),(7,'Durmukha'),(7,'Dushasana'),(8,'Karna'),(8,'Radheya'),(8,'Vasushena'),(9,'Shakuni'),(9,'Subala'),(10,'Bhishma'),(10,'Devavrata'),(11,'Brahmastra'),(11,'Drona'),(12,'Ashwatthama'),(12,'Brahmastra'),(13,'Madhava'),(13,'Shalya'),(14,'Jayadratha'),(14,'Sindhura'),(15,'Satyaki'),(15,'Yuyudhana'),(16,'Govinda'),(16,'Krishna'),(16,'Vasudeva');
/*!40000 ALTER TABLE `WARRIOR_NAME` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WARRIOR_SKILLS`
--

DROP TABLE IF EXISTS `WARRIOR_SKILLS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `WARRIOR_SKILLS` (
  `WARRIOR_ID` int NOT NULL,
  `SKILLS` varchar(255) NOT NULL,
  PRIMARY KEY (`WARRIOR_ID`,`SKILLS`),
  CONSTRAINT `WARRIOR_SKILLS_ibfk_1` FOREIGN KEY (`WARRIOR_ID`) REFERENCES `WARRIOR` (`WARRIOR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WARRIOR_SKILLS`
--

LOCK TABLES `WARRIOR_SKILLS` WRITE;
/*!40000 ALTER TABLE `WARRIOR_SKILLS` DISABLE KEYS */;
INSERT INTO `WARRIOR_SKILLS` VALUES (1,'Archery'),(1,'Diplomacy'),(1,'Strategy'),(2,'Mace Fighting'),(2,'Strength'),(3,'Leadership'),(3,'Wisdom'),(4,'Horsemanship'),(4,'Swordsmanship'),(5,'Strategy'),(5,'Swordsmanship'),(6,'Leadership'),(6,'Mace Fighting'),(7,'Mace Fighting'),(7,'Strength'),(8,'Archery'),(8,'Loyalty'),(8,'Strategy'),(9,'Deception'),(9,'Strategy'),(10,'Mace Fighting'),(10,'Strategy'),(11,'Leadership'),(11,'Strategy'),(11,'Weaponry'),(12,'Archery'),(12,'Strategy'),(12,'War Tactics'),(13,'Leadership'),(13,'Mace Fighting'),(13,'Strategy'),(14,'Strategy'),(14,'Swordsmanship'),(15,'Archery'),(15,'Strategy'),(15,'Swordsmanship'),(16,'Diplomacy'),(16,'Divinity'),(16,'Strategy');
/*!40000 ALTER TABLE `WARRIOR_SKILLS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WAR_ACHIEVEMENT`
--

DROP TABLE IF EXISTS `WAR_ACHIEVEMENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `WAR_ACHIEVEMENT` (
  `WARRIOR_ID` int NOT NULL,
  `ACHIEVEMENT_NAME` varchar(255) NOT NULL,
  `DESCRIPTION` varchar(255) NOT NULL,
  `DAY` int NOT NULL,
  PRIMARY KEY (`WARRIOR_ID`,`ACHIEVEMENT_NAME`),
  CONSTRAINT `WAR_ACHIEVEMENT_ibfk_1` FOREIGN KEY (`WARRIOR_ID`) REFERENCES `WARRIOR` (`WARRIOR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WAR_ACHIEVEMENT`
--

LOCK TABLES `WAR_ACHIEVEMENT` WRITE;
/*!40000 ALTER TABLE `WAR_ACHIEVEMENT` DISABLE KEYS */;
INSERT INTO `WAR_ACHIEVEMENT` VALUES (1,'Slaying Bhishma','Arjuna finally slays Bhishma after receiving guidance from Shikhandi.',10),(2,'Killing of Drona','Dhrishtadyumna kills Drona, the great teacher of the Kauravas.',14),(3,'Defeating Karna','Arjuna defeats Karna, breaking his armor and killing him.',17),(4,'Killing of Duryodhana','Bheema kills Duryodhana in a mace duel, fulfilling his vow.',18);
/*!40000 ALTER TABLE `WAR_ACHIEVEMENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `YUDDHAHANI`
--

DROP TABLE IF EXISTS `YUDDHAHANI`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `YUDDHAHANI` (
  `EVENT_ID` int NOT NULL,
  `CAUSE` varchar(255) NOT NULL,
  PRIMARY KEY (`EVENT_ID`),
  CONSTRAINT `YUDDHAHANI_ibfk_1` FOREIGN KEY (`EVENT_ID`) REFERENCES `BATTLE_EVENT` (`EVENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `YUDDHAHANI`
--

LOCK TABLES `YUDDHAHANI` WRITE;
/*!40000 ALTER TABLE `YUDDHAHANI` DISABLE KEYS */;
INSERT INTO `YUDDHAHANI` VALUES (1,'Karna fatally wounded by Arjuna using Pashupatastra'),(2,'Bhishma killed by Arjuna on the 10th day of the war'),(3,'Abhimanyu killed in Chakravyuha by Kaurava warriors'),(4,'Duryodhana killed by Bhima in the final days of the war'),(5,'Shakuni killed by Pandavas after the war');
/*!40000 ALTER TABLE `YUDDHAHANI` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `YUDDHAHANI_WARRIOR_ID`
--

DROP TABLE IF EXISTS `YUDDHAHANI_WARRIOR_ID`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `YUDDHAHANI_WARRIOR_ID` (
  `EVENT_ID` int NOT NULL,
  `WARRIOR_ID` int NOT NULL,
  PRIMARY KEY (`EVENT_ID`,`WARRIOR_ID`),
  KEY `WARRIOR_ID` (`WARRIOR_ID`),
  CONSTRAINT `YUDDHAHANI_WARRIOR_ID_ibfk_1` FOREIGN KEY (`EVENT_ID`) REFERENCES `YUDDHAHANI` (`EVENT_ID`),
  CONSTRAINT `YUDDHAHANI_WARRIOR_ID_ibfk_2` FOREIGN KEY (`WARRIOR_ID`) REFERENCES `WARRIOR` (`WARRIOR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `YUDDHAHANI_WARRIOR_ID`
--

LOCK TABLES `YUDDHAHANI_WARRIOR_ID` WRITE;
/*!40000 ALTER TABLE `YUDDHAHANI_WARRIOR_ID` DISABLE KEYS */;
INSERT INTO `YUDDHAHANI_WARRIOR_ID` VALUES (1,2),(2,4),(3,6),(4,7),(5,8);
/*!40000 ALTER TABLE `YUDDHAHANI_WARRIOR_ID` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-26 19:21:11
