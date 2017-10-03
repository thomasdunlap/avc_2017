import cv2
import numpy as np
import os
import pygame
from pygame.locals import *
import serial
import socket
import time

class GetTrainingImages(object):

    def __init__(self):

        self.server_socket = socket.socket() #
        self.server_socket.bind((ip_address, 8000)) #
        self.server_socket.listen(0) #

        # Accept single connection
        self.connection = self.server_socket.accept()[0].makefile('rb') #

        # Connect to serial port
        self.ser = serial.Serial('/dev/tty.usbmodem1421', 115200, timeout=1) #
        self.send_inst = True #

        #create labels
        self.k = np.zeros((4, 4), 'float')
        for i in range(4):
            self.k[i, i] = 1
        self.temp_label = np.zeros((1, 4), 'float')

        pygame.init()
        self.collect_image()

    def collect_image(self):

        saved_frame = 0
        total_frame = 0

        # Collect images for training
        print('Start collecting images')
        e1 = cv2.getTickCount() #
        image_array = np.zeros((1, 38400)) # Probably has to do with pixels
        label_array = np.zeros((1, 4), 'float')

        # stream video frames one by one
        try:
            stream_bytes = ' '
            frame = 1
            while self.send_inst:
                stream_bytes += self.connection.read(1024) #
                first = stream_bytes.find('\xff\xd8') #
                last = stream_bytes.find('\xff\xd9') #
                
