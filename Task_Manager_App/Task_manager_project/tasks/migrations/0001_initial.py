# Generated by Django 4.2.16 on 2024-09-10 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Epic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epic_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_key', models.CharField(max_length=20, unique=True)),
                ('summary', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('issue_type', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('priority', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assignee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_issues', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('project_key', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lead_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lead_projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_field', models.CharField(default='dummy', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workflow_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_name', models.CharField(max_length=255)),
                ('step_order', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='tasks.workflow')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_worked', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_logged', models.DateTimeField()),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.issue')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sprint_name', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.project')),
            ],
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.permission')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IssueWorkflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transitioned_at', models.DateTimeField(auto_now_add=True)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.issue')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.workflowstep')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.workflow')),
            ],
        ),
        migrations.CreateModel(
            name='IssueSprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.issue')),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.sprint')),
            ],
        ),
        migrations.CreateModel(
            name='IssueLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.issue')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.label')),
            ],
        ),
        migrations.CreateModel(
            name='IssueHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_changed', models.CharField(max_length=255)),
                ('old_value', models.CharField(max_length=255)),
                ('new_value', models.CharField(max_length=255)),
                ('changed_at', models.DateTimeField(auto_now_add=True)),
                ('changed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.issue')),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='tasks.project'),
        ),
        migrations.AddField(
            model_name='issue',
            name='reporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_issues', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='EpicIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.epic')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.issue')),
            ],
        ),
        migrations.AddField(
            model_name='epic',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.project'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tasks.issue')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.CharField(max_length=255)),
                ('file_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='tasks.issue')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
