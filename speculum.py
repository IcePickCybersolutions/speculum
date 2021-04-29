import os

print('''
                            _                 
                           | |                
  ___ _ __   ___  ___ _   _| |_   _ _ __ ___  
 / __| '_ \ / _ \/ __| | | | | | | | '_ ` _ \ 
 \__ \ |_) |  __/ (__| |_| | | |_| | | | | | |
 |___/ .__/ \___|\___|\__,_|_|\__,_|_| |_| |_|
     | |                                      
     |_|  
     
Making deepfakes as easy as 123, ABC, you and me!

Ingredients:
- python (the language, but snakes are pretty cool)
- pip (thingy that helps download python stuff)
- the code from my github (all in one folder)
- a photo to animate (in code folder)
- a video to animate the photo to do (again, same folder)
- a big idea (at least one cup)

Directions are available on my github page. 
If you're seeing this and those steps are finished, just answer some of my questions...
''')

qimage = input("what is your source image named?: ")
qvideo = input("what is your driving video named?: ")
qgpu = input("do you have a bespoke gpu?: ")

if qgpu == no:
	os.system("deep_animate", qimage, qvideo, "conf.yaml deep_animator_model.pth.tar")
	
elif gpu == yes:
	os.system("deep_animate", qimage, qvideo, "conf.yaml deep_animator_model.pth.tar --device cuda")

else: print("Incorrect input, please answer the gpu question with either yes or no")

print("Your video is now saved to the folder with the code, process complete")
