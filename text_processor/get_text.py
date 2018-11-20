import random 

texts = {
	"AGENT_WAKES": [
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

		"Woke up without appetite.",

		"The overwhelming feeling was that of someone watching me as I woke.",

		"The overwhelming feeling was that something fundamental had shifted and I hadn't noticed.",

		"I woke up with a fever.",

		"I woke up and could't open my eyes.",

		"I woke up and couldn't feel the texture of the sheets with my fingers.",

		"I woke up and vomited.",

		"I woke up and I could see nothing in the dark.",

		"I woke up and scribbled several pages in my notebook. It seemed important. Then I burned the pages."
	],

	"AGENT_OBSERVES_SELF": [
		"I looked in the mirror.",
		"I looked at my nails, how dirty they were.",
		"I looked at my hands, which were covered in cuts."
	],

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

	"AGENT_SLEEPS": [
		"I fell asleep."
	],

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


def get_random_text(text_key: str) -> str:
	""" gets texts from text based on key"""

	return random.choice(texts[text_key])

def get_text_unique(text_key: str) -> str:
	""" TODO: like get_text but keeps state so every return is unique """
	pass
