-- MySQL dump 10.13  Distrib 8.3.0, for Win64 (x86_64)
--
-- Host: databaserafael.cj2mqqcw6wf0.us-east-2.rds.amazonaws.com    Database: analisis
-- ------------------------------------------------------
-- Server version	8.0.35

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `analisis`
--

DROP TABLE IF EXISTS `analisis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analisis` (
  `ana_id` int unsigned NOT NULL AUTO_INCREMENT,
  `ana_area_id_fk` int unsigned NOT NULL DEFAULT '0',
  `ana_nombre` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT '',
  `ana_costo` decimal(20,2) NOT NULL DEFAULT '0.00',
  `ana_sta` char(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT 'A',
  PRIMARY KEY (`ana_id`),
  KEY `FK_analisis_1` (`ana_area_id_fk`)
) ENGINE=InnoDB AUTO_INCREMENT=185 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci COMMENT='tabla donde se guardan los analisis\r\n';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analisis`
--

LOCK TABLES `analisis` WRITE;
/*!40000 ALTER TABLE `analisis` DISABLE KEYS */;
INSERT INTO `analisis` VALUES (1,1,'Ácido Úrico en orina 24H',95.00,'A'),(2,1,'Ácido Úrico en suero (líquido sinovial)',95.00,'A'),(3,1,'Amiba en fresco',69.00,'A'),(4,1,'Amilasa',110.00,'A'),(5,3,'Anfetaminas Semicuantitativo',129.00,'A'),(6,3,'Anfetaminas Cualitativo',52.00,'A'),(7,3,'Anticuerpos anti-Dengue IgG/IgM',345.00,'A'),(8,3,'Anticuerpos anti-HBsAg',181.00,'A'),(9,3,'Anticuerpos anti-HCV',181.00,'A'),(10,3,'Anticuerpos anti HIV 1 y 2',190.00,'A'),(11,3,'Anticuerpos Anti-HIV 1 y 2 / Antígeno p24',560.00,'A'),(12,3,'Anticuerpos Sars-Cov2 IgG e IgM Cualitativos (Entr',302.00,'A'),(13,3,'Antidoping 3 (Anfetamina, marihuana, cocaína) (Sem',388.00,'A'),(14,3,'Antidoping 3 (Anfetamina, marihuana, cocaína) (Cua',156.00,'A'),(15,3,'Antidoping 5 (Anfetamina, marihuana, cocaína, barb',646.50,'A'),(16,3,'Antidoping 6 (Anfetamina, marihuana, cocaína, barb',776.00,'A'),(17,3,'Antidoping 6 (Anfetamina, marihuana, cocaína, barb',312.00,'A'),(18,3,'Antigeno COVID (entrega en 1 hora)*',388.00,'A'),(19,3,'Antígeno de Dengue virus NS1',302.00,'A'),(20,3,'Antígeno para Influenza A Y B',431.00,'A'),(21,3,'Antígeno Prostático Específico (PSA)',215.50,'A'),(22,1,'Azúcares reductores',69.00,'A'),(23,1,'Azul de metileno (moco fecal)',60.00,'A'),(24,4,'BAAR',95.00,'A'),(25,4,'BAAR (2 Muestras)',129.00,'A'),(26,4,'BAAR (3 muestras)',237.00,'A'),(27,4,'BAAR (5 muestras)',315.00,'A'),(28,4,'Bacterioscópico (Gram)',86.00,'A'),(29,3,'Barbitúricos en orina semicuantitativo',129.00,'A'),(30,3,'Barbitúricos semicualitativa',52.00,'A'),(31,3,'Benzodiacepina cualitativa',52.00,'A'),(32,3,'Benzodiacepina en orina semicuantitativa',129.00,'A'),(33,1,'Bilirrubina',78.00,'A'),(34,2,'Biometría Hemática',112.00,'A'),(35,1,'Búsqueda de helmintos: aguas, lixiviados',388.00,'A'),(36,1,'Calcio en orina (24 hrs)',129.00,'A'),(37,1,'Calcio en suero',86.00,'A'),(38,3,'Cannabinoides \"Marihuana\" semicuantitativo',129.00,'A'),(39,3,'Cannabinoides \"Marihuana\" cualitativo',52.00,'A'),(40,5,'Cinética de hierro. (capacidad de fijación de Hier',474.00,'A'),(41,1,'Cloro en orina',73.00,'A'),(42,1,'Cloro en sangre',86.00,'A'),(43,3,'Cocaína Metabólico semicuantitativo',129.00,'A'),(44,3,'Cocaína Metabólico cualitativo',52.00,'A'),(45,1,'Colesterol de alta Densidad HDL-CHOL',78.00,'A'),(46,1,'Colesterol de baja Densidad LDL-CHOL',78.00,'A'),(47,1,'Colesterol de muy baja Densidad VLDL-CHOL',78.00,'A'),(48,1,'Colesterol total',60.00,'A'),(49,2,'Coombs Directo',142.00,'A'),(50,1,'Coprológico General',155.00,'A'),(51,1,'Coproparasitoscópico',69.00,'A'),(52,1,'Coproparasitoscópico (2 muestras)',129.00,'A'),(53,1,'Coproparasitoscópico + sangre oculta',129.00,'A'),(54,1,'Coproparasitoscópico (3 muestras)',190.00,'A'),(55,1,'Creatinina',52.00,'A'),(56,1,'Creatinina en orina',52.00,'A'),(57,4,'Cultivo Bacteriológico',478.50,'A'),(58,4,'Cultivo Bacteriológico CMI',681.00,'A'),(59,4,'Cultivo de Anaeróbios',474.00,'A'),(60,4,'Cultivo de BAAR Identificación de la cepa. En caso',884.00,'A'),(61,4,'Cultivo de BAAR sin Antibiograma',409.50,'A'),(62,4,'Cultivo de Esperma',478.50,'A'),(63,4,'Cultivo de Expectoración',478.50,'A'),(64,4,'Cultivo de Expectoración. CMI',685.00,'A'),(65,4,'Cultivo de Exudado Cérvico Vaginal',478.50,'A'),(66,4,'Cultivo de Exudado Cérvico Vaginal. CMI',685.00,'A'),(67,4,'Cultivo de Exudado Faríngeo',478.50,'A'),(68,4,'Cultivo de Exudado Faríngeo: CMI',681.00,'A'),(69,4,'Cultivo de Heces',478.50,'A'),(70,4,'Cultivo de Heces. CMI',685.00,'A'),(71,4,'Cultivo de Orina',478.50,'A'),(72,4,'Cultivo de Orina. CMI',685.00,'A'),(73,4,'Cultivo de Sangre',1039.00,'A'),(74,4,'Cultivo de Sangre. CMI',1039.00,'A'),(75,4,'Cultivo de Secreción',422.00,'A'),(76,4,'Cultivo de Secreción. CMI',681.00,'A'),(77,4,'Cultivo de Superficie inertes',409.50,'A'),(78,4,'Cultivo de superficie vivas',478.50,'A'),(79,4,'Cultivo Micológico. CMI para levadura',681.00,'A'),(80,3,'Dengue Combo DUO - IgG/IgM + NS1',388.00,'A'),(81,1,'Depuración de Creatinina',129.00,'A'),(82,1,'Deshidrogenasa Láctica DHL',95.00,'A'),(83,3,'Dimero D',422.00,'A'),(84,1,'Electrolitos en Orina (Na, K, Cl)',129.00,'A'),(85,1,'Electrolitos Sérico (Na, K, Cl)',129.00,'A'),(86,1,'Electrolitos Sérico (Na, K, Cl, Ca, Mg, P)',259.00,'A'),(87,2,'Eosinófilos en moco nasal',103.50,'A'),(88,1,'Espermatobioscopia',431.00,'A'),(89,3,'Estradiol (E2)',172.00,'A'),(90,3,'Estradiol libre',158.00,'A'),(91,1,'Examen general de orina (EGO)',86.00,'A'),(92,3,'Factor reumatoide',69.00,'A'),(93,3,'Ferritina',215.50,'A'),(94,2,'Fibrinógeno',142.00,'A'),(95,2,'Fórmula Blanca',86.00,'A'),(96,2,'Fórmula Roja',86.00,'A'),(97,1,'Fosfatasa Alcalina',73.00,'A'),(98,1,'Fósforo sérico',86.00,'A'),(99,1,'Gamma glutamil transpeptidasa (GGT)',73.00,'A'),(100,1,'Glucosa',52.00,'A'),(101,1,'Glucosa en orina',52.00,'A'),(102,1,'Glucosa Post-Carga (3 determinaciones)',589.00,'A'),(103,1,'Glucosa Post-prandial',86.00,'A'),(104,3,'Gonadotrofinas Hipofisiarias. LH, FSH',259.00,'A'),(105,2,'Grupos Sanguineos y Rh',103.50,'A'),(106,1,'Hemoglobina Glucosilada A1c',215.50,'A'),(107,3,'Hierro Sérico',78.00,'A'),(108,3,'Hierro Sérico y Capacidad de fijación',207.00,'A'),(109,3,'Hormonas de Crecimiento',215.50,'A'),(110,3,'Hormona Folículo Estimulante FSH',159.50,'A'),(111,3,'Hormona Luteinizante LH',142.00,'A'),(112,3,'Hormona Tiroideo Estimulante TSH',103.50,'A'),(113,1,'Identificación de parásitos Remitidos',129.00,'A'),(114,3,'Indice de Tiroxina Libre',250.00,'A'),(115,3,'Insulina',238.50,'A'),(116,1,'Investigación de Cryptosporidium sp.',129.00,'A'),(117,1,'Isospora Belli y Cyclospora cayetanensis',483.00,'A'),(118,1,'Lipasa',110.00,'A'),(119,1,'Lípidos Totales',78.00,'A'),(120,1,'Magnesio en orina',315.00,'A'),(121,1,'Magnesio sérico',86.00,'A'),(122,3,'Metanfetamina cualitativo',52.00,'A'),(123,3,'Metanfetamina semicuantitativo',129.00,'A'),(124,1,'Nitrógeno Ureico',65.00,'A'),(125,1,'Nitrógeno Ureico en orina de 24 hrs',65.00,'A'),(126,3,'Opiáceos semicuantitativos',129.00,'A'),(127,3,'Opiáceos cualitativo',52.00,'A'),(128,5,'PCR COVID (entrega en 24/48 hrs)*',1364.00,'A'),(129,5,'PCR COVID express (entrega el mismo día)*',2155.00,'A'),(130,5,'PCR COVIFLU (influenza/covid entrega en 24/48 hrs)',2500.00,'A'),(131,1,'PH y azúcar reductores',82.00,'A'),(132,2,'Plaquetas',69.00,'A'),(133,1,'Potasio en Orina',86.00,'A'),(134,1,'Potasio en sangre',86.00,'A'),(135,3,'Progesterona',134.00,'A'),(136,3,'Prolactina',134.00,'A'),(137,3,'Proteína C Reactiva (PCR)',69.00,'A'),(138,1,'Proteínas en orina 24 H',103.50,'A'),(139,1,'Proteínas Totales Relación A/G',82.00,'A'),(140,3,'Prueba de embarazo cuantitativa (Sub unidad Beta)',315.00,'A'),(141,5,'Prueba de embarazo cualitativa (Sub unidad Beta)',129.00,'A'),(142,3,'Reacciones Febriles',129.00,'A'),(143,2,'Reticulocitos',65.00,'A'),(144,3,'Rotavirus',259.00,'A'),(145,2,'Sedimentación Globular ó VSG ó Eritrosedimentación',65.00,'A'),(146,5,'Sodio en orina',86.00,'A'),(147,1,'Sodio en sangre',86.00,'A'),(148,3,'T3 Captación',103.50,'A'),(149,3,'T3 Libre',103.50,'A'),(150,3,'T3 Triyodotironina total',103.50,'A'),(151,3,'T4 Tiroxina libre',103.50,'A'),(152,3,'T4 Tiroxina Total',103.50,'A'),(153,3,'Testosterona',174.20,'A'),(154,3,'Testosterona libre',166.50,'A'),(155,2,'Tiempo de coagulación recalcificación de plasma',60.00,'A'),(156,2,'Tiempo de Protrombina',86.00,'A'),(157,2,'Tiempo de Sangrado',65.00,'A'),(158,2,'Tiempo de sangrado y Coagulación',78.00,'A'),(159,2,'Tiempo de tromboplastina parcial',86.00,'A'),(160,1,'Tolerancia a la glucosa 2h.',155.00,'A'),(161,1,'Tolerancia a la glucosa 3h.',207.00,'A'),(162,1,'Tolerancia a la glucosa 4h.',259.00,'A'),(163,1,'Transaminasa G. Oxalacetica (TGO/AST)',60.00,'A'),(164,1,'Transaminasa G. Piruvuca (TGP/ALT)',60.00,'A'),(165,1,'Triglicéridos',65.00,'A'),(166,1,'Urea en líquido de Diálisis',65.00,'A'),(167,1,'Urea en orina',65.00,'A'),(168,1,'Urea Sérica',52.00,'A'),(169,3,'VDRL',69.00,'A'),(170,3,'Vitamina D total (OH) 25 (D2+D3)',517.00,'A'),(171,1,'Índice Aterogénico',0.00,'O'),(172,1,'Prueba',10.00,'O'),(176,1,'Aaaa',45.00,'O'),(177,1,'Aaa',1.00,'O'),(178,1,'A',1.00,'O'),(179,1,'Prueba1',22.00,'O'),(180,1,'Testest',111.00,'O'),(183,1,'assa',0.00,'A');
/*!40000 ALTER TABLE `analisis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `areas`
--

DROP TABLE IF EXISTS `areas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `areas` (
  `area_id` int unsigned NOT NULL AUTO_INCREMENT,
  `area_nombre` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT '',
  `area_sta` char(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT 'A',
  PRIMARY KEY (`area_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `areas`
--

LOCK TABLES `areas` WRITE;
/*!40000 ALTER TABLE `areas` DISABLE KEYS */;
INSERT INTO `areas` VALUES (1,'Urianálisis/QS','A'),(2,'Hematología','A'),(3,'Serología/Hormonas','A'),(4,'Bacteriología','A'),(6,'Recepción','A'),(7,'Admin','A');
/*!40000 ALTER TABLE `areas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `areas_analisis_rel`
--

DROP TABLE IF EXISTS `areas_analisis_rel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `areas_analisis_rel` (
  `aana_area_id_fk` int unsigned NOT NULL,
  `aana_ana_id_fk` int unsigned NOT NULL,
  PRIMARY KEY (`aana_area_id_fk`,`aana_ana_id_fk`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `areas_analisis_rel`
--

LOCK TABLES `areas_analisis_rel` WRITE;
/*!40000 ALTER TABLE `areas_analisis_rel` DISABLE KEYS */;
/*!40000 ALTER TABLE `areas_analisis_rel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `descuentos`
--

DROP TABLE IF EXISTS `descuentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `descuentos` (
  `des_id` int unsigned NOT NULL AUTO_INCREMENT,
  `des_nombre` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT '',
  `des_dsc` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT '',
  `des_sta` char(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT 'A',
  `des_descuento` decimal(5,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (`des_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `descuentos`
--

LOCK TABLES `descuentos` WRITE;
/*!40000 ALTER TABLE `descuentos` DISABLE KEYS */;
INSERT INTO `descuentos` VALUES (1,'Sin Descuento','Sin Descuento','A',0.00),(2,'Egresados','Egresados','A',15.00),(3,'Comunidad UdeG y Discapacitados','Alumnos, personal administrativo y académicos, de la Universidad de Guadalajara y Familiares directos del personal administrativo y académicos de la Universidad de Guadalajara','A',20.00),(4,'Tercera Edad','Tercera Edad','A',30.00),(5,'Especial','Especial','A',50.00);
/*!40000 ALTER TABLE `descuentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grupos`
--

DROP TABLE IF EXISTS `grupos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grupos` (
  `grupo_id` int unsigned NOT NULL AUTO_INCREMENT,
  `grupo_nombre` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT '',
  `grupo_sta` char(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT 'A',
  `grupo_costo` decimal(20,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (`grupo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci COMMENT='tabla para los nombre de los grupos';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grupos`
--

LOCK TABLES `grupos` WRITE;
/*!40000 ALTER TABLE `grupos` DISABLE KEYS */;
INSERT INTO `grupos` VALUES (1,'Perfil Hepático con TP','A',461.00),(2,'Perfil Hepático sin TP','A',383.40),(3,'Perfil de Lípidos','A',345.00),(4,'Perfil Óseo I','A',259.00),(5,'Perfil Ovárico','A',733.00),(6,'Perfil Ovarico conTSH','A',819.00),(7,'Perfil Renal','A',560.00),(8,'Perfil Reúmatico','A',474.00),(9,'Perfil Rotavirus','A',418.00),(10,'Perfil Tiroideo I de 5 determinaciones','A',534.50),(11,'Perfil Tiroideo II de 3 determinaciones','A',284.50),(12,'Perfil Veterinario I','A',276.00),(13,'Perfil Veterinario II','A',310.00),(14,'Perfil Veterinario III','A',379.00),(15,'Perfil Veterinario IV','A',534.50),(16,'Química Sanguínea de 3 determinaciones','A',142.00),(17,'Química Sanguínea de 4 determinaciones','A',172.00),(18,'Química Sanguínea de 6 determinaciones','A',237.00),(19,'Química Sanguínea de 18 determinaciones','A',448.00),(20,'Química Sanguínea de 20 determinaciones','A',534.50),(21,'Química Sanguínea de 24 determinaciones','A',672.00),(22,'Química Sanguínea de 27 determinaciones','A',686.00),(23,'Química Sanguínea de 35 determinaciones','A',1250.00),(25,'prueba','O',1.00),(26,'Pruebaa','O',1.00),(27,'test','A',1.00),(28,'test222','A',1.00),(29,'aaaaaaaa','A',11111.00),(30,'test555','A',21.00),(33,'test26','A',16.00),(34,'test16','A',12.00);
/*!40000 ALTER TABLE `grupos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grupos_analisis_rel`
--

DROP TABLE IF EXISTS `grupos_analisis_rel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grupos_analisis_rel` (
  `gana_grupo_id_fk` int unsigned NOT NULL,
  `gana_ana_id_fk` int unsigned NOT NULL,
  PRIMARY KEY (`gana_grupo_id_fk`,`gana_ana_id_fk`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grupos_analisis_rel`
--

LOCK TABLES `grupos_analisis_rel` WRITE;
/*!40000 ALTER TABLE `grupos_analisis_rel` DISABLE KEYS */;
INSERT INTO `grupos_analisis_rel` VALUES (0,1),(0,2),(0,3),(0,5),(1,33),(1,97),(1,99),(1,139),(1,156),(1,163),(1,164),(2,33),(2,97),(2,99),(2,139),(2,163),(2,164),(3,45),(3,46),(3,47),(3,48),(3,119),(3,165),(3,171),(4,36),(4,97),(4,98),(4,139),(5,89),(5,110),(5,111),(5,135),(5,136),(6,89),(6,110),(6,111),(6,112),(6,135),(6,136),(8,2),(8,92),(8,97),(8,137),(8,145),(10,112),(10,149),(11,112),(12,34),(12,97),(12,164),(13,34),(13,97),(13,164),(14,34),(14,91),(14,97),(14,139),(14,164),(15,34),(15,87),(15,91),(15,139),(15,164),(18,48),(18,165);
/*!40000 ALTER TABLE `grupos_analisis_rel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mediciones_analisis`
--

DROP TABLE IF EXISTS `mediciones_analisis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mediciones_analisis` (
  `mediciones_analisis_id` int unsigned NOT NULL AUTO_INCREMENT,
  `mediciones_analisis_ana_id_fk` int unsigned DEFAULT NULL,
  `mediciones_analisis_componente` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT '',
  `mediciones_analisis_unidad` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT '',
  `mediciones_analisis_rango` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT '',
  PRIMARY KEY (`mediciones_analisis_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mediciones_analisis`
--

LOCK TABLES `mediciones_analisis` WRITE;
/*!40000 ALTER TABLE `mediciones_analisis` DISABLE KEYS */;
INSERT INTO `mediciones_analisis` VALUES (3,91,'ASPECTO','','TRANSPARENTE'),(4,91,'COLOR','','AMARILLO'),(5,91,'GLUCOSA','g/L','NEGATIVO'),(6,91,'BILIRRUBINAS','mg/dL','NEGATIVO'),(7,91,'CETONAS','mg/dL','NEGATIVO'),(8,33,'BILIRRUBINA TOTAL','mg/dL','0.2 – 1.3'),(9,97,'FOSFATASA ALCALINA','U/L','53 – 279'),(10,99,'GAMMAGLUTAMIL TRANSPEPTIDASA (GGT)','U/L','< 32'),(11,139,'PROTEÍNAS TOTALES RELACION A/G','g/dL','6.8 – 8.3'),(12,156,'TIEMPO DE PROTOMBINA','seg','11 - 13.5'),(13,163,'TRANSAMINASA G. OXALACETICA (TGO/AST)','U/L',' 5 - 40'),(14,164,'TRANSAMINASA G. PIRUVUCA','U/L','7 - 56');
/*!40000 ALTER TABLE `mediciones_analisis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `muestra_analisis_rel`
--

DROP TABLE IF EXISTS `muestra_analisis_rel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `muestra_analisis_rel` (
  `muan_mues_id_fk` int unsigned NOT NULL DEFAULT '0',
  `muan_ana_id_fk` int unsigned NOT NULL DEFAULT '0',
  `muan_alta_fec` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `muan_sta` char(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT 'A',
  `muan_resultado` float DEFAULT NULL,
  PRIMARY KEY (`muan_mues_id_fk`,`muan_ana_id_fk`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `muestra_analisis_rel`
--

LOCK TABLES `muestra_analisis_rel` WRITE;
/*!40000 ALTER TABLE `muestra_analisis_rel` DISABLE KEYS */;
INSERT INTO `muestra_analisis_rel` VALUES (20,2,'2022-06-15 22:41:01','A',NULL),(20,5,'2022-06-15 22:41:01','A',NULL),(20,36,'2022-06-15 22:41:01','A',NULL),(20,130,'2022-06-15 22:41:01','A',NULL),(21,4,'2024-02-03 16:58:43','A',NULL);
/*!40000 ALTER TABLE `muestra_analisis_rel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `muestras`
--

DROP TABLE IF EXISTS `muestras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `muestras` (
  `mues_id` int unsigned NOT NULL AUTO_INCREMENT,
  `mues_des_id_fk` int unsigned NOT NULL DEFAULT '0',
  `mues_sta` char(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT 'A',
  `mues_alta_fec` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `mues_folio` char(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT '0',
  `mues_nombre` blob NOT NULL,
  `mues_apellido_paterno` blob NOT NULL,
  `mues_apellido_materno` blob NOT NULL,
  `mues_calle` blob,
  `mues_num_ext` char(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT '',
  `mues_num_int` char(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT '',
  `mues_colonia` blob,
  `mues_tel` blob,
  `mues_email` blob,
  `mues_horas_ayuno` int DEFAULT '0',
  `mues_alimentos` varchar(1024) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT '',
  `mues_enfermedades` varchar(1024) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT '',
  `mues_medicamentos` varchar(1024) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT '',
  `mues_rubrica` varchar(80) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT '',
  `mues_edad` int unsigned DEFAULT '0',
  `mues_fec_nac` datetime DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`mues_id`),
  KEY `mues_des_id_fk` (`mues_des_id_fk`),
  CONSTRAINT `muestras_ibfk_1` FOREIGN KEY (`mues_des_id_fk`) REFERENCES `descuentos` (`des_id`)
) ENGINE=InnoDB AUTO_INCREMENT=150 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci COMMENT='Tabla donde se guardan los datos de las muestras';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `muestras`
--

LOCK TABLES `muestras` WRITE;
/*!40000 ALTER TABLE `muestras` DISABLE KEYS */;
INSERT INTO `muestras` VALUES (142,1,'O','2024-04-22 01:11:07','PHG1SNFWZ20XSIBT981Q',_binary 'jey2UkY4ec+sMvxOWTo2HQ==',_binary '4pJfOPp/dNTvJpPA0Rg5hg==',_binary 'bbANoIoSi9xsQlGIdF/MWw==',_binary 'O0TydLr3T6n2B+mdlH9Z76QrkOOXvHx0W53Etf4tlnA=','1311','A',_binary 'aU5D2DQe88aCaNimJJ9xUw==',_binary '1wa3G0d15PAwP93pX1/3gQ==',_binary 'OrZJ8UVXtN9ZtqfK44BACxc+Gb5m76HbIihii3QfBg4=',8,'Ninguno','Ninguna','Ninguno',NULL,24,'1999-12-16 00:00:00'),(143,1,'O','2024-04-22 18:48:44','Q7ZHJ5700HLF92E4CFBW',_binary 'SnJrmqzl86ZSrBf0WWZ0pQ==',_binary 'EqHei5Uuvws5dBt9j+KZv5iKtAXhMu9RMbyjDmAiPNo=',_binary 'EqHei5Uuvws5dBt9j+KZv5iKtAXhMu9RMbyjDmAiPNo=',_binary 'LWje/qy4JSg1r3Oai2oT7g==','1','A',_binary 'n+RyWz80TJDHvtuuxHPI5A==',_binary 'OHWhhgH8R/6lLDDPXNhsvQ==',_binary 'CzB+s6bg45KnmCa/W95E0P5f2fHtlJlOeMRUKyl48Ro=',4,'Ninguno','Ninguna','Ninguno',NULL,40,'1983-12-12 00:00:00'),(144,1,'O','2024-04-22 18:50:54','4TLMOOZEHXS3PQ7UQFTJ',_binary 'pFJDOkqJFKCAisZ3N1e5LQ==',_binary '3LfiOz6CJeldk55tlTr/ew==',_binary '49L45qsod7CeZNK+8Mz1pA==',_binary '1GnL9Du8XoTTbXOp3vWLfQ==','12','C',_binary '2hyeCL0Mjx7eLr78MQ3YLT9U0cbrVWkgB/xG9OR9mI0=',_binary 'Glml+sSGBySCbmoSj54K2g==',_binary 'FeKUGXz5xK1c5/sxRw3EYMt+pQ5cZkQ0mg+PVpI7uE4=',3,'Ninguno','Ninguna','Ninguno',NULL,31,'1992-12-19 00:00:00'),(147,1,'O','2024-04-22 21:06:48','QZVG4O5HSZK5AUHDT9LQ',_binary 'iRniwUoXRsJCQuO1ZC9JbA==',_binary 'H3B8d1kIXFhQNVoIFFvMGw==',_binary 'u7u3DnA3oT379sj0dh5TGA==',_binary 'fB1EEs7IwtaDC0FgM/a0OA==','2','',_binary 'xF2laK0s7Vx7HLJFqKFSMQ==',_binary 'OHWhhgH8R/6lLDDPXNhsvQ==',_binary 'B+8LukcVcf3spT5PWTjT+2ZOXHyEkGxNc4+iiETrbrg=',7,'Ninguno','Ninguna','Ninguno',NULL,25,'1998-12-13 00:00:00'),(149,1,'O','2024-04-23 00:06:00','GL6SN8GAZB294KLFC9TH',_binary '/HHywk0jZhrvXwu3Ua119Q==',_binary '+w0W5025TGK2yfW6B5zmGg==',_binary 'z1KAoTTN+73kg3YZNtB5KA==',_binary '57OBUYe/gkz2dYhOgy7Qtw==','1','1',_binary 'L5bnakn6ekFUjfKRarrh1w==',_binary 'OHWhhgH8R/6lLDDPXNhsvQ==',_binary 'crMvqAE2qtspQQhGRrMahg==',12,'Ninguno','Ninguna','Ninguno',NULL,22,'2001-10-10 00:00:00');
/*!40000 ALTER TABLE `muestras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perfiles`
--

DROP TABLE IF EXISTS `perfiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `perfiles` (
  `per_id` int unsigned NOT NULL AUTO_INCREMENT,
  `per_nombre` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT '',
  `per_sta` char(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT 'A',
  PRIMARY KEY (`per_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perfiles`
--

LOCK TABLES `perfiles` WRITE;
/*!40000 ALTER TABLE `perfiles` DISABLE KEYS */;
INSERT INTO `perfiles` VALUES (1,'RECEPCION','A'),(2,'ANALISTA','A');
/*!40000 ALTER TABLE `perfiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resultados`
--

DROP TABLE IF EXISTS `resultados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resultados` (
  `resul_id` int NOT NULL AUTO_INCREMENT,
  `resul_medicion_analisis_id_fk` int unsigned NOT NULL,
  `resul_ana_id_fk` int unsigned NOT NULL,
  `resul_mues_id_fk` int unsigned NOT NULL,
  `resul_fecha` date DEFAULT '0000-00-00',
  `resul_resultado` float DEFAULT '0',
  `resul_fuera_de_rango` tinyint DEFAULT '0',
  `resul_sta` varchar(50) DEFAULT '',
  PRIMARY KEY (`resul_id`),
  KEY `resul_ana_id_fk` (`resul_ana_id_fk`),
  KEY `resul_mues_id_fk` (`resul_mues_id_fk`)
) ENGINE=InnoDB AUTO_INCREMENT=520 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resultados`
--

LOCK TABLES `resultados` WRITE;
/*!40000 ALTER TABLE `resultados` DISABLE KEYS */;
INSERT INTO `resultados` VALUES (433,3,91,134,'0000-00-00',NULL,NULL,'O'),(434,4,91,134,'0000-00-00',NULL,NULL,'O'),(435,5,91,134,'0000-00-00',NULL,NULL,'O'),(436,6,91,134,'0000-00-00',NULL,NULL,'O'),(437,7,91,134,'0000-00-00',NULL,NULL,'O'),(438,8,33,135,'2024-03-13',0.5,1,'F'),(439,9,97,135,'2024-03-13',55,0,'F'),(440,10,99,135,'2024-03-13',30,0,'F'),(441,11,139,135,'2024-03-13',9,1,'F'),(442,12,156,135,'2024-03-13',12,0,'F'),(443,13,163,135,'2024-03-13',45,1,'F'),(444,14,164,135,'2024-03-13',10,0,'F'),(445,3,91,136,'0000-00-00',NULL,NULL,'O'),(446,4,91,136,'0000-00-00',NULL,NULL,'O'),(447,5,91,136,'0000-00-00',NULL,NULL,'O'),(448,6,91,136,'0000-00-00',NULL,NULL,'O'),(449,7,91,136,'0000-00-00',NULL,NULL,'O'),(450,3,91,137,'0000-00-00',NULL,NULL,'O'),(451,4,91,137,'0000-00-00',NULL,NULL,'O'),(452,5,91,137,'0000-00-00',NULL,NULL,'O'),(453,6,91,137,'0000-00-00',NULL,NULL,'O'),(454,7,91,137,'0000-00-00',NULL,NULL,'O'),(455,3,91,138,'0000-00-00',NULL,NULL,'O'),(456,4,91,138,'0000-00-00',NULL,NULL,'O'),(457,5,91,138,'0000-00-00',NULL,NULL,'O'),(458,6,91,138,'0000-00-00',NULL,NULL,'O'),(459,7,91,138,'0000-00-00',NULL,NULL,'O'),(460,8,33,139,'2024-03-14',0.5,0,'F'),(461,9,97,139,'2024-03-14',280,1,'F'),(462,10,99,139,'2024-03-14',33,0,'F'),(463,11,139,139,'2024-03-14',8,0,'F'),(464,12,156,139,'2024-03-14',12,0,'F'),(465,13,163,139,'2024-03-14',10,0,'F'),(466,14,164,139,'2024-03-14',8,0,'F'),(467,8,33,140,'0000-00-00',NULL,NULL,'O'),(468,9,97,140,'0000-00-00',NULL,NULL,'O'),(469,10,99,140,'0000-00-00',NULL,NULL,'O'),(470,11,139,140,'0000-00-00',NULL,NULL,'O'),(471,12,156,140,'0000-00-00',NULL,NULL,'O'),(472,13,163,140,'0000-00-00',NULL,NULL,'O'),(473,14,164,140,'0000-00-00',NULL,NULL,'O'),(474,8,33,141,'0000-00-00',NULL,NULL,'O'),(475,9,97,141,'0000-00-00',NULL,NULL,'O'),(476,10,99,141,'0000-00-00',NULL,NULL,'O'),(477,11,139,141,'0000-00-00',NULL,NULL,'O'),(478,12,156,141,'0000-00-00',NULL,NULL,'O'),(479,13,163,141,'0000-00-00',NULL,NULL,'O'),(480,14,164,141,'0000-00-00',NULL,NULL,'O'),(481,8,33,142,'2024-05-06',10,1,'F'),(482,9,97,142,'2024-05-06',3,0,'F'),(483,10,99,142,'0000-00-00',NULL,NULL,'O'),(484,11,139,142,'0000-00-00',NULL,NULL,'O'),(485,12,156,142,'0000-00-00',NULL,NULL,'O'),(486,13,163,142,'0000-00-00',NULL,NULL,'O'),(487,14,164,142,'0000-00-00',NULL,NULL,'O'),(488,3,91,143,'0000-00-00',NULL,NULL,'O'),(489,4,91,143,'0000-00-00',NULL,NULL,'O'),(490,5,91,143,'0000-00-00',NULL,NULL,'O'),(491,6,91,143,'0000-00-00',NULL,NULL,'O'),(492,7,91,143,'0000-00-00',NULL,NULL,'O'),(493,3,91,144,'0000-00-00',NULL,NULL,'O'),(494,4,91,144,'0000-00-00',NULL,NULL,'O'),(495,5,91,144,'0000-00-00',NULL,NULL,'O'),(496,6,91,144,'0000-00-00',NULL,NULL,'O'),(497,7,91,144,'0000-00-00',NULL,NULL,'O'),(498,3,91,146,'0000-00-00',NULL,NULL,'O'),(499,4,91,146,'0000-00-00',NULL,NULL,'O'),(500,5,91,146,'0000-00-00',NULL,NULL,'O'),(501,6,91,146,'0000-00-00',NULL,NULL,'O'),(502,7,91,146,'0000-00-00',NULL,NULL,'O'),(503,3,91,147,'0000-00-00',NULL,NULL,'O'),(504,4,91,147,'0000-00-00',NULL,NULL,'O'),(505,5,91,147,'0000-00-00',NULL,NULL,'O'),(506,6,91,147,'0000-00-00',NULL,NULL,'O'),(507,7,91,147,'0000-00-00',NULL,NULL,'O'),(508,3,91,148,'0000-00-00',NULL,NULL,'O'),(509,4,91,148,'0000-00-00',NULL,NULL,'O'),(510,5,91,148,'0000-00-00',NULL,NULL,'O'),(511,6,91,148,'0000-00-00',NULL,NULL,'O'),(512,7,91,148,'0000-00-00',NULL,NULL,'O'),(513,8,33,149,'0000-00-00',NULL,NULL,'O'),(514,9,97,149,'0000-00-00',NULL,NULL,'O'),(515,10,99,149,'0000-00-00',NULL,NULL,'O'),(516,11,139,149,'0000-00-00',NULL,NULL,'O'),(517,12,156,149,'0000-00-00',NULL,NULL,'O'),(518,13,163,149,'0000-00-00',NULL,NULL,'O'),(519,14,164,149,'0000-00-00',NULL,NULL,'O');
/*!40000 ALTER TABLE `resultados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_area_id_fk` int unsigned NOT NULL DEFAULT '0',
  `user_username` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `user_password` text CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci,
  `user_perfil_id_fk` int unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (6,7,'admin','scrypt:32768:8:1$mLnG1rhvsFGIg05T$0d03cae4de979350eb39e06031232b2065234cc28983bb2fddc307c3b9a3d6554624a253111a183984f2d33d92c7d7f7c85c72b736fdcb97248bbaa02e000b6a',0),(40,7,'PRUEBA','scrypt:32768:8:1$UnR4AOx02sEiYkBg$49f4fc30863b678c64e18fc4573005a33618c3c67b401da490a865195173647bdcf621f8072c4489774a8ceb76c4eb382e375fdbc60ab1cd4fdb6cc165b12151',0),(41,1,'uri','scrypt:32768:8:1$1sABDe1h5de8xSJV$5c1b926bbb36d69275ef3e83bc05f92e98731938f956e6a9dc1cf5c8aa156b4b4a6065fb35cea766fc4ae6529be72595dd3d3607796549a7247ae6a232030c6e',0),(42,7,'admin2','scrypt:32768:8:1$zObLgaJs336ZJMYV$e2fb1d3a5968dd681ee515034339fd85110a6f0e9e6f43a9a62be5298cf81ca1143ef8aee4a4dcd35b4315ad27c64ec97bd715674a1215e01d4bbfba177aa56a',0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-06 19:41:31
