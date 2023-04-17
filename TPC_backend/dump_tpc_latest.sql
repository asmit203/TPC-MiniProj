-- MySQL dump 10.13  Distrib 8.0.32, for macos13.0 (arm64)
--
-- Host: localhost    Database: tpc_backend
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (2,'allView'),(1,'credit_manager');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,25),(2,1,26),(3,1,27),(4,1,28);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add credits',7,'add_credits'),(26,'Can change credits',7,'change_credits'),(27,'Can delete credits',7,'delete_credits'),(28,'Can view credits',7,'view_credits'),(29,'Can add company',8,'add_company'),(30,'Can change company',8,'change_company'),(31,'Can delete company',8,'delete_company'),(32,'Can view company',8,'view_company'),(33,'Can add alumni',9,'add_alumni'),(34,'Can change alumni',9,'change_alumni'),(35,'Can delete alumni',9,'delete_alumni'),(36,'Can view alumni',9,'view_alumni'),(37,'Can add student',10,'add_student'),(38,'Can change student',10,'change_student'),(39,'Can delete student',10,'delete_student'),(40,'Can view student',10,'view_student'),(41,'Can add applied',11,'add_applied'),(42,'Can change applied',11,'change_applied'),(43,'Can delete applied',11,'delete_applied'),(44,'Can view applied',11,'view_applied'),(45,'Can add job',12,'add_job'),(46,'Can change job',12,'change_job'),(47,'Can delete job',12,'delete_job'),(48,'Can view job',12,'view_job');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$FqpYtKPEv72JQj3nxXtRzW$9cm1iDAm5x90l6TCu2MvDmpH07oSubDTRcs0dlilAik=','2023-04-13 18:35:30.736967',1,'tpc','','','tpc_dev@gmail.com',1,1,'2023-04-12 22:20:18.479951'),(2,'pbkdf2_sha256$600000$bhAwpNIB0cYiGNcnOwL0Ie$A61SzgJaO+guauFqjYONc94xwsVoVrGgQUlnoYZ892E=',NULL,0,'creditmanager@iitp.ac.in','','','',1,1,'2023-04-17 12:16:06.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,2,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-04-12 23:09:16.553421','1','2023',1,'[{\"added\": {}}]',7,1),(2,'2023-04-12 23:10:05.533938','2','2023',1,'[{\"added\": {}}]',7,1),(3,'2023-04-12 23:22:15.270733','2101CS87','Asmit Ganguly',1,'[{\"added\": {}}]',10,1),(4,'2023-04-12 23:22:20.928797','2101CS87','Asmit Ganguly',2,'[]',10,1),(5,'2023-04-13 19:11:10.282671','2101CS23','randomperson',3,'',10,1),(6,'2023-04-14 07:15:54.583528','1','DIVIT AJMERA',1,'[{\"added\": {}}]',8,1),(7,'2023-04-14 07:18:49.466093','sde_001','sde_001',1,'[{\"added\": {}}]',12,1),(8,'2023-04-14 07:19:08.435772','sde_001','sde_001',2,'[{\"changed\": {\"fields\": [\"MinQual\"]}}]',12,1),(9,'2023-04-14 07:19:11.546886','sde_001','sde_001',2,'[]',12,1),(10,'2023-04-14 07:34:16.994729','1','Google_01',2,'[{\"changed\": {\"fields\": [\"SalaryPackage\"]}}]',8,1),(11,'2023-04-14 14:42:32.860671','3','2023 MNC',1,'[{\"added\": {}}]',7,1),(12,'2023-04-15 13:08:21.231943','2101CS87','Asmit Ganguly',2,'[{\"changed\": {\"fields\": [\"Resume\", \"Studprofilepic\"]}}]',10,1),(13,'2023-04-15 13:08:21.236466','2101CS87','Asmit Ganguly',2,'[{\"changed\": {\"fields\": [\"Resume\", \"Studprofilepic\"]}}]',10,1),(14,'2023-04-15 13:19:22.907586','2101CS87','Asmit Ganguly',2,'[{\"changed\": {\"fields\": [\"Resume\", \"Studprofilepic\"]}}]',10,1),(15,'2023-04-15 13:20:08.148367','2101CS87','Asmit Ganguly',2,'[{\"changed\": {\"fields\": [\"Resume\", \"Studprofilepic\"]}}]',10,1),(16,'2023-04-15 13:22:05.834811','2101CS87','Asmit Ganguly',2,'[]',10,1),(17,'2023-04-15 19:32:01.765228','1','True',1,'[{\"added\": {}}]',11,1),(18,'2023-04-17 04:57:47.131225','1921CS23','testalumni1',2,'[{\"changed\": {\"fields\": [\"Cid\", \"Batch\"]}}]',9,1),(19,'2023-04-17 05:59:15.843590','1921CS23','testalumni1',3,'',9,1),(20,'2023-04-17 06:00:21.244292','2023','2023',3,'',7,1),(21,'2023-04-17 06:00:21.247297','2023','2023',3,'',7,1),(22,'2023-04-17 06:00:21.248652','2023','2023',3,'',7,1),(23,'2023-04-17 06:00:28.170702','2023','2023',3,'',7,1),(24,'2023-04-17 06:00:28.172475','2023','2023',3,'',7,1),(25,'2023-04-17 06:00:28.173324','2023','2023',3,'',7,1),(26,'2023-04-17 06:16:11.276887','2023_CSE','2023_CSE',1,'[{\"added\": {}}]',7,1),(27,'2023-04-17 06:16:41.813134','2101CS87','ASMIT GANGULY',1,'[{\"added\": {}}]',10,1),(28,'2023-04-17 09:02:47.374454','NONE','NONE',1,'[{\"added\": {}}]',8,1),(29,'2023-04-17 09:04:28.493615','Google_01','Google_01',1,'[{\"added\": {}}]',8,1),(30,'2023-04-17 09:05:36.327396','other','other',2,'[{\"changed\": {\"fields\": [\"Cid\", \"Name\"]}}]',8,1),(31,'2023-04-17 09:05:53.304737','NONE','NONE',3,'',8,1),(32,'2023-04-17 09:07:34.051768','1900cs01','testalum',1,'[{\"added\": {}}]',9,1),(33,'2023-04-17 09:22:14.151529','1900cs01','testalum',2,'[{\"changed\": {\"fields\": [\"Email\", \"Password\"]}}]',9,1),(34,'2023-04-17 11:01:55.840166','2023_AIDS','2023_AIDS',1,'[{\"added\": {}}]',7,1),(35,'2023-04-17 11:02:17.029596','2023_MNC','2023_MNC',1,'[{\"added\": {}}]',7,1),(36,'2023-04-17 11:31:20.008141','1900cs02','testalum',2,'[{\"changed\": {\"fields\": [\"Roll no\", \"Cgpa\", \"M10\", \"M11\", \"M12\", \"Msem1\", \"Msem2\", \"Msem3\", \"Msem4\", \"Msem5\", \"Msem6\", \"Msem7\", \"Msem8\"]}}]',9,1),(37,'2023-04-17 11:31:26.036698','1900cs01','testalum',3,'',9,1),(38,'2023-04-17 11:31:36.589438','1900cs02','testalum',2,'[{\"changed\": {\"fields\": [\"Cid\", \"Cgpa\", \"M10\", \"M11\", \"M12\", \"Msem1\", \"Msem2\", \"Msem3\", \"Msem4\", \"Msem5\", \"Msem6\", \"Msem7\", \"Msem8\"]}}]',9,1),(39,'2023-04-17 11:34:18.054025','1900cs02','testalum',2,'[{\"changed\": {\"fields\": [\"Cgpa\", \"M10\", \"M11\", \"M12\", \"Msem1\", \"Msem2\", \"Msem3\", \"Msem4\", \"Msem5\", \"Msem6\", \"Msem7\", \"Msem8\"]}}]',9,1),(40,'2023-04-17 11:42:46.653139','1900cs02','(\'test alum\',)',2,'[{\"changed\": {\"fields\": [\"Email\", \"Cgpa\", \"M10\", \"M11\", \"M12\", \"Msem1\", \"Msem2\", \"Msem3\", \"Msem4\", \"Msem5\", \"Msem6\", \"Msem7\", \"Msem8\"]}}]',9,1),(41,'2023-04-17 11:46:31.095743','1900cs02','test alum',2,'[{\"changed\": {\"fields\": [\"Cid\", \"Batch\", \"Cgpa\", \"M10\", \"M11\", \"M12\", \"Msem1\", \"Msem2\", \"Msem3\", \"Msem4\", \"Msem5\", \"Msem6\", \"Msem7\", \"Msem8\"]}}]',9,1),(42,'2023-04-17 12:07:32.960076','1900_CSE','1900_CSE',1,'[{\"added\": {}}]',7,1),(43,'2023-04-17 12:09:10.485576','1','credit_manager',1,'[{\"added\": {}}]',3,1),(44,'2023-04-17 12:09:52.692542','1','credit_manager',2,'[]',3,1),(45,'2023-04-17 12:10:26.805749','2','allView',1,'[{\"added\": {}}]',3,1),(46,'2023-04-17 12:16:06.183754','2','creditmanager@iitp.ac.in',1,'[{\"added\": {}}]',4,1),(47,'2023-04-17 12:16:33.364427','2','creditmanager@iitp.ac.in',2,'[{\"changed\": {\"fields\": [\"Staff status\", \"Groups\"]}}]',4,1),(48,'2023-04-17 12:17:05.248420','2','allView',2,'[]',3,1),(49,'2023-04-17 12:17:17.628085','2','creditmanager@iitp.ac.in',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(11,'jobs','applied'),(12,'jobs','job'),(6,'sessions','session'),(9,'users','alumni'),(8,'users','company'),(7,'users','credits'),(10,'users','student');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-04-10 04:53:48.837812'),(2,'auth','0001_initial','2023-04-10 04:53:48.949836'),(3,'admin','0001_initial','2023-04-10 04:53:48.976874'),(4,'admin','0002_logentry_remove_auto_add','2023-04-10 04:53:48.980943'),(5,'admin','0003_logentry_add_action_flag_choices','2023-04-10 04:53:48.992094'),(6,'contenttypes','0002_remove_content_type_name','2023-04-10 04:53:49.012694'),(7,'auth','0002_alter_permission_name_max_length','2023-04-10 04:53:49.024416'),(8,'auth','0003_alter_user_email_max_length','2023-04-10 04:53:49.031339'),(9,'auth','0004_alter_user_username_opts','2023-04-10 04:53:49.034033'),(10,'auth','0005_alter_user_last_login_null','2023-04-10 04:53:49.045539'),(11,'auth','0006_require_contenttypes_0002','2023-04-10 04:53:49.046177'),(12,'auth','0007_alter_validators_add_error_messages','2023-04-10 04:53:49.048753'),(13,'auth','0008_alter_user_username_max_length','2023-04-10 04:53:49.063913'),(14,'auth','0009_alter_user_last_name_max_length','2023-04-10 04:53:49.077129'),(15,'auth','0010_alter_group_name_max_length','2023-04-10 04:53:49.083299'),(16,'auth','0011_update_proxy_permissions','2023-04-10 04:53:49.086229'),(17,'auth','0012_alter_user_first_name_max_length','2023-04-10 04:53:49.098294'),(18,'sessions','0001_initial','2023-04-10 04:53:49.106727'),(19,'users','0001_initial','2023-04-12 22:12:20.185246'),(20,'jobs','0001_initial','2023-04-12 22:12:20.224812'),(21,'users','0002_remove_student_specialization_alter_student_m10_and_more','2023-04-12 23:21:45.144093'),(22,'users','0003_alter_credits_batch_alter_credits_credits1_and_more','2023-04-13 18:52:04.052276'),(23,'users','0004_alter_student_resume','2023-04-13 18:52:08.228854'),(24,'users','0005_alter_company_minqual','2023-04-14 07:00:05.417666'),(25,'jobs','0002_job_minqual','2023-04-14 07:00:05.442676'),(26,'jobs','0003_job_flag_job','2023-04-14 07:01:14.758560'),(27,'jobs','0004_remove_job_minqual','2023-04-14 07:01:55.028603'),(28,'jobs','0005_job_minqual','2023-04-14 07:10:29.078742'),(29,'users','0006_remove_company_minqual','2023-04-14 14:35:49.997387'),(30,'users','0007_rename_rollnumber_alumni_roll_no','2023-04-14 14:50:41.136669'),(31,'users','0008_alter_alumni_cid','2023-04-14 15:07:34.194549'),(32,'users','0009_alter_alumni_batch_alter_alumni_branch_and_more','2023-04-14 15:09:43.017583'),(33,'jobs','0006_remove_applied_sid_alter_applied_roll_no','2023-04-14 15:35:17.048159'),(34,'users','0010_alumni_alumprofilepic_company_companypic_and_more','2023-04-14 15:40:08.860547'),(35,'users','0011_alter_student_studprofilepic','2023-04-15 19:22:28.500235'),(36,'users','0012_alter_alumni_alumprofilepic','2023-04-15 19:22:28.515981'),(37,'users','0013_remove_alumni_branch_alumni_cgpa_alter_alumni_batch','2023-04-17 04:54:39.513621'),(38,'users','0014_alter_student_cgpa','2023-04-17 05:40:58.902009'),(39,'users','0015_alter_student_cgpa_alter_student_m10_and_more','2023-04-17 05:43:46.722760');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0ta4j1lt4ma9ek1fiimutvjfk672hjq8','.eJxVjMsOgjAQRf-la9P0ZQdcGfd-A5kyRapQCC0LY_x3i2Gh23PuPS_W4Jr7Zk1-aQKxE5Ps8Msctg8fN0F3jLeJt1PMS3B8m_DdJn6dyA-XffsX6DH15Q0KKxAkqJaVlaq2SpJGYyyABLIgjs4Zjco6ZTQIoQ0BgUVfd7U2sivRby4_Z19yKa_kYy7UjxiGQjCNITdKCtmmCs4h5Jljy0Nk7w8rQUmQ:1pnL88:HWwssZoJ0Xh14jV4slIqZU7sgdJqRtC9tpFxjQf4qCI','2023-04-28 15:14:28.421908'),('kardq2u2yo88y50lijeapg489xbrhm6a','.eJxVjssOgjAURP-la0P6shdcGfd-A7nlFkGgJbQsiPHfLYaFbs_MnMyL1bimrl6jW-qe2IUJdvplFpvB-T2gJ_pHKJrg09LbYq8URxqLeyA33o7un6DD2OU1SCyBE6dKlEbIykhBCrU2AALIAD9bqxVKY6VWwLnSBAQGXdVWSos2S7-6tM0u65owzei3TN2E_ZjJFK9hTWMIQ744sfcHGcJGpw:1poR8B:1V4SlDh1aJLa-4I4YyJzKs2l3AL5y02Qx_3crv4UUjg','2023-05-01 15:51:03.201286');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_applied`
--

DROP TABLE IF EXISTS `jobs_applied`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs_applied` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `jid_id` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `roll_no_id` varchar(8) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jobs_applied_jid_id_6f868233_fk_jobs_job_jid` (`jid_id`),
  KEY `jobs_applied_roll_no_id_33ec97d7_fk_users_student_roll_no` (`roll_no_id`),
  CONSTRAINT `jobs_applied_jid_id_6f868233_fk_jobs_job_jid` FOREIGN KEY (`jid_id`) REFERENCES `jobs_job` (`jid`),
  CONSTRAINT `jobs_applied_roll_no_id_33ec97d7_fk_users_student_roll_no` FOREIGN KEY (`roll_no_id`) REFERENCES `users_student` (`roll_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_applied`
--

LOCK TABLES `jobs_applied` WRITE;
/*!40000 ALTER TABLE `jobs_applied` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobs_applied` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_job`
--

DROP TABLE IF EXISTS `jobs_job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs_job` (
  `cid_id` varchar(100) NOT NULL,
  `jid` varchar(100) NOT NULL,
  `jobTitle` varchar(100) NOT NULL,
  `jobDesc` longtext NOT NULL,
  `flag_job` tinyint(1) NOT NULL,
  `minQual` double NOT NULL,
  PRIMARY KEY (`jid`),
  KEY `jobs_job_cid_id_2b740f72_fk_users_company_cid` (`cid_id`),
  CONSTRAINT `jobs_job_cid_id_2b740f72_fk_users_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `users_company` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_job`
--

LOCK TABLES `jobs_job` WRITE;
/*!40000 ALTER TABLE `jobs_job` DISABLE KEYS */;
INSERT INTO `jobs_job` VALUES ('MS_ms_outlook_com','2','SDE0001','wqefjjguiwfg',1,8);
/*!40000 ALTER TABLE `jobs_job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_alumni`
--

DROP TABLE IF EXISTS `users_alumni`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_alumni` (
  `name` varchar(100) NOT NULL,
  `roll_no` varchar(8) NOT NULL,
  `cid_id` varchar(100) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `batch_id` varchar(10) NOT NULL,
  `cgpa` double DEFAULT NULL,
  `company` varchar(100) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  `m10` double DEFAULT NULL,
  `m11` double DEFAULT NULL,
  `m12` double DEFAULT NULL,
  `msem1` double DEFAULT NULL,
  `msem2` double DEFAULT NULL,
  `msem3` double DEFAULT NULL,
  `msem4` double DEFAULT NULL,
  `msem5` double DEFAULT NULL,
  `msem6` double DEFAULT NULL,
  `msem7` double DEFAULT NULL,
  `msem8` double DEFAULT NULL,
  `alumprofilepic` longtext,
  PRIMARY KEY (`roll_no`),
  KEY `users_alumni_cid_id_d9a794e6_fk_users_company_cid` (`cid_id`),
  KEY `users_alumni_batch_id_a5a47493_fk_users_credits_batch` (`batch_id`),
  CONSTRAINT `users_alumni_batch_id_a5a47493_fk_users_credits_batch` FOREIGN KEY (`batch_id`) REFERENCES `users_credits` (`batch`),
  CONSTRAINT `users_alumni_cid_id_d9a794e6_fk_users_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `users_company` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_alumni`
--

LOCK TABLES `users_alumni` WRITE;
/*!40000 ALTER TABLE `users_alumni` DISABLE KEYS */;
INSERT INTO `users_alumni` VALUES ('test alum','1900cs02','Google_01','test@g.com','asmitganguly','2023_CSE',9.72,'MS','SDE 01',95,95,95,8,8,8,8,8,8,8,8,'https://google.com');
/*!40000 ALTER TABLE `users_alumni` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_company`
--

DROP TABLE IF EXISTS `users_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_company` (
  `cid` varchar(100) NOT NULL,
  `reqCandDet` longtext NOT NULL,
  `marksCriteria` longtext NOT NULL,
  `salaryPackage` longtext NOT NULL,
  `mode_of_interview` varchar(50) NOT NULL,
  `time_of_start_iitp` longtext NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(100) NOT NULL,
  `companypic` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_company`
--

LOCK TABLES `users_company` WRITE;
/*!40000 ALTER TABLE `users_company` DISABLE KEYS */;
INSERT INTO `users_company` VALUES ('Google_01','Lorem ipsum is a placeholder or dummy text used in typesetting and graphic design for previewing layouts. It features scrambled Latin text, which emphasizes the design over content of the layout. It is the standard placeholder text of the printing and publishing industries','Lorem ipsum is a placeholder or dummy text used in typesetting and graphic design for previewing layouts. It features scrambled Latin text, which emphasizes the design over content of the layout. It is the standard placeholder text of the printing and publishing industries','10000000','Online_written','1900','Google','google_sde@gmail.com','googlecompany',''),('MS_ms_outlook_com','','','','','','MS','ms@outlook.com','asmitganguly',''),('other','NILL','NILL','NULL','Offine_interview','NULL','other','NONE@NONE.NONE','NONE','');
/*!40000 ALTER TABLE `users_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_credits`
--

DROP TABLE IF EXISTS `users_credits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_credits` (
  `batch` varchar(10) NOT NULL,
  `credits1` int DEFAULT NULL,
  `credits2` int DEFAULT NULL,
  `credits3` int DEFAULT NULL,
  `credits4` int DEFAULT NULL,
  `credits5` int DEFAULT NULL,
  `credits6` int DEFAULT NULL,
  `credits7` int DEFAULT NULL,
  `credits8` int DEFAULT NULL,
  PRIMARY KEY (`batch`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_credits`
--

LOCK TABLES `users_credits` WRITE;
/*!40000 ALTER TABLE `users_credits` DISABLE KEYS */;
INSERT INTO `users_credits` VALUES ('1900_CSE',10,11,11,11,11,11,11,11),('2023_AIDS',40,40,40,40,40,40,40,40),('2023_CSE',50,50,50,50,50,50,50,50),('2023_MNC',44,44,44,44,44,44,44,44);
/*!40000 ALTER TABLE `users_credits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_student`
--

DROP TABLE IF EXISTS `users_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_student` (
  `roll_no` varchar(8) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(100) NOT NULL,
  `batch_id` varchar(10) NOT NULL,
  `cgpa` longtext,
  `areaofInterest` longtext,
  `m10` longtext,
  `m11` longtext,
  `m12` longtext,
  `msem1` longtext,
  `msem2` longtext,
  `msem3` longtext,
  `msem4` longtext,
  `msem5` longtext,
  `msem6` longtext,
  `msem7` longtext,
  `msem8` longtext,
  `resume` varchar(100) DEFAULT NULL,
  `studprofilepic` longtext,
  PRIMARY KEY (`roll_no`),
  KEY `users_student_batch_id_e8543593_fk_users_credits_batch` (`batch_id`),
  CONSTRAINT `users_student_batch_id_e8543593_fk_users_credits_batch` FOREIGN KEY (`batch_id`) REFERENCES `users_credits` (`batch`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_student`
--

LOCK TABLES `users_student` WRITE;
/*!40000 ALTER TABLE `users_student` DISABLE KEYS */;
INSERT INTO `users_student` VALUES ('2101CS87','Asmit Ganguly','asmit_2101cs87@iitp.ac.in','asmitganguly','2023_CSE','9.72','sdhhdlivhlekdfiehfleh','95','95','95','8','8','8','8','8','8','8','8','','https://google.com');
/*!40000 ALTER TABLE `users_student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-17 22:42:11
