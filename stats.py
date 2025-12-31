
def get_book_text(path_string):
    with open(path_string) as file:
        file_contents = file.read()
    return file_contents

def get_word_count(contents_fs):
    word_count = len(contents_fs.split())
    return word_count

def get_characters(contents):
    character_dict = {}
    characters = contents.lower()
    for char in characters:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict
     
def create_list(full_dict):
    character_list = []
    for char, count in full_dict.items():
        temp_dict = {"char": char, "num": count}
        character_list.append(temp_dict)
    return character_list

def sort_on(item):
    return item["num"]

