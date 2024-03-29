from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model): # django uses ORM Object Relational Mapping
    # Write out the model definition in pyhton and django can auto handle the conversion into database code
    title = models.CharField(max_length=100)  # Added the title
    content = models.TextField() # content is just the text field
    created_at = models.DateTimeField(auto_now_add=True) # We want to auto populate whenever we make a new instance of this note
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    # author specifies who made the note, author is a primary key in a different db, so when u call on CASCADE we are saying
    # to delete everything that follows is contained within the user db
    # related name tells us what field nae we want to put on the user to refrence all its notes

    def __str__(self):
        return self.title


