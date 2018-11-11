import random 

texts = {
	"AGENT_WAKES": ["I woke up suddenly."],

	"AGENT_OBSERVES_SELF": [
		"I looked in the mirror."
	],

	"AGENT_USES_BATHROOM": [
		"I washed my face over and over again."
	],

	"AGENT_SLEEPS": [
		"I fell asleep without dreaming."
	],

	"AGENT_KILLS_REV": [
		"I put the machine over his mouth and turned it on."
	]
}


def get_random_text(text_key: str) -> str:
	""" gets texts from text based on key"""

	return random.choice(texts[text_key])

def get_text_unique(text_key: str) -> str:
	""" TODO: like get_text but keeps state so every return is unique """
	pass
