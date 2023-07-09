import re

file_path = 'links.txt'  # Замените на фактический путь к вашему файлу

def convert_links_to_intent(file_path):
    # Открываем файл для чтения
    new_file = ''
    with open(file_path, 'r') as file:
        for line in file:
            if re.match(r'(https?://twitter\.com/[^/]+/status/\d+)', line):
                tw_id = line.split("/")[-1]
                line = f'https://twitter.com/intent/like?tweet_id={tw_id}'
            elif re.match(r'@(\w+)', line):
                tw_name = line.replace("@",'')
                line = f'https://twitter.com/intent/user?screen_name={tw_name}'
            elif re.match(r"https://twitter\.com/", line):
                tw_name = line.split("/")[-1]
                line = f'https://twitter.com/intent/user?screen_name={tw_name}'
            else:
                line = f'https://twitter.com/intent/user?screen_name={line}'
            new_file += line

    # Открываем файл для записи и записываем преобразованный контент
    with open(file_path, 'w') as file:
        file.write(new_file)

    print("Преобразование завершено. Ссылки были преобразованы в ссылки типа 'intent' и записаны обратно в файл.")


convert_links_to_intent(file_path)