-- MySQL Script generated by MySQL Workbench
-- Mon Jul 25 13:44:19 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema carsDB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema carsDB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `carsDB` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema recipedb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema recipedb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `recipedb` DEFAULT CHARACTER SET utf8mb3 ;
USE `carsDB` ;

-- -----------------------------------------------------
-- Table `carsDB`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `carsDB`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `updated_date` DATETIME NULL,
  `created_date` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `carsDB`.`cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `carsDB`.`cars` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `make` VARCHAR(45) NULL,
  `model` VARCHAR(45) NULL,
  `price` INT NULL,
  `description` VARCHAR(45) NULL,
  `isPurchased` TINYINT NULL,
  `year` INT NULL,
  `created_date` DATETIME NULL,
  `updated_date` DATETIME NULL,
  `user_id` INT NOT NULL,
  `buyer_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_cars_users_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_cars_users1_idx` (`buyer_id` ASC) VISIBLE,
  CONSTRAINT `fk_cars_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `carsDB`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cars_users1`
    FOREIGN KEY (`buyer_id`)
    REFERENCES `carsDB`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `recipedb` ;

-- -----------------------------------------------------
-- Table `recipedb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipedb`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(30) NULL DEFAULT NULL,
  `last_name` VARCHAR(30) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `created_date` DATETIME NULL DEFAULT NULL,
  `updated_date` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `recipedb`.`recipes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recipedb`.`recipes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `description` TINYTEXT NULL DEFAULT NULL,
  `instructions` MEDIUMTEXT NULL DEFAULT NULL,
  `under30` TINYINT NULL DEFAULT NULL,
  `created_date` DATETIME NULL DEFAULT NULL,
  `updated_date` DATETIME NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_recipes_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_recipes_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `recipedb`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
