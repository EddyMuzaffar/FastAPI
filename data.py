team_group : list = [
    {
        "team": 1,
        "members":["Thomas Lamiable", "Ptit Bat","Eddy Muzzahar"],
        "git":"https://github.com/EddyMuzaffar/FastAPI"

    },
    {
        "team": 2,
        "members": ["Lucie ", "Johan", "Monsieur Propre"],
        "git": "https://github.com/Lucie/FastAPI"
    },
]


def pingAllTeam() -> list:
    """Return Specificly team"""
    return team_group

def pingSelectedTeam():
    for x in team_group:
        (print(team_group.index(x)))

def get_full_Name(first_name:str, second_name:str):
    full_name = first_name.title() + "" + second_name.title()
    return full_name