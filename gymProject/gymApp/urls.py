from django.urls import path , include
from gymApp import views
from gymApp.views import *

urlpatterns = [
    path("",views.home,name="home"),
    path("get",gymMembership.as_view()),
    path("post",gymMembership.as_view()),
    path('deleteApi', views.Delete.as_view()),
    path('delete_again/<int:pk>', views.Deleteagain.as_view()),
    path("update",views.UpdateData.as_view()),
    path("signup",views.signup,name='signup'),
    path("members",views.retrieval,name="members"),
    path("trainers",views.trainers,name="trainers"),
    path('delete',views.deletingEntry, name="delete"),
    # path("upd/<int:pk>/",views.updatingEntry,name="upd"),
    path("updation/upd", views.updatingEntry, name="upd"),
    path("slotUpdation/updatingSlot", views.updatingSlot, name="updatingSlot"),
    path("updationTrainer/updatingTrainer", views.updatingTrainer, name="updatingTrainer"),
    path("updationPlans/updatingPlans", views.updatingPlans, name="updatingPlans"),
    path("updation/<int:id>",views.updation.as_view(),name="updation"),
    path("slotUpdation/<int:id>",views.slotUpdation.as_view(),name="slotUpdation"),
    path("updationTrainer/<int:id>",views.updationTrainer.as_view(),name="updationTrainer"),
    path("updationPlans/<int:id>",views.updationPlans.as_view(),name="updationPlans"),
    path("services",views.services,name="services"),
    path("registration",views.registration,name="registration"),
    path("gymAdminPlans",views.gymAdminPlans,name="gymAdminPlans"),
    path("gymAdmin",views.gymMyAdmin.as_view(),name="gymAdmin"),
    path("adminPage",views.adminPage),
    path("deleted",views.deleted),
    path("passing",views.passingAdmin),
    path("passingTrainer",views.passingTrainer),
    path("deletingTrainer",views.deletingTrainer,name="deletingTrainer"),
    path("deletingPlans",views.deletingPlans,name="deletingPlans"),
    path("updated",views.updated),
    path("blog",views.blog),
    path("addPlan",views.addPlan),
    path("viewPlans",views.viewPlans),
    path("addGymPlans",views.addGymPlans,name="addGymPlans"),
    path("plansAdded",views.addedPlans,name="plansAdded"),
    path("contact",views.contact),
    path("trainerReg",views.trainerReg),
    path("trainerRegistration",views.trainerRegistration, name="trainerRegistration"),
    path("bookSlotsPage",views.bookSlotsPage,name="bookSlotsPage"),
    path("bookingSlots",views.bookingSlots,name="bookingSlots"),
    path("slots",views.listOfBookedSlots,name="slots"),
    path("deletedSlots",views.deletingSlots,name="deletedSlots")
]