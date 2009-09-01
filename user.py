#!/usr/bin/env python
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
import os
from google.appengine.ext.webapp import template

import db_model

class MyHandler(webapp.RequestHandler):
	def get(self):
		user = users.get_current_user()
    
		if user:
			members = db_model.QUser.gql( " WHERE uid = :1", user )
			member=members.get()
			if not member:
				member = db_model.QUser( uid = user , type = 0 ) 
				db.put( member )
			values = { 'member' : member , 'test' : 0 , 'logout' : users.create_logout_url("/") }
			path = os.path.join(os.path.dirname(__file__), 'user.html')
			self.response.out.write(template.render(path, values))
                           
		else:
			self.redirect(users.create_login_url(self.request.uri))

class MyHandler2 ( webapp.RequestHandler ):
	def get(self):
		path = os.path.join(os.path.dirname(__file__),'create.html')
		self.response.out.write(template.render(path,{ 'logout' : users.create_logout_url("/") } ) )
		
	def post(self):
		qset = db_model.QuizSet()
		qset.uid = users.get_current_user()
		qset.name = self.request.get( 'name' )
		qset.comment = db.Text(self.request.get ( 'comment' ))
		qset.qtlist = db.Text(self.request.get( 'qtlist' ))
		db.put(qset)
		self.redirect('/user.html')

		
		
app = webapp.WSGIApplication( [ ( '/user.html', MyHandler ) , ( '/user_createquiz.html' , MyHandler2 ) ],debug=True)

def main():
	run_wsgi_app(app)

if __name__ == "__main__":
	main()
