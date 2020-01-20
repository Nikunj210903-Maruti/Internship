use Wotnot

CREATE TABLE `channel_vendor` (
  `name` varchar(45) DEFAULT NULL,
  `channel_id` bigint(20) NOT NULL,
  `created_at` datetime(3) DEFAULT NULL,
  `modified_at` datetime(3) DEFAULT NULL,
  `created_by` bigint(20) unsigned NOT NULL,
  `modified_by` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`channel_id`),
  KEY `fk_modified_by_user_id` (`modified_by`),
  KEY `fk_created_by_user_id` (`created_by`),
  CONSTRAINT `fk_modified_by_user_id` FOREIGN KEY (`modified_by`) REFERENCES `user` (`id`),
  CONSTRAINT `fk_created_by_user_id` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `whatsapp_channel_configuration` (
  `id` bigint(20) unsigned NOT NULL,
  `channel_vendor_id` bigint(20) DEFAULT NULL,
  `bot_id` bigint(20) DEFAULT NULL,
  `bot_phone_number` bigint(11) DEFAULT NULL,
  `webhook_key` varchar(40) DEFAULT NULL,
  `auth_details` varchar(100) DEFAULT NULL,
  `created_at` datetime(3) DEFAULT NULL,
  `modified_at` datetime(3) DEFAULT NULL,
  `created_by` bigint(20) unsigned NOT NULL,
  `modified_by` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bot_id_UNIQUE` (`bot_id`),
  UNIQUE KEY `whatsapp_number_UNIQUE` (`bot_phone_number`),
  KEY `created_by` (`created_by`),
  KEY `modified_by` (`modified_by`),
  KEY `fk_channel_vendor_id` (`channel_vendor_id`),
  CONSTRAINT `fk_channel_vendor_id` FOREIGN KEY (`channel_vendor_id`) REFERENCES `channel_vendor` (`channel_id`),
  CONSTRAINT `whatsapp_channel_configuration_ibfk_1` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`),
  CONSTRAINT `whatsapp_channel_configuration_ibfk_2` FOREIGN KEY (`modified_by`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `channel` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `created_at` datetime(3) NOT NULL,
  `modified_at` datetime(3) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_channel_name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

CREATE TABLE `user` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `first_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `last_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image_name` varchar(50) DEFAULT NULL,
  `contact` varchar(50) DEFAULT NULL,
  `is_unsubscribe` tinyint(1) NOT NULL DEFAULT '0',
  `created_by` bigint(20) unsigned DEFAULT NULL,
  `created_at` datetime(3) NOT NULL,
  `modified_by` bigint(20) unsigned DEFAULT NULL,
  `modified_at` datetime(3) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_email` (`email`),
  KEY `fk_user_type_master_id` (`user_type_master_id`),
  KEY `fk_user_created_by_idx` (`created_by`),
  KEY `fk_user_modified_by_idx` (`modified_by`),
  CONSTRAINT `fk_user_created_by` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`),
  CONSTRAINT `fk_user_modified_by` FOREIGN KEY (`modified_by`) REFERENCES `user` (`id`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `channel_configuration` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `bot_lead_id` bigint(20) unsigned NOT NULL,
  `channel_id` bigint(20) unsigned NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '0',
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint(20) unsigned DEFAULT NULL,
  `modified_at` datetime(3) NOT NULL,
  `modified_by` bigint(20) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_channel_configuration_bot_lead_channel_id` (`bot_lead_id`,`channel_id`),
  KEY `fk_channel_configuration_channel_id` (`channel_id`),
  KEY `fk_channel_configuration_created_by` (`created_by`),
  KEY `fk_channel_configuration_modified_by` (`modified_by`),
  CONSTRAINT `fk_channel_configuration_bot_lead_id` FOREIGN KEY (`bot_lead_id`) REFERENCES `bot_lead` (`id`),
  CONSTRAINT `fk_channel_configuration_channel_id` FOREIGN KEY (`channel_id`) REFERENCES `channel` (`id`),
  CONSTRAINT `fk_channel_configuration_created_by` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`),
  CONSTRAINT `fk_channel_configuration_modified_by` FOREIGN KEY (`modified_by`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;

INSERT INTO `channel` (`name`, `created_at`, `modified_at`) VALUES ('WhatsApp', '2019-12-30T12:45', '2019-12-30T12:45');

INSERT INTO `channel_vendor` (`name`, `channel_id`, `created_at`, `modified_at`, `created_by`, `modified_by`) VALUES ('Karix', '1', '2019-12-30T12:45', '2019-12-30T12:45', '1', '1');


