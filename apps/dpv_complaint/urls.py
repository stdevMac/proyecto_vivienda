from django.conf.urls import url
from django.urls import re_path
from . import views as complaint_view
from .index import index as complaint_index
from .render_form import render_forms as rendered_form
from .render_form import render_natural_complaint_form as render_natural_complaint
from .render_form import render_juridic_complaint_form as render_juridic_complaint

urlpatterns = [
    url(r'^$', complaint_view.main_view, name='main_complaint'),
    url(r'^natural/$', complaint_index.index_natural_complaint, name="index_natural_complaint"),
    url(r'^juridic/$', complaint_index.index_juridic_complaint, name="index_juridic_complaint"),
    url(r'^natural/new$', render_natural_complaint.form_person_for_complaint, name="add_natural_person"),
    url(r'^juridic/new$', render_juridic_complaint.form_juridic_complaint, name="add_juridic_complaint"),
    url(r'^wait_distribution/$', complaint_index.index_waiting_for_distribution, name="waiting_for_distribution"),
    url(r'^finished/$', complaint_index.index_finished_complaint, name="index_finished_complaint"),
    url(r'^accepted_all/$', complaint_index.index_accepted, name="index_accepted_all"),

    re_path(r'^complaint_nat/(?P<person_id>[1-9]\d*)/$', render_natural_complaint.form_natural_complaint,
            name='add_natural_complaint'),
    re_path(r'^get_complaints/(?P<person_id>[1-9]\d*)/$', render_natural_complaint.middle_form_natural_complaint,
            name='get_complaints_for_person'),
    re_path(r'^complaints_by_person/(?P<person_id>[1-9]\d*)/$', render_natural_complaint.middle_form_natural_complaint,
            name='complaints_by_person'),
    re_path(r'^get_accepted/(?P<accepted_id>[1-9]\d*)/$', complaint_view.index_accepted_all, name='accepted_complaint'),
    re_path(r'^assign_department/(?P<complaint_id>[1-9]\d*)/$', rendered_form.form_assign_department,
            name='form_assign_department'),
    re_path(r'^assigned_to_technical/(?P<technical_id>[1-9]\d*)/$',
            complaint_index.index_assigned_to_technician, name="index_assigned_to_technical"),
    re_path(r'^add_finished/(?P<complaint_id>[1-9]\d*)/(?P<technical_id>[0-9]*)/$',
            complaint_view.from_assigned_to_technician_to_finished_complaint, name="form_finished_complaint"),
    re_path(r'^add_accepted/(?P<finished_id>[1-9]\d*)/$', rendered_form.form_accepted, name="form_accepted_complaint"),
    re_path(r'^complaint/(?P<complaint_id>[1-9]\d*)/$', complaint_view.watch_complaint, name="watch_complaint"),
    re_path(r'^trans_wait_to_assigned/(?P<complaint_id>[1-9]\d*)/$',
            complaint_view.from_waiting_for_distribution_to_assigned_to_technician, name='trans_Wait_To_Asigned'),
    re_path(r'^trans_finished_to_accepted/(?P<complaint_id>[1-9]\d*)/(?P<technical_id>[1-9]\d*)/$',
            complaint_view.from_finished_complaint_to_accepted_complaint, name='trans_Finished_to_Accepted'),
]
