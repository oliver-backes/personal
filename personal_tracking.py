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

date = input('Enter the date: ')

weight = input('Enter your weight: ')

calories = input('Enter caloric intake: ')

steps = input('Enter step count: ')

exercisecount = input('Enter exercise count: ')

exercisemin = input('Enter exercise minutes: ')

water = input('Enter water intake: ')

oev = input('Enter OEV count: ')

print "Here are the personal health indicators that you entered. Are they correct?"

print "date: %d; weight: %d; calories: %d; steps: %d; exercise - count: %d; exercise - min: %d; water: %d; and OEV: %d" % (date, weight, calories, steps, exercisecount, exercisemin, water, oev)