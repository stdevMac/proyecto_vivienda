from django.urls import path
from .views import index, login_page, recover_pass_page, logout_page, users_view, groups_view, logs_view, user_add, group_add, configure_email, \
                   user_edit, group_edit, user_deactivate, user_detail, user_setpass, group_delete, group_detail

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
    path('admin/groups/view/<int:id_grp>', group_detail, name='admin_group_view'),
    path('admin/groups/remove/<int:id_grp>', group_delete, name='admin_group_remove'),
    path('admin/users/form/<int:id_usuario>', user_edit, name='admin_user_edit'),
    path('admin/users/view/<int:id_usuario>', user_detail, name='admin_user_view'),
    path('admin/users/setpass/<int:id_usr>', user_setpass, name='admin_user_setpass'),
    path('admin/users/remove/<int:id_usr>', user_deactivate, name='admin_user_deactive'),
]