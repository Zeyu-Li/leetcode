'''
File Type Gen by Andrew Li
Generate a List of Files along With File Type
'''

import os
# requires pyperclip to copy to clipboard, otherwise, leave it in
# import pyperclip


def main():
    files = os.listdir()

    # remove non folder items manually
    ignore = ['.git', '.github', 'index.py', 'LICENSE', 'README.md']

    print(files)
    for item in ignore:
        files.remove(item)

    # inits
    text = '\n'
    mapping = {'py': 'Python', '.c': 'C', 'pp': 'C++', 'va': "Java"}

    # generate clipboard items
    for index, _file in enumerate(files, start=1):
        file_types = ''
        # find file type
        items = os.listdir(_file)
        for item in items:
            if item[-2:] in mapping.keys():
                file_types += mapping[item[-2:]] + ', '
        
        text += f" {index}. [{' '.join(x.capitalize() or ' ' for x in _file.split('-'))}](https://leetcode.com/problems/{_file}) - {file_types[:-2]} \n"

    front = """# Leetcode

![Build](https://github.com/Zeyu-Li/leetcode/workflows/Generate%20MD/badge.svg)

[Leetcode](https://leetcode.com/) questions



## Questions """

    end = """


## License

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)"""

    # debug
    # print(text)
    # pyperclip.copy(text)

    # write to file README.md
    with open('README.md', 'w') as fp:
        fp.writelines(front + text + f"\nCount: {len(files)}" + end)

    return 

if __name__ == "__main__":
    main()
