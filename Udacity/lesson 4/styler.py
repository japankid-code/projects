$ ls
spin.py
$ cat spin.py
import time


def spin():
    for _ in range( 100 ):
        for ch in '-\\|/':
            print(ch, end='', flush=True)
            time.sleep(0.1)
            print('\b', end='', flush=True)


if __name__ == '__main__':
  spin()

$ pycodestyle spin.py
spin.py:5:20: E201 whitespace after '('
spin.py:5:24: E202 whitespace before ')'
spin.py:13:3: E111 indentation is not a multiple of four
spin.py:14:1: W391 blank line at end of file