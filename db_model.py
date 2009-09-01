#!/usr/bin/env python

# q refers to quiz* and qt to questions u for user

from google.appengine.ext import db

class QUser ( db.Model ):
	uid = db.UserProperty()
	type = db.IntegerProperty()                       # 0,1,2  one for admin
	
class QuizSet ( db.Model ):
	uid = db.UserProperty()
#	qid = db.IntegerProperty()                         we might not need this , db automatically creates a unique key
	name = db.StringProperty()                      # wont be more dan 500 bytes right?
	comment = db.TextProperty()
	qtlist =  db.TextProperty()
	time = db.TimeProperty()
	
class AnsSet( db.Model ):
	qid = db.ReferenceProperty( QuizSet )
	uid = db.UserProperty()
	ans = db.TextProperty()
	
	