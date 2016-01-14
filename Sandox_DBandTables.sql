CREATE DATABASE `sandbox` /*!40100 DEFAULT CHARACTER SET utf8 */;
CREATE TABLE `employees` (
    `EmployeeID` INT(11) NOT NULL AUTO_INCREMENT,
    `LastName` VARCHAR(20) NOT NULL,
    `FirstName` VARCHAR(10) NOT NULL,
    `Title` VARCHAR(30) DEFAULT NULL,
    `TitleOfCourtesy` VARCHAR(25) DEFAULT NULL,
    `BirthDate` DATETIME DEFAULT NULL,
    `HireDate` DATETIME DEFAULT NULL,
    `Address` VARCHAR(60) DEFAULT NULL,
    `City` VARCHAR(15) DEFAULT NULL,
    `Region` VARCHAR(15) DEFAULT NULL,
    `PostalCode` VARCHAR(10) DEFAULT NULL,
    `Country` VARCHAR(15) DEFAULT NULL,
    `HomePhone` VARCHAR(24) DEFAULT NULL,
    `Extension` VARCHAR(4) DEFAULT NULL,
    `Photo` LONGBLOB,
    `Notes` MEDIUMTEXT NOT NULL,
    `ReportsTo` INT(11) DEFAULT NULL,
    `PhotoPath` VARCHAR(255) DEFAULT NULL,
    `Salary` FLOAT DEFAULT NULL,
    PRIMARY KEY (`EmployeeID`),
    KEY `LastName` (`LastName`),
    KEY `PostalCode` (`PostalCode`),
    KEY `FK_Employees_Employees` (`ReportsTo`)
)  ENGINE=INNODB AUTO_INCREMENT=10 DEFAULT CHARSET=UTF8;

CREATE TABLE `orderdetails` (
    `OrderID` INT(11) NOT NULL,
    `ProductID` INT(11) NOT NULL,
    `UnitPrice` DECIMAL(10 , 4 ) NOT NULL DEFAULT '0.0000',
    `Quantity` SMALLINT(2) NOT NULL DEFAULT '1',
    `Discount` DOUBLE(8 , 0 ) NOT NULL DEFAULT '0',
    PRIMARY KEY (`OrderID` , `ProductID`)
)  ENGINE=INNODB DEFAULT CHARSET=UTF8;

CREATE TABLE `orders` (
    `OrderID` INT(11) NOT NULL AUTO_INCREMENT,
    `CustomerID` VARCHAR(5) DEFAULT NULL,
    `EmployeeID` INT(11) DEFAULT NULL,
    `OrderDate` DATETIME DEFAULT NULL,
    `RequiredDate` DATETIME DEFAULT NULL,
    `ShippedDate` DATETIME DEFAULT NULL,
    `ShipVia` INT(11) DEFAULT NULL,
    `Freight` DECIMAL(10 , 4 ) DEFAULT '0.0000',
    `ShipName` VARCHAR(40) DEFAULT NULL,
    `ShipAddress` VARCHAR(60) DEFAULT NULL,
    `ShipCity` VARCHAR(15) DEFAULT NULL,
    `ShipRegion` VARCHAR(15) DEFAULT NULL,
    `ShipPostalCode` VARCHAR(10) DEFAULT NULL,
    `ShipCountry` VARCHAR(15) DEFAULT NULL,
    PRIMARY KEY (`OrderID`),
    KEY `OrderDate` (`OrderDate`),
    KEY `ShippedDate` (`ShippedDate`),
    KEY `ShipPostalCode` (`ShipPostalCode`),
    KEY `FK_Orders_Customers` (`CustomerID`),
    KEY `FK_Orders_Employees` (`EmployeeID`),
    KEY `FK_Orders_Shippers` (`ShipVia`)
)  ENGINE=INNODB AUTO_INCREMENT=11078 DEFAULT CHARSET=UTF8;


CREATE TABLE `customers` (
    `CustomerID` VARCHAR(5) NOT NULL,
    `CompanyName` VARCHAR(40) NOT NULL,
    `ContactName` VARCHAR(30) DEFAULT NULL,
    `ContactTitle` VARCHAR(30) DEFAULT NULL,
    `Address` VARCHAR(60) DEFAULT NULL,
    `City` VARCHAR(15) DEFAULT NULL,
    `Region` VARCHAR(15) DEFAULT NULL,
    `PostalCode` VARCHAR(10) DEFAULT NULL,
    `Country` VARCHAR(15) DEFAULT NULL,
    `Phone` VARCHAR(24) DEFAULT NULL,
    `Fax` VARCHAR(24) DEFAULT NULL,
    PRIMARY KEY (`CustomerID`),
    KEY `City` (`City`),
    KEY `CompanyName` (`CompanyName`),
    KEY `PostalCode` (`PostalCode`),
    KEY `Region` (`Region`)
)  ENGINE=INNODB DEFAULT CHARSET=UTF8;



