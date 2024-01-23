from django.db.models import *

from django.contrib.auth.models import User

class Pinterest(Model):

    name  = CharField(
        'Name of the post',
        max_length=128
    )

    description = TextField(
        'Description of the post',
    )

    author = ForeignKey(
        User,
        verbose_name='Author',
        on_delete=CASCADE
    )

    released_date = DateField(
        'Date of release'
    )

    cover = ImageField(
        'Post Image',
        upload_to='posts-images/'
    )

    def __str__(self):
        return f'(self.name)'

    class Meta:

        verbose_name = 'Post'
        verbose_name_plural='Posts'
       