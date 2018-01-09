#!/usr/bin/env python2

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

date = input('Enter the date: ')

inputs.append(date)

weight = input('Enter your weight: ')

inputs.append(weight)

calories = input('Enter caloric intake: ')

inputs.append(calories)

steps = input('Enter step count: ')

inputs.append(steps)

exercisecount = input('Enter exercise count: ')

inputs.append(exercisecount)

exercisemin = input('Enter exercise minutes: ')

inputs.append(exercisemin)

water = input('Enter water intake: ')

inputs.append(water)

oev = input('Enter OEV count: ')

inputs.append(oev)

print inputs

print "Here are the personal health indicators that you entered. Are they correct?"

print "date: %d; weight: %d; calories: %d; steps: %d; exercise - count: %d; exercise - min: %d; water: %d; and OEV: %d" % (date, weight, calories, steps, exercisecount, exercisemin, water, oev)