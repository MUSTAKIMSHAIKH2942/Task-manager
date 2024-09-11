from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .Serializers import *
from rest_framework import viewsets

class UserTableViewSet(viewsets.ModelViewSet):
    queryset = UserTable.objects.all()
    serializer_class = UserTableSerializer

# Project Views
@api_view(['GET', 'POST'])
def project_list(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Issue Views
@api_view(['GET', 'POST'])
def issue_list(request):
    if request.method == 'GET':
        issues = Issue.objects.all()
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def issue_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == 'GET':
        serializer = IssueSerializer(issue)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = IssueSerializer(issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Comment Views
@api_view(['GET', 'POST'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Attachment Views
@api_view(['GET', 'POST'])
def attachment_list(request):
    if request.method == 'GET':
        attachments = Attachment.objects.all()
        serializer = AttachmentSerializer(attachments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AttachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def attachment_detail(request, pk):
    attachment = get_object_or_404(Attachment, pk=pk)
    if request.method == 'GET':
        serializer = AttachmentSerializer(attachment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AttachmentSerializer(attachment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        attachment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Workflow Views
@api_view(['GET', 'POST'])
def workflow_list(request):
    if request.method == 'GET':
        workflows = Workflow.objects.all()
        serializer = WorkflowSerializer(workflows, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WorkflowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def workflow_detail(request, pk):
    workflow = get_object_or_404(Workflow, pk=pk)
    if request.method == 'GET':
        serializer = WorkflowSerializer(workflow)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = WorkflowSerializer(workflow, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        workflow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# WorkflowStep Views
@api_view(['GET', 'POST'])
def workflowstep_list(request):
    if request.method == 'GET':
        workflow_steps = WorkflowStep.objects.all()
        serializer = WorkflowStepSerializer(workflow_steps, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WorkflowStepSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def workflowstep_detail(request, pk):
    workflow_step = get_object_or_404(WorkflowStep, pk=pk)
    if request.method == 'GET':
        serializer = WorkflowStepSerializer(workflow_step)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = WorkflowStepSerializer(workflow_step, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        workflow_step.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# IssueWorkflow Views
@api_view(['GET', 'POST'])
def issueworkflow_list(request):
    if request.method == 'GET':
        issue_workflows = IssueWorkflow.objects.all()
        serializer = IssueWorkflowSerializer(issue_workflows, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = IssueWorkflowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def issueworkflow_detail(request, pk):
    issue_workflow = get_object_or_404(IssueWorkflow, pk=pk)
    if request.method == 'GET':
        serializer = IssueWorkflowSerializer(issue_workflow)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = IssueWorkflowSerializer(issue_workflow, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        issue_workflow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Permission Views
@api_view(['GET', 'POST'])
def permission_list(request):
    if request.method == 'GET':
        permissions = Permission.objects.all()
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def permission_detail(request, pk):
    permission = get_object_or_404(Permission, pk=pk)
    if request.method == 'GET':
        serializer = PermissionSerializer(permission)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PermissionSerializer(permission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        permission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# RolePermission Views
@api_view(['GET', 'POST'])
def rolepermission_list(request):
    if request.method == 'GET':
        role_permissions = RolePermission.objects.all()
        serializer = RolePermissionSerializer(role_permissions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RolePermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def rolepermission_detail(request, pk):
    role_permission = get_object_or_404(RolePermission, pk=pk)
    if request.method == 'GET':
        serializer = RolePermissionSerializer(role_permission)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RolePermissionSerializer(role_permission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        role_permission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ProjectUser Views
@api_view(['GET', 'POST'])
def projectuser_list(request):
    if request.method == 'GET':
        project_users = ProjectUser.objects.all()
        serializer = ProjectUserSerializer(project_users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProjectUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def projectuser_detail(request, pk):
    project_user = get_object_or_404(ProjectUser, pk=pk)
    if request.method == 'GET':
        serializer = ProjectUserSerializer(project_user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProjectUserSerializer(project_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        project_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# IssueHistory Views
@api_view(['GET', 'POST'])
def issuehistory_list(request):
    if request.method == 'GET':
        issue_histories = IssueHistory.objects.all()
        serializer = IssueHistorySerializer(issue_histories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = IssueHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def issuehistory_detail(request, pk):
    issue_history = get_object_or_404(IssueHistory, pk=pk)
    if request.method == 'GET':
        serializer = IssueHistorySerializer(issue_history)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = IssueHistorySerializer(issue_history, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        issue_history.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Sprint Views
@api_view(['GET', 'POST'])
def sprint_list(request):
    if request.method == 'GET':
        sprints = Sprint.objects.all()
        serializer = SprintSerializer(sprints, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SprintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def sprint_detail(request, pk):
    sprint = get_object_or_404(Sprint, pk=pk)
    if request.method == 'GET':
        serializer = SprintSerializer(sprint)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SprintSerializer(sprint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        sprint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# IssueSprint Views
@api_view(['GET', 'POST'])
def issuesprint_list(request):
    if request.method == 'GET':
        issue_sprints = IssueSprint.objects.all()
        serializer = IssueSprintSerializer(issue_sprints, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = IssueSprintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def issuesprint_detail(request, pk):
    issue_sprint = get_object_or_404(IssueSprint, pk=pk)
    if request.method == 'GET':
        serializer = IssueSprintSerializer(issue_sprint)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = IssueSprintSerializer(issue_sprint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        issue_sprint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Label Views
@api_view(['GET', 'POST'])
def label_list(request):
    if request.method == 'GET':
        labels = Label.objects.all()
        serializer = LabelSerializer(labels, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LabelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def label_detail(request, pk):
    label = get_object_or_404(Label, pk=pk)
    if request.method == 'GET':
        serializer = LabelSerializer(label)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = LabelSerializer(label, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        label.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# IssueLabel Views
@api_view(['GET', 'POST'])
def issuelabel_list(request):
    if request.method == 'GET':
        issue_labels = IssueLabel.objects.all()
        serializer = IssueLabelSerializer(issue_labels, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = IssueLabelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def issuelabel_detail(request, pk):
    issue_label = get_object_or_404(IssueLabel, pk=pk)
    if request.method == 'GET':
        serializer = IssueLabelSerializer(issue_label)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = IssueLabelSerializer(issue_label, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        issue_label.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# TimeTracking Views
@api_view(['GET', 'POST'])
def timetracking_list(request):
    if request.method == 'GET':
        time_trackings = TimeTracking.objects.all()
        serializer = TimeTrackingSerializer(time_trackings, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TimeTrackingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def timetracking_detail(request, pk):
    time_tracking = get_object_or_404(TimeTracking, pk=pk)
    if request.method == 'GET':
        serializer = TimeTrackingSerializer(time_tracking)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TimeTrackingSerializer(time_tracking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        time_tracking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Epic Views
@api_view(['GET', 'POST'])
def epic_list(request):
    if request.method == 'GET':
        epics = Epic.objects.all()
        serializer = EpicSerializer(epics, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EpicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def epic_detail(request, pk):
    epic = get_object_or_404(Epic, pk=pk)
    if request.method == 'GET':
        serializer = EpicSerializer(epic)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EpicSerializer(epic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        epic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# EpicIssue Views
@api_view(['GET', 'POST'])
def epicissue_list(request):
    if request.method == 'GET':
        epic_issues = EpicIssue.objects.all()
        serializer = EpicIssueSerializer(epic_issues, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EpicIssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def epicissue_detail(request, pk):
    epic_issue = get_object_or_404(EpicIssue, pk=pk)
    if request.method == 'GET':
        serializer = EpicIssueSerializer(epic_issue)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EpicIssueSerializer(epic_issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        epic_issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ProjectTable Views
@api_view(['GET', 'POST'])
def projecttable_list(request):
    if request.method == 'GET':
        project_tables = Project_table.objects.all()
        serializer = ProjectTableSerializer(project_tables, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProjectTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def projecttable_detail(request, pk):
    project_table = get_object_or_404(Project_table, pk=pk)
    if request.method == 'GET':
        serializer = ProjectTableSerializer(project_table)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProjectTableSerializer(project_table, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        project_table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
