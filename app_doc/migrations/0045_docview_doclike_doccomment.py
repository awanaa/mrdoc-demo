# 手动创建：文档浏览记录 / 点赞 / 评论 三张表（语雀化首页 Tab 数据源）

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_doc', '0044_space_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_time', models.DateTimeField(auto_now=True, verbose_name='浏览时间')),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_doc.doc', verbose_name='文档')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '文档浏览记录',
                'verbose_name_plural': '文档浏览记录',
                'ordering': ['-view_time'],
            },
        ),
        migrations.CreateModel(
            name='DocLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='点赞时间')),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_doc.doc', verbose_name='文档')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '文档点赞',
                'verbose_name_plural': '文档点赞',
            },
        ),
        migrations.CreateModel(
            name='DocComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_doc.doc', verbose_name='文档')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '文档评论',
                'verbose_name_plural': '文档评论',
                'ordering': ['-create_time'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='doclike',
            unique_together={('doc', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='docview',
            unique_together={('doc', 'user')},
        ),
    ]
