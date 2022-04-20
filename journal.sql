-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Апр 06 2022 г., 18:44
-- Версия сервера: 8.0.24
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `journal`
--

-- --------------------------------------------------------

--
-- Структура таблицы `amendments`
--

CREATE TABLE `amendments` (
  `id` int NOT NULL,
  `jourmal_id` int NOT NULL,
  `meters` int NOT NULL,
  `amendment` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Структура таблицы `journals`
--

CREATE TABLE `journals` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `note` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Структура таблицы `roles`
--

CREATE TABLE `roles` (
  `id` int NOT NULL,
  `role` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Дамп данных таблицы `roles`
--

INSERT INTO `roles` (`id`, `role`) VALUES
(1, 'admin'),
(2, 'user');

-- --------------------------------------------------------

--
-- Структура таблицы `stations`
--

CREATE TABLE `stations` (
  `id` int NOT NULL,
  `jourmal_id` int NOT NULL,
  `number` int NOT NULL,
  `level` float NOT NULL,
  `sighting_point1` int NOT NULL,
  `sighting_point2` int NOT NULL,
  `sighting_point3` int NOT NULL,
  `sighting_point4` int NOT NULL,
  `horizontal_L_R1` tinyint(1) NOT NULL,
  `horizontal_L_R2` tinyint(1) NOT NULL,
  `horizontal_L_R3` tinyint(1) NOT NULL,
  `horizontal_L_R4` tinyint(1) NOT NULL,
  `horizontal_degree1` int NOT NULL,
  `horizontal_minute1` float NOT NULL,
  `horizontal_degree2` int NOT NULL,
  `horizontal_minute2` float NOT NULL,
  `horizontal_degree3` int NOT NULL,
  `horizontal_minute3` float NOT NULL,
  `horizontal_degree4` int NOT NULL,
  `horizontal_minute4` float NOT NULL,
  `level1` float DEFAULT NULL,
  `level2` float DEFAULT NULL,
  `vertical_L_R1` tinyint(1) DEFAULT NULL,
  `vertical_L_R2` tinyint(1) DEFAULT NULL,
  `vertical_degree1` int DEFAULT NULL,
  `vertical_minute1` float DEFAULT NULL,
  `vertical_degree2` int DEFAULT NULL,
  `vertical_minute2` float DEFAULT NULL,
  `by_rail1` float DEFAULT NULL,
  `by_rail2` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `login` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` int NOT NULL,
  `mail` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `login`, `password`, `role`, `mail`) VALUES
(1, 'Admin', 'password', 1, 'Mail@mail.com');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `amendments`
--
ALTER TABLE `amendments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `jourmal_id` (`jourmal_id`);

--
-- Индексы таблицы `journals`
--
ALTER TABLE `journals`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Индексы таблицы `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `stations`
--
ALTER TABLE `stations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `jourmal_id` (`jourmal_id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `role` (`role`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `amendments`
--
ALTER TABLE `amendments`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `journals`
--
ALTER TABLE `journals`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `stations`
--
ALTER TABLE `stations`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `amendments`
--
ALTER TABLE `amendments`
  ADD CONSTRAINT `amendments_ibfk_1` FOREIGN KEY (`jourmal_id`) REFERENCES `journals` (`id`);

--
-- Ограничения внешнего ключа таблицы `journals`
--
ALTER TABLE `journals`
  ADD CONSTRAINT `journals_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Ограничения внешнего ключа таблицы `stations`
--
ALTER TABLE `stations`
  ADD CONSTRAINT `stations_ibfk_1` FOREIGN KEY (`jourmal_id`) REFERENCES `journals` (`id`);

--
-- Ограничения внешнего ключа таблицы `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role`) REFERENCES `roles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
