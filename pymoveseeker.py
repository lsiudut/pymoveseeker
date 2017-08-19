#!/usr/bin/env python3

# shamelessly stolen, simplified and adapted to Python
# from https://github.com/cedricve/motion-detection

import cv2

kernel_ero = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

vcap = cv2.VideoCapture(0)


def readframe(vcap):
    ret, frame = vcap.read()
    if not ret:
        return ret, None, None
    ts = vcap.get(cv2.CAP_PROP_POS_MSEC)
    frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return ret, ts, frame


buff = []
while len(buff) < 3:
    ret, ts, frame = readframe(vcap)
    if ret:
        buff.append(frame)

while True:
    ret, ts, frame = readframe(vcap)
    if ret:
        buff.append(frame)
        buff.pop(0)

    d1 = cv2.absdiff(buff[0], buff[2])
    d2 = cv2.absdiff(buff[2], buff[1])
    motion = cv2.bitwise_and(d1, d2)
    ret, motion = cv2.threshold(motion, 25, 255, cv2.THRESH_BINARY)
    cv2.erode(motion, motion, kernel_ero)

    mean, stddev = cv2.meanStdDev(motion)
    if stddev[0][0] > 20:
        motionum = 0
        h, w = motion.shape
        for x in range(0, w-1, 2):
            for y in range(0, h-1, 2):
                if motion[y][x] == 255:
                    motionum += 1

        print(f"{ts} {motionum}")

    cv2.imshow('VIDEO', motion)
    cv2.waitKey(1)
