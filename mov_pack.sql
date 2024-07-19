-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 28, 2024 at 10:18 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mov_pack`
--

-- --------------------------------------------------------

--
-- Table structure for table `area`
--

CREATE TABLE `area` (
  `area_id` int(11) NOT NULL,
  `area_name` varchar(20) NOT NULL,
  `area_pincode` varchar(6) NOT NULL,
  `city_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `area`
--

INSERT INTO `area` (`area_id`, `area_name`, `area_pincode`, `city_id`) VALUES
(1, 'Chandlodiya', '382481', 1),
(2, 'Ghatlodiya', '380061', 1),
(3, 'Ranip', '382480', 1),
(4, 'New Ranip', '382478', 1);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add area', 1, 'add_area'),
(2, 'Can change area', 1, 'change_area'),
(3, 'Can delete area', 1, 'delete_area'),
(4, 'Can view area', 1, 'view_area'),
(5, 'Can add customer', 2, 'add_customer'),
(6, 'Can change customer', 2, 'change_customer'),
(7, 'Can delete customer', 2, 'delete_customer'),
(8, 'Can view customer', 2, 'view_customer'),
(9, 'Can add driver', 3, 'add_driver'),
(10, 'Can change driver', 3, 'change_driver'),
(11, 'Can delete driver', 3, 'delete_driver'),
(12, 'Can view driver', 3, 'view_driver'),
(13, 'Can add state', 4, 'add_state'),
(14, 'Can change state', 4, 'change_state'),
(15, 'Can delete state', 4, 'delete_state'),
(16, 'Can view state', 4, 'view_state'),
(17, 'Can add vehicle_ category', 5, 'add_vehicle_category'),
(18, 'Can change vehicle_ category', 5, 'change_vehicle_category'),
(19, 'Can delete vehicle_ category', 5, 'delete_vehicle_category'),
(20, 'Can view vehicle_ category', 5, 'view_vehicle_category'),
(21, 'Can add vehicle_ details', 6, 'add_vehicle_details'),
(22, 'Can change vehicle_ details', 6, 'change_vehicle_details'),
(23, 'Can delete vehicle_ details', 6, 'delete_vehicle_details'),
(24, 'Can view vehicle_ details', 6, 'view_vehicle_details'),
(25, 'Can add feedback', 7, 'add_feedback'),
(26, 'Can change feedback', 7, 'change_feedback'),
(27, 'Can delete feedback', 7, 'delete_feedback'),
(28, 'Can view feedback', 7, 'view_feedback'),
(29, 'Can add city', 8, 'add_city'),
(30, 'Can change city', 8, 'change_city'),
(31, 'Can delete city', 8, 'delete_city'),
(32, 'Can view city', 8, 'view_city'),
(33, 'Can add booking', 9, 'add_booking'),
(34, 'Can change booking', 9, 'change_booking'),
(35, 'Can delete booking', 9, 'delete_booking'),
(36, 'Can view booking', 9, 'view_booking'),
(37, 'Can add log entry', 10, 'add_logentry'),
(38, 'Can change log entry', 10, 'change_logentry'),
(39, 'Can delete log entry', 10, 'delete_logentry'),
(40, 'Can view log entry', 10, 'view_logentry'),
(41, 'Can add permission', 11, 'add_permission'),
(42, 'Can change permission', 11, 'change_permission'),
(43, 'Can delete permission', 11, 'delete_permission'),
(44, 'Can view permission', 11, 'view_permission'),
(45, 'Can add group', 12, 'add_group'),
(46, 'Can change group', 12, 'change_group'),
(47, 'Can delete group', 12, 'delete_group'),
(48, 'Can view group', 12, 'view_group'),
(49, 'Can add user', 13, 'add_user'),
(50, 'Can change user', 13, 'change_user'),
(51, 'Can delete user', 13, 'delete_user'),
(52, 'Can view user', 13, 'view_user'),
(53, 'Can add content type', 14, 'add_contenttype'),
(54, 'Can change content type', 14, 'change_contenttype'),
(55, 'Can delete content type', 14, 'delete_contenttype'),
(56, 'Can view content type', 14, 'view_contenttype'),
(57, 'Can add session', 15, 'add_session'),
(58, 'Can change session', 15, 'change_session'),
(59, 'Can delete session', 15, 'delete_session'),
(60, 'Can view session', 15, 'view_session');

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `book_id` int(11) NOT NULL,
  `book_date_time` date NOT NULL,
  `pickup_address` longtext NOT NULL,
  `drop_address` longtext NOT NULL,
  `approx_km` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `payment_status` int(11) NOT NULL,
  `cust_id` int(11) NOT NULL,
  `dri_id` int(11) DEFAULT NULL,
  `veh_id` int(11) NOT NULL,
  `booking` int(11) NOT NULL,
  `otp` varchar(10) DEFAULT NULL,
  `payment_type` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`book_id`, `book_date_time`, `pickup_address`, `drop_address`, `approx_km`, `amount`, `payment_status`, `cust_id`, `dri_id`, `veh_id`, `booking`, `otp`, `payment_type`) VALUES
(1, '2023-02-02', '123, Tejas soc., Chandlodiya, Ahmedabad', '45,Satatya Avenue ,New-ranip ,Ahmedabad', 12, 2784, 1, 2, 1, 1, 3, '4205748', 1),
(2, '2023-02-12', '45,Satatya Avenue ,New-ranip ,Ahmedabad', '510-511, 5th floor D Block, Near YMCA Club, SG Road, Ahmedabad', 25, 12500, 1, 2, 2, 2, 3, '9091235', 2),
(3, '2023-02-22', '510-511, 5th floor D Block, Near YMCA Club, SG Road, Ahmedabad', '801, dev soc., Ghatloadiya, Ahmedabad', 20, 28000, 0, 2, 4, 4, 1, '2669792', 1),
(4, '2013-02-26', '801, dev soc., Ghatloadiya, Ahmedabad', '260, shrinath bunglows, ranip,Ahmedabad', 20, 10000, 0, 2, NULL, 2, 1, '9430221', 2),
(5, '2023-04-24', '260, shrinath bunglows, ranip,Ahmedabad', '405, hari flats, C.G.Road, Ahmedabad', 32, 9600, 0, 2, NULL, 6, 2, NULL, 1),
(6, '2023-04-24', '45,Satatya Avenue ,New-ranip ,Ahmedabad', '510-511, 5th floor D Block, Near YMCA Club, SG Road, Ahmedabad', 10, 2320, 1, 3, 1, 2, 3, '7557109', 2),
(7, '2023-03-03', '510-511, 5th floor D Block, Near YMCA Club, SG Roa...', '801, dev soc., Ghatloadiya, Ahmedabad', 20, 28000, 0, 3, 2, 4, 1, '8129109', 1),
(8, '2023-03-13', '801, dev soc., Ghatloadiya, Ahmedabad', '260, shrinath bunglows, ranip, Ahmedabad', 20, 10000, 0, 3, NULL, 2, 1, '5090484', 2),
(9, '2023-03-20', '260, shrinath bunglows, ranip,Ahmedabad', '405, hari flats, C.G.Road, Ahmedabad', 32, 9600, 0, 3, NULL, 6, 2, NULL, 1),
(10, '2023-03-30', '123, Tejas soc., Chandlodiya, Ahmedabad', '45,Satatya Avenue ,New-ranip ,Ahmedabad', 12, 2784, 1, 3, 4, 1, 3, '2178362', 1),
(11, '2023-04-04', '510-511, 5th floor D Block, Near YMCA Club, SG Roa...', '801, dev soc., Ghatloadiya, Ahmedabad', 20, 28000, 0, 4, 1, 4, 1, '6613090', 1),
(12, '2023-04-08', '801, dev soc., Ghatloadiya, Ahmedabad', '260, shrinath bunglows, ranip, Ahmedabad', 20, 10000, 0, 4, NULL, 2, 1, '7178411', 2),
(13, '2023-04-14', '260, shrinath bunglows, ranip,Ahmedabad', '405, hari flats, C.G.Road, Ahmedabad', 32, 9600, 0, 4, NULL, 6, 2, NULL, 1),
(14, '2023-04-24', '123, Tejas soc., Chandlodiya, Ahmedabad', '45,Satatya Avenue ,New-ranip ,Ahmedabad', 12, 6000, 1, 4, 4, 2, 3, '9724750', 1),
(15, '2023-04-25', '45,Satatya Avenue ,New-ranip ,Ahmedabad', '510-511, 5th floor D Block, Near YMCA Club, SG Road, Ahmedabad', 25, 5800, 1, 4, 4, 1, 3, '6950899', 2);

-- --------------------------------------------------------

--
-- Table structure for table `city`
--

CREATE TABLE `city` (
  `city_id` int(11) NOT NULL,
  `city_name` varchar(30) NOT NULL,
  `state_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `city`
--

INSERT INTO `city` (`city_id`, `city_name`, `state_id`) VALUES
(1, 'Ahmedabad', 1),
(2, 'Gandhinagar', 1),
(3, 'Surat', 1),
(4, 'Jaipur', 2),
(5, 'Udaipur', 2);

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `cust_id` int(11) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `cust_email` varchar(40) NOT NULL,
  `address` longtext NOT NULL,
  `cust_contact` bigint(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `is_admin` int(11) NOT NULL,
  `otp` varchar(10) DEFAULT NULL,
  `otp_used` int(11) DEFAULT NULL,
  `area_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`cust_id`, `first_name`, `last_name`, `username`, `gender`, `cust_email`, `address`, `cust_contact`, `password`, `is_admin`, `otp`, `otp_used`, `area_id`) VALUES
(1, 'Shubham', 'Patel', 'shubham_123', 'Male', 'pshubham86@gmail.com', '12, Ganga soc., part-2, Chandlodiya, Ahmedabad-382475', 9853462509, '123', 0, '17028', 1, 1),
(2, 'Rahul', 'Nuwal', 'Rahul_12', 'Male', 'rahulmaheshwari94@gmail.com', '123, Tejas soc., Chandlodiya, Ahmedabad', 9855657547, 'asd', 1, NULL, NULL, 1),
(3, 'Shubh', 'Patel', 'shubh_12', 'Male', 'shubhpatel14@gmail.com', '81, Balol nagar soc., Chandlodiya, Ahmedanad', 7052590525, 'asd', 1, '16311', 0, 1),
(4, 'Harsh', 'Patel', 'Harsh_12', 'Male', 'rahulshah95@gmail.com', '15, Krishna soc., K.K.Nagar, Ahmedabad', 8627501838, 'asd', 1, NULL, NULL, 2),
(5, 'Neha', 'Shah', 'neha_12', 'Female', 'Neha@gmail.com', '23, Om soc., K.K.Nagar, Ahmedabad', 9729495969, 'asd', 1, NULL, NULL, 2);

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(10, 'admin', 'logentry'),
(12, 'auth', 'group'),
(11, 'auth', 'permission'),
(13, 'auth', 'user'),
(14, 'contenttypes', 'contenttype'),
(15, 'sessions', 'session'),
(1, 'ssr', 'area'),
(9, 'ssr', 'booking'),
(8, 'ssr', 'city'),
(2, 'ssr', 'customer'),
(3, 'ssr', 'driver'),
(7, 'ssr', 'feedback'),
(4, 'ssr', 'state'),
(5, 'ssr', 'vehicle_category'),
(6, 'ssr', 'vehicle_details');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-02-08 12:17:03.540489'),
(2, 'auth', '0001_initial', '2023-02-08 12:17:04.048063'),
(3, 'admin', '0001_initial', '2023-02-08 12:17:04.205693'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-02-08 12:17:04.210545'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-02-08 12:17:04.228867'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-02-08 12:17:04.294493'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-02-08 12:17:04.347918'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-02-08 12:17:04.372377'),
(9, 'auth', '0004_alter_user_username_opts', '2023-02-08 12:17:04.386045'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-02-08 12:17:04.468435'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-02-08 12:17:04.472016'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-02-08 12:17:04.472016'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-02-08 12:17:04.503942'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-02-08 12:17:04.526878'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-02-08 12:17:04.551598'),
(16, 'auth', '0011_update_proxy_permissions', '2023-02-08 12:17:04.573625'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-02-08 12:17:04.589492'),
(18, 'sessions', '0001_initial', '2023-02-08 12:17:04.633510'),
(19, 'ssr', '0001_initial', '2023-02-08 12:17:05.295780'),
(20, 'ssr', '0002_alter_booking_dri_alter_booking_veh', '2023-02-08 12:30:05.794462'),
(21, 'ssr', '0002_alter_customer_otp_used', '2023-02-10 19:28:39.833366'),
(22, 'ssr', '0003_alter_feedback_feed_date', '2023-02-14 18:48:54.517996'),
(23, 'ssr', '0002_alter_booking_veh', '2023-02-16 09:39:33.811814'),
(24, 'ssr', '0003_vehicle_category_cate_img', '2023-02-16 14:24:12.667632'),
(25, 'ssr', '0004_vehicle_details_capacity_vehicle_details_size', '2023-02-17 17:25:50.342999'),
(26, 'ssr', '0005_alter_vehicle_details_size', '2023-02-17 18:00:25.149003'),
(27, 'ssr', '0006_alter_vehicle_details_size', '2023-02-17 18:03:16.326220'),
(28, 'ssr', '0002_customer_cust_img', '2023-02-21 12:20:34.244717'),
(29, 'ssr', '0003_alter_customer_cust_img', '2023-02-21 12:21:54.740972'),
(30, 'ssr', '0004_alter_driver_is_available', '2023-02-25 10:57:18.794834'),
(31, 'ssr', '0005_alter_driver_dri_license', '2023-02-25 11:01:19.479553'),
(32, 'ssr', '0006_booking_status', '2023-02-25 11:50:14.710532'),
(33, 'ssr', '0007_rename_status_booking_booking', '2023-02-25 11:54:36.314204'),
(34, 'ssr', '0008_remove_customer_cust_img', '2023-02-25 17:37:41.831910'),
(35, 'ssr', '0002_driver_otp_driver_otp_used', '2023-02-25 18:18:58.288453'),
(36, 'ssr', '0003_booking_otp', '2023-02-26 07:14:39.619062'),
(37, 'ssr', '0002_alter_booking_book_date_time', '2023-03-01 13:32:25.688848'),
(38, 'ssr', '0003_alter_booking_payment_status', '2023-03-02 09:24:50.261930'),
(39, 'ssr', '0004_booking_payment_type_alter_booking_payment_status', '2023-03-02 10:43:46.743705'),
(40, 'ssr', '0005_alter_booking_payment_status_and_more', '2023-03-02 11:41:26.282663'),
(41, 'ssr', '0006_alter_booking_amount', '2023-03-03 09:02:52.623158'),
(42, 'ssr', '0007_remove_vehicle_details_veh_img', '2023-03-03 10:50:04.922130'),
(43, 'ssr', '0002_alter_booking_amount', '2023-03-04 10:01:18.421405'),
(44, 'ssr', '0003_booking_booking_status', '2023-03-07 08:07:58.700219'),
(45, 'ssr', '0004_remove_booking_booking_status', '2023-03-07 08:54:43.972268'),
(46, 'ssr', '0002_alter_vehicle_category_cate_type', '2023-03-16 17:51:35.340365'),
(47, 'ssr', '0003_alter_vehicle_details_veh_desc', '2023-03-19 08:24:41.780267');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('4c7farv241e11ww22zmrke19kbsapman', '.eJyNzkEKwyAQheG7zFoKGkvTrHqTMlGpA5qKY7IpvXubYA3Zdfvz-HgvKC4iBRggsZ9Hj7G_dPr2WOPJPCMIQBtpuv85S8j8XeFoWiILgxRgArmpNCejnwN79NdenQ9QHf4ktntbKS3AZlpcbtT2KGFxQWp1PFWX1ZKq29tmvT_H-1ZY:1phsE2:qHpKw_L-mEt0FRPmGpDwENCc3exLrsGQPi3MV_RU1zk', '2023-04-13 13:21:58.333445'),
('8nedperrmzd2kp4tpogbp4auyzg6xpfu', '.eJyrVspMUbIy1lFKzslMzSuJL0gsLlayUjI0MlbSUUrNTczMAfKKM0qTMgoSS1JzDE2MTBzSQcJ6yfm5SnBtYENqAa_tGMA:1pS1TW:MHCfdQkNgWmDR1pxt1ShSAGH_alY8iF6aaOzosdW-Oc', '2023-02-28 20:00:26.512652'),
('9f3bcv3z6bk3wjw0islmn02md75p29vw', '.eJyrVipJzU3MzFGyUipKzCjNyU3MSC3OKE8syrQ0NTdxSAfJ6SXn5yrpKGWmKFlZ6Cil5SXmpgKVB4GUA4VzoHy_0vJEEJ8442oBpaAoeQ:1pR6D7:if52Ci_XEXWMEJGi_Ivv7eiDtT5guYcyTmARjbj1pY8', '2023-02-26 06:51:41.070873'),
('mi02gt12ptjh4xs6p8kw3692wputh10c', '.eJyrVkrNTczMUbJSKs4oTcooSCxJzTE0MTJxSAcJ6yXn5yrpKJUQoSY5JzM1ryQ-LT4vMTcVqDQYpBQhngMTDwDpBoonpuRm5sXDDC4Am5yYa2FujGosRFlBYnExyPqCeEMjY7hoZoqSlWEtABZTQSM:1pTn8s:iFY1vzmlvR6pUG5C-yEylOGnWUk-JZs08jUb8kEmPVg', '2023-03-05 17:06:26.360217'),
('sawsivccozpm0v0vrog7zmgv6izuyoko', '.eJyrVspMUbKy0FFKy0vMTVWyUgpKzCjNUdJRyoHy_UrLE0H81NzEzBwgvwgkn5uYkVqcUZ5YlGlpam7ikA6S00vOz1WqBQD6iBo6:1pQbwp:3Z4vGuhvXNMSjF5_lh2jsCq2wdnIxrcLjw45uePYniw', '2023-02-24 22:32:51.396253'),
('sc6yphp15n68bhhwp9bdvqhivbdggpdk', '.eJyFjksKgCAUAO_y1hKYEdGqm8QrpR6oSVab6O59tKJV22EYZgU50qLGWhkkDSU4389Nj6bIq-5ESTsYYLfl0PtD4ql4GUkoOYNWk7LT07kyDielefYpRS-W0MuXnSXBAKUh-zcUpM9PQNfOtgNkGkjV:1qTHAT:cHCiJghgh087IoCrkQH4GC0sRFdKp7dENBQHORkaOJw', '2023-08-22 07:30:13.216539'),
('tujgidv9yrn3jq5oflyiqz19sqztiwsy', '.eJyrVipJzU3MzFGyUioozihNykjMtTA3NnFIBwnqJefnKukopRRllqUWxcPUgZUVJJak5hiaGGFVWZBYXAxUaGhkjBDLTFGyMtFRSkzJzcyLJ2glRBmKORAhkDGGtQABjTxh:1prBqE:qMtXfB2fqN-yxruIttdONOYuE2FczlJ_afd8m9o1bmU', '2023-05-09 06:07:54.978101'),
('uf2np2hptnz3z7mwj8pgssp8lr7e7ptd', '.eJxVjkEKgzAQAP-yZykkplQ9-ZOyNcFdSDRktZfSv7fWVMl1GIZ5gU38dOnuArKHDoTWB0VcnFdGm37c8GWYA1R_M6LIV1S6Phlb6EwFg2c3LUcrIa1eCKlt9LVIZTGnUOzJcgpt4Okoxd8WhuZWl0-7ViztaMuo9wck9Ep5:1qCiFY:Ff3ox_wt05M8sxax0w8ZFHWZkmNj1U4x9cmpY6CZXZA', '2023-07-07 14:59:00.077996'),
('v7cw43jp9lu77a7jlpkca6zsfqtya6pw', 'e30:1rRrfJ:QXfOUD7ZKmjn90Rk6Nmh2yNFyUQEbavSwZKdufZHa14', '2024-02-05 10:36:29.424951'),
('zrdem05lblqvaefan1qhuhls2yimhq45', '.eJyrVspMUbIy1lFKy0vMTVWyUgpKzFLSUcqB8oIzEjOA3NTcxMwcILcoMcshHcTWS87PBYon52Sm5pXEg4wwrwUAWwYXfg:1pRvXB:T1zWuTntE0K4oHCInW-hxP5_SFo_-C-QlMEy_a6O69w', '2023-02-28 13:39:49.800827');

-- --------------------------------------------------------

--
-- Table structure for table `driver`
--

CREATE TABLE `driver` (
  `dri_id` int(11) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `dri_email` varchar(40) NOT NULL,
  `password` varchar(20) NOT NULL,
  `dri_contact` bigint(20) NOT NULL,
  `dri_license` varchar(20) NOT NULL,
  `is_available` tinyint(1) DEFAULT NULL,
  `otp` varchar(10) DEFAULT NULL,
  `otp_used` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `driver`
--

INSERT INTO `driver` (`dri_id`, `first_name`, `last_name`, `username`, `gender`, `dri_email`, `password`, `dri_contact`, `dri_license`, `is_available`, `otp`, `otp_used`) VALUES
(1, 'Mubin', 'Mansuri', 'mubin_12', 'Male', 'pshubham86@gmail.com', '123', 9918766655, 'GJ02 12345678901', 1, NULL, NULL),
(2, 'Kaif', 'Kazi', 'kaif_12', 'Male', 'kaif.kazi20@gmail.com', '123', 7211533921, 'GJ02 12345678902', 1, '59637', 1),
(3, 'Rahul', 'Shah', 'Rahul_Shah_12', 'Male', 'rahulshah97@gmail.com', '123', 9525157567, 'GJ01 12345678901', 0, '92973', 1),
(4, 'Shubh', 'Patel', 'shubh_1234', 'Male', 'shubhpatel14@gmail.com', '123', 7001494526, 'GJ01 12345678912', 2, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `feed_id` int(11) NOT NULL,
  `feed_desc` longtext NOT NULL,
  `feed_date` date NOT NULL,
  `cust_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`feed_id`, `feed_desc`, `feed_date`, `cust_id`) VALUES
(1, 'Excellent service by multiple drivers. I own a business and do multiple shiftings. Rather than ask local drivers and bargain every time, I use porter which fulfils all my need. Thanks a lot!', '2023-02-22', 3),
(2, 'Way better than naaka waalas. Have shifted all my logistics needs to Porter and I can now safely focus on my business growth. Amazing service!', '2023-03-13', 2),
(3, 'Have had an amazing experience. Had three successful deliveries where it’s a struggle to arrange a tempo service for your desired pickup and drop off. Must try this app!', '2023-02-26', 3),
(4, 'They providing fast and good service. I was amazing and surprised at how well they did everything. great experience The packers and movers.', '2023-04-08', 4),
(5, 'They do things quickly and you can shift to your destination without having to worry about wasting your time.', '2023-04-24', 4);

-- --------------------------------------------------------

--
-- Table structure for table `state`
--

CREATE TABLE `state` (
  `state_id` int(11) NOT NULL,
  `state_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `state`
--

INSERT INTO `state` (`state_id`, `state_name`) VALUES
(1, 'Gujarat'),
(2, 'Rajasthan'),
(3, 'Goa');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_category`
--

CREATE TABLE `vehicle_category` (
  `cate_id` int(11) NOT NULL,
  `cate_type` varchar(30) NOT NULL,
  `cate_img` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle_category`
--

INSERT INTO `vehicle_category` (`cate_id`, `cate_type`, `cate_img`) VALUES
(1, 'Tata Ace', 'tataace.jpg'),
(2, 'Eicher19', 'eicher19.jpeg'),
(3, 'Tata Tauras', 'TataTaurus.jpeg'),
(4, 'Container 32FT SXL', 'sxlcontainer.jpeg'),
(5, 'Ashok LeyLand Dost', 'ashokleylanddost.jpg'),
(6, 'Mahindra Bolero', 'mbp.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_details`
--

CREATE TABLE `vehicle_details` (
  `veh_id` int(11) NOT NULL,
  `veh_no` varchar(15) NOT NULL,
  `chassis_no` varchar(20) NOT NULL,
  `rent` bigint(20) NOT NULL,
  `veh_desc` longtext NOT NULL,
  `cate_id` int(11) NOT NULL,
  `capacity` int(11) NOT NULL,
  `size` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle_details`
--

INSERT INTO `vehicle_details` (`veh_id`, `veh_no`, `chassis_no`, `rent`, `veh_desc`, `cate_id`, `capacity`, `size`) VALUES
(1, 'GJ-01-SS-333', '2H2XA59BWDY987665', 232, 'Tata Super Ace Mint is a last-mile cargo mini-truck with a load body length of 8.6 feet and a payload capacity of 1000 kgs (1 tonne). Powered by a 1396 cc engine, it offers a class-leading 70 HP of maximum power and 140 Nm of max torque. It also offers a top speed of 80 km/ph for faster turnaround times.', 1, 850, '7L x 4.8W x 4.8H'),
(2, 'GJ-01-UG-9250', '4S3BMHB68B3286050', 500, 'Eicher Motors Limited is an Indian multinational automotive company that manufactures motorcycles and commercial vehicles, headquartered in New Delhi.', 2, 9000, '19L x 7W x 7H'),
(3, 'GJ-01-SS-4444', '5D8CMSB70A2397161', 800, 'The Taurus Truck is the latest Premium offering from Tata Motors in Light Commercial Vehicle segment under the world-class Ultra Platform. This is India’s first LCV offering meeting International standard Crash Tested comfortable and stunning Ultra Narrow Cabin, designed and developed for Indian road conditions redefining transportation industry, leveraging enhanced technologies blending ideally both technology and economy of operations. It\'s capacity is 21Tons.', 3, 21000, '24L x 7.3W x 7H'),
(4, 'GJ-01-AS-8888', '9W4ZA59BWDY382302', 1400, 'Product Description Windson Logistics Can Offer 32 FT Single Axcle Container for Light weight Goods transporation. This 32FT SXL Truck are widely use for plastic item, light weight box, furniture, drum, etc.', 4, 40000, '32L x 8W x 8H'),
(5, 'GJ-01-RR-5555', '4T4WA59BWDY982332', 240, 'Ashok Leyland Dost is a compact and reliable mini truck designed to cater to the growing demand for an efficient and versatile transportation solution for small businesses. The vehicle is known for its powerful engine, sturdy build, and exceptional load-carrying capacity, making it a popular choice among fleet owners and entrepreneurs.', 5, 1000, '7L x 4.8W x 4.8H'),
(6, 'GJ-18-AB-2736', '1G7UN05AWDY230318', 300, 'The Mahindra Bolero is an SUV -based pickup truck, available in AC and non-AC variants. Single or double cabin models are on offer. It was originally sold as the Bolero Single Cab or Bolero Double Cab, but from early 2002 the Double Cab model has been marketed as the Bolero Camper in India.', 6, 1700, '8L x 4.8W x 4.8H');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`area_id`),
  ADD UNIQUE KEY `area_pincode` (`area_pincode`),
  ADD KEY `area_city_id_6c07a4b7_fk_city_city_id` (`city_id`);

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
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`book_id`),
  ADD KEY `booking_cust_id_5361a6d9_fk_customer_cust_id` (`cust_id`),
  ADD KEY `booking_dri_id_07efc06a_fk_driver_dri_id` (`dri_id`),
  ADD KEY `booking_veh_id_90e69f21_fk_vehicle_details_veh_id` (`veh_id`);

--
-- Indexes for table `city`
--
ALTER TABLE `city`
  ADD PRIMARY KEY (`city_id`),
  ADD KEY `city_state_id_b686921b_fk_state_state_id` (`state_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`cust_id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `cust_email` (`cust_email`),
  ADD UNIQUE KEY `cust_contact` (`cust_contact`),
  ADD KEY `customer_area_id_916acf30_fk_area_area_id` (`area_id`);

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
-- Indexes for table `driver`
--
ALTER TABLE `driver`
  ADD PRIMARY KEY (`dri_id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `dri_email` (`dri_email`),
  ADD UNIQUE KEY `dri_contact` (`dri_contact`),
  ADD UNIQUE KEY `dri_license` (`dri_license`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`feed_id`),
  ADD KEY `feedback_cust_id_69972daa_fk_customer_cust_id` (`cust_id`);

--
-- Indexes for table `state`
--
ALTER TABLE `state`
  ADD PRIMARY KEY (`state_id`);

--
-- Indexes for table `vehicle_category`
--
ALTER TABLE `vehicle_category`
  ADD PRIMARY KEY (`cate_id`);

--
-- Indexes for table `vehicle_details`
--
ALTER TABLE `vehicle_details`
  ADD PRIMARY KEY (`veh_id`),
  ADD UNIQUE KEY `veh_no` (`veh_no`),
  ADD UNIQUE KEY `chassis_no` (`chassis_no`),
  ADD KEY `vehicle_details_cate_id_a053978d_fk_vehicle_category_cate_id` (`cate_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `area`
--
ALTER TABLE `area`
  MODIFY `area_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

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
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `book_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `city`
--
ALTER TABLE `city`
  MODIFY `city_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `cust_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

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
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT for table `driver`
--
ALTER TABLE `driver`
  MODIFY `dri_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `feed_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `state`
--
ALTER TABLE `state`
  MODIFY `state_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `vehicle_category`
--
ALTER TABLE `vehicle_category`
  MODIFY `cate_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `vehicle_details`
--
ALTER TABLE `vehicle_details`
  MODIFY `veh_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `area`
--
ALTER TABLE `area`
  ADD CONSTRAINT `area_city_id_6c07a4b7_fk_city_city_id` FOREIGN KEY (`city_id`) REFERENCES `city` (`city_id`);

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
-- Constraints for table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_cust_id_5361a6d9_fk_customer_cust_id` FOREIGN KEY (`cust_id`) REFERENCES `customer` (`cust_id`),
  ADD CONSTRAINT `booking_dri_id_07efc06a_fk_driver_dri_id` FOREIGN KEY (`dri_id`) REFERENCES `driver` (`dri_id`);

--
-- Constraints for table `city`
--
ALTER TABLE `city`
  ADD CONSTRAINT `city_state_id_b686921b_fk_state_state_id` FOREIGN KEY (`state_id`) REFERENCES `state` (`state_id`);

--
-- Constraints for table `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `customer_area_id_916acf30_fk_area_area_id` FOREIGN KEY (`area_id`) REFERENCES `area` (`area_id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `feedback`
--
ALTER TABLE `feedback`
  ADD CONSTRAINT `feedback_cust_id_69972daa_fk_customer_cust_id` FOREIGN KEY (`cust_id`) REFERENCES `customer` (`cust_id`);

--
-- Constraints for table `vehicle_details`
--
ALTER TABLE `vehicle_details`
  ADD CONSTRAINT `vehicle_details_cate_id_a053978d_fk_vehicle_category_cate_id` FOREIGN KEY (`cate_id`) REFERENCES `vehicle_category` (`cate_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
