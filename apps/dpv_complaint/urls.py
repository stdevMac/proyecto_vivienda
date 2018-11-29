from django.conf.urls import url
from django.urls import path, re_path
from . import views as complaint_view
from .index import index as complaint_index
from .render_form import render_forms as rendered_form

urlpatterns = [
    url(r'^$',complaint_view.main_view, name='main_complaint'),
    url(r'^natural/$', complaint_index.index_NaturalComplaint, name="index_natural_complaint"),
    url(r'^juridic/$', complaint_index.index_JuridicComplaint, name="index_juridic_complaint"),
    url(r'^natural/new$', rendered_form.form_NaturalComplaint, name="add_natural_complaint"),
    url(r'^juridic/new$', rendered_form.form_JuridicComplaint, name="add_juridic_complaint"),
    url(r'^waitDistrib/$', complaint_index.index_WaitingForDistribution, name="waiting_for_distribution"),
    url('^finished/$', complaint_index.index_FinishedComplaint, name="index_finished_complaint"),
    url('^acceptedAll/$', complaint_index.index_Accepted, name="index_accepted_all"),

    re_path(r'^accepted/(?P<accepted_id>[0-9]\d*/$)', complaint_view.index_accepted_all, name='accepted_complaint'),
    re_path(r'^asignDepartment/(?P<complaint_id>[1-9]\d*)/$', rendered_form.form_AsignDepartment, name='form_asign_department'),
    re_path(r'^asignedToTecnic/(?P<tecnic_id>[1-9]\d*)/$', complaint_index.index_AsignedToTecnic, name="index_asigned_to_tecnic"),
    re_path(r'^addFinished/(?P<complaint_id>[1-9]\d*)/(?P<tecnic_id>[0-9]*)/$', complaint_view.from_asignedToTecnic_to_finishedComplaint, name="form_finished_complaint"),
    re_path(r'^addAccepted/(?P<finished_id>[1-9]\d*)/$', rendered_form.form_Accepted , name="form_accepted_complaint"),
    re_path(r'^complaint/(?P<complaint_id>[1-9]\d*)/$', complaint_view.watch_complaint, name="watch_complaint"),
    re_path(r'^transWaitToASigned/(?P<complaint_id>[1-9]\d*)/$',complaint_view.from_waitingForDistribution_to_asignedToTecnic, name='trans_Wait_To_Asigned'),
    re_path(r'^transFinishedToAccepted/(?P<complaint_id>[1-9]\d*)/(?P<tecnic_id>[1-9]\d*)/$',complaint_view.from_finishedComplaint_to_acceptedComplaint, name='trans_Finished_to_Accepted'),
]


