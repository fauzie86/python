def count_words(input_file_path, output_file_path):
    try:
 
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            content = input_file.read()

      
        word_count = len(content.split())

      
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(str(word_count))

        print(f"Word count: {word_count} words. Result written to {output_file_path}")

    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


input_file_path = 'input.txt'
output_file_path = 'word_count.txt'
count_words(input_file_path, output_file_path)


