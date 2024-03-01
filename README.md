# HOW TO USE
- Unzip the dictionary.zip
- From the same folder execute with python the script english_dict.py


# Configuring it as default on Linux shell
- You can create a folder on /opt like `mkdir /opt/pytdictionary`
- Download files into this folder, extract the dictionary
- Create a file named `dict` or something similar on /usr/local/bin with `touch /usr/local/bin/dict`
- In this file you configure the script like that
```
#!/bin/bash
cd /opt/pydictionary
python3 english_dict.py
```
- allow execution of this file with `chmod +x /usr/local/bin/dict`
- DONE

With that you can just run `dict` on your terminal and then you have it.

[![Watch the video](https://img.youtube.com/vi/7adYl398hhs/hqdefault.jpg)](https://www.youtube.com/embed/7adYl398hhs)


#### Note:
This database was got from Ayesh Jayasekara, github link: https://github.com/AyeshJayasekara/English-Dictionary-SQLite/tree/master my script is only mining it. Thx bro.
