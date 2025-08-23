def get_num_words(string):
    return len(string.split())

def get_char_count(string):
    char_counter = {}
    text = string.lower()
    for c in list(text):
        char_counter[c]=char_counter.setdefault(c,0)+1
    return char_counter

def sort_on(list_to_sort):
    return list_to_sort['num']

def sort_count(char_counter):
    list_sorted = []
    for d in char_counter.keys():
        list_sorted.append({'char': d, 'num': char_counter[d]})    
    list_sorted.sort(reverse=True, key=sort_on)
    return list_sorted