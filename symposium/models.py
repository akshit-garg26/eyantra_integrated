from django.db import models
from django.utils.text import slugify
from django.utils.html import mark_safe

import uuid

class Event(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.id


class NavLink(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Exhibition_Entry(models.Model):
    #Title of exhibition entry
    title = models.CharField(max_length=100)  # default=str(uuid.uuid4())
    #username of submission
    username = models.CharField(max_length=100) 

    #Unique slug for this entry
    slug = models.SlugField(max_length=40, editable=False)
    #Model_link to link to model.html template
    model_link = models.CharField(max_length=100, default='/model/')
    
    #Poster
    poster = models.FileField(upload_to='uploads/Poster',  default='uploads/Poster/eyrcs2023.png')

    #Exhibition Front view to display on lobby in frames
    exhibition_front_view = models.FileField(upload_to='uploads/Exhibition_front_view', default='uploads/Exhibition_front_view/eyrcs2023.png')

    #Exhibition Front view to display on lobby in frames
    description = models.TextField()

    #Category choices for different exhibit types
    CATEGORY_CHOICES = [
        ("0", "Country 1"),
        ("1", "Country 2"),
        ("2", "Country 3"),
        ("3", "Country 4"),
        ("4", "Country 5"),
    ]

    #Explanation video with voiceover
    explanation_video_link = models.CharField(max_length=500, default='/')
    #Research Paper as link
    research_paper_link = models.CharField(max_length=500, default='/')
    #Animation video to play for 3D view
    animation_video = models.FileField(upload_to='uploads/Animation_Video',  default='uploads/Poster/eyrcs2023.png')
    #Model to display as orbital view
    exhibit_model = models.FileField(upload_to='uploads/Exhibition_Walls',  default='uploads/Poster/eyrcs2023.png')

    #Team members seperated by commas
    team_members = models.TextField()
    #School name of team members
    school_name = models.CharField(max_length=100, default='', blank=True)

    #category of artifact
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default="0")

   #If is_verified is true only then the entry is shown on the lobby page
    is_Verified = models.BooleanField(default=False)

    @property
    def front_view_preview(self):
        if self.exhibition_front_view:
            return mark_safe('<img src="{}" width="192" height="108" />'.format(self.exhibition_front_view.url))
        return ""

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug_link = self.title + " " +str(uuid.uuid4())
        self.slug = slugify(slug_link)
        self.model_link = "/model/" + self.slug
        super(Exhibition_Entry, self).save(*args, **kwargs)