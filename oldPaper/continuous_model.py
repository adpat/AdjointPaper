from latexslides import *
import utils
from collections import defaultdict

slides = defaultdict(list)

################
#
# Authors
#
################


# Set institutions
berkeley = "UC Berkeley"
inria = "INRIA"

# people
jack = "Jack Reilly"
walid = "Walid Krichene"
samitha = "Samitha Samaranayake"
maria = "Maria-Laura Delle-Monache"

# Set authors
authors = (
	(jack, berkeley),
	(maria, inria),
	(walid, berkeley),
	(samitha, berkeley),
	)

################
#
# Presentation
#
################


pres_title = "Continuous, Junction-based Model for Ramp Metering"
pres_title_short = "Cont. model for ramps"


presentation = BeamerSlides(
	title=pres_title,
	short_title=pres_title_short,
	author_and_inst=authors,
	beamer_colour_theme='seahorse'
	)

################
#
# Sections
#
################


section_keys = (
	'mot',
	'out',
	'existing',
	'piccoli',
	'2x2',
	'demand',
	'riemann'
	)

section_titles = {
	"mot":"Motivation",
	"existing":"Existing Models",
	"piccoli":"Piccoli Junction Model",
	"2x2":"Fixing Two-by-two Junctions",
	"demand":"Guaranteeing Onramp Demand Conservation",
	'riemann': "Riemann Solver for Junction"
	}

section_slides = dict((k,Section(v)) for k,v in section_titles.iteritems())

for key, slide in section_slides.iteritems():
	slides[key].append(slide)

################
#
# Motivation
#
################

key = 'mot'

slide1 = Slide("Slide 1",
               content=[TextBlock(r"""
Program for computing the height of a ball thrown up in the air:
$y=v_0t- {1\over 2} gt^2$""") ,
               TextBlock(utils.grab_adjoint('variableDimensions'))
               ],
               figure='triangletikzpdf.pdf',
               figure_pos='w',
               figure_fraction_width=0.4,
               left_column_width=0.3,
               )
slides[key].append(slide1)

################
#
# Motivation
#
################

key = 'mot'

################
#
# Motivation
#
################

key = 'mot'

################
#
# Motivation
#
################

key = 'mot'

################
#
# Motivation
#
################

key = 'mot'




################
#
# Compile and View
#
################


slides = [slide for key in section_keys for slide in slides[key]]

for slide in slides:
    presentation.add_slide(slide)

# Dump to file:

utils.view_presentation(presentation)
