-- phpMyAdmin SQL Dump
-- version 2.11.3
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 20, 2008 at 09:44 AM
-- Server version: 5.0.45
-- PHP Version: 5.2.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

--
-- Database: `bluechannel_dev`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_group`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `permission_id_refs_id_5886d21f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_group_permissions`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_message`
--

CREATE TABLE IF NOT EXISTS `auth_message` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `auth_message_user_id` (`user_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `auth_message`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id` (`content_type_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=73 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add message', 1, 'add_message'),
(2, 'Can change message', 1, 'change_message'),
(3, 'Can delete message', 1, 'delete_message'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add permission', 4, 'add_permission'),
(11, 'Can change permission', 4, 'change_permission'),
(12, 'Can delete permission', 4, 'delete_permission'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add site', 7, 'add_site'),
(20, 'Can change site', 7, 'change_site'),
(21, 'Can delete site', 7, 'delete_site'),
(22, 'Can add log entry', 8, 'add_logentry'),
(23, 'Can change log entry', 8, 'change_logentry'),
(24, 'Can delete log entry', 8, 'delete_logentry'),
(25, 'Can add comment', 9, 'add_comment'),
(26, 'Can change comment', 9, 'change_comment'),
(27, 'Can delete comment', 9, 'delete_comment'),
(28, 'Can add free comment', 10, 'add_freecomment'),
(29, 'Can change free comment', 10, 'change_freecomment'),
(30, 'Can delete free comment', 10, 'delete_freecomment'),
(31, 'Can add karma score', 11, 'add_karmascore'),
(32, 'Can change karma score', 11, 'change_karmascore'),
(33, 'Can delete karma score', 11, 'delete_karmascore'),
(34, 'Can add moderator deletion', 12, 'add_moderatordeletion'),
(35, 'Can change moderator deletion', 12, 'change_moderatordeletion'),
(36, 'Can delete moderator deletion', 12, 'delete_moderatordeletion'),
(37, 'Can add user flag', 13, 'add_userflag'),
(38, 'Can change user flag', 13, 'change_userflag'),
(39, 'Can delete user flag', 13, 'delete_userflag'),
(40, 'Can add redirect', 14, 'add_redirect'),
(41, 'Can change redirect', 14, 'change_redirect'),
(42, 'Can delete redirect', 14, 'delete_redirect'),
(43, 'Can add media', 15, 'add_media'),
(44, 'Can change media', 15, 'change_media'),
(45, 'Can delete media', 15, 'delete_media'),
(46, 'Can add type', 16, 'add_type'),
(47, 'Can change type', 16, 'change_type'),
(48, 'Can delete type', 16, 'delete_type'),
(49, 'Can add profile', 17, 'add_profile'),
(50, 'Can change profile', 17, 'change_profile'),
(51, 'Can delete profile', 17, 'delete_profile'),
(52, 'Can add Content', 18, 'add_content'),
(53, 'Can change Content', 18, 'change_content'),
(54, 'Can delete Content', 18, 'delete_content'),
(55, 'Can add Type', 19, 'add_type'),
(56, 'Can change Type', 19, 'change_type'),
(57, 'Can delete Type', 19, 'delete_type'),
(58, 'Can add page', 20, 'add_page'),
(59, 'Can change page', 20, 'change_page'),
(60, 'Can delete page', 20, 'delete_page'),
(61, 'Can add template', 21, 'add_template'),
(62, 'Can change template', 21, 'change_template'),
(63, 'Can delete template', 21, 'delete_template'),
(64, 'Can add vote', 22, 'add_vote'),
(65, 'Can change vote', 22, 'change_vote'),
(66, 'Can delete vote', 22, 'delete_vote'),
(67, 'Can add tagged item', 23, 'add_taggeditem'),
(68, 'Can change tagged item', 23, 'change_taggeditem'),
(69, 'Can delete tagged item', 23, 'delete_taggeditem'),
(70, 'Can add tag', 24, 'add_tag'),
(71, 'Can change tag', 24, 'change_tag'),
(72, 'Can delete tag', 24, 'delete_tag');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL auto_increment,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`) VALUES
(1, 'admin', '', '', 'schmoopy@schmoopy.com', 'sha1$777cb$e3bde605e35404e75207b3a1fb7ef918dee76deb', 1, 1, 1, '2008-05-20 09:32:12', '2008-05-20 09:31:46');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `group_id_refs_id_f116770` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_user_groups`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `permission_id_refs_id_67e79cb` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_user_user_permissions`
--


-- --------------------------------------------------------

--
-- Table structure for table `comments_comment`
--

CREATE TABLE IF NOT EXISTS `comments_comment` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `object_id` int(11) NOT NULL,
  `headline` varchar(255) NOT NULL,
  `comment` longtext NOT NULL,
  `rating1` smallint(5) unsigned default NULL,
  `rating2` smallint(5) unsigned default NULL,
  `rating3` smallint(5) unsigned default NULL,
  `rating4` smallint(5) unsigned default NULL,
  `rating5` smallint(5) unsigned default NULL,
  `rating6` smallint(5) unsigned default NULL,
  `rating7` smallint(5) unsigned default NULL,
  `rating8` smallint(5) unsigned default NULL,
  `valid_rating` tinyint(1) NOT NULL,
  `submit_date` datetime NOT NULL,
  `is_public` tinyint(1) NOT NULL,
  `ip_address` char(15) default NULL,
  `is_removed` tinyint(1) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `comments_comment_user_id` (`user_id`),
  KEY `comments_comment_content_type_id` (`content_type_id`),
  KEY `comments_comment_site_id` (`site_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `comments_comment`
--


-- --------------------------------------------------------

--
-- Table structure for table `comments_freecomment`
--

CREATE TABLE IF NOT EXISTS `comments_freecomment` (
  `id` int(11) NOT NULL auto_increment,
  `content_type_id` int(11) NOT NULL,
  `object_id` int(11) NOT NULL,
  `comment` longtext NOT NULL,
  `person_name` varchar(50) NOT NULL,
  `submit_date` datetime NOT NULL,
  `is_public` tinyint(1) NOT NULL,
  `ip_address` char(15) NOT NULL,
  `approved` tinyint(1) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `comments_freecomment_content_type_id` (`content_type_id`),
  KEY `comments_freecomment_site_id` (`site_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `comments_freecomment`
--


-- --------------------------------------------------------

--
-- Table structure for table `comments_karmascore`
--

CREATE TABLE IF NOT EXISTS `comments_karmascore` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `comment_id` int(11) NOT NULL,
  `score` smallint(6) NOT NULL,
  `scored_date` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`comment_id`),
  KEY `comments_karmascore_user_id` (`user_id`),
  KEY `comments_karmascore_comment_id` (`comment_id`),
  KEY `comments_karmascore_score` (`score`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `comments_karmascore`
--


-- --------------------------------------------------------

--
-- Table structure for table `comments_moderatordeletion`
--

CREATE TABLE IF NOT EXISTS `comments_moderatordeletion` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `comment_id` int(11) NOT NULL,
  `deletion_date` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`comment_id`),
  KEY `comments_moderatordeletion_user_id` (`user_id`),
  KEY `comments_moderatordeletion_comment_id` (`comment_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `comments_moderatordeletion`
--


-- --------------------------------------------------------

--
-- Table structure for table `comments_userflag`
--

CREATE TABLE IF NOT EXISTS `comments_userflag` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `comment_id` int(11) NOT NULL,
  `flag_date` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`comment_id`),
  KEY `comments_userflag_user_id` (`user_id`),
  KEY `comments_userflag_comment_id` (`comment_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `comments_userflag`
--


-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL auto_increment,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) default NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `django_admin_log_user_id` (`user_id`),
  KEY `django_admin_log_content_type_id` (`content_type_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `user_id`, `content_type_id`, `object_id`, `object_repr`, `action_flag`, `change_message`) VALUES
(1, '2008-05-20 09:33:01', 1, 21, '1', 'Default', 1, ''),
(2, '2008-05-20 09:33:28', 1, 20, '1', 'About', 1, ''),
(3, '2008-05-20 09:34:02', 1, 20, '2', 'Company History', 1, ''),
(4, '2008-05-20 09:34:12', 1, 20, '2', 'Company History', 2, 'Changed modified, enable comments, in nav, in site map and has next.'),
(5, '2008-05-20 09:34:41', 1, 20, '3', 'Portfolio', 1, ''),
(6, '2008-05-20 09:34:53', 1, 20, '3', 'Portfolio', 2, 'Changed modified, enable comments, in nav, in site map and has next.'),
(7, '2008-05-20 09:36:19', 1, 20, '4', 'Contact us', 1, ''),
(8, '2008-05-20 09:36:49', 1, 21, '2', 'Contact Form', 1, ''),
(9, '2008-05-20 09:36:57', 1, 20, '5', 'Contact Form', 1, ''),
(10, '2008-05-20 09:38:12', 1, 21, '3', 'Homepage', 1, ''),
(11, '2008-05-20 09:38:21', 1, 20, '6', 'Home', 1, ''),
(12, '2008-05-20 09:43:47', 1, 20, '6', 'Home', 2, 'Changed modified, enable comments, in nav, is home, in site map and has next.');

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=25 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'message', 'auth', 'message'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'permission', 'auth', 'permission'),
(5, 'content type', 'contenttypes', 'contenttype'),
(6, 'session', 'sessions', 'session'),
(7, 'site', 'sites', 'site'),
(8, 'log entry', 'admin', 'logentry'),
(9, 'comment', 'comments', 'comment'),
(10, 'free comment', 'comments', 'freecomment'),
(11, 'karma score', 'comments', 'karmascore'),
(12, 'moderator deletion', 'comments', 'moderatordeletion'),
(13, 'user flag', 'comments', 'userflag'),
(14, 'redirect', 'redirects', 'redirect'),
(15, 'media', 'media', 'media'),
(16, 'type', 'media', 'type'),
(17, 'profile', 'profiles', 'profile'),
(18, 'Content', 'page', 'content'),
(19, 'Type', 'page', 'type'),
(20, 'page', 'page', 'page'),
(21, 'template', 'layout', 'template'),
(22, 'vote', 'voting', 'vote'),
(23, 'tagged item', 'tagging', 'taggeditem'),
(24, 'tag', 'tagging', 'tag');

-- --------------------------------------------------------

--
-- Table structure for table `django_redirect`
--

CREATE TABLE IF NOT EXISTS `django_redirect` (
  `id` int(11) NOT NULL auto_increment,
  `site_id` int(11) NOT NULL,
  `old_path` varchar(200) NOT NULL,
  `new_path` varchar(200) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `site_id` (`site_id`,`old_path`),
  KEY `django_redirect_site_id` (`site_id`),
  KEY `django_redirect_old_path` (`old_path`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `django_redirect`
--


-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY  (`session_key`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('189ad12ac24cce633fb021ee6296291a', 'gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS41MWY1YmI5NGZiNDljODdhODUx\nNDViMWQxMjQ5ZTMzMA==\n', '2008-06-03 09:32:12');

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL auto_increment,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

-- --------------------------------------------------------

--
-- Table structure for table `layout_template`
--

CREATE TABLE IF NOT EXISTS `layout_template` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `layout_template`
--

INSERT INTO `layout_template` (`id`, `name`, `description`, `created`, `modified`) VALUES
(1, 'Default', 'This is the Default page template.', '2008-05-20 09:33:01', '2008-05-20 09:33:01'),
(2, 'Contact Form', '', '2008-05-20 09:36:49', '2008-05-20 09:36:49'),
(3, 'Homepage', '', '2008-05-20 09:38:12', '2008-05-20 09:38:12');

-- --------------------------------------------------------

--
-- Table structure for table `media_media`
--

CREATE TABLE IF NOT EXISTS `media_media` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(250) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `media_type_id` int(11) default NULL,
  `media_file` varchar(255) NOT NULL,
  `media_embed` longtext NOT NULL,
  `title_text` varchar(100) NOT NULL,
  `alt_text` varchar(100) NOT NULL,
  `caption` varchar(200) NOT NULL,
  `author` varchar(100) NOT NULL,
  `liscense_type` varchar(100) NOT NULL,
  `liscense_url` varchar(200) NOT NULL,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  `display` tinyint(1) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `media_media_slug` (`slug`),
  KEY `media_media_media_type_id` (`media_type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `media_media`
--


-- --------------------------------------------------------

--
-- Table structure for table `media_type`
--

CREATE TABLE IF NOT EXISTS `media_type` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(200) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `media_type_slug` (`slug`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `media_type`
--


-- --------------------------------------------------------

--
-- Table structure for table `page_content`
--

CREATE TABLE IF NOT EXISTS `page_content` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `status` varchar(20) NOT NULL,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `page_content`
--


-- --------------------------------------------------------

--
-- Table structure for table `page_page`
--

CREATE TABLE IF NOT EXISTS `page_page` (
  `id` int(11) NOT NULL auto_increment,
  `title` varchar(200) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `parent_id` int(11) default NULL,
  `status` varchar(20) NOT NULL,
  `main_content` longtext NOT NULL,
  `summary` longtext NOT NULL,
  `template_id` int(11) NOT NULL,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  `author_id` int(11) NOT NULL,
  `enable_comments` tinyint(1) NOT NULL,
  `order` int(11) default NULL,
  `in_nav` tinyint(1) NOT NULL,
  `is_home` tinyint(1) NOT NULL,
  `in_site_map` tinyint(1) NOT NULL,
  `has_next` tinyint(1) NOT NULL,
  `tags` varchar(255) NOT NULL,
  `categories` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `page_page_slug` (`slug`),
  KEY `page_page_parent_id` (`parent_id`),
  KEY `page_page_template_id` (`template_id`),
  KEY `page_page_author_id` (`author_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `page_page`
--

INSERT INTO `page_page` (`id`, `title`, `slug`, `parent_id`, `status`, `main_content`, `summary`, `template_id`, `created`, `modified`, `author_id`, `enable_comments`, `order`, `in_nav`, `is_home`, `in_site_map`, `has_next`, `tags`, `categories`) VALUES
(1, 'About', 'about', NULL, 'publish', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nunc at quam ac lorem venenatis ullamcorper. Fusce lacinia. Suspendisse ultrices, libero ut consequat ultrices, orci tortor congue quam, sed consectetuer enim augue at nulla. Proin placerat tincidunt eros. Nulla facilisi. Suspendisse potenti. Curabitur quis risus eu ipsum rhoncus lacinia. Sed turpis augue, blandit non, semper ac, placerat at, quam. Proin egestas ornare elit. Duis eleifend lacinia lectus. Donec ut risus ac ligula pharetra faucibus. Curabitur nec leo. Duis ac dui. Vestibulum hendrerit nisi sit amet tellus. Aenean blandit.\r\n\r\nEtiam faucibus velit semper libero. Phasellus scelerisque dolor a risus. Etiam placerat turpis in leo. Etiam ligula nisl, consectetuer nec, convallis et, vestibulum ac, sapien. Aenean gravida. Nam ultricies velit eu enim. Sed malesuada auctor neque. Nulla feugiat. Maecenas in quam. Sed vitae orci ac ligula rhoncus dictum. Nulla diam justo, laoreet a, viverra vel, dictum non, massa. Sed libero nisl, vulputate eget, tempor gravida, aliquam ac, massa.\r\n\r\nVivamus aliquet, metus at ultricies dictum, libero augue tincidunt nunc, a mollis sapien est vitae velit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec posuere. Proin nisl velit, vehicula ut, blandit eu, eleifend nec, lectus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum sodales condimentum arcu. Morbi elementum, nisl vitae accumsan mattis, augue purus pellentesque nulla, at dignissim lacus orci dapibus magna. In in felis ac est lacinia scelerisque. Duis massa mauris, ultricies id, ornare et, lobortis ut, ante. Sed viverra. Phasellus venenatis accumsan neque. Donec velit lorem, iaculis ac, faucibus quis, elementum id, mi. Donec justo elit, malesuada quis, malesuada nec, posuere in, lacus. Etiam venenatis velit ac purus. Vivamus hendrerit libero vel sapien. ', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nunc at quam ac lorem venenatis ullamcorper. Fusce lacinia. Suspendisse ultrices, libero ut consequat ultrices, orci tortor congue quam, sed consectetuer enim augue at nulla.', 1, '2008-05-20 09:33:28', '2008-05-20 09:33:28', 1, 0, NULL, 1, 0, 1, 0, '', ''),
(2, 'Company History', 'company-history', 1, 'publish', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nunc at quam ac lorem venenatis ullamcorper. Fusce lacinia. Suspendisse ultrices, libero ut consequat ultrices, orci tortor congue quam, sed consectetuer enim augue at nulla. Proin placerat tincidunt eros. Nulla facilisi. Suspendisse potenti. Curabitur quis risus eu ipsum rhoncus lacinia. Sed turpis augue, blandit non, semper ac, placerat at, quam. Proin egestas ornare elit. Duis eleifend lacinia lectus. Donec ut risus ac ligula pharetra faucibus. Curabitur nec leo. Duis ac dui. Vestibulum hendrerit nisi sit amet tellus. Aenean blandit.\r\n\r\nEtiam faucibus velit semper libero. Phasellus scelerisque dolor a risus. Etiam placerat turpis in leo. Etiam ligula nisl, consectetuer nec, convallis et, vestibulum ac, sapien. Aenean gravida. Nam ultricies velit eu enim. Sed malesuada auctor neque. Nulla feugiat. Maecenas in quam. Sed vitae orci ac ligula rhoncus dictum. Nulla diam justo, laoreet a, viverra vel, dictum non, massa. Sed libero nisl, vulputate eget, tempor gravida, aliquam ac, massa.\r\n\r\nVivamus aliquet, metus at ultricies dictum, libero augue tincidunt nunc, a mollis sapien est vitae velit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec posuere. Proin nisl velit, vehicula ut, blandit eu, eleifend nec, lectus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum sodales condimentum arcu. Morbi elementum, nisl vitae accumsan mattis, augue purus pellentesque nulla, at dignissim lacus orci dapibus magna. In in felis ac est lacinia scelerisque. Duis massa mauris, ultricies id, ornare et, lobortis ut, ante. Sed viverra. Phasellus venenatis accumsan neque. Donec velit lorem, iaculis ac, faucibus quis, elementum id, mi. Donec justo elit, malesuada quis, malesuada nec, posuere in, lacus. Etiam venenatis velit ac purus. Vivamus hendrerit libero vel sapien. ', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nunc at quam ac lorem venenatis ullamcorper. Fusce lacinia. Suspendisse ultrices, libero ut consequat ultrices, orci tortor congue quam, sed consectetuer enim augue at nulla.', 1, '2008-05-20 09:34:02', '2008-05-20 09:34:12', 1, 0, NULL, 0, 0, 1, 0, '', ''),
(3, 'Portfolio', 'portfolio', NULL, 'publish', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nunc at quam ac lorem venenatis ullamcorper. Fusce lacinia. Suspendisse ultrices, libero ut consequat ultrices, orci tortor congue quam, sed consectetuer enim augue at nulla. Proin placerat tincidunt eros. Nulla facilisi. Suspendisse potenti. Curabitur quis risus eu ipsum rhoncus lacinia. Sed turpis augue, blandit non, semper ac, placerat at, quam. Proin egestas ornare elit. Duis eleifend lacinia lectus. Donec ut risus ac ligula pharetra faucibus. Curabitur nec leo. Duis ac dui. Vestibulum hendrerit nisi sit amet tellus. Aenean blandit.\r\n\r\nEtiam faucibus velit semper libero. Phasellus scelerisque dolor a risus. Etiam placerat turpis in leo. Etiam ligula nisl, consectetuer nec, convallis et, vestibulum ac, sapien. Aenean gravida. Nam ultricies velit eu enim. Sed malesuada auctor neque. Nulla feugiat. Maecenas in quam. Sed vitae orci ac ligula rhoncus dictum. Nulla diam justo, laoreet a, viverra vel, dictum non, massa. Sed libero nisl, vulputate eget, tempor gravida, aliquam ac, massa.\r\n\r\nVivamus aliquet, metus at ultricies dictum, libero augue tincidunt nunc, a mollis sapien est vitae velit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec posuere. Proin nisl velit, vehicula ut, blandit eu, eleifend nec, lectus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum sodales condimentum arcu. Morbi elementum, nisl vitae accumsan mattis, augue purus pellentesque nulla, at dignissim lacus orci dapibus magna. In in felis ac est lacinia scelerisque. Duis massa mauris, ultricies id, ornare et, lobortis ut, ante. Sed viverra. Phasellus venenatis accumsan neque. Donec velit lorem, iaculis ac, faucibus quis, elementum id, mi. Donec justo elit, malesuada quis, malesuada nec, posuere in, lacus. Etiam venenatis velit ac purus. Vivamus hendrerit libero vel sapien. ', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nunc at quam ac lorem venenatis ullamcorper. Fusce lacinia. Suspendisse ultrices, libero ut consequat ultrices, orci tortor congue quam, sed consectetuer enim augue at nulla.', 1, '2008-05-20 09:34:41', '2008-05-20 09:34:53', 1, 0, NULL, 0, 0, 1, 0, '', ''),
(4, 'Contact us', 'contact-us', NULL, 'publish', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nunc at quam ac lorem venenatis ullamcorper. Fusce lacinia. Suspendisse ultrices, libero ut consequat ultrices, orci tortor congue quam, sed consectetuer enim augue at nulla.', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nunc at quam ac lorem venenatis ullamcorper. Fusce lacinia. Suspendisse ultrices, libero ut consequat ultrices, orci tortor congue quam, sed consectetuer enim augue at nulla.', 1, '2008-05-20 09:36:19', '2008-05-20 09:36:19', 1, 0, NULL, 1, 0, 1, 0, '', ''),
(5, 'Contact Form', 'contact-form', 4, 'publish', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nunc at quam ac lorem venenatis ullamcorper. Fusce lacinia. Suspendisse ultrices, libero ut consequat ultrices, orci tortor congue quam, sed consectetuer enim augue at nulla.', '', 2, '2008-05-20 09:36:57', '2008-05-20 09:36:57', 1, 0, NULL, 0, 0, 1, 0, '', ''),
(6, 'Home', 'home', NULL, 'publish', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nunc at quam ac lorem venenatis ullamcorper. Fusce lacinia. Suspendisse ultrices, libero ut consequat ultrices, orci tortor congue quam, sed consectetuer enim augue at nulla. Proin placerat tincidunt eros. Nulla facilisi. Suspendisse potenti. Curabitur quis risus eu ipsum rhoncus lacinia. Sed turpis augue, blandit non, semper ac, placerat at, quam. Proin egestas ornare elit. Duis eleifend lacinia lectus. Donec ut risus ac ligula pharetra faucibus. Curabitur nec leo. Duis ac dui. Vestibulum hendrerit nisi sit amet tellus. Aenean blandit.\r\n\r\nEtiam faucibus velit semper libero. Phasellus scelerisque dolor a risus. Etiam placerat turpis in leo. Etiam ligula nisl, consectetuer nec, convallis et, vestibulum ac, sapien. Aenean gravida. Nam ultricies velit eu enim. Sed malesuada auctor neque. Nulla feugiat. Maecenas in quam. Sed vitae orci ac ligula rhoncus dictum. Nulla diam justo, laoreet a, viverra vel, dictum non, massa. Sed libero nisl, vulputate eget, tempor gravida, aliquam ac, massa.\r\n\r\nVivamus aliquet, metus at ultricies dictum, libero augue tincidunt nunc, a mollis sapien est vitae velit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec posuere. Proin nisl velit, vehicula ut, blandit eu, eleifend nec, lectus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum sodales condimentum arcu. Morbi elementum, nisl vitae accumsan mattis, augue purus pellentesque nulla, at dignissim lacus orci dapibus magna. In in felis ac est lacinia scelerisque. Duis massa mauris, ultricies id, ornare et, lobortis ut, ante. Sed viverra. Phasellus venenatis accumsan neque. Donec velit lorem, iaculis ac, faucibus quis, elementum id, mi. Donec justo elit, malesuada quis, malesuada nec, posuere in, lacus. Etiam venenatis velit ac purus. Vivamus hendrerit libero vel sapien. ', 'Etiam faucibus velit semper libero. Phasellus scelerisque dolor a risus. Etiam placerat turpis in leo. Etiam ligula nisl, consectetuer nec, convallis et, vestibulum ac, sapien. ', 3, '2008-05-20 09:38:21', '2008-05-20 09:43:47', 1, 0, NULL, 1, 1, 1, 0, '', '');

-- --------------------------------------------------------

--
-- Table structure for table `page_page_content_hilight`
--

CREATE TABLE IF NOT EXISTS `page_page_content_hilight` (
  `id` int(11) NOT NULL auto_increment,
  `page_id` int(11) NOT NULL,
  `content_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `page_id` (`page_id`,`content_id`),
  KEY `content_id_refs_id_25d896a2` (`content_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `page_page_content_hilight`
--


-- --------------------------------------------------------

--
-- Table structure for table `page_page_extra_content`
--

CREATE TABLE IF NOT EXISTS `page_page_extra_content` (
  `id` int(11) NOT NULL auto_increment,
  `page_id` int(11) NOT NULL,
  `content_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `page_id` (`page_id`,`content_id`),
  KEY `content_id_refs_id_29d34599` (`content_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `page_page_extra_content`
--


-- --------------------------------------------------------

--
-- Table structure for table `page_page_media`
--

CREATE TABLE IF NOT EXISTS `page_page_media` (
  `id` int(11) NOT NULL auto_increment,
  `page_id` int(11) NOT NULL,
  `media_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `page_id` (`page_id`,`media_id`),
  KEY `media_id_refs_id_6f3679d6` (`media_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `page_page_media`
--


-- --------------------------------------------------------

--
-- Table structure for table `page_page_similar_pages`
--

CREATE TABLE IF NOT EXISTS `page_page_similar_pages` (
  `id` int(11) NOT NULL auto_increment,
  `from_page_id` int(11) NOT NULL,
  `to_page_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `from_page_id` (`from_page_id`,`to_page_id`),
  KEY `to_page_id_refs_id_2984c236` (`to_page_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `page_page_similar_pages`
--

INSERT INTO `page_page_similar_pages` (`id`, `from_page_id`, `to_page_id`) VALUES
(1, 3, 2),
(2, 2, 3);

-- --------------------------------------------------------

--
-- Table structure for table `page_type`
--

CREATE TABLE IF NOT EXISTS `page_type` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `created` datetime NOT NULL,
  `modified` datetime NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `page_type`
--


-- --------------------------------------------------------

--
-- Table structure for table `profiles_profile`
--

CREATE TABLE IF NOT EXISTS `profiles_profile` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `profile_text` longtext NOT NULL,
  `url` varchar(200) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `profiles_profile_user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `profiles_profile`
--


-- --------------------------------------------------------

--
-- Table structure for table `tagging_tag`
--

CREATE TABLE IF NOT EXISTS `tagging_tag` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `tagging_tag_name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `tagging_tag`
--


-- --------------------------------------------------------

--
-- Table structure for table `tagging_taggeditem`
--

CREATE TABLE IF NOT EXISTS `tagging_taggeditem` (
  `id` int(11) NOT NULL auto_increment,
  `tag_id` int(11) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `object_id` int(10) unsigned NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `tag_id` (`tag_id`,`content_type_id`,`object_id`),
  KEY `tagging_taggeditem_tag_id` (`tag_id`),
  KEY `tagging_taggeditem_content_type_id` (`content_type_id`),
  KEY `tagging_taggeditem_object_id` (`object_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `tagging_taggeditem`
--


-- --------------------------------------------------------

--
-- Table structure for table `votes`
--

CREATE TABLE IF NOT EXISTS `votes` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `object_id` int(10) unsigned NOT NULL,
  `vote` smallint(6) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`content_type_id`,`object_id`),
  KEY `votes_user_id` (`user_id`),
  KEY `votes_content_type_id` (`content_type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `votes`
--

