from rest_framework import serializers
from .models import Project, Issue, Comment, Attachment, Workflow, WorkflowStep, IssueWorkflow, Permission, RolePermission, ProjectUser, IssueHistory, Sprint, IssueSprint, Label, IssueLabel, TimeTracking, Epic, EpicIssue, Project_table

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'

class WorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workflow
        fields = '__all__'

class WorkflowStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowStep
        fields = '__all__'

class IssueWorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueWorkflow
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = '__all__'

class ProjectUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUser
        fields = '__all__'

class IssueHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueHistory
        fields = '__all__'

class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'

class IssueSprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueSprint
        fields = '__all__'

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'

class IssueLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueLabel
        fields = '__all__'

class TimeTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTracking
        fields = '__all__'

class EpicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epic
        fields = '__all__'

class EpicIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpicIssue
        fields = '__all__'

class ProjectTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_table
        fields = '__all__'
