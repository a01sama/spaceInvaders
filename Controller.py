#Abdul Samad
# Controller class inherits event handling methods from viz.EventClass
import viz
from spaceInvadersModule import *
class Controller(viz.EventClass):
	def __init__(self):
		
		# must call constructor of EventClass first!!
		viz.EventClass.__init__(self)
		self.callback(viz.TIMER_EVENT,self.onTimer)
		self.callback(viz.KEYDOWN_EVENT,self.onKeyDown)
		self.Ship = Ship(0,0)
		self.bulletList= []
		self.alienList= []
		self.direction = 0
		self.Ship.setXY(self.Ship.getX(), self.Ship.getY() - 220)
		self.starttimer(1,1/50.0,viz.FOREVER)
		yCord = 250
		for y in range (3):
			xCord = -200
			yCord = yCord - 50
			for x in range (11):
				self.Alien = Alien(0,0)
				self.Alien.setXY(self.Alien.getX() + xCord, self.Alien.getY()+ yCord)
				self.alienList.append(self.Alien)
				xCord = xCord + 40

		
	# key down functions 		
	def onKeyDown(self,key):
		#left key
		if(key == viz.KEY_LEFT):
			self.Ship.setXY(self.Ship.getX() - 10, self.Ship.getY())
		#right key	
		if(key == viz.KEY_RIGHT):
			self.Ship.setXY(self.Ship.getX() + 10, self.Ship.getY())
		#space key
		if(key == " "):
			self.bullet = Bullet(0,0)
			self.bullet.setXY(self.Ship.getX() , self.bullet.getY() - 200)
			self.bulletList.append(self.bullet)
				
	#on timer functions			
	def onTimer(self,num):
		#alien list
		for alien in self.alienList:
			if self.direction == 0: 
				if (alien.getX() != -300):
					alien.setXY(alien.getX()- 0.5 , alien.getY())
				else: 
					self.direction = 1
					for alien in self.alienList:
						alien.setXY(alien.getX(), alien.getY() -20)
			if self.direction == 1:  
				if (alien.getX() != 300):
					alien.setXY(alien.getX()  + 0.5 , alien.getY())
				else: 
					self.direction = 0
					for alien in self.alienList:
						alien.setXY(alien.getX(), alien.getY() -20 )
			
		#bullet list		
		for b in self.bulletList:
			b.setXY(b.getX(), b.getY() + 10)
		#kill alien and bullets
		for b in self.bulletList:
			for a in self.alienList:
				if (b.getX() < a.getX() + 10) and (b.getX() > a.getX() - 10) and (b.getY() < a.getY() + 5) and (b.getY() > a.getY() - 5):
					self.bulletList.remove(b)
					self.alienList.remove(a)
					b.kill()
					a.kill()