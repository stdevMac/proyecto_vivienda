from django.urls import path
from . import views as  complaint_view

urlpatterns = [

    path('complaint/new', complaint_view.form_Complaint, name="form_complaint"),
    path('complaint/', complaint_view.index_Complaint , name="index_complaint"),
    path('presentedComplaint/new', complaint_view.form_PresentedComplaint, name="form_presented_complaint"),
    path('presentedComplaint/', complaint_view.index_PresentedComplaint, name="index_presented_complaint"),
    path('waitingForDistribution/new', complaint_view.form_WaitingForDistribution, name="form_waiting_for_distribution"),
    path('waitingForDistribution/', complaint_view.index_WaitingForDistribution, name="index_waiting_for_distribution"),
    path('asignedToTecnic/new', complaint_view.form_AsignedToTecnic, name="form_asigned_to_tecnic"),
    path('asignedToTecnic/', complaint_view.index_AsignedToTecnic, name="index_asigned_to_tecnic"),
    path('finishedComplaint/new', complaint_view.form_FinishedComplaint, name="form_finished_complaint"),
    path('finishedComplaint/', complaint_view.index_FinishedComplaint, name="index_finished_complaint"),
    path('accepted/', complaint_view.index_Accepted, name="index_accepted"),

    # path('naturalPerson/new', complaint_view.form_NaturalPerson, name="FormNaturalperson"),
    # # path('juridicPerson/new', complaint_view.post_JuridicPerson, name="FormJuridicperson"),
    # path('naturalPerson/', complaint_view.index_NaturalPerson, name="naturalPerson"),
    # # path('juridicPerson/', complaint_view.index_JuridicPerson, name="juridicPerson"),
    # path('', complaint_view.index_Complaint, name="quejas"),

]
