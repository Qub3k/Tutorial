class Font:
	def __init__(self,name)
		self.letters = ()
		self.name = name

class FontLoader:
	def loadFont(self, directory):
		font = Font("fancy")

		font.letters['O'] = r'''
	 ______
   (  __  )
   ( (__) ) 
   (______)	  

   	'''
   		font.letters['I'] = r'''

   	 __
   	(  )
   	 ><
   	(__)

   	'''
      font.letters['T'] = r'''

       ______
      (_    _) 
         ><
        (__)
      '''
      return font