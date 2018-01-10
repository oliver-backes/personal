#!/usr/bin/env python2

import sys

print "This program will help you track various indicators of personal health on a day to day basis."
print"Please input the following data points below:"
print "- date (DD/MM/YYYY);"
print "- weight (lb);"
print "- calories;"
print "- steps;"
print "- exercise - count;" 
print "- exercise - minutes;"
print "- water (fl oz);"
print "- and OEV count."

inputs = []

date = raw_input('Enter the date (YYYYDDMM): ')

inputs.append(date)

weight = raw_input('Enter your weight: ')

inputs.append(weight)

calories = raw_input('Enter caloric intake: ')

inputs.append(calories)

steps = raw_input('Enter step count: ')

inputs.append(steps)

exercisecount = raw_input('Enter exercise count: ')

inputs.append(exercisecount)

exercisemin = raw_input('Enter exercise minutes: ')

inputs.append(exercisemin)

water = raw_input('Enter water intake: ')

inputs.append(water)

oev = raw_input('Enter OEV count: ')

inputs.append(oev)

for input in inputs:
	if not (input.isint()):
		sys.exit(input + " is not a number.")

print "Here are the personal health indicators that you entered. Are they correct?"

print "date: %d; weight: %d; calories: %d; steps: %d; exercise - count: %d; exercise - min: %d; water: %d; and OEV: %d" % (date, weight, calories, steps, exercisecount, exercisemin, water, oev)