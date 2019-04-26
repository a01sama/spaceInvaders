#Abdul Samad
import viz
from Controller import *
window = viz.MainWindow
#set screen dimensions
window.ortho(-320,320,-240,240,-1,1)
window.clearcolor(viz.BLACK)
viz.eyeheight(0);
#call the controler
Controller()
# record the video
vizact.onkeydown('b',viz.window.startRecording, 'c:\\Temp\\test.avi')
vizact.onkeydown('e',viz.window.stopRecording)
viz.go()