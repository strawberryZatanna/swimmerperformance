from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Swimmer, SwimStroke, SwimMeet, SwimStrokeSkills, SkillLevel

def get_skill_level(swimmer, skill, meet):
    # Query the SkillLevel model for the specific swimmer, skill (swim_stroke_skill), and meet
    skill_level = SkillLevel.objects.filter(
        swimmer=swimmer,
        swim_stroke_skill=skill,  # `skill` should be a `SwimStrokeSkills` instance
        swim_meet=meet
    ).first()  # Get the first result (there is only one SkillLevel per swimmer, skill, and meet)

    if skill_level:
        return skill_level.level  # Return the level (e.g., 'Beginner', 'Intermediate', etc.)
    else:
        return "Unknown"  # Return 'Unknown' if no SkillLevel entry is found

def get_skills(skills, swimmers):
    swim_meets = SwimMeet.objects.all()
    skills_dict = {}

    for meet in swim_meets:
        meet_dict = {}

        for skill in skills:
            skill_dict = {}

            for swimmer in swimmers:
                # `get_skill_level` is a function that retrieves a swimmer's skill level for a given skill
                skill_level = get_skill_level(swimmer, skill, meet)
                skill_dict[swimmer] = skill_level

            meet_dict[skill] = skill_dict

        skills_dict[meet] = meet_dict

    return skills_dict


def get_stroke(request, stroke_name):
    # Get the swim stroke object
    stroke = SwimStroke.objects.filter(stroke_name=stroke_name).first()

    if stroke:
        # Get all the skills related to this stroke
        skills = SwimStrokeSkills.objects.filter(swim_stroke = stroke)

        # Fetch all swimmers in the database (but not use them in the response)
        swimmers = Swimmer.objects.all()

        # Call the get_skills function, passing in the skills and swimmers
        skills_dict = get_skills(skills, swimmers)

        return render(request, 'matrix.html', {'skills_dict': skills_dict, 'stroke': stroke})

    else:
        # Handle the case where the stroke doesn't exist
        return render(request, 'matrix.html', {'error': 'Stroke not found.'})



