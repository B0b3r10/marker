import os

main_directory = 'data/240/'

for root, dirs, files in os.walk(main_directory):
    for file in files:
        if file.endswith('.png') or file.endswith('.json') or file.endswith('_valuations_gpb.md'):
            file_path = os.path.join(root, file)
            os.remove(file_path)  
            print(f"Удален файл: {file_path}")

print("Удаление завершено!")