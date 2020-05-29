# -*- coding: utf-8 -*-
"""
This modual is used for all of the functions related to videos
"""

import cv2
import numpy as np

class Video(object):
    """
    This class is used to create the functions that are used for each of the
    videos
    """
    def __init__(self, path_to_video=0):
        self.video = list()
        capture = cv2.VideoCapture(path_to_video)
        videoReturn = True
        counter = 1
        while videoReturn:
            videoReturn, frame = capture.read()
            counter += 1
            self.numberOfRows = capture.get(4)
            self.numberOfColumns = capture.get(3)
            self.video.append(frame)
            if path_to_video == 0:
                cv2.imshow("Frame", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        self.numberOfFrames = counter
        

class CombinedVideos(object):
    """
    This class is used to create the combined video 
    """
    def __init__(self, videos=None, grid = (3,3)):
        """
        This function creates the combined video object in a grid
        
        :param videos:
        :param grid:
        """
        self.videos = videos
        self.combined_videos = None
        self.grid = grid
        self.max_number_of_videos = grid[0]*grid[1]
        self.rows = list()


    def combine_videos(self):
        """
        This function combines the videos into one array
        """
        row = list()
        for count, video in enumerate(self.videos):
            if self.max_number_of_videos <= count:
                break
            if count % self.grid[0] == 0 and count > 0:
                self.rows.append(row)
                row = list()
            row.append(video)
        self.rows.append(row)
        for frameNumber in range(self.rows[0][0].numberOfFrames):
            print("Tired")

    
    def save_video(self, name):
        """
        This function saves the video
        
        :param name:
        """
        raise NotImplementedError