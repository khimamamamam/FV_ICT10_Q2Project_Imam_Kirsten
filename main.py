
from pyscript import document

# GET TO KNOW ME

about_cards = [
    ("🧬 ABOUT ME", "My name is Kirsten Heart Imam, currently in Grade 10 from OBMC Fairview. I've been doing ICT for 4 years now (from Grade 7-10). I can describe myself as an average, curious, and creative student; despite not being ideally smart or computer expert."),
    ("🔬 MY INTERESTS", "Although ICT's one of my weak subjects, I find it very fascinating and fun when it comes to coding. Some subjects I find intriguing though are Mathematics, Science, and English Literature. Other personal things that spark my curiosity are animals, nature, and aspects related to psychology."),
    ("🦠 MY HOBBIES", "Under hobbies, specifically indoors, I either study for school and accomplish as much assignments as I can; or do my personal leisures such as playing games. For outdoor activities, I spend time with my family even if it's something as simple as going out to eat."),
    ("🧪 MY DREAMS & ASPIRATIONS", "I am looking forward mostly onto studying psychology in the future, and applying it in our society (such as theories, archetypes, frameworks, etc.). It will be a challenge though, considering how complex and abstract it is than I thought; but I'd be willing to take the challenge.")
] #lists of tuples

about_html = ""

for title, description in about_cards:
    about_html += f'<div class="card"><h3>{title}</h3><p>{description}</p></div>'

document.getElementById("about-cards").innerHTML = about_html


# PROJECTS SHOWCASE

projects = [
    ("PROJECT 01", "SEATWORK 1", "🌐 NICKNAME ATLAS", "Candidate Verification System that checks whether a certain person is included in the list of club members.", "https://khimamamamam.github.io/FV_ICT10_Q2Seatwork1_Imam_Kirsten/"),
    ("PROJECT 02", "DRILL 2", "🧬 SCHOOL CLUB MEMBERS", "A digital showcase where users can add themselves as part of the club members list.", "https://khimamamamam.github.io/FV_ICT10_Q2Drill2_Imam_Kirsten/"),
    ("PROJECT 03", "SKILLS TEST", "⚗️ ELEMENT CHECKER", "An interactive element checker that allows the user to search for details on any non-metal elements.", "https://khimamamamam.github.io/FV_ICT10_Q2SkillsTest_Imam_Kirsten/")
]

project_html = ""

for number, category, name, description, link in projects:
    project_html += f'<div class="project-card"><div class="project-number">{number}</div><div class="project-type">{category}</div><h3>{name}</h3><p>{description}</p><a href="{link}">EXPLORE PROJECT ↗</a></div>'

document.getElementById("project-cards").innerHTML = project_html
