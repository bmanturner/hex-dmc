hex-dmc
=======

Finds closest DMC thread color based on hex color. Useful for cross-stitching. Would potentially serve well as a web app.

**hex_dmc.py**

Prompts for hex, loops through DMC color chart and returns the closest color in DMC color format. Uses a weighted Euclidean distance function to determine closeness.

**jpg_dmc.py**

In progress: Uses Python Imaging Library to create a RGB frequency map of the image. Uses hex_dmc.py to create a DMC frequency map instead. Currently slow. Optimizations in progress.
