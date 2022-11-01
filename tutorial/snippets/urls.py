from django.urls import path
from . import views, views2, views3, views4

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
     path("snippet/", views.snippet_list),
     path("snippet/<int:pk>/", views.snippet_detail),
     
     path("snippet2/", views2.snippet_list2),
     path("snippet2/<int:pk>/", views2.snippet_detail2),
     
     path("snippet3/", views3.snippet_view_list),
     path("snippet3/<int:pk>/", views3.snippet_view_detail),
     
     path("snippet4/", views4.SnippetList.as_view()),
     path("snippet4/<int:pk>/", views4.SnippetDetail.as_view()),
     
     path("snippet5/", views4.SnippetListCreate.as_view()),
     path("snippet5/<int:pk>/", views4.SnippetAllDetail.as_view()),
     
     path('users/', views4.UserList.as_view()),
     path('users/<int:pk>/', views4.UserDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)