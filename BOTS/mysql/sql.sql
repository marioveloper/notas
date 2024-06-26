CREATE TABLE `users` (
 `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
 `telegram_id` varchar(255) DEFAULT NULL,
 `firstname` varchar(255) DEFAULT NULL,
 `username` varchar(255) DEFAULT NULL,
 `referred_by` varchar(255) DEFAULT NULL,
 `invite_link` varchar(255) DEFAULT NULL,
 `rank` varchar(255) DEFAULT 'none',
 `wallet` varchar(255) DEFAULT 'none',
 `referrals` int(11) DEFAULT 0,
 `status` int(11) DEFAULT 0,
 `active` int(11) DEFAULT 0,
 PRIMARY KEY (`id`),
 UNIQUE KEY `telegram_id` (`telegram_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4

CREATE TABLE `investments` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `date` date NOT NULL,
 `user_id` int(11) unsigned NOT NULL,
 `succes` int(11) unsigned DEFAULT 0,
 PRIMARY KEY (`id`),
 KEY `user_id` (`user_id`),
 CONSTRAINT `investments_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4

CREATE TRIGGER activar_usuario
AFTER INSERT
ON investments
FOR EACH ROW
UPDATE users u
INNER JOIN investments i
SET active = 1
WHERE u.id = i.user_id;

$$DELIMITER
CREATE TRIGGER desactivar_usuario
AFTER UPDATE
ON investments
FOR EACH ROW
IF NEW.succes = 1
THEN
UPDATE users
SET active = 0
WHERE id = user_id
END IF;
END; $$