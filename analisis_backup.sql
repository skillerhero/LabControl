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
  `ana_nombre` varchar(50) COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT '',
  `ana_costo` decimal(20,2) NOT NULL DEFAULT '0.00',
  `ana_sta` char(50) COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT 'A',
  PRIMARY KEY (`ana_id`),
  KEY `FK_analisis_1` (`ana_area_id_fk`)
) ENGINE=InnoDB AUTO_INCREMENT=185 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci COMMENT='tabla donde se guardan los analisis\r\n';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analisis`
--

LOCK TABLES `analisis` WRITE;
/*!40000 ALTER TABLE `analisis` DISABLE KEYS */;
INSERT INTO `analisis` VALUES (1,1,'Ácido Úrico en orina 24H',95.00,'A'),(2,1,'Ácido Úrico en suero (líquido sinovial)',95.00,'A'),(3,1,'Amiba en fresco',69.00,'A'),(4,1,'Amilasa',110.00,'A'),(5,3,'Anfetaminas Semicuantitativo',129.00,'A'),(6,3,'Anfetaminas Cualitativo',52.00,'A'),(7,3,'Anticuerpos anti-Dengue IgG/IgM',345.00,'A'),(8,3,'Anticuerpos anti-HBsAg',181.00,'A'),(9,3,'Anticuerpos anti-HCV',181.00,'A'),(10,3,'Anticuerpos anti HIV 1 y 2',190.00,'A'),(11,3,'Anticuerpos Anti-HIV 1 y 2 / Antígeno p24',560.00,'A'),(12,3,'Anticuerpos Sars-Cov2 IgG e IgM Cualitativos (Entr',302.00,'A'),(13,3,'Antidoping 3 (Anfetamina, marihuana, cocaína) (Sem',388.00,'A'),(14,3,'Antidoping 3 (Anfetamina, marihuana, cocaína) (Cua',156.00,'A'),(15,3,'Antidoping 5 (Anfetamina, marihuana, cocaína, barb',646.50,'A'),(16,3,'Antidoping 6 (Anfetamina, marihuana, cocaína, barb',776.00,'A'),(17,3,'Antidoping 6 (Anfetamina, marihuana, cocaína, barb',312.00,'A'),(18,3,'Antigeno COVID (entrega en 1 hora)*',388.00,'A'),(19,3,'Antígeno de Dengue virus NS1',302.00,'A'),(20,3,'Antígeno para Influenza A Y B',431.00,'A'),(21,3,'Antígeno Prostático Específico (PSA)',215.50,'A'),(22,1,'Azúcares reductores',69.00,'A'),(23,1,'Azul de metileno (moco fecal)',60.00,'A'),(24,4,'BAAR',95.00,'A'),(25,4,'BAAR (2 Muestras)',129.00,'A'),(26,4,'BAAR (3 muestras)',237.00,'A'),(27,4,'BAAR (5 muestras)',315.00,'A'),(28,4,'Bacterioscópico (Gram)',86.00,'A'),(29,3,'Barbitúricos en orina semicuantitativo',129.00,'A'),(30,3,'Barbitúricos semicualitativa',52.00,'A'),(31,3,'Benzodiacepina cualitativa',52.00,'A'),(32,3,'Benzodiacepina en orina semicuantitativa',129.00,'A'),(33,1,'Bilirrubina',78.00,'A'),(34,2,'Biometría Hemática',112.00,'A'),(35,1,'Búsqueda de helmintos: aguas, lixiviados',388.00,'A'),(36,1,'Calcio en orina (24 hrs)',129.00,'A'),(37,1,'Calcio en suero',86.00,'A'),(38,3,'Cannabinoides \"Marihuana\" semicuantitativo',129.00,'A'),(39,3,'Cannabinoides \"Marihuana\" cualitativo',52.00,'A'),(40,5,'Cinética de hierro. (capacidad de fijación de Hier',474.00,'A'),(41,1,'Cloro en orina',73.00,'A'),(42,1,'Cloro en sangre',86.00,'A'),(43,3,'Cocaína Metabólico semicuantitativo',129.00,'A'),(44,3,'Cocaína Metabólico cualitativo',52.00,'A'),(45,1,'Colesterol de alta Densidad HDL-CHOL',78.00,'A'),(46,1,'Colesterol de baja Densidad LDL-CHOL',78.00,'A'),(47,1,'Colesterol de muy baja Densidad VLDL-CHOL',78.00,'A'),(48,1,'Colesterol total',60.00,'A'),(49,2,'Coombs Directo',142.00,'A'),(50,1,'Coprológico General',155.00,'A'),(51,1,'Coproparasitoscópico',69.00,'A'),(52,1,'Coproparasitoscópico (2 muestras)',129.00,'A'),(53,1,'Coproparasitoscópico + sangre oculta',129.00,'A'),(54,1,'Coproparasitoscópico (3 muestras)',190.00,'A'),(55,1,'Creatinina',52.00,'A'),(56,1,'Creatinina en orina',52.00,'A'),(57,4,'Cultivo Bacteriológico',478.50,'A'),(58,4,'Cultivo Bacteriológico CMI',681.00,'A'),(59,4,'Cultivo de Anaeróbios',474.00,'A'),(60,4,'Cultivo de BAAR Identificación de la cepa. En caso',884.00,'A'),(61,4,'Cultivo de BAAR sin Antibiograma',409.50,'A'),(62,4,'Cultivo de Esperma',478.50,'A'),(63,4,'Cultivo de Expectoración',478.50,'A'),(64,4,'Cultivo de Expectoración. CMI',685.00,'A'),(65,4,'Cultivo de Exudado Cérvico Vaginal',478.50,'A'),(66,4,'Cultivo de Exudado Cérvico Vaginal. CMI',685.00,'A'),(67,4,'Cultivo de Exudado Faríngeo',478.50,'A'),(68,4,'Cultivo de Exudado Faríngeo: CMI',681.00,'A'),(69,4,'Cultivo de Heces',478.50,'A'),(70,4,'Cultivo de Heces. CMI',685.00,'A'),(71,4,'Cultivo de Orina',478.50,'A'),(72,4,'Cultivo de Orina. CMI',685.00,'A'),(73,4,'Cultivo de Sangre',1039.00,'A'),(74,4,'Cultivo de Sangre. CMI',1039.00,'A'),(75,4,'Cultivo de Secreción',422.00,'A'),(76,4,'Cultivo de Secreción. CMI',681.00,'A'),(77,4,'Cultivo de Superficie inertes',409.50,'A'),(78,4,'Cultivo de superficie vivas',478.50,'A'),(79,4,'Cultivo Micológico. CMI para levadura',681.00,'A'),(80,3,'Dengue Combo DUO - IgG/IgM + NS1',388.00,'A'),(81,1,'Depuración de Creatinina',129.00,'A'),(82,1,'Deshidrogenasa Láctica DHL',95.00,'A'),(83,3,'Dimero D',422.00,'A'),(84,1,'Electrolitos en Orina (Na, K, Cl)',129.00,'A'),(85,1,'Electrolitos Sérico (Na, K, Cl)',129.00,'A'),(86,1,'Electrolitos Sérico (Na, K, Cl, Ca, Mg, P)',259.00,'A'),(87,2,'Eosinófilos en moco nasal',103.50,'A'),(88,1,'Espermatobioscopia',431.00,'A'),(89,3,'Estradiol (E2)',172.00,'A'),(90,3,'Estradiol libre',158.00,'A'),(91,1,'Examen general de orina (EGO)',86.00,'A'),(92,3,'Factor reumatoide',69.00,'A'),(93,3,'Ferritina',215.50,'A'),(94,2,'Fibrinógeno',142.00,'A'),(95,2,'Fórmula Blanca',86.00,'A'),(96,2,'Fórmula Roja',86.00,'A'),(97,1,'Fosfatasa Alcalina',73.00,'A'),(98,1,'Fósforo sérico',86.00,'A'),(99,1,'Gamma glutamil transpeptidasa (GGT)',73.00,'A'),(100,1,'Glucosa',52.00,'A'),(101,1,'Glucosa en orina',52.00,'A'),(102,1,'Glucosa Post-Carga (3 determinaciones)',589.00,'A'),(103,1,'Glucosa Post-prandial',86.00,'A'),(104,3,'Gonadotrofinas Hipofisiarias. LH, FSH',259.00,'A'),(105,2,'Grupos Sanguineos y Rh',103.50,'A'),(106,1,'Hemoglobina Glucosilada A1c',215.50,'A'),(107,3,'Hierro Sérico',78.00,'A'),(108,3,'Hierro Sérico y Capacidad de fijación',207.00,'A'),(109,3,'Hormonas de Crecimiento',215.50,'A'),(110,3,'Hormona Folículo Estimulante FSH',159.50,'A'),(111,3,'Hormona Luteinizante LH',142.00,'A'),(112,3,'Hormona Tiroideo Estimulante TSH',103.50,'A'),(113,1,'Identificación de parásitos Remitidos',129.00,'A'),(114,3,'Indice de Tiroxina Libre',250.00,'A'),(115,3,'Insulina',238.50,'A'),(116,1,'Investigación de Cryptosporidium sp.',129.00,'A'),(117,1,'Isospora Belli y Cyclospora cayetanensis',483.00,'A'),(118,1,'Lipasa',110.00,'A'),(119,1,'Lípidos Totales',78.00,'A'),(120,1,'Magnesio en orina',315.00,'A'),(121,1,'Magnesio sérico',86.00,'A'),(122,3,'Metanfetamina cualitativo',52.00,'A'),(123,3,'Metanfetamina semicuantitativo',129.00,'A'),(124,1,'Nitrógeno Ureico',65.00,'A'),(125,1,'Nitrógeno Ureico en orina de 24 hrs',65.00,'A'),(126,3,'Opiáceos semicuantitativos',129.00,'A'),(127,3,'Opiáceos cualitativo',52.00,'A'),(128,5,'PCR COVID (entrega en 24/48 hrs)*',1364.00,'A'),(129,5,'PCR COVID express (entrega el mismo día)*',2155.00,'A'),(130,5,'PCR COVIFLU (influenza/covid entrega en 24/48 hrs)',2500.00,'A'),(131,1,'PH y azúcar reductores',82.00,'A'),(132,2,'Plaquetas',69.00,'A'),(133,1,'Potasio en Orina',86.00,'A'),(134,1,'Potasio en sangre',86.00,'A'),(135,3,'Progesterona',134.00,'A'),(136,3,'Prolactina',134.00,'A'),(137,3,'Proteína C Reactiva (PCR)',69.00,'A'),(138,1,'Proteínas en orina 24 H',103.50,'A'),(139,1,'Proteínas Totales Relación A/G',82.00,'A'),(140,3,'Prueba de embarazo cuantitativa (Sub unidad Beta)',315.00,'A'),(141,5,'Prueba de embarazo cualitativa (Sub unidad Beta)',129.00,'A'),(142,3,'Reacciones Febriles',129.00,'A'),(143,2,'Reticulocitos',65.00,'A'),(144,3,'Rotavirus',259.00,'A'),(145,2,'Sedimentación Globular ó VSG ó Eritrosedimentación',65.00,'A'),(146,5,'Sodio en orina',86.00,'A'),(147,1,'Sodio en sangre',86.00,'A'),(148,3,'T3 Captación',103.50,'A'),(149,3,'T3 Libre',103.50,'A'),(150,3,'T3 Triyodotironina total',103.50,'A'),(151,3,'T4 Tiroxina libre',103.50,'A'),(152,3,'T4 Tiroxina Total',103.50,'A'),(153,3,'Testosterona',174.20,'A'),(154,3,'Testosterona libre',166.50,'A'),(155,2,'Tiempo de coagulación recalcificación de plasma',60.00,'A'),(156,2,'Tiempo de Protrombina',86.00,'A'),(157,2,'Tiempo de Sangrado',65.00,'A'),(158,2,'Tiempo de sangrado y Coagulación',78.00,'A'),(159,2,'Tiempo de tromboplastina parcial',86.00,'A'),(160,1,'Tolerancia a la glucosa 2h.',155.00,'A'),(161,1,'Tolerancia a la glucosa 3h.',207.00,'A'),(162,1,'Tolerancia a la glucosa 4h.',259.00,'A'),(163,1,'Transaminasa G. Oxalacetica (TGO/AST)',60.00,'A'),(164,1,'Transaminasa G. Piruvuca (TGP/ALT)',60.00,'A'),(165,1,'Triglicéridos',65.00,'A'),(166,1,'Urea en líquido de Diálisis',65.00,'A'),(167,1,'Urea en orina',65.00,'A'),(168,1,'Urea Sérica',52.00,'A'),(169,3,'VDRL',69.00,'A'),(170,3,'Vitamina D total (OH) 25 (D2+D3)',517.00,'A'),(171,1,'Índice Aterogénico',0.00,'O'),(172,1,'Prueba',10.00,'O'),(176,1,'Aaaa',45.00,'O'),(177,1,'Aaa',1.00,'O'),(178,1,'A',1.00,'O'),(179,1,'Prueba1',22.00,'O'),(180,1,'Testest',111.00,'O'),(183,1,'assa',0.00,'A'),(184,1,'asd',0.00,'A');
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
  `area_nombre` varchar(50) COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT '',
  `area_sta` char(1) COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT 'A',
  PRIMARY KEY (`area_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `areas`
--

LOCK TABLES `areas` WRITE;
/*!40000 ALTER TABLE `areas` DISABLE KEYS */;
INSERT INTO `areas` VALUES (1,'Urianálisis/QS','A'),(2,'Hematología','A'),(3,'Serología/Hormonas','A'),(4,'Bacteriología','A'),(6,'Recepción','A'),(7,'Admin','A'),(16,'Prueba','A');
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
  `des_nombre` varchar(50) COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT '',
  `des_dsc` varchar(255) COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT '',
  `des_sta` char(1) COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT 'A',
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
  `grupo_nombre` varchar(50) COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT '',
  `grupo_sta` char(1) COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT 'A',
  `grupo_costo` decimal(20,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (`grupo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci COMMENT='tabla para los nombre de los grupos';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grupos`
--

LOCK TABLES `grupos` WRITE;
/*!40000 ALTER TABLE `grupos` DISABLE KEYS */;
INSERT INTO `grupos` VALUES (1,'Perfil Hepático con TP','A',461.00),(2,'Perfil Hepático sin TP','A',383.40),(3,'Perfil de Lípidos','A',345.00),(4,'Perfil Óseo I','A',259.00),(5,'Perfil Ovárico','A',733.00),(6,'Perfil Ovarico conTSH','A',819.00),(7,'Perfil Renal','A',560.00),(8,'Perfil Reúmatico','A',474.00),(9,'Perfil Rotavirus','A',418.00),(10,'Perfil Tiroideo I de 5 determinaciones','A',534.50),(11,'Perfil Tiroideo II de 3 determinaciones','A',284.50),(12,'Perfil Veterinario I','A',276.00),(13,'Perfil Veterinario II','A',310.00),(14,'Perfil Veterinario III','A',379.00),(15,'Perfil Veterinario IV','A',534.50),(16,'Química Sanguínea de 3 determinaciones','A',142.00),(17,'Química Sanguínea de 4 determinaciones','A',172.00),(18,'Química Sanguínea de 6 determinaciones','A',237.00),(19,'Química Sanguínea de 18 determinaciones','A',448.00),(20,'Química Sanguínea de 20 determinaciones','A',534.50),(21,'Química Sanguínea de 24 determinaciones','A',672.00),(22,'Química Sanguínea de 27 determinaciones','A',686.00),(23,'Química Sanguínea de 35 determinaciones','A',1250.00),(25,'prueba','O',1.00),(26,'Pruebaa','O',1.00),(27,'test','A',1.00),(28,'test222','A',1.00),(29,'aaaaaaaa','A',11111.00),(30,'test555','A',21.00);
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
INSERT INTO `grupos_analisis_rel` VALUES (1,33),(1,97),(1,99),(1,139),(1,156),(1,163),(1,164),(2,33),(2,97),(2,99),(2,139),(2,163),(2,164),(3,45),(3,46),(3,47),(3,48),(3,119),(3,165),(3,171),(4,36),(4,97),(4,98),(4,139),(5,89),(5,110),(5,111),(5,135),(5,136),(6,89),(6,110),(6,111),(6,112),(6,135),(6,136),(8,2),(8,92),(8,97),(8,137),(8,145),(10,112),(10,149),(11,112),(12,34),(12,97),(12,164),(13,34),(13,97),(13,164),(14,34),(14,91),(14,97),(14,139),(14,164),(15,34),(15,87),(15,91),(15,139),(15,164),(18,48),(18,165);
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
  `mediciones_analisis_componente` varchar(50) COLLATE utf8mb4_spanish_ci DEFAULT '',
  `mediciones_analisis_unidad` varchar(50) COLLATE utf8mb4_spanish_ci DEFAULT '',
  `mediciones_analisis_rango` varchar(50) COLLATE utf8mb4_spanish_ci DEFAULT '',
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
  `muan_sta` char(1) COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT 'A',
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
  `mues_sta` char(1) COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT 'A',
  `mues_alta_fec` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `mues_folio` char(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT '0',
  `mues_nombre` varchar(80) COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT '',
  `mues_apellido_paterno` varchar(80) COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT '',
  `mues_apellido_materno` varchar(80) COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT '',
  `mues_calle` varchar(80) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT '',
  `mues_num_ext` char(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT '',
  `mues_num_int` char(8) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT '',
  `mues_colonia` varchar(80) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT '',
  `mues_tel` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci DEFAULT '',
  `mues_email` varchar(80) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `mues_horas_ayuno` int DEFAULT '0',
  `mues_alimentos` varchar(1024) COLLATE utf8mb3_spanish_ci DEFAULT '',
  `mues_enfermedades` varchar(1024) COLLATE utf8mb3_spanish_ci DEFAULT '',
  `mues_medicamentos` varchar(1024) COLLATE utf8mb3_spanish_ci DEFAULT '',
  `mues_rubrica` varchar(80) COLLATE utf8mb3_spanish_ci DEFAULT '',
  `mues_edad` int unsigned DEFAULT '0',
  `mues_fec_nac` datetime DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`mues_id`),
  KEY `mues_des_id_fk` (`mues_des_id_fk`),
  CONSTRAINT `muestras_ibfk_1` FOREIGN KEY (`mues_des_id_fk`) REFERENCES `descuentos` (`des_id`)
) ENGINE=InnoDB AUTO_INCREMENT=140 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci COMMENT='Tabla donde se guardan los datos de las muestras';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `muestras`
--

LOCK TABLES `muestras` WRITE;
/*!40000 ALTER TABLE `muestras` DISABLE KEYS */;
INSERT INTO `muestras` VALUES (134,1,'O','2024-03-13 22:06:58','1DZ1DIEKP803PDWZ0XGC','rafael','leon','estrada','calle','1','','colonia','1122334455','rafael@hotmail.com',3,'Ninguno','Ninguna','Ninguno',NULL,20,'2003-12-14 00:00:00'),(135,2,'F','2024-03-13 22:08:23','L4LFISOT6BHZJRY0R728','danna','medina','bolaños','calle','123','','ca','1234565780','q@q',3,'Ninguno','Ninguna','Ninguno',NULL,31,'1993-03-12 00:00:00'),(137,1,'O','2024-03-13 23:37:47','OQ6DJK04Y18LD627WE3Y','yessenia','carbajal','armenta','calle','123','','colonia','1234565780','danna@danna',3,'Ninguno','Ninguna','Ninguno',NULL,30,'1993-12-19 00:00:00'),(138,3,'O','2024-03-14 09:25:33','X37OGGVVLRP6A77084ZE','Pedro','Perez','Mendoza','Calle avenida','123','','Aves del paraíso','1122334455','rafa@hotmail.com',8,'','Ninguna','Ninguno',NULL,30,'1993-12-19 00:00:00'),(139,1,'F','2024-03-14 09:26:35','XBY2CNYG45RCJAZHIR8W','Ignacio','Martinez','Rodriguez','Avenida san gilberto','1311','','Aves del paraíso','3323403259','rafa@hotmail.com',3,'Ninguno','Ninguna','Ninguno',NULL,28,'1995-12-12 00:00:00');
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
  `per_nombre` varchar(50) COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT '',
  `per_sta` char(1) COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT 'A',
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
) ENGINE=InnoDB AUTO_INCREMENT=467 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resultados`
--

LOCK TABLES `resultados` WRITE;
/*!40000 ALTER TABLE `resultados` DISABLE KEYS */;
INSERT INTO `resultados` VALUES (433,3,91,134,'0000-00-00',NULL,NULL,'O'),(434,4,91,134,'0000-00-00',NULL,NULL,'O'),(435,5,91,134,'0000-00-00',NULL,NULL,'O'),(436,6,91,134,'0000-00-00',NULL,NULL,'O'),(437,7,91,134,'0000-00-00',NULL,NULL,'O'),(438,8,33,135,'2024-03-13',0.5,1,'F'),(439,9,97,135,'2024-03-13',55,0,'F'),(440,10,99,135,'2024-03-13',30,0,'F'),(441,11,139,135,'2024-03-13',9,1,'F'),(442,12,156,135,'2024-03-13',12,0,'F'),(443,13,163,135,'2024-03-13',45,1,'F'),(444,14,164,135,'2024-03-13',10,0,'F'),(445,3,91,136,'0000-00-00',NULL,NULL,'O'),(446,4,91,136,'0000-00-00',NULL,NULL,'O'),(447,5,91,136,'0000-00-00',NULL,NULL,'O'),(448,6,91,136,'0000-00-00',NULL,NULL,'O'),(449,7,91,136,'0000-00-00',NULL,NULL,'O'),(450,3,91,137,'0000-00-00',NULL,NULL,'O'),(451,4,91,137,'0000-00-00',NULL,NULL,'O'),(452,5,91,137,'0000-00-00',NULL,NULL,'O'),(453,6,91,137,'0000-00-00',NULL,NULL,'O'),(454,7,91,137,'0000-00-00',NULL,NULL,'O'),(455,3,91,138,'0000-00-00',NULL,NULL,'O'),(456,4,91,138,'0000-00-00',NULL,NULL,'O'),(457,5,91,138,'0000-00-00',NULL,NULL,'O'),(458,6,91,138,'0000-00-00',NULL,NULL,'O'),(459,7,91,138,'0000-00-00',NULL,NULL,'O'),(460,8,33,139,'2024-03-14',0.5,0,'F'),(461,9,97,139,'2024-03-14',280,1,'F'),(462,10,99,139,'2024-03-14',33,0,'F'),(463,11,139,139,'2024-03-14',8,0,'F'),(464,12,156,139,'2024-03-14',12,0,'F'),(465,13,163,139,'2024-03-14',10,0,'F'),(466,14,164,139,'2024-03-14',8,0,'F');
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
  `user_username` varchar(50) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `user_password` text COLLATE utf8mb3_spanish_ci,
  `user_perfil_id_fk` int unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,0,'admin2','pbkdf2:sha256:260000$2r2Lf5oWH84UD2OR$0cbc096ef50d9b624381a063d3e747cbe92069fc7aaac9832dbb040fef136677',0),(6,7,'admin','scrypt:32768:8:1$mLnG1rhvsFGIg05T$0d03cae4de979350eb39e06031232b2065234cc28983bb2fddc307c3b9a3d6554624a253111a183984f2d33d92c7d7f7c85c72b736fdcb97248bbaa02e000b6a',0),(7,2,'rafa','scrypt:32768:8:1$Kh4zalGP0w8OiwxU$309f7eefe8d24fc985d8e58cb0811d7decf94d68d201548ec6ff851c3c6afcc4f8123f274ef6407a5554f5c8898c5dffc496935b2082795fc6e63a043de1153d',0),(8,5,'rafa2','scrypt:32768:8:1$dtIzay0encUe3Gc6$0159ff6502ea3eb0180a4812b7b965f6e400492489551b5c52181224f1cf80fc8d3f56196d3dfc491edbb4049c6aee02cbed04849481fcf7c976238f875ad6fb',0),(9,7,'danna','pbkdf2:sha256:260000$yFksAwExQWFqeGLD$30ef1856af7524d7490ebf8b8b6d8324a263f43b46159aa3d5de744362d920a0',0),(10,4,'da','pbkdf2:sha256:260000$IZu7VeMwRtTGGJY4$4d277948e4eadbf657bc1bc6443ec2f09b6b3f606b2fd5fed885cf42df81244a',0),(11,2,'dan','pbkdf2:sha256:260000$OUWjWdUhOEz60wzJ$09d00fac64b2e1a9826a34eb78b2760a4e021419dce64766ffb089aa37dea8bd',0),(12,1,'dada','pbkdf2:sha256:260000$lKL4SiWKG2YD1Vx1$e81e5e857a24dec143b3009998df43d9b337b8f26ac595eb7d06952f959a0d38',0),(15,4,'abc','scrypt:32768:8:1$mqngXtCYWPX8XJmo$af89e24963922ac86a5e2f1b84b43d1c066fb038a7b39c764ef3a4f8f74cadd54f9bd271f8b1eca415826681c30c7e567807ccdff54ec54f1ea2ad79b952f566',0),(16,6,'yessrecepcion','scrypt:32768:8:1$qNF8WmS8bPIqZji7$609d613588b2d7568bf4d3c4b4225760e92aa8be42a13404a04a1a724fb05467ece09492a1a608148b60ed7ab3b1c65e8df3e11055e3cb6d795f6a521d1e777c',0),(17,7,'20310238','scrypt:32768:8:1$Ei0QH7VFM2hKk6qd$5232c45ca252cdc50cf9546ee6d5b4f52c07cb624956b472d15033a9aee158ee72d2cc8f5c9af3c5f8a7a3f98ee29c01bfcc35ab3763beeec2c07167c0065f67',0),(18,1,'test','scrypt:32768:8:1$trE69stHIHwVqf2I$73250dacdb36338d8f2d6081e480eae9922637b3576277c4f985eeed6952d6484ec684fd64c587f36d1cbf083bd22a5a64401a8ff1a9d4947a13e6c2017caa9d',0),(19,2,'test2','scrypt:32768:8:1$WMhmoiDlfd1n3eUh$003a79baa093f556dac922b71b287fbd93dfd85799d7c635edd11817e04ac67ef7fd6c13f9b9475d6edec4f6eaa450b8bd93641ec03bf386d9eb605450959623',0),(20,6,'recepcion','scrypt:32768:8:1$QhuHXrLLh56UD22H$77dd40babc3c2e08b9ca0306f6756432410d5beafae8407e820e8cea56a6410eeba31d497e133b39000bc1d30b2392300a2e3124b77839437171bdeb6714fa6f',0),(21,2,'hematologia','scrypt:32768:8:1$T3Bz0GRaSipwVpNG$905312db37e424727c17b09adba5e2f7448c5d58f9d73dd41890a962c4bd41606558166ae6f57f78b2b26da6b132d6ed19c72b1b724055a833bfff84667d488e',0),(22,1,'prueba','scrypt:32768:8:1$UVW2iBMbSOnWIzHn$1a95a6829c7ac8098eda3a58e5b5898cbd61164eee6669929178757a05b9cb017a6491ab6cc7352a6fb7db642be8868e3a520abd37d4e966bb19adcfdbbe2f87',0),(23,3,'serologia','scrypt:32768:8:1$V7xMAHpazc5MBJOW$47551bb0cb767f3a4807753edaaf8be52a6b479454b6e4f1393ff76df70ea312d4a5b9a517b25e8e0f6a0d08deb83c44bec2ee74b9b438615d9c97479f0be799',0),(24,1,'uri','scrypt:32768:8:1$cQbYoKq37JAZkBxq$bd568b4dd2d9e83d650c661c14b4f7caa6d478590e5ed66357a8dadeada61ca4884c2d64f662e960aa546987ce2daa968e03fb13a9781ba5759e03222be3acfb',0),(25,4,'bacteria','scrypt:32768:8:1$6TA5wXYmYpfeYzda$d7856f0342e60c6123011e2a00c244017f8556e2f8f69b3189662b63f60367bfde924836dbbfd97c3ef9be98e5f225d2273e3a41bf87b88a925503c8eb4a9383',0),(26,3,'hormona','scrypt:32768:8:1$cX8z4f2USdF37EGP$3671dfc8178c8da5e354ee06bbcc06eec0cd5ff819bff7e7df76f25fc1ed20f32516c046054c5cfb10eb3b41c28868367ff1625b0f4300613a6422ae9ede1bc1',0),(27,7,'hola','scrypt:32768:8:1$rLeHKOROlf7H0H41$7d567401861fab6df6d6c1d4490a8ea771b1b10511df51892fc9f4a8b360b470d6b09e69b6bdfffce3a7d3a14d86020071a1c2af4969595ec2142d8fa0967f25',0),(28,1,'dana','pbkdf2:sha256:260000$RmZtEE733x9M4Ugy$befcec5e285641125639a7632de65ba618bf0e8a4c389aea873d6181843288f5',0),(29,6,'ola','scrypt:32768:8:1$feuR8509jYWt80Z8$8674e22234f26e54e13bde9c18461eb931ed8a8f8c6d6b19d7f56798a9ab3e5138760ebfc4a181dfef7db683f5e3e4b8cc3f1e25b976161f18ad0254a88fbfad',0),(30,1,'uri2','scrypt:32768:8:1$hwFUCO7Gexc338sI$16b47164087e76ffe4b18fa477a6d6f5f6ca9c218d52834a9290df2af1bc2ea15fdb9a5d6ff5694822ef8968c222fa55b1dcb901ddea77b833a5cfe745e2b142',0),(31,7,'admin3','pbkdf2:sha256:260000$aoqt94T9GWaucVC0$a3353d9a053e6eeb72d588afc9ce1abfb9da8287229d75a2b1252a2144a73f8f',0),(32,6,'pepito','scrypt:32768:8:1$sJ9q2JitcLW3giDD$f325e0d8aa1e89311f82b511cc4c85768d406336e96e14594b5042b3111643f12db4411620497be19f0ed407a1afe1e3d173339c76ce74db6d0ab13bb9fffa69',0),(33,6,'juan','scrypt:32768:8:1$PAtpq6NrhpCNpw8z$4187de933d39f9fab57a272eed44bf9858bc0fc3631259952063e39ba7694a29dd7bb6995c058e58122ed8d45473d143e86f5969c4fdd02dee56417c338db5d7',0),(34,2,'juanito','scrypt:32768:8:1$SVBZHxckpNl8Qakl$3286e4076c5e927d6af455b1fba3a36688fa2ecffc9fbc40e379fd19bad9e34082653ce35d5fddc66101dad48f5e8b007902ae74e1d42ce9a00158b7a21d4847',0),(35,1,'mario','scrypt:32768:8:1$7ptfwsHa3IO0d3uK$5db90c77bef0b30ab29edb68a7da2313cd71caf0413c06e6e41e003dcedd8a0eca193a92c3951df5980179ea8e87533cd07e2f691db7fe023f82826585391165',0),(36,1,'jessica','scrypt:32768:8:1$gfukLuKapknoz5f3$badb7ead5e053d84d1f5e400f91ac7130e3001739b754f5195f5678cf6d8338786ffd20e45ae5c2cb23c0ec3c745e3a32c6e53d1c59ad78de9440d4675421d62',0);
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

-- Dump completed on 2024-04-15 21:36:50
