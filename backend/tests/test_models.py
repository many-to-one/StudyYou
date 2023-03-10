# from http import client
from django.urls import reverse
from django.utils import timezone
from django.test import Client, TestCase
from ..models import *
from ..serializers import *
from rest_framework import status
from users_app.models import User


class EventTest(TestCase):
    def setUp(self):
        self.eve = Event.objects.create(
            date = timezone.now(),
            event='test-event',
            hours=1,
            minutes=1,
            visits=1,
            publications=1,
            films=1,
            studies=1,
            user=User.objects.create(
                id=2,
            )
        )

    def testEvent(self):
        Event.objects.get(date=timezone.now()) 
        Event.objects.get(event='test-event')
        Event.objects.get(hours=1)
        Event.objects.get(minutes=1)
        Event.objects.get(visits=1)
        Event.objects.get(publications=1)
        Event.objects.get(films=1)
        Event.objects.get(studies=1)   
        Event.objects.get(user=2)


    def testEventsApiGET(self):
        client = Client()
        response = client.get(reverse('events', kwargs={'pk': self.eve.user.pk}))
        events = Event.objects.filter(user__id=self.eve.user.pk)
        serializer = EventSerializer(events, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testEventApiGET(self):
        client = Client()
        response = client.get(reverse('event', kwargs={'ev_pk': self.eve.pk, 'user_pk': self.eve.user.pk}))
        event = Event.objects.get(
            id=self.eve.pk,
            user__id=self.eve.user.pk 
        )
        serializer = EventSerializer(event, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class MonthTest(TestCase):
    def setUp(self):
        Months.objects.create(
            date = '2023-03-02',
            hours=2,
            minutes=2,
            visits=2,
            publications=2,
            films=2,
            user=User.objects.create(
                id=5,
            )
        )

    def testMonth(self):
        Months.objects.get(date='2023-03-02') 
        Months.objects.get(hours=2)
        Months.objects.get(minutes=2)
        Months.objects.get(visits=2)
        Months.objects.get(publications=2)
        Months.objects.get(films=2)  
        Months.objects.get(user=5)


class EventsHistoryTest(TestCase):
    def setUp(self):
        self.ev_history=EventsHistory.objects.create(
            date = timezone.now(),
            event='test-history-event',
            hours=2,
            minutes=2,
            visits=2,
            publications=2,
            films=2,
            studies=2,
            user=User.objects.create(
                id=4,
            ),
            month=Months.objects.create(
                id=2,
            )
        )

    def testHistoryEvent(self):
        EventsHistory.objects.get(date=timezone.now()) 
        EventsHistory.objects.get(event='test-history-event')
        EventsHistory.objects.get(hours=2)
        EventsHistory.objects.get(minutes=2)
        EventsHistory.objects.get(visits=2)
        EventsHistory.objects.get(publications=2)
        EventsHistory.objects.get(films=2)
        EventsHistory.objects.get(studies=2)   
        EventsHistory.objects.get(user=4)
        EventsHistory.objects.get(month=2)

    def testEventsHistoryApi(self):
        client = Client()
        response = client.get(reverse('events_history', kwargs={'user_pk': self.ev_history.user.pk}))
        events = EventsHistory.objects.filter(user=self.ev_history.user.pk)
        serializer = EventsHistorySerializer(events, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CalendarTest(TestCase):
    def setUp(self):
        Calendar.objects.create(
            date='test-date',
            action='test-action',
            user=User.objects.create(
                id=5,
            ),
        )

    def testCalendar(self):
        Calendar.objects.get(date='test-date')
        Calendar.objects.get(action='test-action')
        Calendar.objects.get(user=5)
