import os

# Путь к директории с .md файлами
main_directory = 'data/GPB/'

# Проходим по всем файлам в main_directory
for root, dirs, files in os.walk(main_directory):
    for file in files:
        if file.endswith('.md'):
            input_file_path = os.path.join(root, file)
            
            # Создаем директорию для сохранения таблиц, если она не существует
            output_directory = f"{root}_table/"
            os.makedirs(output_directory, exist_ok=True)
            
            # Читаем содержимое файла
            with open(input_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Разделяем содержимое на строки
            lines = content.splitlines()
            table = []
            table_counter = 1  # Счетчик для нумерации таблиц
            
            for line in lines:
                # Проверяем, является ли строка заголовком таблицы
                if line.startswith('|'):
                    table.append(line)  # Добавляем строку таблицы
                elif table:  # Если мы уже начали собирать таблицу
                    # Проверяем, если строка не является частью таблицы
                    if line.strip() == '' or not line.startswith('|'):
                        # Сохраняем таблицу в файл, если она не пустая
                        if table:
                            # Создаем имя файла для сохранения таблицы с номером
                            base_name = os.path.splitext(os.path.basename(input_file_path))[0]
                            new_file_name = f"{base_name}_table_{table_counter}.md"
                            new_file_path = os.path.join(output_directory, new_file_name)
                            
                            # Сохраняем таблицу в новый файл
                            with open(new_file_path, 'w', encoding='utf-8') as table_file:
                                table_file.write('\n'.join(table) + '\n')
                            
                            print(f"Таблица {table_counter} из файла {file} сохранена в {new_file_name}.")
                            table_counter += 1  # Увеличиваем счетчик таблиц
                        table = []  # Сбрасываем таблицу для следующей
                        
            # Проверяем, осталась ли таблица после окончания цикла
            if table:
                new_file_name = f"{base_name}_table_{table_counter}.md"
                new_file_path = os.path.join(output_directory, new_file_name)
                with open(new_file_path, 'w', encoding='utf-8') as table_file:
                    table_file.write('\n'.join(table) + '\n')
                print(f"Таблица {table_counter} из файла {file} сохранена в {new_file_name}.")

print("Обработка всех файлов завершена!")
