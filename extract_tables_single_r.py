import os 
input_file_path = 'data/240/GPB_EQ_Navigator_20240109/GPB_EQ_Navigator_20240109.md'
with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

start_capture = False
extracted_lines = []

for line in lines:
    cleaned_line = line.strip().lower()
    if "компания" in cleaned_line and "тикер" in cleaned_line:
        start_capture = True
    if start_capture:
        extracted_lines.append(line)
    if "Источник:" in line:
        break

base_name = os.path.splitext(os.path.basename(input_file_path))[0]
new_file_name = f"{base_name}_valuations_gpb.md"
new_file_path = os.path.join(os.path.dirname(input_file_path), new_file_name)
with open(new_file_path, 'w', encoding='utf-8') as output_file:
    output_file.writelines(extracted_lines)

print("Данные успешно извлечены!")