from django import forms
from .models import Project, Issue, Comment, Attachment

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'project_key', 'description', 'lead_user']

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['issue_key', 'project', 'reporter', 'assignee', 'summary', 'description', 'issue_type', 'status', 'priority']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['file_path', 'file_name']
