from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        hulk = User.objects.create(name='Hulk', email='hulk@marvel.com', team=marvel)
        thor = User.objects.create(name='Thor', email='thor@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)
        wonderwoman = User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc)

        # Create Activities
        Activity.objects.create(user=ironman, activity_type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=hulk, activity_type='Swimming', duration=45, date=timezone.now().date())
        Activity.objects.create(user=thor, activity_type='Cycling', duration=60, date=timezone.now().date())
        Activity.objects.create(user=batman, activity_type='Running', duration=25, date=timezone.now().date())
        Activity.objects.create(user=superman, activity_type='Flying', duration=120, date=timezone.now().date())
        Activity.objects.create(user=wonderwoman, activity_type='Climbing', duration=50, date=timezone.now().date())

        # Create Workouts
        w1 = Workout.objects.create(name='Pushups', description='Upper body workout')
        w2 = Workout.objects.create(name='Situps', description='Core workout')
        w3 = Workout.objects.create(name='Squats', description='Leg workout')
        w1.suggested_for.set([ironman, batman])
        w2.suggested_for.set([hulk, superman])
        w3.suggested_for.set([thor, wonderwoman])

        # Create Leaderboard
        Leaderboard.objects.create(user=ironman, score=100, rank=1)
        Leaderboard.objects.create(user=batman, score=90, rank=2)
        Leaderboard.objects.create(user=superman, score=80, rank=3)
        Leaderboard.objects.create(user=thor, score=70, rank=4)
        Leaderboard.objects.create(user=hulk, score=60, rank=5)
        Leaderboard.objects.create(user=wonderwoman, score=50, rank=6)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
