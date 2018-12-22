from django.urls import path
from .views import index, login_page, recover_pass_page, logout_page, users_view, groups_view, logs_view, user_add, group_add, configure_email, user_edit, group_edit

urlpatterns = [
    path('dashboard/', index, name='base_dashboard'),
    path('login/', login_page, name='base_login'),
    path('recoverpass/', recover_pass_page, name='base_recoverpass'),
    path('logout/', logout_page, name='base_logout'),
    path('admin/users/', users_view, name='admin_user'),
    path('admin/users/form/', user_add, name='admin_user_add'),
    path('admin/groups/', groups_view, name='admin_group'),
    path('admin/groups/form/', group_add, name='admin_group_add'),
    path('admin/email/', configure_email, name='admin_emailconf'),
    path('admin/logs/', logs_view, name='admin_logs'),
    path('admin/groups/form/<int:id_group>', group_edit, name='admin_group_edit'),
    path('admin/users/form/<int:id_usuario>', user_edit, name='admin_user_edit'),
]