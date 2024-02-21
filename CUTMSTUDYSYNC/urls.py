"""
URL configuration for CUTMSTUDYSYNC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

# -----views-----
from CUTMSTUDYSYNC import views
# -----notes-------S
from addnotes import views as addnoteviews
from adminnotes import views as adminnoteviews
from notes import views as noteviews

# -----notice-----C
from addnotice import views as addnoticeviews
from adminnotice import views as adminnoticeviews
from notice import views as noticeviews




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='HOME'),
    path('add/',views.add,name='Add'),
    path('tryy/',views.tryy,name='TRY'),
    # -----notes-------
    path('add_notes/',addnoteviews.addnotes,name='Add Notes'),
    path('admin_notes/',adminnoteviews.adminnotes,name='Admin Notes'),
    path('delete_note/<int:id>/', adminnoteviews.delete_note, name='delete_note'),
    path('viewnotes/',noteviews.viewnotes,name='View Notes'),
    path('filternotes',noteviews.filternotes,name='filternotes'),
    path('filternotesadmin',adminnoteviews.filternotesadmin,name='filternotesadmin'),
    # ------------------------
    path('add_notice/',addnoticeviews.addnotice,name='Add Notice'),
    path('admin_notice/',adminnoticeviews.adminnotice,name='Admin Notice'),
    path('delete_notice/<int:id>/', adminnoticeviews.delete_notice, name='delete_notice'),
    path('viewnotice/',noticeviews.viewnotice,name='View Notice'),



    #-------------------                                      ------------------------
    #------------------- url atributes redirecting (menu bar) ------------------------
    #-------------------                                      ------------------------
    path('admin_notes/admin_notes',adminnoteviews.adminnotes,name='Admin Notes'),
    path('admin_notice/admin_notice',adminnoticeviews.adminnotice,name='Admin Notice'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
