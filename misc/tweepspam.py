#!/usr/bin/env python
# Basic twitter spam bot. Signs into twitter and follows people in the
# public timeline and then attempts to get their attention using 
# a tweet with a @mention contained. 
# This bot will likely be killed by anti-spam rules on twitter and have
# its account suspended. 
#
# Coded this for a "Wall of tweeps" idea, people would be "phished" and
# only store 2 chars of their password and give them advice about how to
# protect from phishing and also tweet the username + 2 chars of pass for
# amusement on a seperate account.
#
# Unfortunately the whole idea is a complete violation of Twitter ToS
# so it has been completely abandonded.
#
import twitter
import random


def tweetspam(username,password):
	try:
        	api = twitter.Api(username=username,password=password)
		statuses = api.GetPublicTimeline()
	except:
		return 0
	errorcount = 0
	for s in statuses:
		try:
                        msg = "Hey"
                        terminate = "you have a %d%% tweep rating! Get more stats with TweepGrader http://bit.ly/" % random.randint(40,100)
                        # Get each users 'unique' rating.. waste of clock cycles.
                        user = s.GetUser()
                        print "[ Trying to follow %s" % user.screen_name
                        retuser = api.CreateFriendship(user.screen_name)
                        print "[ Following %s" % user.screen_name
                        # adds a user in public timeline to follow list.
                        tweet = "%s @%s %s" % (msg, user.screen_name, terminate)
                        if len(tweet) < 140:
                                api.PostUpdate(tweet)
                                # tweets to @user so long as less than MAXTWEET size.
                        print "[ Mention sent to %s" % user.screen_name
		except:
			errorcount = errorcount + 1
			print "! A problem occured."
	return 20 - errorcount

if __name__ == "__main__":
	username = 'tweeterforyou'
	password = 'spamb0t'
	print "[ Twitter wall-of-tweeps spambot launched"
	# current API limit gives approx 3 runs an hour.
	# run this often and your account will be suspended.
	print "[ Hit %d users" % tweetspam(username,password)
	print "[ Hit %d users" % tweetspam(username,password)
	print "[ Hit %d users" % tweetspam(username,password)

