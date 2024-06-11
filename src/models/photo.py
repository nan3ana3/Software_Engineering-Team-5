from flask import current_app as app

class Photo:
    def __init__(self, uploader_id, description, keywords, imageName):
        self.uploader_id = uploader_id
        self.description = description
        self.keywords = keywords
        self.imageName = imageName

    def save(self):
        photo_collection = app.mongo['photos']
        photo_collection.insert_one({
            "uploader_id": self.uploader_id,
            "description": self.description,
            "keywords": self.keywords,
            "imageName": self.imageName
        })

    @staticmethod
    def search_by_keyword(keyword):
        photo_collection = app.mongo['photos']
        return list(photo_collection.find({"keywords": keyword}))

