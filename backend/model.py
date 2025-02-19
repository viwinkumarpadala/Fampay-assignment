#Iport statements
from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

#creating a class for defining the data format
class YouTubeVideo:
    def __init__(self, title, description, publishedAt, thumbnail, video_id):
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.thumbnail = thumbnail
        self.video_id = video_id

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'publishedAt': self.publishedAt,
            'thumbnail': self.thumbnail,
            'video_id': self.video_id
        }
#get the url from dotenv file
db_url=os.getenv('db_url')

# Connect to MongoDB
client = MongoClient(db_url)
db = client['youtube_database']  
collection = db['videos'] 
# creating index on the field published_at
collection.create_index([('publishedAt', -1)])
