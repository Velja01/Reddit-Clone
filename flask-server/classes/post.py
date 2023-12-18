# Post.py

import datetime


class Post:
    def __init__(self, id, title, content, author, created_at, upvotes, downvotes, comments, user_id):
        self.id = id
        self.title = title
        self.content = content
        self.author = author
        self.created_at = created_at or datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.upvotes = upvotes
        self.downvotes = downvotes
        self.comments = comments,
        self.user_id=user_id
    def tuple(self):
        return (self.id,self.title, self.content, self.author, self.created_at, self.upvotes, self.downvotes, self.comments, self.user_id)