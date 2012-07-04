from string import Template
from flask import Flask, render_template, request	
import tweepy
import datetime

app = Flask(__name__)

@app.route('/')
def func1():
    return render_template('twi1new.html')

@app.route("/grade", methods=["POST"])
def func2():
	un = request.form["uname"]
	#Get the User object for twitter...
	try:
		user = tweepy.api.get_user(un)	
		x=user.screen_name
		n=user.name
		y=user.followers_count
		z=user.statuses_count
		w=user.friends_count
		twit=user.created_at
		u=user.profile_image_url
		s=str(getgrade(y,w,z,twit))
		return render_template("twi2new.html",n=n,u=u,x=x,twit=twit,y=y,z=z,w=w,s=s)
	except	tweepy.TweepError, e:			
#		print "\nFailed\n"
		flag=-1
		return render_template("twi1new.html",flag=flag)

def getdays(twit):
	now=datetime.datetime.now()
	duration = now-twit
	return duration.days

def getgrade(a,c,b,twit):
	fer=float(a) #followers
	fing=float(c) #following
	no_of_tweets=float(b)
	no_of_days=float(getdays(twit))

	r1=fer/fing
	r2=no_of_tweets/no_of_days
	m1=0
	m2=0
	#calculate r1
	if r1 == 0:
		m1=0
	else:
		for i in range(1,11):
			y=i-1
			if r1<=i and r1>y:
				m1=i*5
			elif r1>11:
				m1=50
			else:
				continue

	#calculate r2
	if r2== 0:
		m2=0
	else:
		for i in range(1,11):
			y=i-1
			if r2<=i and r2>y:
				m2=i*5
			elif r2>11:
				m2=50			
			else:
				continue

	grade=m1+m2
	return grade

if __name__ == '__main__':
    app.run(debug=True)
