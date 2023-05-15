import os

txt_file = 'translated_text.txt'


with open(txt_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            id_ = line.split(" ")[0]
            N1 = id_.split('-')[0]
            N2 = id_.split('-')[1]
            output_folder = f'../dev-clean/LibriSpeech/dev-clean/{N1}/{N2}/'
            # id_parts = id_.split('-')
            folder_path = os.path.join(output_folder)
            os.makedirs(folder_path, exist_ok=True)
            output_file = f'{N1}-{N2}.fr.txt'
            output_path = os.path.join(folder_path, output_file)
            with open(output_path, 'a', encoding='utf-8') as output:
                output.write(line + '\n')