#!/usr/bin/python
# -*- coding: utf-8 -*-

# Скрипт для удаление сохранений на кириллице в игре S.T.A.L.K.E.R.
# Все информации об обновлении/ошибки, и инструкция в файле readme.txt.

import os

LETTERS = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
		 		'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 
		 		'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я')

# Путь к сохранениям. Указываем путь до файла.
saves = r'D:\Games\S.T.A.L.K.E.R. - Объединенный Пак 2\appdata\savedgames'

# Открываем файлы.
for top, dirs, files in os.walk(saves):
	print(f'Общее количество файлов - {len(files)}.')
	for name in files:
		
		# Проверяем файлы на кириллицу.
		for letter in LETTERS:
			if letter in name:

				# Если файл на кириллице, тогда удаляем.
				print(f'{name} - удалена.')
				os.remove(os.path.join(saves, name))
				break

# Некорректно работает.
# print(f'Количество файлов после удаление - {len(files)}.')
