#!/usr/bin/env python
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MyHandler(webapp.RequestHandler):
	def get(self):
		self.response.out.write("""
		<html>
			<body style="background-color:#000000">
				<p style="color:#99ff00;text-align:center;font-wieght:bold;font-size:40px"><br><br><br><br><br> MTNFPY</p>
			</body>
		</html> """)
		
app = webapp.WSGIApplication ( [ ( '/.*' ,MyHandler) ] , debug=True )

def main():
	run_wsgi_app(app)

if __name__ == "__main__":
	main()