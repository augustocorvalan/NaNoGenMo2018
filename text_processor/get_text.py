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

		"The overwhelming feeling was of urgency.",

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

		"I woke up clenching my teeth.",

		"I woke up without really sleeping.",

		"I woke up confused.",

		"Woke up agitated.",

		"I woke from a type of vision. I couldn't puzzle it together.",

		"I woke up with some words from a prophecy.",

		"I woke up mumbling non-sense.",

		"I woke up with a gasp.",

		"I woke up very early.",

		"I woke up very late.",

		"I didn't want to wake up.",

		"I woke up though it was still dark.",

		"I jumped out of bed. My nose was bleeding."
	],

	## AGENT_OBSERVES_SELF ##
	"AGENT_OBSERVES_SELF": [
		"I looked in the mirror.",
		"I looked in the mirror for what felt like a long time.",
		"I looked in the mirror for as long as I could.",
		"I couldn't see my face in the mirror.",
		"It was too dark to see the mirror.",
		"I cleaned the mirror but it didn't make much difference.",

		"Time passes in strange ways here.",
		"Time is confused here.",

		"I took off my shirt and looked at my ribs.",
		"I took off my shirt and counted my ribs.",
		"I took off my shirt and saw several scars I didn't recognize.",
		"I took off my shirt. Was this my body?",
		"I took off my shirt and tried to memorize my body.",

		"I looked at my nails, how dirty they were.",
		"I looked at my nails, they were long and jagged.",
		"I looked at my nails, pressed them again the palm of my hand",

		"My hands were covered in dirt.",
		"My hands were covered in some type of oil.",
		"I looked at my hands, which were covered in cuts.",

		"I examined my eyes in the mirror, red and unfocused.",
		"My eyes didn't look right.",
		"I felt tired.",

		"I checked my face in the mirror. I looked the same but much older.",
		"I checked my face in the mirror. I looked the same but scared.",
		"I checked my face in the mirror. I looked the same but something was off.",
		"I checked my face in the mirror. I looked as long as I could.",

		"I'd lost weight.",
		"I looked skinny.",
		"I looked pale.",
		"I looked pale and skinny.",
		"My teeth looked crooked."
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

		"I drank water in gulps.",

		"I drank three glasses of water.",

		"I stood in the bathroom in the dark.",

		"I washed my hands.",

		"I washed my hands over and over again.",

		"I brushed my teeth.",

		"I filled the tub with cold water.",

		"I filled the basin with cold water. I put my face in."
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
		"I felt #drunk_states#.",
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
		"I tried to eat #fruits.a#.",
		"I tried to eat #foods.a#.",
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
		"I stretched my legs.",
		"I did as many push-ups as I could.",
		"I did as many leg squats as I could.",
		"I did as many push-ups and leg squats as I could.",
		"I tried to stretch but my whole body felt wrong.",
		"I tried to stretch but everything hurt and I couldn't explain why.",
		"I tried to do some push-ups but my body felt wrong.",
		"I tried to do some push-ups but immediately I felt dizzy and had to sit on the floor until it passed.",
		"I tried to go for a run around the house but I blacked out and can't remember what happened.",
		"I tried to go for a run around the house but the door was jammed and I couldn't push it open.",
	],

	## AGENT_DISCOVERS_SURVEILLANCE ##
	"AGENT_DISCOVERS_SURVEILLANCE": [
		"The telephone still didn't work. When I tried to call I heard a click, as if someone else was listening.",
		"I opened a drawer and found a small tape recorder, still running.",
		"The lamp wouldn't turn on but from inside came a noise like a tape recorder.",
		"My papers were all out of order as if someone had read them while I slept.",
		"I felt watched.",
		"I felt watched all the time.",
		"I thought I saw a silhouette at the window. When I looked again it was gone.",
		"The furniture was all rearranged.",
		"I found a small insect in my coat pocket, round and dark like a small camera.",
		"I found a small insect in my coat pocket, round and dark like a small camera. I squished it.",
		"I heard a mechanical clicking like a camera shutter.",
		"Someone had left a stack of photographs on my desk--a series of hallways.",
		"I heard someone stop outside the door.",
		"I heard footsteps in the distance.",
		"I heard a siren in the distance.",
		"I heard a siren in the distance but getting closer.",
		"I heard a sound like a gunshot in the distance."
	],

	## AGENT_RECEIVES_DIRECTION ##
	"AGENT_RECEIVES_DIRECTION": [
		"#finds_note# #reads_note#",
		"#finds_note# #reads_note#",
		"#finds_note# #describes_note# #reads_note#",
	],
	"finds_note": [
		"I found a note from the agency.",
		"I found a note from the agency on the #surfaces#.",
		"I found a note from the agency in my pocket.",
		"On the #surfaces# was another note from the agency.",
		"There was a pile of notes from the agency on the #surfaces#. I picked up the top one."
		"There was a pile of notes from the agency on the #surfaces#. I picked out one at random."
	],
	"describes_note": [
		"#note_prefix# was black with white edges.",
		"#note_prefix# was white with black type.",
		"#note_prefix# was a small piece of square paper.",
		"#note_prefix# was folded over twice.",
		"#note_prefix# was rumpled, as if it had been fished out of the trash.",
	],
	"reads_note": [
		"#note_prefix# was blank.",
		"#note_prefix# read: #note_content#",
		"#note_prefix# read: #note_content# #note_content#",
		"#note_prefix# read: #note_content# #note_content# #note_content#"
	],
	"note_content": [
		"CONTINUE-SURVEILLANCE.",
		"EAT-ONLY-MEAT.",
		"REPORT.",
		"DO-NOT-WAKE.",
		"HURRY.",
		"KEEP-ROUTINE.",
		"KEEP-STRICT-ROUTINE.",
		"DO-NOT-RETURN-HOME.",
		"ELIMINATE-SUSPECT-IF-POSSIBLE.",
		"ELIMINATE-SUSPECT-AS-SOON-AS-POSSIBLE.",
		"ONLY-SLEEP.",
		"MANTAIN-PHYSICAL-PERFORMANCE.",
		"MANTAIN-FOCUS.",
		"OBSERVE-SUSPECT."
	],
	"note_prefix": [
		"It",
		"The note"
	],
	"surfaces": [
		"table",
		"side-table",
		"window sill",
		"floor",
		"counter",
		"desk"
	],

	## AGENT_OBSERVES_SPACE ##
	"AGENT_OBSERVES_SPACE": [
		"The kitchen didn't have any knifes.",
		"The kitchen didn't have any forks.",
		"There were no chairs in the house.",
		"The house had more hallways than it should.",
		"The windows were always locked.",
		"The house didn't have any curtains.",
		"The door to the basement was always locked.",
		"Only one of the lamps worked.",
		"All the lightbulbs had burned out."
	],

	## AGENT_OBSERVES_REV ##
	"AGENT_OBSERVES_REV": [
		"#agent_sees_rev#",
		"#agent_sees_rev# #agent_describes_rev#",
		"#agent_sees_rev# #agent_describes_rev#",
		"#agent_sees_rev# #agent_describes_rev# #rev_acts#",
	],
	"agent_sees_rev": [
		"I watched through the window.",
		"I observed.",
		"I set up the camera equipment and photographed.",
		"I set up the camera equipment.",
		"I photographed.",
		"I sat at my desk and watched surveillance tapes.",
		"I watched surveillance tapes.",
	],
	"agent_describes_rev": [
		"The suspect was acting fearful.",
		"The suspect was beginning to act with suspicion.",
		"The suspect had let their hair grow long.",
		"The suspect appeared unfocused.",
		"The suspect was acting more alert than usual.",
		"The suspect was acting less alert than usual.",
		"The suspect was beginning to fidget nervously.",
		"The suspect avoided people and contact of any kind.",
		"The suspect was beginning to look unbalanced.",
	],
	"rev_acts": [
		"They #rev_actions#.",
		"They #rev_actions# and #rev_actions#.",
		"They #rev_actions# then #rev_actions#.",
	],
	"rev_actions": [
		"stayed up all night",
		"hardly leave the house",
		"have not eaten in days",
		"have stopped sleeping",
		"sat for many hours, not doing anything",
		"sat for many hours, thinking or mumbling",
		"read all night",
		"have stopped sleeping",
		"bathed for hours",
		"spoke on telephone in a hurry",
		"took several phone calls",
		"wrote for a long time then burned the pages",
		"wrote several letters but never sent them"
		"copied words from a book",
		"filled out a ledger"
		"worked on what appeared to be complicated calculations",
		"moved from room to room"
	],

	## AGENT_WRITES_REPORT ##
	"AGENT_WRITES_REPORT": [
		"#prepares_report#",
		"#prepares_report# #reads_report#",
		"#reads_report#"
	],
	"prepares_report": [
		"I sat at the desk and wrote out my report.",
		"I sat on the floor and wrote my report.",
		"I wrote out my report.",
		"I found a fresh piece of paper and begun to write my report.",
		"I wrote my daily report.",
		"I wrote my report.",
		"I wrote for what felt like a long time.",
		"I wrote."
	],
	"reads_report": [
		"#report_content#",
		"#report_content# #report_content#",
		"#report_content# #report_content# #report_content#",
	],
	"report_content": [
		"DREAMS CONTINUE.",
		"NIGHTMARES CONTINUE.",
		"HAVE BEGUN TO SEE GHOSTS.",
		"CANNOT TRUST WHAT I SEE ANYMORE.",
		"CANNOT TRUST WHAT I SEE.",
		"PLEASE SEND RELIEF.",
		"WHAT DAY IS IT.",
		"READY TO RETURN HOME.",
		"HAVE BEGUN TO SEE MONSTERS.",
		"SURVEILLANCE IS TOTAL.",
		"MISSION CONTINUES."
	],

	## AGENT_DESCRIBES_THE_MACHINE ##
	"AGENT_DESCRIBES_MACHINE": [
		"The machine must be wound up for 60 minutes before use.",
		"The machine must be used within fifteen minutes of being fully wound.",
		"The machine is best used while the suspect is asleep.",
		"The machine weighs 20 lbs fully wound.",
		"The machine can only be used once.",
		"The machine can be accessed with the secret key.",
		"The machine will emit a quiet hum while being wound and when it is in use.",
		"The machine is completely inert until activated.",
		"The machine consists of a cylinder of compressed nitrogen and a regulator to supply the nitrogen into a plastic mask.",
	],

	## AGENT_SLEEPS ##
	"AGENT_SLEEPS": [
		"I fell asleep."
	],

	## AGENT_DREAMS ##
	"AGENT_DREAMS": [
		"I had a dream about a hallway."
	],


	## AGENT_WAKES_IN_THE_NIGHT ##
	 "AGENT_WAKES_IN_THE_NIGHT": [
		 "#agent_checks_window#",
		 "#agent_checks_window# #suspect_is_awake#",
		 "#agent_checks_window# #suspect_is_awake#",
		 "#agent_checks_window# #suspect_is_asleep#"
		 "#agent_checks_window# #suspect_is_asleep#"
	 ],
	 "agent_checks_window": [
		 "I woke up in the middle of the night. I checked the window.",
	 ],
  	 "suspect_is_awake": [
        "The suspect was sleep-walking through the kitchen.",
        "The suspect was sleep-walking through the lawn.",
        "The suspect was sleep-walking through the hallways of their house.",
        "The suspect was awake, sitting on the edge of their bed."
	 ],
	 "suspect_is_asleep": [
		 "The suspect was asleep.",
		 "The suspect was sleeping."
	 ],

	## AGENT_KILLS_REV ##
	"AGENT_KILLS_REV": [
		"#agent_preps_machine# I put the machine over the suspect's mouth and turned it on. #rev_dies#",
		"#agent_preps_machine# I put the machine over the suspect's mouth and turned it on. #rev_dies# It took six minutes.",

		"#agent_preps_machine# I put the machine over suspect's mouth and turned it on. #rev_dies# It took fifteen minutes.",

		"#agent_preps_machine# I put the machine over the suspect's mouth and turned it on. #rev_dies# It took eight minutes.",

		"#agent_preps_machine# I put the machine over the suspect's mouth and turned it on. #rev_dies# It took six minutes.",

		"#agent_preps_machine# I went into the suspect's room. They were asleep. It was impossible to see in the dark. I sensed their figure and heard their breath. I put the machine on the nightstand. I unspooled the mask and placed it over their face. The rhythm of their breath changed but they didn't move. I turned the machine on. #rev_dies# It took seven minutes.",

		"#agent_preps_machine# I went into the suspect's room. They were asleep. It was impossible to see in the dark. I sensed their figure and heard their breath. I put the machine on the nightstand. I unspooled the mask and placed it over their face. The rhythm of their breath changed but they didn't move. I turned the machine on. #rev_dies# It took seven minutes.",

		"#agent_preps_machine# I went into the suspect's room. I put the mask over their mouth and turned it on. #rev_dies# It took eight minutes.",

		"#agent_preps_machine# I went into the suspect's room. They were asleep. I put the machine on the nightstand. I put the mask over their mouth and turned it on. #rev_dies# It took fifteen minutes.",

		"#agent_preps_machine# I went into the suspect's room. They were asleep. I unspooled the mask and placed it over their face. I turned on the machine. #rev_dies# It took eight minutes.",
	],
	"rev_dies": [
		"Their breath slowed. Their breath stopped.",
		"The breath became rapid and shallow. Then it couldn't be heard.",
		"The breath became rapid and shallow. Then it slowed. Then it couldn't be heard."
	],
	 "agent_preps_machine": [
		 "I went to where the machine was. I activated the machine. I wound up the machine for one hour. The machine emitted a quiet hum. I checked the window. #suspect_is_asleep# I strapped the machine on my back. It was heavy. I crossed the lawn to the suspect's house. I had the key and I let myself in.",
	 ],
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
