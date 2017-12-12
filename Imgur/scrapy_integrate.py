# Pass the search string you want
# It search and download the first image(thumbnail) on imgur.com
# Then it will return the name of the file stored in ./images/full/

import subprocess
import re


def search_image(arg):

    out = subprocess.check_output(['scrapy', 'crawl', 'imgur', '-a',
                                   'arg='+arg], stderr=subprocess.STDOUT,
                                   cwd='Imgur')

    string = out.decode()
    return re.findall(r"full.(\S*)'",string)[0]
