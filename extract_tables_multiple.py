import os
import re 

main_directory = 'data/240/'

for root, dirs, files in os.walk(main_directory):
    for file in files:
        if file.endswith('.md'):
            input_file_path = os.path.join(root, file)
            with open(input_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            start_capture = False
            extracted_lines = []

            for line in lines:
                if re.search(r'\b КОМПАНИЯ\b', line) and (re.search(r'\b ТИКЕР\b', line) or re.search(r'\b2023П\b', line) or re.search(r'\bEV/REVENUE\b', line)):
                    start_capture = True
                if start_capture:
                    extracted_lines.append(line)
                if re.search(r'\b Источник:\b', line):
                    break
            if not extracted_lines:
                print(f"В файле {input_file_path} не найдены данные для извлечения.")
            base_name = os.path.splitext(os.path.basename(input_file_path))[0]
            new_file_name = f"{base_name}_valuations_gpb.md"
            new_file_path = os.path.join(root, new_file_name)

            with open(new_file_path, 'w', encoding='utf-8') as output_file:
                output_file.writelines(extracted_lines)

print("Обработка всех файлов завершена!")