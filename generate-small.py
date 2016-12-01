#!/usr/bin/env python

from jinja2 import Environment, Template, FileSystemLoader
import inflect
import random

INFLECT = inflect.engine()
env = Environment(loader=FileSystemLoader('./'))
def a_or_an(value):
	return INFLECT.a(value)
env.filters['a_or_an'] = a_or_an

def pipe_rand(value):
	return random.choice(value.split("|"))
env.filters['pipe_rand'] = pipe_rand

template = {}
template["past"] = env.get_template("story-short-past.jinja2")
template["present"] = env.get_template("story-short-present.jinja2")
template["future"] = env.get_template("story-short-future.jinja2")

villains = {}

villains["past"] = [
		{"title": ["evil witch", "sorceress", "dark queen"],
		"name": ["Esmerelda", "Zieba", "Deniza", "Gorna"],
		"p": "she"
		},
		{"title": ["evil wizard", "sorcerer", "dark knight", "vampire"],
		"name": ["Grinzlok", "Fonkal", "Grisbit", "Neckbone", "Dark Cloak"],
		"p": "he"
		},
		{"title": ["terrible dragon", "angry ghost"],
		"name": ["Quixod", "Clang", "Shougin", "Drizat"],
		"p": "it"
		},
	]

villains["present"] = [
		{"title": ["evil spy", "thief", "burglar"],
		"name": ["Vivian", "Esmerelda", "Margret", "Miss Demeanor", "Mary Contrary"],
		"p": "she"
		},
		{"title": ["evil spy", "thief", "burglar"],
		"name": ["Devon Demeanor", "Dillan Tangle", "Mr. Bigs", "Dr. Snaps", "Mr. Muscles"],
		"p": "he"
		}
	]

villains["future"] = [
		{"title": ["emperess", "evil scientist", "pirate queen"],
		"name": ["Zang", "Grine", "Dr. Shade", "Miss Fire"],
		"p": "she"
		},
		{"title": ["emperor", "space pirate", "cyborg"],
		"name": ["Fizzbuzz", "Dangnark", "Mr. Shadow"],
		"p": "he"
		},
		{"title": ["robot"],
		"name": ["Nixnod", "Shatter", "Smash", "Slam", "Dr. Eradicate"],
		"p": "it"
		},
	]


villain_deck = {}
for era in villains.keys():
	villain_d = []
	for villain in villains[era]:
		for title in villain["title"]:
			for name in villain["name"]:
				villain_d.append({"title":title,"name":name,"p": villain['p']})
	random.shuffle(villain_d)
	villain_deck[era] = villain_d


descriptions = ["happy", "carefree", "curious", "adventurous", "proper", "studious", "careful", "serious"]
characters = [ [
		{"name": ["Clara", "Irma", "Ashlee", "Lisa", "Jillian"],
		"p": "she",
		"gender": "girl",
		"relation": "sister"
		},
		{"name": ["Arthur", "Alejandro", "Weslee", "Jeff", "Jackson"],
		"p": "he",
		"gender": "boy",
		"relation": "brother"
		}], [
		{"name": ["Tessa"],
		"p": "she",
		"gender": "girl",
		"relation": "cousin"
		},
		{"name": ["Lincoln"],
		"p": "he",
		"gender": "boy",
		"relation": "cousin"
		}],[
		{"name": ["Irma", "Nadia", "Deanna", "Crystal", "Autumn", "Susan", "Monica", "Max"],
		"p": "she",
		"gender": "girl",
		"relation": "girlfriend"
		},
		{"name": ["Jeff", "Josh", "Kurt", "Zabe", "Kyle", "Matt", "Philip", "Jimmie"],
		"p": "he",
		"gender": "boy",
		"relation": "boyfriend"
		}],[
		{"name": ["Casi", "Amber"],
		"p": "she",
		"gender": "girl",
		"relation": "girlfriend"
		},
		{"name": ["Audrey", "Helen"],
		"p": "she",
		"gender": "girl",
		"relation": "girlfriend"
		}],[
		{"name": ["Sabdy"],
		"p": "he",
		"gender": "boy",
		"relation": "boyfriend"
		},
		{"name": ["Eddie"],
		"p": "he",
		"gender": "boy",
		"relation": "boyfriend"
		}]
	]


character_deck = [[],[]]

for cgroups in characters:
	for x in xrange(len(cgroups[0]["name"])):
		character_deck[0].append({"name":cgroups[0]["name"][x],"p": cgroups[0]['p'], "gender": cgroups[0]['gender'], "relation": cgroups[0]['relation']})
		character_deck[1].append({"name":cgroups[1]["name"][x],"p": cgroups[1]['p'], "gender": cgroups[1]['gender'], "relation": cgroups[1]['relation']})

random.shuffle(descriptions)

story_vars = {}

story_vars["past"] = {
	"activity": ["shopping at the market", "fishing", "picking berries", "collecting apples", "collecting firewood", "milking cows"],
	"home": ["cottage", "windmill", "little house", "treehouse", "farm house"],
	"lair": ["castle", "dungeon", "dark cave", "tower", "magical tent", "ancient temple", "graveyard tomb"],
	"house_loc": ["next to a creek", "beside a lake", "at the edge of town", "on top of a hill"],
	"route": ["road", "path", "trail", "wagon", "pony", "horse", "cart", "boat", "canoe"],
	"evidence": ["piece of a broken toy", "long scrape on the ground", "torn piece of clothing", "piece of parchment"],
	"clothing": ["cloak", "jacket", "hat", "cape"],
	"tool": ["axe", "sword", "hoe", "knife", "scythe", "dagger", "rapier", "hammer"],
	"prison": ["cage", "big pot", "trunk", "crate", "basket"],
	"traveller": ["a group of book sellers", "some traveling minstrels", "a few old farmers", "a troupe of royal messengers"],
	"road_help": ["directions", "something to drink", "a snack to eat", "a ride a few miles"],
	"evil_activity": ["brewing a potion", "reading a spell from a spell book", "cutting up vegetables for a stew", "taking a nap on a pile of pillows", "reciting a chant from an old book", "drawing some runes on the floor"]
}

story_vars["present"] = {
	"activity": ["shopping at the grocery store", "working at an office", "picking up the mail", "shopping at the farmers market", "taking a hike", "taking a bike ride"],
	"home": ["home", "apartment", "house", "townhome", "trailer"],
	"house_loc": ["downtown", "in the country", "near the college", "on a hill overlooking the city"],
	"lair": ["laboratory", "headquarters", "abandoned factory", "penthouse", "old mill"],
	"route": ["road", "highway", "bike", "car", "motorcycle", "bus", "train", "metro", "subway"],
	"evidence": ["broken laptop", "cut off video recording", "shatted phone", "scrap of a newspaper"],
	"clothing": ["glasses", "jacket", "coat", "gloves"],
	"tool": ["phone", "computer", "multitool", "crowbar", "audio recorder", "camera"],
	"prison": ["metal cage", "wooden crate", "plastic box"],
	"traveller": ["some pizza delivery drivers", "a van full of musicians", "a few skateborders", "some police officers"],
	"road_help": ["directions", "something to drink", "something to eat", "a ride a few miles"],
	"evil_activity": ["cracking a code", "reading an instruction manual", "sharpening medical tools", "taking a nap on a big bed", "watching television", "talking on the phone"]
}

story_vars["future"] = {
	"activity": ["delivering a package to Europa", "swiming with space whales", "cleaning the solar panels"],
	"home": ["observation tower", "apartment", "farming habitat", "dome home"],
	"house_loc": ["on Mars", "in outer space", "on the Moon", "on a colonized asteroid", "under the ocean"],
	"lair": ["space station", "space ship", "ice planet", "ice planet"],
	"route": ["space ship", "rocket", "monorail", "flying car", "rocket boots"],
	"evidence": ["broken helper robot", "destroyed replicator", "frightened robomouse"],
	"clothing": ["space suit", "helmet", "radiation visor"],
	"tool": ["sonic socket wrench", "electroblade", "laser sword", "dematerializer pistol", "remote control"],
	"prison": ["electro-cage", "suspension tank", "metal crate", "detention cell"],
	"traveller": ["some friendly aliens", "a group of peacekeeper robots", "a couple of galactic truckers"],
	"road_help": ["some spaceship fuel", "some pure Venusian water", "a snack to eat", "a ride around the planets"],
	"evil_activity": ["talking to a robot", "examining a giant crystal", "tuning a laser", "taking a nap in zero gravity", "searching for a missing sock", "practicing a monologue"]
}

story_deck = {}
for era in story_vars.keys():
	story_d = []
	for activity in story_vars[era]["activity"]:
		for home in story_vars[era]["home"]:
			for lair in story_vars[era]["lair"]:
				deck = {"activity": activity,
					"home": home,
					"lair": lair}
				for kind in story_vars[era].keys():
					if not deck.get(kind, None):
						deck[kind] = random.choice(story_vars[era][kind])
				story_d.append(deck)
	random.shuffle(story_d)
	story_deck[era] = story_d


# From MOO:
# Pronouns:
#     %s => subject pronoun:          either `he',  `she', or `it'
#     %o => object pronoun:           either `him', `her', or `it'
#     %p => posessive pronoun (adj):  either `his', `her', or `its'  
#     %q => posessive pronoun (noun): either `his', `hers', or `its'
#     %r => reflexive pronoun:  either `himself', `herself', or `itself'

pronouns = {
	"he": {
		"s": "he",
		"o": "him",
		"p": "his",
		"q": "his",
		"r": "himself"
	},
	"she": {
		"s": "she",
		"o": "her",
		"p": "her",
		"q": "hers",
		"r": "herself"
	},
	"it": {
		"s": "it",
		"o": "it",
		"p": "its",
		"q": "its",
		"r": "itself"
	}	
}

for p in pronouns:
	newpronouns = {}
	for sub in pronouns[p]:
		newpronouns[sub.upper()] = pronouns[p][sub].capitalize()
	pronouns[p].update(newpronouns)

for x in xrange(len(character_deck[0])):
	c1 = character_deck[0][x]
	c2 = character_deck[1][x]

	for era in ["past","present","future"]:

		villains = villain_deck[era]
		story = story_deck[era]
		random.shuffle(story)
		s = story[0]
		random.shuffle(villains)
		v1 = villains[0]
		random.shuffle(descriptions)
		c1["description"] = descriptions[0]
		c2["description"] = descriptions[1]
		randoms = []
		for x in xrange(5):
			randoms.append(random.randint(1,3))
		print template[era].render(s=s, c1=c1, c2=c2, v1=v1, p=pronouns, r=randoms)

		if era is not "future":
			print "And then...\n"
	print "---------------\n\n"
