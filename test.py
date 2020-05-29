# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 17:21:01 2019

@author: Chris
"""
import video


def video_test():
    issues = list()
    passed = True
    correctNumberOfFrames = 162
    correctNumberOfRows = 368
    correctNumberOfColumns = 640
    pathToTestVideo = r"testFiles\SampleVideo_640x360_1mb.mp4"
    videoTest = video.Video(pathToTestVideo)
    if videoTest.numberOfFrames != correctNumberOfFrames:
        issues.append("Number of frames is not correct")
    if videoTest.numberOfRows != correctNumberOfRows:
        issues.append("Number of rows is not correct")
    if videoTest.numberOfColumns != correctNumberOfColumns:
        issues.append("Number of columns is not correct")
    if len(issues) > 0:
        passed = False
    return (passed, issues)

if __name__ == "__main__":
    video_test()