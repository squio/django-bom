from django.conf.urls import include
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin

from bom.views import json_views
from bom.third_party_apis import google_drive
from bom.urls_core import bom_patterns

google_drive_patterns = [
    path('folder/<int:part_id>/', google_drive.get_or_create_and_open_folder, name='add-folder'),
]

json_patterns = [
    path('mouser-part-match-bom/<int:part_revision_id>/', json_views.MouserPartMatchBOM.as_view(), name='mouser-part-match-bom')
]

urlpatterns = [
    path('', include((bom_patterns, 'bom'))),
    path('', include('social_django.urls', namespace='social')),
    path('google-drive/', include((google_drive_patterns, 'google-drive'))),
    path('json/', include((json_patterns, 'json'))),

    # you will likely have your own implementation of these in your app
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), {'redirect_authenticated_user': True, }, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
]
