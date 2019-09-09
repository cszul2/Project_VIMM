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
    def __init__(self, path_to_video):
        self.video = cv2.VideoCapture(path_to_video)
        self.number_of_frames = self.video.shape[0]
        self.number_of_rows = self.video.shape[1]
        self.number_of_columns = self.video.shape[2]
        

class CombinedVideos(Video):
    """
    This class is used to create the combined video 
    """
    def __init__(self, grid = (3,3)):
        self.videos = list()
        self.grid = grid
        self.max_number_of_videos = grid[0]*grid[1]
        
    def combine_videos(self, videos_to_combine):
        if len(videos_to_combine) > self.max_number_of_videos:
            print(f"There are {len(videos_to_combine)} videos and only {self.max_number_of_videos} spots. The last {len(videos_to_combine)-self.max_number_of_videos} will be dropped.")
        for video in videos_to_combine:
            self.videos.append(video)
        