from django.db import models



class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)

    class Meta:
        ordering = ['order', ]


    def __str__(self):
        return self.title



# c = Course()
# c.title = "Python Basics"
# c.description = "Learn the basics of Python"
# c.save()
#
# Course(title="Python Collections", description="Learn about list, dict, and tuple").save()
#
# Course.objects.create(title="Object-Oriented Python", description = "Learn about Python's classes")
#
