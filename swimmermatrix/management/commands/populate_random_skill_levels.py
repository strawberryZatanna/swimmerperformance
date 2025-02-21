import random
from django.core.management.base import BaseCommand
from swimmermatrix.models import Swimmer, SwimMeet, SwimStrokeSkills, SkillLevel

class Command(BaseCommand):
    help = 'Randomizes skill levels for every swimmer for each skill at every swim meet'

    def handle(self, *args, **kwargs):
        skill_levels = ["beginner", "intermediate", "advanced", "competitive", "champion"]

        # Get all the existing swimmers, swim meets, and swim stroke skills
        swimmers = Swimmer.objects.all()
        swim_meets = SwimMeet.objects.all()
        swim_stroke_skills = SwimStrokeSkills.objects.all()

        # Loop through all swimmers
        for swimmer in swimmers:
            # For each swimmer, loop through all swim strokes
            for swim_stroke_skill in swim_stroke_skills:
                # For each swimmer-stroke combination, loop through all swim meets
                for swim_meet in swim_meets:
                    # Randomly choose a skill level for the swimmer for this stroke and meet
                    level = random.choice(skill_levels)

                    # Check if a SkillLevel entry already exists for this combination
                    skill_level_exists = SkillLevel.objects.filter(
                        swimmer=swimmer,
                        swim_stroke_skill=swim_stroke_skill,
                        swim_meet=swim_meet
                    ).exists()

                    if not skill_level_exists:
                        # Create a new SkillLevel entry if it doesn't exist
                        SkillLevel.objects.create(
                            swimmer=swimmer,
                            swim_stroke_skill=swim_stroke_skill,
                            swim_meet=swim_meet,
                            level=level
                        )

        self.stdout.write(self.style.SUCCESS('Successfully randomized skill levels for swimmers!'))

