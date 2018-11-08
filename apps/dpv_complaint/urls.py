from django.urls import path
from . import views as  complaint_view

urlpatterns = [

    path('complaint/new', complaint_view.form_Complaint, name="form_complaint"),

    # path('naturalPerson/new', complaint_view.form_NaturalPerson, name="FormNaturalperson"),
    # # path('juridicPerson/new', complaint_view.post_JuridicPerson, name="FormJuridicperson"),
    # path('naturalPerson/', complaint_view.index_NaturalPerson, name="naturalPerson"),
    # # path('juridicPerson/', complaint_view.index_JuridicPerson, name="juridicPerson"),
    # path('', complaint_view.index_Complaint, name="quejas"),

]
