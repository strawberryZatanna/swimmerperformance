from django.db import models

# swimmers
class Swimmer(models.Model):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# strokes
class SwimStroke(models.Model):
    id = models.AutoField(primary_key=True)
    stroke_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.stroke_name

# the different skills of each stroke
class SwimStrokeSkills(models.Model):
    id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=100)
    swim_stroke = models.ForeignKey(SwimStroke, on_delete=models.CASCADE, related_name="skills")

    def __str__(self):
        return f"{self.swim_stroke.stroke_name}: {self.skill_name}"


# swim meets in the season. Each meet has a different color setting that can be accessed by the view.
class SwimMeet(models.Model):
    id = models.AutoField(primary_key=True)
    meet_title = models.CharField(max_length=100)
    meet_color = models.CharField(max_length=50)

    sequence = models.PositiveIntegerField(default=0)  # Add a field to determine the order

    def __str__(self):
        return f"{self.meet_title} ({self.meet_color}) - Sequence {self.sequence}"

    class Meta:
        ordering = ['sequence']  # Order by the sequence field



# skill levels of swimmer for EACH skill in EACH stroke
class SkillLevel(models.Model):
    SKILL_LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
        ("competitive", "Competitive"),
        ("champion", "Champion"),
    ]

    id = models.AutoField(primary_key=True)
    level = models.CharField(max_length=20, choices=SKILL_LEVEL_CHOICES)
    swimmer = models.ForeignKey(Swimmer, on_delete=models.CASCADE, related_name="skill_levels")
    swim_stroke_skill = models.ForeignKey(SwimStrokeSkills, on_delete=models.CASCADE, related_name="swimmer_levels")
    swim_meet = models.ForeignKey(SwimMeet, on_delete=models.CASCADE, related_name="skill_levels", null=True)

    def __str__(self):
        return f"{self.swimmer.first_name} {self.swimmer.last_name} - {self.swim_stroke_skill.swim_stroke.stroke_name} ({self.level})"


