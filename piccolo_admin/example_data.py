import datetime


DIRECTORS = [
    {"id": 1, "name": "Peter Jackson"},
    {"id": 2, "name": "George Lucas"},
    {"id": 3, "name": "J.J. Abrams"},
    {"id": 4, "name": "Gareth Edwards"},
    {"id": 5, "name": "Irvin Kershner"},
    {"id": 6, "name": "Richard Marquand"},
    {"id": 7, "name": "Rian Johnson"},
    {"id": 8, "name": "Ron Howard"},
]

MOVIES = [
    {
        "name": "Star Wars: Episode IV - A New Hope",
        "rating": 93,
        "director": 2,
        "description": (
            "After Princess Leia, the leader of the Rebel Alliance, is held "
            "hostage by Darth Vader, Luke and Han Solo must free her and "
            "destroy the powerful weapon created by the Galactic Empire."
        ),
        "release_date": datetime.datetime(year=1977, month=12, day=27),
    },
    {
        "name": "The Empire Strikes Back",
        "rating": 94,
        "director": 5,
        "description": (
            "Darth Vader is adamant about turning Luke Skywalker to the dark "
            "side. Master Yoda trains Luke to become a Jedi Knight while his "
            "friends try to fend off the Imperial fleet."
        ),
        "release_date": datetime.datetime(year=1980, month=5, day=20),
    },
    {
        "name": "Return of the Jedi",
        "rating": 82,
        "director": 6,
        "description": (
            "Luke Skywalker attempts to bring his father back to the light "
            "side of the 'Force'. At the same time, the rebels hatch a plan "
            "to destroy the second Death Star."
        ),
        "release_date": datetime.datetime(year=1983, month=6, day=2),
    },
    {
        "name": "Star Wars: Episode I – The Phantom Menace",
        "rating": 53,
        "director": 2,
        "description": (
            "Two Jedi Knights set out to search for someone who can "
            "bring peace to the Force. Their search ends when they come "
            "across a young, gifted boy. But the Sith returns to stake claim "
            "to the Force."
        ),
        "release_date": datetime.datetime(year=1999, month=7, day=16),
    },
    {
        "name": "Star Wars: Episode II – Attack of the Clones",
        "rating": 65,
        "director": 2,
        "description": (
            "While pursuing an assassin, Obi Wan uncovers a sinister plot to "
            "destroy the Republic. With the fate of the galaxy hanging in the "
            "balance, the Jedi must defend the galaxy against the evil Sith."
        ),
        "release_date": datetime.datetime(year=2002, month=5, day=16),
    },
    {
        "name": "Star Wars: Episode III – Revenge of the Sith",
        "rating": 80,
        "director": 2,
        "description": (
            "Anakin joins forces with Obi-Wan and sets Palpatine free from "
            "the evil clutches of Count Doku. But he falls prey to mind games "
            "that are played by Palpatine and the Jedis and gives into "
            "temptation."
        ),
        "release_date": datetime.datetime(year=2005, month=5, day=19),
    },
    {
        "name": "Star Wars: The Force Awakens",
        "rating": 93,
        "director": 3,
        "description": (
            "A new order threatens to destroy the New Republic. Finn, Rey and "
            "Poe, backed by the Resistance and the Republic, must find a way "
            "to stop them and find Luke, the last surviving Jedi."
        ),
        "release_date": datetime.datetime(year=2015, month=12, day=17),
    },
    {
        "name": "Rogue One: A Star Wars Story",
        "rating": 83,
        "director": 4,
        "description": (
            "When she's a child, Jyn's father is forcibly taken by the Empire "
            "to help them complete the Death Star. As an adult, she joins a "
            "group of resistance fighters, who aim to steal its blueprints."
        ),
        "release_date": datetime.datetime(year=2016, month=12, day=13),
    },
    {
        "name": "Star Wars: The Last Jedi",
        "rating": 91,
        "director": 7,
        "description": (
            "Rey seeks to learn the ways of the Jedi under Luke Skywalker, "
            "its remaining member, to reinvigorate the Resistance's war "
            "against the First Order."
        ),
        "release_date": datetime.datetime(year=2017, month=12, day=14),
    },
    {
        "name": "Solo: A Star Wars Story",
        "rating": 70,
        "director": 8,
        "description": (
            "In a galaxy where hyperfuel is in high demand, Han Solo gets "
            "involved in a large-scale heist within the criminal underworld "
            "and meets individuals who change his life."
        ),
        "release_date": datetime.datetime(year=2018, month=5, day=25),
    },
    {
        "name": "Star Wars: The Rise of Skywalker",
        "rating": 54,
        "director": 3,
        "description": (
            "The surviving Resistance faces the First Order once more as Rey, "
            "Finn and Poe Dameron's journey continues. With the power and "
            "knowledge of generations behind them, the final battle commences."
        ),
        "release_date": datetime.datetime(year=2019, month=12, day=19),
    },
    {
        "name": "The Lord of the Rings: The Fellowship of the Ring",
        "rating": 91,
        "director": 1,
        "description": (
            "A young hobbit, Frodo, who has found the One Ring that belongs "
            "to the Dark Lord Sauron, begins his journey with eight "
            "companions to Mount Doom, the only place where it can be "
            "destroyed."
        ),
        "release_date": datetime.datetime(year=2001, month=12, day=10),
    },
    {
        "name": "The Lord of the Rings: The Two Towers",
        "rating": 95,
        "director": 1,
        "description": (
            "Frodo and Sam arrive in Mordor with the help of Gollum. A number "
            "of new allies join their former companions to defend Isengard as "
            "Saruman launches an assault on it."
        ),
        "release_date": datetime.datetime(year=2002, month=12, day=11),
    },
    {
        "name": "The Lord of the Rings - The Return of the King",
        "rating": 93,
        "director": 1,
        "description": (
            "The former Fellowship members prepare for the final battle. "
            "While Frodo and Sam approach Mount Doom to destroy the One Ring, "
            "they follow Gollum unaware of the path he is leading them to."
        ),
        "release_date": datetime.datetime(year=2003, month=12, day=17),
    },
    {
        "name": "The Hobbit: An Unexpected Journey",
        "rating": 64,
        "director": 1,
        "description": (
            "Bilbo Baggins, a hobbit, is persuaded into accompanying a wizard "
            "and a group of dwarves on a journey to reclaim the city of "
            "Erebor and all its riches from the dragon Smaug."
        ),
        "release_date": datetime.datetime(year=2012, month=12, day=12),
    },
    {
        "name": "The Hobbit: The Desolation of Smaug",
        "rating": 74,
        "director": 1,
        "description": (
            "Bilbo Baggins, a hobbit, and his companions face great dangers "
            "on their journey to Laketown. Soon, they reach the Lonely "
            "Mountain, where Bilbo comes face-to-face with the fearsome "
            "dragon Smaug."
        ),
        "release_date": datetime.datetime(year=2013, month=12, day=13),
    },
    {
        "name": "The Hobbit: The Battle of the Five Armies",
        "rating": 59,
        "director": 1,
        "description": (
            "Bilbo fights against a number of enemies to save the life of his "
            "Dwarf friends and protects the Lonely Mountain after a conflict "
            "arises."
        ),
        "release_date": datetime.datetime(year=2014, month=12, day=1),
    },
]