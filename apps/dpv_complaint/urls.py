from django.urls import path, re_path
from . import views as complaint_view
from .index import index as complaint_index
from .render_form import render_forms as rendered_form

urlpatterns = [
    #  teniente rey y habana
    path('naturalComplaint/', complaint_index.index_NaturalComplaint, name="index_natural_complaint"),
    path('juridicComplaint/', complaint_index.index_JuridicComplaint, name="index_juridic_complaint"),
    path('naturalComplaint/new', rendered_form.form_NaturalComplaint, name="form_Nat_complaint"),
    path('juridicComplaint/new', rendered_form.form_JuridicComplaint, name="form_Jurid_complaint"),
    path('waitingForDistribution/', complaint_index.index_WaitingForDistribution, name="index_waiting_for_distribution"),
    path('asignedToTecnic/new', rendered_form.form_AsignedToTecnic, name="form_asigned_to_tecnic"),
    path('finished/', complaint_index.index_FinishedComplaint, name="index_finished_complaint"),
    path('accepted/', complaint_index.index_Accepted, name="index_accepted"),
    re_path(r'asignDepartment/(?P<complaint_id>[1-9]\d*)/$', rendered_form.form_AsignDepartment, name='form_asign_department'),
    re_path(r'asignedToTecnic/(?P<tecnic_id>[1-9]\d*)/$', complaint_index.index_AsignedToTecnic, name="index_asigned_to_tecnic"),
    re_path(r'finishedComplaint/(?P<complaint_id>[1-9]\d*)/(?P<tecnic_id>[0-9]*)/$', complaint_view.from_asignedToTecnic_to_finishedComplaint, name="form_finished_complaint"),
    re_path(r'complaint/(?P<complaint_id>[1-9]\d*)/$', complaint_view.watch_complaint, name="watch_complaint"),
    re_path(r'transWaitToASigned/(?P<complaint>[1-9]\d*)/$',complaint_view.from_waitingForDistribution_to_asignedToTecnic, name='trans_Wait_To_Asigned'),
    re_path(r'transFinishedToAccepted/(?P<complaint_id>[1-9]\d*)/(?P<tecnic_id>[1-9]\d*)/$',complaint_view.from_finishedComplaint_to_acceptedComplaint, name='trans_Finished_to_Accepted'),
    # re_path(r'finishedComplaint/(?P<complaint>[0-9]\d*)/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$')
]


