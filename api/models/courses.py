from django.db import models
from api.models.utils import ApiModel
from api.models.users import User


class Course(ApiModel):
    id = models.CharField(max_length=300, primary_key=True, editable=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    extra_txt = models.CharField(max_length=220, blank=True, null=True)
    description_promotional = models.CharField(max_length=400, blank=True, null=True)
    promotional_video = models.CharField(max_length=2000, blank=True, null=True)
    is_free = models.BooleanField(default=False)
    file_promotional = models.FileField(blank=True, null=True)
    authorized_user = models.ManyToManyField(User, blank=True,
            related_name="authorized_user_course", null=True)


    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['created']

    def __str__(self):
        return self.title


class PreRequisite(ApiModel):
    course = models.OneToOneField(Course, on_delete=models.CASCADE,
            related_name='course_affect')
    pre_requisite = models.OneToOneField(Course, on_delete=models.CASCADE,
            related_name='course_prerequisit')

    class Meta:
        verbose_name = 'Curso - Pre requisito'
        verbose_name_plural = 'Cursos - Pre requisitos'

    def __str__(self):
        return str(self.course)


class Module(ApiModel):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        verbose_name = 'Curso - Modulo'
        verbose_name_plural = 'Cursos - Modulos'
        ordering = ['created']

    def __str__(self):
        return self.title
    

class Video(ApiModel):
    title = models.CharField(max_length=200)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    url = models.URLField(max_length=1000)
    
    class Meta: 
        verbose_name = 'Curso - Video'
        verbose_name_plural = 'Cursos - Videos'
        ordering = ['created']

    def __str__(self):
        return self.title

class ViewVideo(ApiModel):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.video)


class Resource(ApiModel):
    title = models.CharField(max_length=200)
    class_video = models.ForeignKey(Video, on_delete=models.CASCADE)
    file_re = models.FileField(upload_to='uploads/resources/')
    
    class Meta:
        verbose_name = 'Curso - Recurso'
        verbose_name_plural = 'Cursos -Recursos'
        ordering = ['created']

    def __str__(self):
        return self.title

