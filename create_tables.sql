DROP TABLE IF EXISTS `transactions`;
DROP TABLE IF EXISTS `transactions_items`;
DROP TABLE IF EXISTS `clicks`;
DROP TABLE IF EXISTS `pageviews_tags`;
DROP TABLE IF EXISTS `pageviews`;
DROP TABLE IF EXISTS `impressions`;
DROP TABLE IF EXISTS `impressions_products`;

CREATE TABLE `transactions` (
	`type`	TEXT,
	`paymentType`	TEXT,
	`id`	INTEGER UNIQUE,
	`info_browserId`	INTEGER,
	`info_browser`	TEXT,
	`info_os`	TEXT,
	`info_geoIPLongitude`	NUMERIC,
	`info_geoIPLatitude`	NUMERIC,
	`info_source`	TEXT,
	`ab`	TEXT,
	`timestamp`	TEXT
);

CREATE TABLE `transactions_items` (
	`id`	INTEGER,
	`items_id`	INTEGER,
	`items_price`	NUMERIC,
	`items_quantity`	INTEGER
);

CREATE TABLE `clicks` (
	`type`	TEXT,
	`feature`	INTEGER,
	`vrlId`	INTEGER,
	`product`	INTEGER,
	`id`	INTEGER,
	`info_browserId`	INTEGER,
	`info_browser`	TEXT,
	`info_os`	TEXT,
	`info_geoIPLongitude`	NUMERIC,
	`info_geoIPLatitude`	NUMERIC,
	`info_source`	TEXT,
	`ab`	TEXT,
	`page`	TEXT,
	`timestamp`	TEXT
);

CREATE TABLE `impressions` (
	`type`	TEXT,
	`feature`	INTEGER,
	`vrlId`	INTEGER,
	`id`	INTEGER,
	`info_browserId`	INTEGER,
	`info_browser`	TEXT,
	`info_os`	TEXT,
	`info_geoIPLongitude`	NUMERIC,
	`info_geoIPLatitude`	NUMERIC,
	`info_source`	TEXT,
	`ab`	TEXT,
	`page`	TEXT,
	`algRef`	INTEGER,
	`my_id` INTEGER UNIQUE,
	`timestamp`	TEXT
);

CREATE TABLE `impressions_products` (
	`my_id`    INTEGER,
	`products`  INTEGER
);

CREATE TABLE `pageviews` (
	`type`    TEXT,
	`name`    TEXT,
	`id`    INTEGER,
	`info_browserId`    INTEGER,
	`info_browser`    TEXT,
	`info_os`    TEXT,
	`info_geoIPLongitude`    NUMERIC,
	`info_geoIPLatitude`    NUMERIC,
	`info_source`    TEXT,
	`ab`    TEXT,
	`my_id` INTEGER UNIQUE,
	`timestamp`    TEXT
);

CREATE TABLE `pageviews_tags` (
	`my_id`    INTEGER,
	`tags`    INTEGER
);
