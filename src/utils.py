"""utils"""
import pandas as pd


def read_file_from(path):
    """"read file"""
    f = open(path)
    line = f.readline()
    ret = ""
    while line:
        ret += line
        line = f.readline().strip('\n')
    f.close()

    ret = ret.replace('\n', '')
    return ret

def write_data_to(path, content):
    with open(path, 'w') as f:
        f.write(content)


def write_to_csv(chars, numbers, frequencies, path):
    """write in csv"""
    # print(chars, numbers, len(chars), frequencies)
    df = pd.DataFrame({
        'chars': chars,
        'numbers': numbers,
        'frequencies': frequencies
    })
    df.to_csv(path)

def statistics_analysis(_dict_chars, _count):
    """input: dict and number of different elements,
    output: statistics_analysis from high frequence to low"""
    sorted_chars = dict(sorted(_dict_chars.items(), key = lambda item:item[1], reverse = True))

    chars = list(sorted_chars.keys())
    numbers =  list(sorted_chars.values())
    frequencies = list(map(lambda x: x/_count, numbers))
    return chars, numbers, frequencies