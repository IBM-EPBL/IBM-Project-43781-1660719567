Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import emoji
>>> print(emoji.emojize('Python is :thumbsup:', language='alias'))
Python is 👍
>>> print(emoji.emojize('Python is :red_heart:', language='alias'))
Python is ❤️
>>> print(emoji.is_emoji("👍"))
True
>>>  print(emoji.demojize('Python is 👍'))
...  
SyntaxError: unexpected indent
>>> print(emoji.demojize('Python is 👍'))
Python is :thumbs_up:
>>> print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
Python is fun ❤️
