import json, os
from django.apps import apps
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from song_app.models import Song
from django.conf import settings

@receiver(post_migrate)
def add_data(sender, **kwargs):

        # Check if the model has any existing data
    if not Song.objects.exists():
        json_file_path = os.path.join(settings.STATIC_ROOT, 'json/data.json')
        with open(json_file_path) as file:
            data = json.load(file)
            songs = data.get('id')
            song_list = []
            for i, song_id in enumerate(songs.values()):
                title = data['title'][str(i)]
                danceability = data['danceability'][str(i)]
                energy = data['energy'][str(i)]
                key = data['key'][str(i)]
                loudness = data['loudness'][str(i)]
                mode = data['mode'][str(i)]
                acousticness = data['acousticness'][str(i)]
                instrumentalness = data['instrumentalness'][str(i)]
                liveness = data['liveness'][str(i)]
                valence = data['valence'][str(i)]
                tempo = data['tempo'][str(i)]
                duration_ms = data['duration_ms'][str(i)]
                time_signature = data['time_signature'][str(i)]
                num_bars = data['num_bars'][str(i)]
                num_sections = data['num_sections'][str(i)]
                num_segments = data['num_segments'][str(i)]
                
                song = Song(id=song_id, title=title, danceability=danceability, energy=energy, key=key,
                            loudness=loudness, mode=mode, acousticness=acousticness,
                            instrumentalness=instrumentalness, liveness=liveness,
                            valence=valence, tempo=tempo, duration_ms=duration_ms,
                            time_signature=time_signature, num_bars=num_bars,
                            num_sections=num_sections, num_segments=num_segments)
                song_list.append(song)
            
            Song.objects.bulk_create(song_list)