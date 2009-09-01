#!/usr/bin/env python

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
import os
from google.appengine.ext.webapp import template

import db_model

class MyHandler ( webapp.RequestHandler ):
	def get(self):
		quizes = db_model.QuizSet.all()
		values = { 'quizes' : quizes , 'logout' : users.create_logout_url("/") }
		path = os.path.join(os.path.dirname(__file__), 'viewquiz.html')
		self.response.out.write(template.render(path, values))
	
class MyHandler2 ( webapp.RequestHandler ):
	def get(self):
		key = self.request.uri.split('/')[3].split('_')[1]
		set = db_model.QuizSet.get(db.Key(key))
		values = { 'set' : set , 'logout' : users.create_logout_url("/") }
		path = os.path.join(os.path.dirname(__file__), 'view.html')
		self.response.out.write(template.render(path, values))
		
	def post(self):
		key = self.request.uri.split('/')[3].split('_')[1]
		aset = db_model.AnsSet()
		aset.qid = db.Key(key)
		aset.uid = users.get_current_user()
		aset.ans = self.request.get('answer')
		db.put(aset)
		self.redirect('/viewquiz.html')

app = webapp.WSGIApplication( [ ( '/viewquiz.html', MyHandler ) , ( r'/view.*' , MyHandler2 ) ],debug=True)

def main():
	run_wsgi_app(app)

if __name__ == "__main__":
	main()
		
		