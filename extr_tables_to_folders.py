import os

main_directory = 'data/240/'

for root, dirs, files in os.walk(main_directory):
    for file in files:
        if file.endswith('.md'):
            input_file_path = os.path.join(root, file)
            
            with open(input_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            lines = content.splitlines()
            table = []
            table_counter = 1  
            
            for line in lines:
                if line.startswith('|'):
                    table.append(line)  
                elif table:  
                    if line.strip() == '' or not line.startswith('|'):
                        if table:
                            folder_name = os.path.splitext(file)[0]  
                            output_directory = os.path.join(root, folder_name)
                            os.makedirs(output_directory, exist_ok=True)  
                            new_file_name = f"{folder_name}_table_{table_counter}.md"
                            new_file_path = os.path.join(output_directory, new_file_name)
                            with open(new_file_path, 'w', encoding='utf-8') as table_file:
                                table_file.write('\n'.join(table) + '\n')
                            
                            print(f"Таблица {table_counter} из файла {file} сохранена в {new_file_name}.")
                            table_counter += 1  
                        table = [] 
            if table:
                folder_name = os.path.splitext(file)[0]
                output_directory = os.path.join(root, folder_name)
                os.makedirs(output_directory, exist_ok=True)
                
                new_file_name = f"{folder_name}_table_{table_counter}.md"
                new_file_path = os.path.join(output_directory, new_file_name)
                with open(new_file_path, 'w', encoding='utf-8') as table_file:
                    table_file.write('\n'.join(table) + '\n')
                print(f"Таблица {table_counter} из файла {file} сохранена в {new_file_name}.")

print("Обработка всех файлов завершена!")
