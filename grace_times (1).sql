-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 18, 2023 at 10:13 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `grace_times`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add idgen', 7, 'add_idgen'),
(26, 'Can change idgen', 7, 'change_idgen'),
(27, 'Can delete idgen', 7, 'delete_idgen'),
(28, 'Can view idgen', 7, 'view_idgen'),
(29, 'Can add tbl_category', 8, 'add_tbl_category'),
(30, 'Can change tbl_category', 8, 'change_tbl_category'),
(31, 'Can delete tbl_category', 8, 'delete_tbl_category'),
(32, 'Can view tbl_category', 8, 'view_tbl_category'),
(33, 'Can add tbl_shope', 9, 'add_tbl_shope'),
(34, 'Can change tbl_shope', 9, 'change_tbl_shope'),
(35, 'Can delete tbl_shope', 9, 'delete_tbl_shope'),
(36, 'Can view tbl_shope', 9, 'view_tbl_shope'),
(37, 'Can add tbl_product', 10, 'add_tbl_product'),
(38, 'Can change tbl_product', 10, 'change_tbl_product'),
(39, 'Can delete tbl_product', 10, 'delete_tbl_product'),
(40, 'Can view tbl_product', 10, 'view_tbl_product'),
(41, 'Can add tbl_coustomer', 11, 'add_tbl_coustomer'),
(42, 'Can change tbl_coustomer', 11, 'change_tbl_coustomer'),
(43, 'Can delete tbl_coustomer', 11, 'delete_tbl_coustomer'),
(44, 'Can view tbl_coustomer', 11, 'view_tbl_coustomer'),
(45, 'Can add tbl_login', 12, 'add_tbl_login'),
(46, 'Can change tbl_login', 12, 'change_tbl_login'),
(47, 'Can delete tbl_login', 12, 'delete_tbl_login'),
(48, 'Can view tbl_login', 12, 'view_tbl_login'),
(49, 'Can add tbl_review', 13, 'add_tbl_review'),
(50, 'Can change tbl_review', 13, 'change_tbl_review'),
(51, 'Can delete tbl_review', 13, 'delete_tbl_review'),
(52, 'Can view tbl_review', 13, 'view_tbl_review'),
(53, 'Can add tbl_order', 14, 'add_tbl_order'),
(54, 'Can change tbl_order', 14, 'change_tbl_order'),
(55, 'Can delete tbl_order', 14, 'delete_tbl_order'),
(56, 'Can view tbl_order', 14, 'view_tbl_order'),
(57, 'Can add tbl_deliveryagent', 15, 'add_tbl_deliveryagent'),
(58, 'Can change tbl_deliveryagent', 15, 'change_tbl_deliveryagent'),
(59, 'Can delete tbl_deliveryagent', 15, 'delete_tbl_deliveryagent'),
(60, 'Can view tbl_deliveryagent', 15, 'view_tbl_deliveryagent');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'Grace', 'idgen'),
(8, 'Grace', 'tbl_category'),
(11, 'Grace', 'tbl_coustomer'),
(15, 'Grace', 'tbl_deliveryagent'),
(12, 'Grace', 'tbl_login'),
(14, 'Grace', 'tbl_order'),
(10, 'Grace', 'tbl_product'),
(13, 'Grace', 'tbl_review'),
(9, 'Grace', 'tbl_shope'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'Grace', '0001_initial', '2023-05-01 06:31:18.847108'),
(2, 'contenttypes', '0001_initial', '2023-05-01 06:31:18.892304'),
(3, 'auth', '0001_initial', '2023-05-01 06:31:19.385125'),
(4, 'admin', '0001_initial', '2023-05-01 06:31:19.490845'),
(5, 'admin', '0002_logentry_remove_auto_add', '2023-05-01 06:31:19.496801'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2023-05-01 06:31:19.512904'),
(7, 'contenttypes', '0002_remove_content_type_name', '2023-05-01 06:31:19.586717'),
(8, 'auth', '0002_alter_permission_name_max_length', '2023-05-01 06:31:19.638367'),
(9, 'auth', '0003_alter_user_email_max_length', '2023-05-01 06:31:19.662213'),
(10, 'auth', '0004_alter_user_username_opts', '2023-05-01 06:31:19.668858'),
(11, 'auth', '0005_alter_user_last_login_null', '2023-05-01 06:31:19.718581'),
(12, 'auth', '0006_require_contenttypes_0002', '2023-05-01 06:31:19.718581'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2023-05-01 06:31:19.726310'),
(14, 'auth', '0008_alter_user_username_max_length', '2023-05-01 06:31:19.810136'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2023-05-01 06:31:19.832876'),
(16, 'auth', '0010_alter_group_name_max_length', '2023-05-01 06:31:19.865556'),
(17, 'auth', '0011_update_proxy_permissions', '2023-05-01 06:31:19.883550'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2023-05-01 06:31:19.914514'),
(19, 'sessions', '0001_initial', '2023-05-01 06:31:19.976034'),
(20, 'Grace', '0002_alter_tbl_category_category_id_and_more', '2023-05-01 06:33:05.578171'),
(21, 'Grace', '0003_idgen_shopeid', '2023-05-01 09:17:59.027338'),
(22, 'Grace', '0004_idgen_productid_tbl_product', '2023-05-02 07:03:30.103395'),
(23, 'Grace', '0005_tbl_product_shope_id', '2023-05-03 06:32:01.538196'),
(24, 'Grace', '0006_idgen_coustomerid', '2023-05-04 05:05:45.367710'),
(25, 'Grace', '0007_tbl_coustomer', '2023-05-04 05:09:07.985402'),
(26, 'Grace', '0008_tbl_login', '2023-05-04 05:56:06.143220'),
(27, 'Grace', '0009_tbl_shope_username', '2023-05-04 08:44:20.966309'),
(28, 'Grace', '0010_tbl_coustomer_username', '2023-05-04 08:45:45.131967'),
(29, 'Grace', '0011_alter_tbl_coustomer_phone_number_and_more', '2023-05-04 10:06:27.920079'),
(30, 'Grace', '0012_tbl_review', '2023-05-04 14:43:17.109068'),
(31, 'Grace', '0013_idgen_reviewid', '2023-05-04 14:44:32.993485'),
(32, 'Grace', '0014_idgen_orderid', '2023-05-05 07:53:37.463052'),
(33, 'Grace', '0015_tbl_order', '2023-05-05 07:58:02.240201'),
(34, 'Grace', '0016_tbl_order_order_adress', '2023-05-05 08:38:00.137548'),
(35, 'Grace', '0017_rename_order_adress_tbl_order_delivery_adress', '2023-05-05 15:44:45.190294'),
(36, 'Grace', '0018_tbl_deliveryagent', '2023-05-06 16:04:06.526236'),
(37, 'Grace', '0019_idgen_agentid', '2023-05-06 16:05:19.423300'),
(38, 'Grace', '0020_tbl_order_total_amount', '2023-05-08 04:43:50.572814'),
(39, 'Grace', '0021_tbl_login_hint', '2023-05-10 05:42:12.092189');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('y5q6q2lk5iw2wynj6v0jrcg6occq8ofz', 'eyJ1aWQiOiJhZG1pbiIsImRlbGl2ZXJ5YWdlbnQiOiJEdW5kdUAyMCJ9:1pwkOI:GEzm4iLK8ZmtlxWzoYz6Ipl9MWQ2uYb08P1Bad2Bl5g', '2023-05-24 14:02:02.466673');

-- --------------------------------------------------------

--
-- Table structure for table `idgen`
--

CREATE TABLE `idgen` (
  `id` bigint(20) NOT NULL,
  `categoryid` int(11) NOT NULL,
  `shopeid` int(11) NOT NULL,
  `productid` int(11) NOT NULL,
  `coustomerid` int(11) NOT NULL,
  `reviewid` int(11) NOT NULL,
  `orderid` int(11) NOT NULL,
  `agentid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `idgen`
--

INSERT INTO `idgen` (`id`, `categoryid`, `shopeid`, `productid`, `coustomerid`, `reviewid`, `orderid`, `agentid`) VALUES
(1, 10, 14, 7, 29, 6, 26, 8);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_category`
--

CREATE TABLE `tbl_category` (
  `category_id` varchar(225) NOT NULL,
  `category_name` varchar(100) NOT NULL,
  `photo` varchar(225) NOT NULL,
  `description` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_category`
--

INSERT INTO `tbl_category` (`category_id`, `category_name`, `photo`, `description`) VALUES
('Category1', 'Electronics', '/media/Eletronics_xPrv0Fw.jpg', 'Includes all kind of electronic devices such as smartphone, laptop, tablets, cameras, and home entertainment'),
('Category10', 'Office and school supplies', '/media/Office%20and%20school%20supplies.jpeg', ' Includes products such as pens, pencils, paper, desk accessories, and electronic devices.'),
('Category2', 'Clothing', '/media/clothing.jpg', 'Reffers to apprisal items such as shirts, pants, dresses,shoes, and accessories like hats, belts and jewelry'),
('Category3', 'Beauty and Personal Care', '/media/beautyandpersonalcare.jpg', 'Covers products such as skincare, hair care, makeup, and grooming tools.'),
('Category4', ' Home and Garden', '/media/homeandgarden.jpg', 'Refers to home decor, furniture, kitchen appliances, gardening tools, and outdoor equipment'),
('Category5', 'Toys and games', '/media/toysandgames.jpg', 'Covers all kinds of games, puzzles, educational toys, action figures, and dolls for kids and adults'),
('Category7', 'Health and wellness', '/media/medicine.webp', 'Includes products such as vitamins, supplements, fitness equipment, and medical supplies.'),
('Category8', 'Sports and outdoor', '/media/Healthandwellness_lJ8aGBN.jpg', 'Refers to products for outdoor activities such as camping, hiking, biking, and sports equipment.'),
('Category9', 'Automotive', '/media/Automotive.webp', 'Covers products for cars, such as car accessories, car parts, and car care products.\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_coustomer`
--

CREATE TABLE `tbl_coustomer` (
  `coustomer_id` varchar(225) NOT NULL,
  `coustomer_name` varchar(100) NOT NULL,
  `adress` varchar(100) NOT NULL,
  `pincode` int(11) NOT NULL,
  `phone_number` varchar(200) NOT NULL,
  `email` varchar(100) NOT NULL,
  `username` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_coustomer`
--

INSERT INTO `tbl_coustomer` (`coustomer_id`, `coustomer_name`, `adress`, `pincode`, `phone_number`, `email`, `username`) VALUES
('Coustomer10', 'gg', 'nn jnjjk', 5566, '5678904435', 'josephgraceson16@gmail.com', 'hbkb'),
('Coustomer11', 'gg', 'nn jnjjk', 5566, '5678904435', 'josephgraceson16@gmail.com', 'hbkb'),
('Coustomer12', 'gg', 'nn jnjjk', 5566, '5678904435', 'josephgraceson16@gmail.com', 'hbkb'),
('Coustomer13', 'gg', 'nn jnjjk', 5566, '5678904435', 'josephgraceson16@gmail.com', 'hbkb'),
('Coustomer14', 'gg', 'nn jnjjk', 5566, '5678904435', 'josephgraceson16@gmail.com', 'hbkb'),
('Coustomer15', 'gg', 'nn jnjjk', 5566, '5678904435', 'josephgraceson16@gmail.com', 'hbkb'),
('Coustomer16', 'sjnj', 'jlknjb', 677, '8976545678', 'josephgraceson16@gmail.com', 'jkhh'),
('Coustomer17', 'sjnj', 'jlknjb', 677, '8976545678', 'josephgraceson16@gmail.com', 'jkhh'),
('Coustomer18', 'tt', 'gg', 666, '7878787878', 'risvana765@gmail.com', 'ss'),
('Coustomer19', 'tt', 'gg', 666, '7878787878', 'risvana765@gmail.com', 'ss'),
('Coustomer20', 'Office and school supplies', 'AAA', 67008, '98845762254', 'paper13@gmail.com', 'AAAA'),
('Coustomer21', 'www', 'wwww', 67004, '9048356672', 'josephgraceson16@gmail.com', 'AAAA'),
('Coustomer22', 'yyy', 'hhhh', 777, '7878787878', 'josephgraceson16@gmail.com', 'ddd'),
('Coustomer23', 'yyy', 'hhhh', 777, '7878787878', 'josephgraceson16@gmail.com', 'ddd'),
('Coustomer24', 'yyy', 'hhhh', 777, '7878787878', 'josephgraceson16@gmail.com', 'ddd'),
('Coustomer25', 'jobin', 'hkbb', 456, '1234567893', 'josephgraceson16@gmail.com', 'jobin'),
('Coustomer26', 'yyy', 'yy', 77, '77', '77@gmail.com', '77'),
('Coustomer27', 'yyy', 'yy', 77, '77', '77@gmail.com', '77'),
('Coustomer28', 'Office and school supplies', 'tttt', 67008, '8989898989', 'paper13@gmail.com', 'ttttA1'),
('Coustomer29', 'graceson', 'koloki', 34455, '2356457789', 'josephgraceson16@gmail.com', 'Graceson1'),
('Coustomer4', 'amal', 'konumanakalam po jondi', 64009, '2147483647', 'amal12@gmail.com', 'Amal@2000'),
('Coustomer5', 'mali', 'hskjjn', 334, '22333838', 'jo5@gmail.com', 'mani@2000'),
('Coustomer6', 'gr', 'ksmmsj', 67009, '9087654312', 'josephgraceson16@gmail.com', 'gr'),
('Coustomer7', 'kutu', 'dde', 78999, '01235678904', 'josephgraceson16@gmail.com', 'kutu'),
('Coustomer8', 'mandu', 'mandu', 566, '8976543367', 'josephgraceson16@gmail.com', 'mandu'),
('Coustomer9', 'gg', 'nn jnjjk', 5566, '5678904435', 'josephgraceson16@gmail.com', 'hbkb');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_deliveryagent`
--

CREATE TABLE `tbl_deliveryagent` (
  `agent_id` varchar(225) NOT NULL,
  `agent_name` varchar(100) NOT NULL,
  `phone_number` varchar(200) NOT NULL,
  `email` varchar(100) NOT NULL,
  `username` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_deliveryagent`
--

INSERT INTO `tbl_deliveryagent` (`agent_id`, `agent_name`, `phone_number`, `email`, `username`) VALUES
('Agent3', 'dundu', '12345678', 'dundu12@gmail.com', 'Dundu@20'),
('Agent4', 'akshay', '2333', 'emmm@kdkk', 'akshay@123'),
('Agent5', 'jobin', '23', 'jobin123@gmail.com', 'jobin@123'),
('Agent6', 'mathew', '2334', 'mathew123@gmail.com', 'mathew@123'),
('Agent7', 'mathew', '2334', 'mathew123@gmail.com', 'mathew@23'),
('Agent8', 'richa', '1224567890', 'richa12@gail.com', 'richa@123');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_login`
--

CREATE TABLE `tbl_login` (
  `username` varchar(225) NOT NULL,
  `password` varchar(100) NOT NULL,
  `category` varchar(200) NOT NULL,
  `hint` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_login`
--

INSERT INTO `tbl_login` (`username`, `password`, `category`, `hint`) VALUES
('77', '77', 'coustomer', '77'),
('AAAA', 'AAAAA', 'coustomer', 'AAAA'),
('admin', 'admin', 'admin', 'grace'),
('akshay@123', 'akshay@123', 'deliveryagent', 'grace'),
('Amal@2000', 'Amal@2000', 'coustomer', 'grace'),
('dady@21', 'dady@21', 'shope', 'grace'),
('ddd', 'AAAAA', 'coustomer', '333'),
('don@2000', 'don@2000', 'shope', 'grace'),
('Dundu@20', 'Dundu@20', 'deliveryagent', 'grace'),
('finedge@123', 'finedge@123', 'shope', 'grace'),
('gr', 'gr', 'coustomer', 'grace'),
('grace', 'grace', 'shope', 'grace'),
('grace@1223', 'grace@1223', 'shope', 'grace'),
('grace@189', 'grace@189', 'shope', 'grace'),
('Graceson1', 'Graceson1', 'coustomer', 'Graceson1'),
('hbkb', 'njk', 'coustomer', 'gg'),
('jjA1', 'jjA1', 'shope', 'jj'),
('jkhh', 'hb', 'coustomer', 'hb'),
('jobin', 'jobin', 'coustomer', 'jobin'),
('jobin@123', 'jobin@123', 'deliveryagent', 'grace'),
('Kola@2000', 'Kola@2000', 'shope', 'grace'),
('kutu', 'kutu', 'shope', 'kutu'),
('kutum', 'kutum', 'shope', 'kutum'),
('kutuma', 'kudu', 'shope', 'kutuma'),
('mandu', 'new', 'coustomer', 'mandu'),
('mani@2000', 'mani@2000', 'coustomer', 'grace'),
('mathew@123', 'mathew@123', 'deliveryagent', 'grace'),
('mathew@23', 'mathew@23', 'deliveryagent', 'grace'),
('papergrid@2000', 'papergrid@2000', 'shope', 'grace'),
('richa@123', 'richa@123', 'deliveryagent', 'grace'),
('ss', 'ss', 'coustomer', '123'),
('ttttA1', 'yyyA6', 'coustomer', 'tt');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_order`
--

CREATE TABLE `tbl_order` (
  `order_id` varchar(225) NOT NULL,
  `status` varchar(225) NOT NULL,
  `order_date` varchar(200) NOT NULL,
  `oder_quandity` int(11) NOT NULL,
  `coustomer_id_id` varchar(225) NOT NULL,
  `product_id_id` varchar(225) NOT NULL,
  `delivery_adress` varchar(200) NOT NULL,
  `total_amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_order`
--

INSERT INTO `tbl_order` (`order_id`, `status`, `order_date`, `oder_quandity`, `coustomer_id_id`, `product_id_id`, `delivery_adress`, `total_amount`) VALUES
('Order1', 'On the way', '2023-05-06', 1, 'Coustomer4', 'Product1', 'sss', 2000),
('Order10', 'pending', '2023-05-08', 2, 'Coustomer4', 'Product3', 'wee', 2000),
('Order11', 'rejected', '2023-05-08', 6, 'Coustomer4', 'Product3', 'www', 22),
('Order12', 'accepted', '2023-05-08', 2, 'Coustomer4', 'Product3', 'sss', 20000),
('Order13', 'accepted', '2023-05-08', 11, 'Coustomer4', 'Product1', 'ww', 880000),
('Order14', 'pending', '2023-05-08', 2344, 'Coustomer4', 'Product3', '', 23440000),
('Order15', 'pending', '2023-05-08', 122, 'Coustomer4', 'Product3', 'sds', 1220000),
('Order16', 'pending', '2023-05-08', 122, 'Coustomer4', 'Product3', 'sds', 1220000),
('Order17', 'pending', '2023-05-08', 2, 'Coustomer4', 'Product3', '', 20000),
('Order18', 'pending', '2023-05-08', 12, 'Coustomer4', 'Product7', '', 147756),
('Order19', 'On the way', '2023-05-08', 2, 'Coustomer4', 'Product5', '', 2426),
('Order2', 'On the way', '2023-05-06', 3, 'Coustomer4', 'Product1', '45hdd', 2000),
('Order20', 'rejected', '2023-05-08', 2, 'Coustomer5', 'Product5', 'ee', 2426),
('Order21', 'pending', '2023-05-08', 22, 'Coustomer4', 'Product3', 'ww', 220000),
('Order22', 'pending', '2023-05-08', 2, 'Coustomer4', 'Product3', 'ssadx', 20000),
('Order23', 'accepted', '2023-05-10', 3, 'Coustomer4', 'Product1', 'kizhakkayil', 240000),
('Order24', 'accepted', '2023-05-10', 1, 'Coustomer4', 'Product1', 'ssssss', 80000),
('Order25', 'Delivred', '2023-05-10', 1, 'Coustomer8', 'Product3', 'swsd', 10000),
('Order26', 'Delivred', '2023-05-10', 1, 'Coustomer29', 'Product5', 'qww', 1213),
('Order3', 'rejected', '2023-05-06', 2, 'Coustomer4', 'Product1', 'w', 2000),
('Order4', 'Delivred', '2023-05-06', 5, 'Coustomer4', 'Product3', 'fgxgg', 2000),
('Order5', 'Delivred', '2023-05-06', 2, 'Coustomer4', 'Product1', 'ee', 2000),
('Order6', 'rejected', '2023-05-06', 2, 'Coustomer4', 'Product1', 'adav', 2000),
('Order7', 'Delivred', '2023-05-06', 2, 'Coustomer4', 'Product1', 'ddd', 2000),
('Order8', 'Delivred', '2023-05-06', 3, 'Coustomer4', 'Product3', 'qde', 2000),
('Order9', 'rejected', '2023-05-06', 5, 'Coustomer5', 'Product3', 'ug', 2000);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_product`
--

CREATE TABLE `tbl_product` (
  `product_id` varchar(225) NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `price` int(11) NOT NULL,
  `description` varchar(200) NOT NULL,
  `photo` varchar(225) NOT NULL,
  `stock` int(11) NOT NULL,
  `category_id_id` varchar(225) NOT NULL,
  `shope_id_id` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_product`
--

INSERT INTO `tbl_product` (`product_id`, `product_name`, `price`, `description`, `photo`, `stock`, `category_id_id`, `shope_id_id`) VALUES
('Product1', 'laptop', 80000, 'assuse v book', '/media/laptop.jpg', -7, 'Category1', 'Shope1'),
('Product3', 'Shirt', 10000, 'hendry polo shirt', '/media/shirt_qLSEu8c.jpg', 9, 'Category2', 'Shope4'),
('Product5', 'werw', 1213, 'asddassds', '/media/Automotive_eZw4zGE.webp', 21, 'Category1', 'Shope4'),
('Product6', 'mm', 223, 'dadad', '/media/Healthandwellness_IuAlJi8.jpg', 2, 'Category8', 'Shope4'),
('Product7', 'mobile', 12313, 'ffsdsfdsdg', '/media/Eletronics_VYXdEef.jpg', 55, 'Category1', 'Shope5');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_review`
--

CREATE TABLE `tbl_review` (
  `review_id` varchar(225) NOT NULL,
  `review` varchar(225) NOT NULL,
  `review_date` varchar(200) NOT NULL,
  `coustomer_id_id` varchar(225) NOT NULL,
  `product_id_id` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_review`
--

INSERT INTO `tbl_review` (`review_id`, `review`, `review_date`, `coustomer_id_id`, `product_id_id`) VALUES
('Review1', 'hh', '2023-05-06', 'Coustomer4', 'Product1'),
('Review2', 'hh', '2023-05-06', 'Coustomer4', 'Product1'),
('Review4', 'sss', '2023-05-06', 'Coustomer5', 'Product5'),
('Review5', 'ss', '2023-05-06', 'Coustomer5', 'Product3');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_shope`
--

CREATE TABLE `tbl_shope` (
  `shope_id` varchar(225) NOT NULL,
  `shope_name` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `pincode` int(11) NOT NULL,
  `phone_number` varchar(200) NOT NULL,
  `email` varchar(100) NOT NULL,
  `photo` varchar(225) NOT NULL,
  `username` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_shope`
--

INSERT INTO `tbl_shope` (`shope_id`, `shope_name`, `location`, `pincode`, `phone_number`, `email`, `photo`, `username`) VALUES
('Shope1', 'Grode Electronics', 'keezhpally', 670704, '2147483647', 'grace1@gmail.com', '/media/electronicshope1_fZDzRGJ.jpg', 'Kola@2000'),
('Shope10', 'grace', 'kannur', 67004, '9048356672', 'josephgraceson16@gmail.com', '/media/electronicshope1_rByZ0Ke.jpg', 'grace@189'),
('Shope11', 'kutu', 'kdty', 89000, '0943256785', 'jhjk2@gmail.com', '/media/clothingshope1_bGXNfAW.jpg', 'kutu'),
('Shope12', 'kutum', 'kdty', 67004, '9012378456', 'josephgraceson16@gmail.com', '/media/clothingshope1_JmyiPoe.jpg', 'kutum'),
('Shope13', 'kutuma', 'kdty', 67004, '9012378456', 'josephgraceson16@gmail.com', '/media/clothingshope1_IW30sZb.jpg', 'kutuma'),
('Shope14', 'lknn', 'huhu', 67004, '9048356672', 'josephgraceson16@gmail.com', '/media/Eletronics_6B89a8b.jpg', 'jjA1'),
('Shope4', 'dadys shope', 'calicut', 67008, '2147483647', 'dady12@gmail.com', '/media/clothing_2hjYYjs.jpg', 'dady@21'),
('Shope5', 'papergroid', 'calicut', 12345, '2147483647', 'paper13@gmail.com', '/media/Automotive_WTAHT2e.webp', 'papergrid@2000'),
('Shope7', 'finedge', 'calicut', 670002, '1222233441', 'fine123@gmail.com', '/media/electronicshope1_G9ztcS4.jpg', 'finedge@123'),
('Shope8', 'grace', 'kannur', 67004, '9048356672', 'josephgraceson16@gmail.com', '/media/electronicshope1_XXVA1ct.jpg', 'grace'),
('Shope9', 'grace', 'kannur', 67004, '9048356672', 'josephgraceson16@gmail.com', '/media/electronicshope1_fq0bLez.jpg', 'grace@1223');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `idgen`
--
ALTER TABLE `idgen`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_category`
--
ALTER TABLE `tbl_category`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `tbl_coustomer`
--
ALTER TABLE `tbl_coustomer`
  ADD PRIMARY KEY (`coustomer_id`);

--
-- Indexes for table `tbl_deliveryagent`
--
ALTER TABLE `tbl_deliveryagent`
  ADD PRIMARY KEY (`agent_id`);

--
-- Indexes for table `tbl_login`
--
ALTER TABLE `tbl_login`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `tbl_order`
--
ALTER TABLE `tbl_order`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `tbl_order_coustomer_id_id_c82fa3ca_fk_tbl_coustomer_coustomer_id` (`coustomer_id_id`),
  ADD KEY `tbl_order_product_id_id_4e72bac0_fk_tbl_product_product_id` (`product_id_id`);

--
-- Indexes for table `tbl_product`
--
ALTER TABLE `tbl_product`
  ADD PRIMARY KEY (`product_id`),
  ADD KEY `tbl_product_category_id_id_478be6cc_fk_tbl_category_category_id` (`category_id_id`),
  ADD KEY `tbl_product_shope_id_id_1027be81_fk_tbl_shope_shope_id` (`shope_id_id`);

--
-- Indexes for table `tbl_review`
--
ALTER TABLE `tbl_review`
  ADD PRIMARY KEY (`review_id`),
  ADD KEY `tbl_review_coustomer_id_id_0d7370e2_fk_tbl_coust` (`coustomer_id_id`),
  ADD KEY `tbl_review_product_id_id_30bc0981_fk_tbl_product_product_id` (`product_id_id`);

--
-- Indexes for table `tbl_shope`
--
ALTER TABLE `tbl_shope`
  ADD PRIMARY KEY (`shope_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `idgen`
--
ALTER TABLE `idgen`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `tbl_order`
--
ALTER TABLE `tbl_order`
  ADD CONSTRAINT `tbl_order_coustomer_id_id_c82fa3ca_fk_tbl_coustomer_coustomer_id` FOREIGN KEY (`coustomer_id_id`) REFERENCES `tbl_coustomer` (`coustomer_id`),
  ADD CONSTRAINT `tbl_order_product_id_id_4e72bac0_fk_tbl_product_product_id` FOREIGN KEY (`product_id_id`) REFERENCES `tbl_product` (`product_id`);

--
-- Constraints for table `tbl_product`
--
ALTER TABLE `tbl_product`
  ADD CONSTRAINT `tbl_product_category_id_id_478be6cc_fk_tbl_category_category_id` FOREIGN KEY (`category_id_id`) REFERENCES `tbl_category` (`category_id`),
  ADD CONSTRAINT `tbl_product_shope_id_id_1027be81_fk_tbl_shope_shope_id` FOREIGN KEY (`shope_id_id`) REFERENCES `tbl_shope` (`shope_id`);

--
-- Constraints for table `tbl_review`
--
ALTER TABLE `tbl_review`
  ADD CONSTRAINT `tbl_review_coustomer_id_id_0d7370e2_fk_tbl_coust` FOREIGN KEY (`coustomer_id_id`) REFERENCES `tbl_coustomer` (`coustomer_id`),
  ADD CONSTRAINT `tbl_review_product_id_id_30bc0981_fk_tbl_product_product_id` FOREIGN KEY (`product_id_id`) REFERENCES `tbl_product` (`product_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
