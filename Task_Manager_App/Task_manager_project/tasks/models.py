from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_key = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    lead_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='lead_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name

class Issue(models.Model):
    issue_key = models.CharField(max_length=20, unique=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_issues')
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_issues')
    summary = models.CharField(max_length=255)
    description = models.TextField()
    issue_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary

class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Attachment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='attachments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Workflow(models.Model):
    workflow_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class WorkflowStep(models.Model):
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='steps')
    step_name = models.CharField(max_length=255)
    step_order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class IssueWorkflow(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    step = models.ForeignKey(WorkflowStep, on_delete=models.CASCADE)
    transitioned_at = models.DateTimeField(auto_now_add=True)

class Permission(models.Model):
    permission_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

class RolePermission(models.Model):
    role = models.CharField(max_length=50)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

class ProjectUser(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

class IssueHistory(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    changed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    field_changed = models.CharField(max_length=255)
    old_value = models.CharField(max_length=255)
    new_value = models.CharField(max_length=255)
    changed_at = models.DateTimeField(auto_now_add=True)

class Sprint(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sprint_name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=50)

class IssueSprint(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)

class Label(models.Model):
    label_name = models.CharField(max_length=255)

class IssueLabel(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)

class TimeTracking(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    date_logged = models.DateTimeField()

class Epic(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    epic_name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class EpicIssue(models.Model):
    epic = models.ForeignKey(Epic, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

class Project_table(models.Model):
    # existing fields...
    new_field = models.CharField(max_length=100, default='dummy')