from __future__ import print_function
import os, sys
from PIL import Image

# make it third of original size
REDUCTION = 6

path = sys.argv[1]
for infile in os.listdir(path):
	if infile.endswith(".png") or infile.endswith(".jpg"):
	    outfile = os.path.join(path, 'thumbnails', infile)
	    print(outfile)
	    if infile != outfile:
	        try:
	        	im = Image.open(path + '/' + infile)
	        	size = tuple(pix/REDUCTION for pix in im.size)
	        	print("size: " + str(size))
	        	im.thumbnail(size)
	        	im.save(outfile)
	        except IOError:
	            print("cannae create thumbnail for", infile)