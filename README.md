# Python Move Seeker

### Hi, my name is Łukasz
Purely for the needs of the open source community I'm giving you this code. It was written only for my needs, I only made sure that it actually works (for me) and flake8 is not overly complaining about it.

The alghoritm is shamelessly stolen from https://github.com/cedricve/motion-detection, simplified and rewritten to Python.

### What's the story?

So I have two cats. Lovely beasts. Unfortunately one of them got very sick when he was just a kitten. Because of that I set bunch of cameras that were looking at them when I was absent and this way I was making sure that he's fine when I was away. Obviously I was recording everything. Even after he got better.

This way I ended up with 600GB of videos, 90% of each was static image of sleeping cats. I could either delete them all or find a way to find the timespans where there is actual movement. Obviosuly I went with the latter. Computer watched all videos for me.

This is not exact code that I used but it can be easily adapted to read a file and print out timestamps when the move is detected.

### Coool, how to use it?

As you wish :).

This one reads camera 0 from the system. It's very simple to read a file, just replace `cv2.VideoCapture()` argument to point to a file:

The output is time in milliseconds and number of measured changes.
```
> ./pymoveseeker.py 
15397.74325908558 1481
15497.728604923797 1725
15597.713950762016 1277
15697.699296600234 1160
15797.684642438453 1558
15997.655334114888 2459
16097.640679953107 1069
16197.626025791324 1255
16297.611371629542 945
16397.59671746776 1219
17097.494138335285 1776
17397.450175849943 1696
20596.98124267292 1786
21596.8347010551 2051
21696.820046893317 1032
21796.805392731534 1691
21996.77608440797 3193
24496.409730363423 3191
24596.39507620164 1704
47293.06858147714 3378
```
