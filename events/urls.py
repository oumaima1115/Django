from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name="Home_Page"),
    path('listStatic/', listEventsStatic, name="events_list_static"),
    path('list/', listEvents, name="events_list"),
    path('add/', addEvent, name="events_add"),
    path('details/<int:id>', detailsEvent, name="events_details"),
    path('update/<int:id>', updateEvent, name="events_update"),
    path('participate/<int:id>', participateEvent, name="events_participate"),
    path('undoParticipate/<int:id>', undoParticipateEvent, name="events_undoParticipate"),
    path('delete/<int:id>', deleteEvent, name="event_delete"),
    path('listEvents/', EventsList.as_view(), name="events_listC"),
    path('eventsDetails/<int:pk>', EventsDetails.as_view(), name="events_DetailsC"),
    path('eventUpdate/<int:pk>', EventUpdateView.as_view(), name="events_UpdateC"),
    path('eventDelete/<int:pk>', EventDeleteView.as_view(), name="event_deleteTwoC"),
]
