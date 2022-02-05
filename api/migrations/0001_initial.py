# Generated by Django 4.0.1 on 2022-01-20 21:32

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('phone', models.CharField(max_length=200, unique=True)),
                ('initial_test_performed', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AlternativeQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=1000)),
                ('is_correct', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Curso - Alternativa',
                'verbose_name_plural': 'Curso - Alternativas',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='AlternativeQuestionTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=1000)),
                ('points', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Test - Alternativa',
                'verbose_name_plural': 'Test - Alternativas',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('code_trip', models.CharField(blank=True, max_length=600, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('tutor_name', models.CharField(blank=True, max_length=220, null=True)),
                ('passing_score', models.IntegerField(blank=True, null=True)),
                ('tutor_text', models.CharField(blank=True, max_length=2000, null=True)),
                ('promotional_video', models.CharField(blank=True, max_length=2000, null=True)),
                ('is_free', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
            ],
            options={
                'verbose_name': 'Module',
                'verbose_name_plural': 'Modules',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=400)),
                ('description', models.CharField(max_length=600)),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': 'Tests',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField(max_length=1000)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.module')),
            ],
            options={
                'verbose_name': 'Curso - Video',
                'verbose_name_plural': 'Cursos - Videos',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='ResultTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('points_total', models.IntegerField(blank=True, null=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Test - Resultado',
                'verbose_name_plural': 'Test - Resultados',
            },
        ),
        migrations.CreateModel(
            name='ResultContest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('code_travel', models.CharField(blank=True, max_length=400, null=True)),
                ('calification', models.FloatField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Curso - Resultado de cuestionario',
                'verbose_name_plural': 'Cursos - Resultados de cuestionarios',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('file_re', models.FileField(upload_to='uploads/resources/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
            ],
            options={
                'verbose_name': 'Curso - Recurso',
                'verbose_name_plural': 'Cursos -Recursos',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='QuestionTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=900)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.test')),
            ],
            options={
                'verbose_name': 'Test - Pregunta',
                'verbose_name_plural': 'Test - Preguntas',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='QuestionCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=1000)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course')),
            ],
            options={
                'verbose_name': 'Curso - Pregunta',
                'verbose_name_plural': 'Cursos - Preguntas',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('approved_courses', models.ManyToManyField(blank=True, related_name='user_aproved_courses', to='api.Course')),
                ('shop_courses', models.ManyToManyField(blank=True, related_name='user_shop_courses', to='api.Course')),
                ('tests_performed', models.ManyToManyField(blank=True, related_name='user_result_test', to='api.ResultTest')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario - Perfil',
                'verbose_name_plural': 'Usuarios - Perfiles',
            },
        ),
        migrations.CreateModel(
            name='PreRequisite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='course_affect', to='api.course')),
                ('pre_requisite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='course_prerequisit', to='api.course')),
            ],
            options={
                'verbose_name': 'Curso - Pre requisito',
                'verbose_name_plural': 'Cursos - Pre requisitos',
            },
        ),
        migrations.CreateModel(
            name='AnswerTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.alternativequestiontest')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.questiontest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Test - Respuesta',
                'verbose_name_plural': 'Test - Respuestas',
            },
        ),
        migrations.CreateModel(
            name='AnswerQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.alternativequestion')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.questioncourse')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Curso - Respuesta',
                'verbose_name_plural': 'Cursos - Respuestas',
            },
        ),
        migrations.AddField(
            model_name='alternativequestiontest',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.questiontest'),
        ),
        migrations.AddField(
            model_name='alternativequestion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.questioncourse'),
        ),
    ]