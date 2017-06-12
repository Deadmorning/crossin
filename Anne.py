# -*- coding: utf-8 -*-
'''
version:python 2.7
author:Deadmorning
system:win64
'''
from os import path
from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt 

from wordcloud import WordCloud,STOPWORDS

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'Romeo.txt')).read()

# read the mask image
# taken from https://git.oschina.net/zx576/novel/attach_files
anne_mask = np.array(Image.open(path.join(d, "anne.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=anne_mask,
               stopwords=stopwords)
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "anne.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(anne_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
