import json, os
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from song_app.views import SongViewSet
from song_app.models import Song
from song_app.config import PAGE_SIZE
from django.conf import settings



class SongListViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = SongViewSet.as_view({'get': 'list'})
        self.url = '/songs/'


    def test_on_migrate_song_creations(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        songs = Song.objects.all() # automatic all the song will be created at time of migrations

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the number of songs returned in the response matches the number of songs in the database
        self.assertEqual(response.data["data"]["count"], songs.count())

    def test_same_json_data_created(self):
        songs_queryset = Song.objects.all() # automatic all the song will be created at time of migrations

        json_file_path = os.path.join(settings.STATIC_ROOT, 'json/data.json')
        with open(json_file_path) as file:
            data = json.load(file)
            for i in range(2):
                song = songs_queryset[i]
                self.assertEqual(data['id'][str(i)], song.id)
                self.assertEqual(data['title'][str(i)], song.title)
                self.assertEqual(data['danceability'][str(i)], song.danceability)
                self.assertEqual(data['energy'][str(i)], song.energy)
                self.assertEqual(data['key'][str(i)], song.key)
                self.assertEqual(data['loudness'][str(i)], song.loudness)
                self.assertEqual(data['mode'][str(i)], song.mode)
                self.assertEqual(data['acousticness'][str(i)], song.acousticness)
                self.assertEqual(data['instrumentalness'][str(i)], song.instrumentalness)
                self.assertEqual(data['liveness'][str(i)], song.liveness)
                self.assertEqual(data['valence'][str(i)], song.valence)
                self.assertEqual(data['tempo'][str(i)], song.tempo)
                self.assertEqual(data['duration_ms'][str(i)], song.duration_ms)
                self.assertEqual(data['time_signature'][str(i)], song.time_signature)
                self.assertEqual(data['num_bars'][str(i)], song.num_bars)
                self.assertEqual(data['num_sections'][str(i)], song.num_sections)
                self.assertEqual(data['num_segments'][str(i)], song.num_segments)


    def test_song_pagination(self):
        request = self.factory.get(self.url)
        response = self.view(request)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the number of songs returned in the response matches the desired page size
        self.assertEqual(len(response.data['data']['results']), PAGE_SIZE)


    def test_song_filter_by_title(self):
        filter_title = '3AM'  # Title to be used for filtering
        request = self.factory.get(self.url, {'title': filter_title})
        response = self.view(request)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the returned songs have the expected title
        for song_data in response.data['data']['results']:
            self.assertEqual(song_data['title'], filter_title)


class SongDetailViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = SongViewSet.as_view({'get': 'retrieve'})
        self.url = '/songs/'

    def test_retrieve_song_by_id(self):
        song_id = "7kcCB7oh6X4bSoFCvrHLvG" # ID of the song to be retrieved
        song_title = "24/7"
        request = self.factory.get(f'{self.url}{song_id}/')
        response = self.view(request, pk=song_id)
        response_data = response.data['data']

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the returned song has the expected ID and title
        self.assertEqual(response_data['id'], song_id)
        self.assertEqual(response_data['title'], song_title)


class SongPartialUpdateTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = SongViewSet.as_view({'patch': 'partial_update'})
        self.url = '/songs/'

    def test_partial_update_song_rating(self):
        song_id = "7kcCB7oh6X4bSoFCvrHLvG"  # ID of the song to be updated
        rating_value = 3  # rating value to be updated


        # Send a PATCH request to update the song rating
        data = {'rating': rating_value}
        request = self.factory.patch(f'{self.url}{song_id}/', data=data)
        response = self.view(request, pk=song_id)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Get the song from the database
        song_obj = Song.objects.get(id = song_id)

        # Assert that the song's rating has been updated correctly
        self.assertEqual(response.data['data']['rating'], rating_value)
        self.assertEqual(song_obj.rating, rating_value)






