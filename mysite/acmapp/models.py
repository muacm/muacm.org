from django.db import models

# datetime module for event custom func (show form link)
from datetime import datetime

# --------------------------------------------------------------------------
# Event Model
# --------------------------------------------------------------------------

class Event(models.Model):
    title = models.CharField(max_length=60)  # required
    description = models.TextField(default="A event conducted by MU-ACM.")
    fromDate = models.DateTimeField(default=datetime.now())
    toDate = models.DateTimeField(default=datetime.now())
    showTime = models.BooleanField(default=False)
    # TODO should it contain 2 images ? (1 before modal opening & one in model)
    image = models.ImageField(upload_to="events/", default="default_img.png")
    formLink = models.URLField(max_length=2000, blank=True, null=True)

    showFormAfterEvent = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     from django.urls import reverse_lazy
    #     return reverse_lazy("acmapp:event_detail_view", kwargs={"pk": self.slug})

    def __str__(self):
        return self.title

    # Few custom functions to reduce redundancy
    def bool_show_form(self):
        if self.fromDate < datetime.now() or self.showFormAfterEvent is True:
            return True
        return False

    def event_from_date(self):
        if self.showTime is True:
            return str(self.fromDate.strftime("%B %d, %Y - %H:%M:%S"))
        return str(self.fromDate.strftime("%B %d, %Y"))

    def event_to_date(self):
        if self.showTime is True:
            return str(self.toDate.strftime("%B %d, %Y - %H:%M:%S"))
        return str(self.toDate.strftime("%B %d, %Y"))

# --------------------------------------------------------------------------
# Project Model
# --------------------------------------------------------------------------

class Project(models.Model):
    title = models.CharField(max_length=60)  # required
    description = models.TextField(default="A project under MU-ACM.")
    image = models.ImageField(upload_to="projects/", default="default_img.png")
    projectLink = models.URLField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.title

    # Few custom functions to reduce redundancy
    def get_project_link(self):
        if self.projectLink is None:
            return str("#")
        return self.projectLink

# --------------------------------------------------------------------------
# Team Model
# --------------------------------------------------------------------------

class TeamMember(models.Model):
    name = models.CharField(max_length=60)  # required
    post = models.TextField(default="Team member of MU-ACM")
    image = models.ImageField(upload_to="team/", default="default_img.png")
    email = models.EmailField(max_length=254, blank=True, null=True)
    linkedin = models.URLField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.name

    # Few custom functions to reduce redundancy
    def get_email(self):
        if self.email is None:
            return str("#")
        return str("mailto:{}".format(self.email))

    def get_linkedin(self):
        if self.linkedin is None:
            return str("#")
        return str(self.linkedin)

# --------------------------------------------------------------------------
# Blog Model
# --------------------------------------------------------------------------

class Blog(models.Model):
    title = models.CharField(max_length=60)  # required
    description = models.TextField(default="A blog created by MU-ACM Team.")
    blogLink = models.URLField(max_length=2000, blank=True, null=True)

    # TODO image not needed can put medium "M" logo like vit did

    def __str__(self):
        return self.title

    # Few custom functions to reduce redundancy
    def get_blog_link(self):
        if self.blogLink is None:
            return str("#")
        return str(self.blogLink)
