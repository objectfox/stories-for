#!/usr/bin/env python

from jinja2 import Template

template = Template(open("story-long.jinja2").read())

story_vars = {
	"c1": {
		"title": "Princess",
		"name": "Clara",
		"p": "she",
		"relation": "sister"
	},
	"c2": {
		"title": "Prince",
		"name": "Arthur",
		"p": "he",
		"relation": "brother"
	},
	"v1": {
		"title": "evil witch",
		"name": "the witch",
		"p": "she",
	}
}

# story_vars = {
# 	"c1": {
# 		"title": "Prince",
# 		"name": "Arthur",
# 		"p": "he",
# 		"relation": "brother"
# 	},
# 	"c2": {
# 		"title": "Princess",
# 		"name": "Clara",
# 		"p": "she",
# 		"relation": "sister"
# 	},
# 	"v1": {
# 		"title": "evil wizard",
# 		"name": "Makroz",
# 		"p": "he",
# 	}
# }


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
		"s": "she",
		"o": "her",
		"p": "her",
		"q": "hhers",
		"r": "herself"
	}	
}

for p in pronouns:
	newpronouns = {}
	for sub in pronouns[p]:
		newpronouns[sub.upper()] = pronouns[p][sub].capitalize()
	pronouns[p].update(newpronouns)

print template.render(s=story_vars, c1=story_vars["c1"], c2=story_vars["c2"], v1=story_vars["v1"], p=pronouns)
