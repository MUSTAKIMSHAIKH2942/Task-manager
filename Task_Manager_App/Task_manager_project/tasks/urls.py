from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', views.UserTableViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('issues/', views.issue_list, name='issue_list'),
    path('issues/<int:pk>/', views.issue_detail, name='issue_detail'),
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/<int:pk>/', views.comment_detail, name='comment_detail'),
    path('attachments/', views.attachment_list, name='attachment_list'),
    path('attachments/<int:pk>/', views.attachment_detail, name='attachment_detail'),
    path('workflows/', views.workflow_list, name='workflow_list'),
    path('workflows/<int:pk>/', views.workflow_detail, name='workflow_detail'),
    path('workflowsteps/', views.workflowstep_list, name='workflowstep_list'),
    path('workflowsteps/<int:pk>/', views.workflowstep_detail, name='workflowstep_detail'),
    path('issueworkflows/', views.issueworkflow_list, name='issueworkflow_list'),
    path('issueworkflows/<int:pk>/', views.issueworkflow_detail, name='issueworkflow_detail'),
    path('permissions/', views.permission_list, name='permission_list'),
    path('permissions/<int:pk>/', views.permission_detail, name='permission_detail'),
    path('rolepermissions/', views.rolepermission_list, name='rolepermission_list'),
    path('rolepermissions/<int:pk>/', views.rolepermission_detail, name='rolepermission_detail'),
    path('projectusers/', views.projectuser_list, name='projectuser_list'),
    path('projectusers/<int:pk>/', views.projectuser_detail, name='projectuser_detail'),
    path('issuehistories/', views.issuehistory_list, name='issuehistory_list'),
    path('issuehistories/<int:pk>/', views.issuehistory_detail, name='issuehistory_detail'),
    path('sprints/', views.sprint_list, name='sprint_list'),
    path('sprints/<int:pk>/', views.sprint_detail, name='sprint_detail'),
    path('issuesprints/', views.issuesprint_list, name='issuesprint_list'),
    path('issuesprints/<int:pk>/', views.issuesprint_detail, name='issuesprint_detail'),
    path('labels/', views.label_list, name='label_list'),
    path('labels/<int:pk>/', views.label_detail, name='label_detail'),
    path('issuelabels/', views.issuelabel_list, name='issuelabel_list'),
    path('issuelabels/<int:pk>/', views.issuelabel_detail, name='issuelabel_detail'),
    path('timetrackings/', views.timetracking_list, name='timetracking_list'),
    path('timetrackings/<int:pk>/', views.timetracking_detail, name='timetracking_detail'),
    path('epics/', views.epic_list, name='epic_list'),
    path('epics/<int:pk>/', views.epic_detail, name='epic_detail'),
    path('epicissues/', views.epicissue_list, name='epicissue_list'),
    path('epicissues/<int:pk>/', views.epicissue_detail, name='epicissue_detail'),
    path('projecttables/', views.projecttable_list, name='projecttable_list'),
    path('projecttables/<int:pk>/', views.projecttable_detail, name='projecttable_detail'),
]
