-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-03-2023 a las 00:05:08
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_objetos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `objetos`
--

CREATE TABLE `objetos` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(100) NOT NULL,
  `OBJ_DESCRIPCION` varchar(255) NOT NULL,
  `TIPO` varchar(100) NOT NULL,
  `PRECIO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `objetos`
--

INSERT INTO `objetos` (`ID`, `NOMBRE`, `OBJ_DESCRIPCION`, `TIPO`, `PRECIO`) VALUES
(3, 'Cas. Dentado', 'Objeto que debe llevar un Pokemon.\r\nSi el Pokemon que lleva el objeto es golpeado por un movimiento que hace contacto, infligira un daño al atacante igual al 16,67% de sus PS por golpe.', 'Equipable', 63000),
(4, 'Restos', 'Objeto que debe llevar un Pokemon.\r\nDurante el combate, restaura los PS un 6,25% del Pokemon que lo lleva al final del turno.', 'Equipable', 33000),
(7, 'Pokeball', 'Dispositivo con diseño capsular que atrapa Pokemon salvajes. Se lanza como una bola contra el blanco.', 'Pokeball', 200),
(9, 'Baya Alcho', 'Si la lleva un Pokemon, debilita un ataque supereficaz de tipo Roca de un enemigo.', 'Bayas', 1100),
(10, 'MT-Imagen', 'Ataca con el doble de potencia si el usuario esta quemado, paralizado o envenenado.', 'MT', 20000),
(16, 'Baya Aranja', 'Los pokemon pueden llevarla o usarla para restaurar 10 PS', 'Bayas', 450),
(17, 'Baya Meloc', 'Los pokemon pueden llevarla o usarla para curarse del envenenamiento', 'Bayas', 400),
(18, 'Globo Helio', 'El Pokemon que lo lleve flotara en el aire. Si recibe un golpe, estallara', 'Equipable', 100),
(19, 'Sustituto', 'Utiliza parte de los PS propios para crear un sustituto que actua como señuelo', 'MT', 30000),
(20, 'Triataque', 'Ataque triple que puede paralizar, quemar o congelar al objetivo.', 'MT', 25000),
(21, 'Superball', 'Pokeball de alto rendimiento.\r\nTiene un indice de exito superior al de la Pokeball.', 'Pokeball', 600),
(22, 'Ultraball', 'Pokeball de alto rendimiento superior.\r\nTiene un indice de exito mayor al de la superball.', 'Pokeball', 1200),
(23, 'Antiparaliz', 'Medicina en espray que cura un pokemon paralizado.', 'Curacion', 300),
(24, 'Carameloraro', 'Caramelo energetico que sube a un pokemon de nivel.', 'Curacion', 10500),
(25, 'Pocion', 'Medicina es espray que cura heridas y restaura 20PS a un Pokemon.', 'Curacion', 200),
(26, 'Ataque X', 'Aumenta el Ataque en combate.\r\nAl cambiar de Pokemon, el efecto desaparece.', 'Combate', 2000),
(27, 'Defensa X', 'Aumenta la Defensa en combate.\r\nAl cambiar de Pokemon, el efecto desaparece.', 'Combate', 2500),
(28, 'Precision X', 'Aumenta la Precision de los ataques en combate.\r\nAl cambiar de Pokemon, el efecto desaparece.', 'Combate', 1500);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `objetos`
--
ALTER TABLE `objetos`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `objetos`
--
ALTER TABLE `objetos`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
