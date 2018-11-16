from django.urls import path
from . import views as  complaint_view
urlpatterns = [

    path('naturalComplaint/', complaint_view.index_NaturalComplaint, name="index_natural_complaint"),
    path('juridicComplaint/', complaint_view.index_JuridicComplaint, name="index_juridic_complaint"),
    path('naturalComplaint/new', complaint_view.form_NaturalComplaint, name="form_Nat_complaint"),
    path('juridicComplaint/new', complaint_view.form_JuridicComplaint, name="form_Jurid_complaint"),
    path('waitingForDistribution/new', complaint_view.form_WaitingForDistribution, name="form_waiting_for_distribution"),
    path('waitingForDistribution/', complaint_view.index_WaitingForDistribution, name="index_waiting_for_distribution"),
    path('asignedToTecnic/new', complaint_view.form_AsignedToTecnic, name="form_asigned_to_tecnic"),
    path('asignedToTecnic/', complaint_view.index_AsignedToTecnic, name="index_asigned_to_tecnic"),
    path('finishedComplaint/new', complaint_view.form_FinishedComplaint, name="form_finished_complaint"),
    path('finishedComplaint/', complaint_view.index_FinishedComplaint, name="index_finished_complaint"),
    path('accepted/', complaint_view.index_Accepted, name="index_accepted"),
]

