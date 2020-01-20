DROP TABLE IF EXISTS `vessel`;
CREATE TABLE `vessel`
(
   `id`          INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
   `name`        VARCHAR(100)     NOT NULL,
   `mmsi`        CHAR(9)          NOT NULL COMMENT ' Maritime Mobile Service Identity (MMSI)',
   `imo`         CHAR(7)          NOT NULL COMMENT ' International Maritime Organization (IMO)',
   `description`  VARCHAR(250) DEFAULT NULL,
   `created_by`  BIGINT(20) UNSIGNED DEFAULT NULL,
   `created_at`  DATETIME(3)      NOT NULL,
   `modified_by` BIGINT(20) UNSIGNED DEFAULT NULL,
   `modified_at` DATETIME(3)      NOT NULL,
   PRIMARY KEY (`id`),
   UNIQUE KEY `uk_vessel` (`name`, `mmsi`, `imo`),
   KEY `fk_vessel_created_by_user_id` (`created_by`),
   KEY `fk_vessel_modified_by_user_id` (`modified_by`),
   CONSTRAINT `fk_vessel_created_by_user_id` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`),
   CONSTRAINT `fk_vessel_modified_by_user_id` FOREIGN KEY (`modified_by`) REFERENCES `user` (`id`)
) ENGINE = INNODB
 DEFAULT CHARSET = LATIN1;

DROP TABLE IF EXISTS `company_vessel`;
CREATE TABLE `company_vessel`
(
   `id`          BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
   `company_id`  INT(10) UNSIGNED    NOT NULL,
   `vessel_id`   INT(10) UNSIGNED    NOT NULL,
   `created_by`  BIGINT(20) UNSIGNED DEFAULT NULL,
   `created_at`  DATETIME(3)         NOT NULL,
   `modified_by` BIGINT(20) UNSIGNED DEFAULT NULL,
   `modified_at` DATETIME(3)         NOT NULL,
   PRIMARY KEY (`id`),
   UNIQUE KEY `uk_company_vessel` (`company_id`, `vessel_id`),
   KEY `fk_company_vessel_created_by_user_id` (`created_by`),
   KEY `fk_company_vessel_modified_by_user_id` (`modified_by`),
   KEY `fk_company_vessel_company_id` (`company_id`),
   KEY `fk_company_vessel_vessel_id` (`vessel_id`),
   CONSTRAINT `fk_company_vessel_created_by_user_id` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`),
   CONSTRAINT `fk_company_vessel_modified_by_user_id` FOREIGN KEY (`modified_by`) REFERENCES `user` (`id`),
   CONSTRAINT `fk_company_vessel_company_id` FOREIGN KEY (`company_id`) REFERENCES `company` (`id`),
   CONSTRAINT `fk_company_vessel_vessel_id` FOREIGN KEY (`vessel_id`) REFERENCES `vessel` (`id`)
) ENGINE = INNODB
 DEFAULT CHARSET = LATIN1;

DROP TABLE IF EXISTS `vessel_noon_report`;
CREATE TABLE `vessel_noon_report`
(
   `id`          BIGINT(20) UNSIGNED                                                                      NOT NULL AUTO_INCREMENT,
   `vessel_id`   INT(10) UNSIGNED                                                                         NOT NULL,
   `type`        enum ('speed_fuel_consumption_param','navigation_param','engine_param','tank_rob_param') NOT NULL,
   `value`       JSON                                                                                     NOT NULL,
   `report_date` DATE                                                                                     NOT NULL,
   `created_by`  BIGINT(20) UNSIGNED DEFAULT NULL,
   `created_at`  DATETIME(3)                                                                              NOT NULL,
   `modified_by` BIGINT(20) UNSIGNED DEFAULT NULL,
   `modified_at` DATETIME(3)                                                                              NOT NULL,
   PRIMARY KEY (`id`),
   UNIQUE KEY `uk_vessel_noon_report` (`vessel_id`, `type`, `report_date`),
   KEY `fk_vessel_noon_report_created_by_user_id` (`created_by`),
   KEY `fk_vessel_noon_report_modified_by_user_id` (`modified_by`),
   KEY `fk_vessel_noon_report_vessel_id` (`vessel_id`),
   CONSTRAINT `fk_vessel_noon_report_created_by_user_id` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`),
   CONSTRAINT `fk_vessel_noon_report_modified_by_user_id` FOREIGN KEY (`modified_by`) REFERENCES `user` (`id`),
   CONSTRAINT `fk_vessel_noon_report_vessel_id` FOREIGN KEY (`vessel_id`) REFERENCES `vessel` (`id`)
) ENGINE = INNODB
 DEFAULT CHARSET = LATIN1;


DROP TABLE IF EXISTS `already_read_eid`;
CREATE TABLE `already_read_eid` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `e_id` bigint(20) DEFAULT NULL,
  `inserted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO `EmailParser`.`noon_report_base_parameter`(`type`,`params`) VALUES ('Speed & Fuel consumption data', '["SOG (knots)", "SOW (knots)", "Total HFO consumption (mT)", "ME HFO Consumption (mT)", "GE HFO Consumption (mT)", "Boiler HFO consumption (mT)", "Total MGO consumption (mT)", "ME MGO Consumption (mT)", "GE MGO Consumption (mT)", "Boiler MGO consumption (mT)", "IGG MGO consumption (mT)", "ME SFOC (gm/kWhr)"]');
INSERT INTO `EmailParser`.`noon_report_base_parameter`(`type`,`params`) VALUES ('Navigation parameters', '["Distance through Water (miles)", "Distance over Ground (miles)", "Vessel Heading", "Course over Ground", "Wind Speed (True)", "Wind Direction (True)", "Wave Height (Significant)", "Wave Direction (True)","Current Speed", "Current Direction (True)", "Current Effect"]');
INSERT INTO `EmailParser`.`noon_report_base_parameter`(`type`,`params`) VALUES ('ME parameters', '["ME shaft power (kW)", "ME RPM", "ME slip", "A/E 1 Power (kW)", "A/E 2 Power (kW)", "A/E 3 Power (kW)", "M/E RH", "A/E 1 RH", "A/E 2 RH", "A/E 3 RH", "Boiler 1 RH", "Boiler 2 RH"]');
INSERT INTO `EmailParser`.`noon_report_base_parameter`(`type`,`params`) VALUES ('ROBs', '["HFO ROB (mT)", "MGO ROB (mT)", "LSFO ROB (mT)", "FW ROB (mT)", "CYL Oil ROB (liters)", "ME Sump LO ROB (litres)", "AE Sump LO ROB (litres)"]')
