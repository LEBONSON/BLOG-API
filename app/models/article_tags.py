from ..extensions import db
from datetime import datetime

# Table d'association pour les relations plusieurs-à-plusieurs entre les articles et les tags et aussi pour éviter les imports circulaires tel que mentionné dans la documentation SQLAlchemy

article_tags = db.Table('article_tags',
    db.Column('article_id', db.Integer, db.ForeignKey('articles.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)