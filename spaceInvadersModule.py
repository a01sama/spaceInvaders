#Abdul Samad
import viz

class Ship:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		#main ship
		viz.startLayer(viz.QUADS)
		viz.vertexColor(0.27, 0.58, 0.16)
		viz.vertex(-15,-9)
		viz.vertexColor(0.5,0.4,0.3)
		viz.vertex(-15,9)
		viz.vertexColor(0.1,0,0.8)
		viz.vertex(15,9)
		viz.vertexColor(0.5,0.4,0.3)
		viz.vertex(15,-9)
		
		#cannon
		viz.vertexColor(0.27, 0.58, 0.16)
		viz.vertex(4.5,9)
		viz.vertex(-4.5,9)
		viz.vertex(-4.5,14)
		viz.vertexColor(0.2,0,0.5)
		viz.vertex(4.5,14)
		
		#top
		viz.vertexColor(0.27, 0.58, 0.16)
		viz.vertex(1.5,14)
		viz.vertex(-1.5,14)
		viz.vertex(-1.5,18)
		viz.vertex(1.5,18)
		self.vertices = viz.endLayer()
		
	#gets X	
	def getX(self):
		return self.x
	#gets y		
	def getY(self):
		return self.y
	#set x and y	
	def setXY(self,x,y):
		self.x = x
		self.y = y
		mat = viz.Matrix()
		mat.postTrans(self.x, self.y)
		self.vertices.setMatrix(mat)
		

class Alien:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		viz.startLayer(viz.QUADS)
		
		#eye
		viz.vertexColor(1,0,0)
		viz.vertex(-5,0)
		viz.vertex(0,3)
		viz.vertex(5,0)
		viz.vertex(0,-3)
		
		#body
		viz.vertexColor(0,0.5,0.5)
		viz.vertex(-10,-10)
		viz.vertex(-6,6.2)
		viz.vertex(6,6.2)
		viz.vertex(10,-10)
		
		#left ear
		viz.vertexColor(1,0,0)
		viz.vertex(-5.8,6)
		viz.vertex(-5.8,10)
		viz.vertex(-1.9,10)
		viz.vertex(-1.9,6)
		
		#right ear
		viz.vertexColor(1,0,0)
		viz.vertex(6,6)
		viz.vertex(6,10)
		viz.vertex(2,10)
		viz.vertex(2,6)
		self.vertices = viz.endLayer()
	#gets X
	def getX(self):
		return self.x
	#gets y	
	def getY(self):
		return self.y
	#set x and y	
	def setXY(self,x,y):
		self.x = x
		self.y = y
		mat = viz.Matrix()
		mat.postTrans(self.x, self.y)
		self.vertices.setMatrix(mat)
	#remove alien	
	def kill(self):
		self.vertices.remove()
		
class Bullet:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		viz.startLayer(viz.QUADS)
		viz.vertexColor(1,0,1)
		viz.vertex(-1,-2)
		viz.vertex(-1,2)
		viz.vertex(1,2)
		viz.vertex(1,-2)
		self.vertices =viz.endLayer()
	#gets X
	def getX(self):
		return self.x
	#gets y
	def getY(self):
		return self.y
	#set x and y
	def setXY(self,x,y):
		self.x = x
		self.y = y
		mat = viz.Matrix()
		mat.postTrans(self.x, self.y)
		self.vertices.setMatrix(mat)
	#remove bullet
	def kill(self):
		self.vertices.remove()