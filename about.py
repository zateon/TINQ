#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template

class MyHandler(webapp.RequestHandler):
	def get(self):
		path = os.path.join(os.path.dirname(__file__),'about.html')
		self.response.out.write(template.render(path,{ } ) )
		
app = webapp.WSGIApplication ( [ ('/about.html' , MyHandler) ] , debug=True )

def main():
	run_wsgi_app(app)

if __name__ == "__main__":
	main()