#!/usr/bin/env python

#all imports required
#facebook-sdk was obtained thru github, please do google

import facebook
import glob
import os
import MySQLdb
import re

#Variables that are required to make a connection to facebook

accesstoken = "Your access token here" 
#Try using 'graph api explorer' to obtian access tokens

versionid = "Mention the version of the facebook-sdk that you are using" 
#Can be obtained from the documentation associated to the sdk

graph = facebook.GraphAPI(access_token=accesstoken, version=versionid)
#Establishes connection with Facebook

directory = "The directoy that contains all the photos that you would like to upload" 
#Please note out the location with respect to where the current python file is placed

os.chdir(directory)
#Changes directory to the mentioned directory

message_text="The Message you desire to enter for ever image that you post"

album_id="The album_id fo the album to which these photos are to be posted" 
#google methods to find album_id of your album

#this loop runs through every file present in the destination folder
for file in glob.glob("*"):
	graph.put_photo(image=open(file), message=message_text,album_path=album_id+"/photos")
#this loop runs through every file present in the directory folder






