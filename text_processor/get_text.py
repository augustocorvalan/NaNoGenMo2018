import random 

import tracery
from tracery.modifiers import base_english
import pycorpora





rules = {
	'origin': ['#AGENT_WAKES#'],

	## AGENT_WAKES ##
	"AGENT_WAKES": [
		"I woke up suddenly.",

		"I woke up suddenly.",

		"I woke up suddenly.",

		"I woke up.",

		"I woke slowly.",

		"I woke up and realized I couldn't hear anything.",

		"I woke up without memory of the day prior.",

		"Woke up in the dark.",

		"Woke up alone.",

		"Woke up whispering my name.",

		"Woke up exhausted.",

		"Woke up tired again.",

		"Woke up without appetite.",

		"The overwhelming feeling was that of someone watching me as I woke.",

		"The overwhelming feeling was that something fundamental had shifted and I hadn't noticed.",

		"The overwhelming feeling was of urgency",

		"The overwhelming feeling was that anything could happen from one moment to the next.",

		"The overwhelming feeling was that everything I knew didn't apply anymore.",

		"I woke up with a fever.",

		"I woke up and couldn't open my eyes.",

		"I woke up and couldn't feel the texture of the sheets with my fingers.",

		"I woke up and vomited.",

		"I woke up and I could see nothing in the dark.",

		"I woke up and scribbled several pages in my notebook. It seemed important. Then I burned the pages.",

		"I woke up tired.",

		"I woke and didn't realize where I was.",

		"I woke up and for a moment thought I was home.",

		"I woke up dizzy.",

		"I woke up wanting to write down a dream but as soon as I stood up I forgot it.",

		"I woke up alone.",

		"I woke up but didn't get out of bed, not for what felt like a long time.",

		"I woke up and held my breath. I didn't move for as long as I could.",

		"I woke up thinking of assassins.",
	],

	## AGENT_OBSERVES_SELF ##
	"AGENT_OBSERVES_SELF": [
		"I looked in the mirror.",
		"I looked in the mirror for what felt like a long time.",
		"I looked in the mirror for as long as I could.",

		"Time passes in strange ways here.",

		"I took off my shirt and looked at my ribs.",

		"I looked at my nails, how dirty they were.",
		"I looked at my nails, they were long and jagged.",
		"I looked at my nails, pressed them again the palm of my hand, hard.",

		"I looked at my hands, which were covered in cuts.",
		"I examined my eyes in the mirror, red and unfocused.",

		"I checked my face in the mirror. I looked the same but much older.",
		"I checked my face in the mirror. I looked the same but scared.",
		"I checked my face in the mirror. I looked the same but something was off.",
		"I checked my face in the mirror. I looked as long as I could. I had to turn away.",
	],

	## AGENT_USES_BATHROOM ##
	"AGENT_USES_BATHROOM": [
		"I washed my face over and over again.",

		"I washed my face.",

		"I washed my face over and over.",

		"I trimmed my hair.",

		"I cut my nails.",

		"I shaved.",

		"I let the water run, first hot then cold.",

		"I locked myself in the bathroom.",

		"I cleaned the mirror in the bathroom.",

		"I got naked and washed in the tub.",

		"I filled the tub and got in.",

		"I sat in the tub for what felt like a long time.",

		"I sat in the tub and looked at my body.",

		"I checked my body in the mirror.",

		"I checked my eyes in the mirror.",

		"I checked my tongue in the mirror.",

		"I took an aspirin.",

		"I took an aspirin.",

		"I drank a glass of water and an aspirin",

		"I didn't feel good so I took an aspirin.",

		"I drank a glass of water.",

		"I drank a glass of water from the sink.",

		"I went to the sink and drank as much water as I could.",

		"I filled the sink with water and put my face in.",
	],

	## AGENT_EATS ##
	"AGENT_EATS": [
		"#agent_drinks#",
		"#agent_eats#",
		"#agent_drinks# #agent_is_sick#",
		"#agent_eats# #agent_is_sick#",
		"#agent_eats# #agent_drinks# #agent_is_sick#",
	],
	"agent_is_sick": [
		"I felt #drunk_states#.",
		"I felt #drunk_states# and I vomited.",
		"I held my stomach for what felt like a long time.",
		"I vomited.",
		"Afterwards, I felt #drunk_states#.",
		"I felt #drunk_states#",
	],
	"agent_drinks": [
		"I drank a glass of #drinks#.",
		"I drank #drinks#.",
		"I had #drinks.a#.",
		"I had as many #drinks.s# as I could."
	],
	"agent_eats": [
		"I ate a bowl of #fruits.s#.",
		"I ate #fruits.a#.",
		"I ate #fruits.s#.",
		"I ate a plate of #foods.s#.",
		"I ate #foods.a#.",
		"I tried to eat #fruits.a#",
		"I tried to eat #food.a#",
	],
	"drunk_states": [
		"terrible",
		"sick",
		"ill",
		"tipsy",
		"gone",
		"stoned",
		"delerious",
		"disorderly",
	],
	"drinks": [
		"vodka",
		"beer",
	],
	"fruits": [
		"apple",
		"apricot",
		"avocado",
		"banana",
		"bell pepper",
		"blackberry",
		"blackcurrant",
		"blood orange",
		"blueberry",
		"cherry",
		"clementine",
		"coconut",
		"cranberry",
		"cucumber",
		"date",
		"eggplant",
		"elderberry",
		"fig",
		"gooseberry",
		"grape",
		"grapefruit",
		"mandarine",
		"mango",
		"mulberry",
		"nectarine",
		"olive",
		"orange",
		"papaya",
		"passionfruit",
		"peach",
		"pear",
		"plum",
		"pomegranate",
		"quince",
		"raisin",
		"raspberry",
		"strawberry",
		"tangerine",
		"tomato",
		"watermelon"
	],
	"foods": [
		"anchovie",
		"bacon",
		"cheese",
		"chicken",
		"garlic",
		"green pepper",
		"grilled onion",
		"ground beef",
		"ham",
		"hot sauce",
		"meatball",
		"mushroom",
		"olive",
		"onion",
		"pepperoni",
		"sausage",
		"spinach",
		"tomato"
	],


	## AGENT_EXERCISES ##
	"AGENT_EXERCISES": [
		"I massaged my face. Afterwards, it felt numb.",
		"I stretched my legs",
		"I did as many push-ups as I could.",
		"I did as many leg squats as I could.",
		"I did as many push-ups and leg squats as I could.",
		"I tried to stretch but my whole body felt wrong.",
		"I tried to stretch but everything hurt and I couldn't explain why.",
		"I tried to do some push-ups but my body felt wrong.",
		"I tried to do some push-ups but immediately I felt dizzy and had to sit on the floor until it passed.",
		"I tried to go for a run around the house but I blacked-out and can't remember what happened.",
		"I tried to go for a run around the house but the door was jammed and I couldn't push it open.",
	],

	## AGENT_DISCOVERS_SURVEILLANCE ##
	"AGENT_DISCOVERS_SURVEILLANCE": [
		"The telephone still didn't work. When I tried to call I heard a click, as if someone else was listening.",
		"I opened a drawer and found a small tape recorder, still running.",
		"The lamp won't turn on but from inside comes a noise like a tape recorder.",
		"My papers were all out of order as if someone had read them while I slept"
	],

	## AGENT_SLEEPS ##
	"AGENT_SLEEPS": [
		"I fell asleep."
	],

	## AGENT_KILLS_REV ##
	"AGENT_KILLS_REV": [
		"I put the machine over his mouth and turned it on.",
		"I put the machine over his mouth and turned it on. It took six minutes.",

		"I put the machine over his mouth and turned it on. It took fifteen minutes.",

		"I put the machine over his mouth and turned it on. It took eight minutes.",

		"I put the machine over his mouth and turned it on. It took six minutes.",

		"I went into his room at night. He was asleep. It was impossible to see in the dark. I sensed his figure and heard his breath. I put the machine on the nightstand. I unspooled the mask and placed it over his face. The rhythm of his breath changed but he didn't move. I turned the machine on. The breath became rapid and shallow. Then it slowed. Then it couldn't be heard. It took seven minutes.",

		"I went into his room at night. He was asleep. It was impossible to see in the dark. I sensed his figure and heard his breath. I put the machine on the nightstand. I unspooled the mask and placed it over his face. The rhythm of his breath changed but he didn't move. I turned the machine on. It took seven minutes.",

		"I went into his room at night. I put the mask over his mouth and turned it on. It took eight minutes.",

		"I went into his room at night. He was asleep. I put the machine on the nightstand. I put the mask over his mouth and turned it on. It took fifteen minutes.",

		"I went into his room at night. He was asleep. I unspooled the mask and placed it over his face. I turned on the machine. The breath became rapid and shallow. Then it couldn't be heard. It took eight minutes.",
	]
}


def get_tracery(rule_key: str) -> str:
	grammar = tracery.Grammar(rules)
	grammar.add_modifiers(base_english)

	sentence = grammar.flatten('#%s#'%rule_key)

	return sentence

def get_random_text(rule_key: str) -> str:
	""" gets texts from text based on key"""

	# return random.choice(rules[rule_key])
	return get_tracery(rule_key)

def get_text_unique(rule_key: str) -> str:
	""" TODO: like get_text but keeps state so every return is unique """
	pass
