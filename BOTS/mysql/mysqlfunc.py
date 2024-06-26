from config import *
import mysql.connector

conexion = mysql.connector.connect(host="bxczsjrrbainic4mxmh2-mysql.services.clever-cloud.com", user="ux9dsrbwg2lfmx8c", password="WcwdtMlxokWcnpZ1wcKk", port="3306", database="bxczsjrrbainic4mxmh2")
cursor = conexion.cursor()

query = """CREATE TABLE `investments` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `date` date NOT NULL,
 `user_id` int(11) unsigned NOT NULL,
 `succes` int(11) unsigned DEFAULT 0,
 PRIMARY KEY (`id`),
 KEY `user_id` (`user_id`),
 CONSTRAINT `investments_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"""
cursor.execute(query)
conexion.commit()
print(conexion)