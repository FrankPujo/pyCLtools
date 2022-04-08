class Table:
	def __init__( self, header ):
		self.rows = 0
		self.cols = len( header )
		self.header = header
		self.maxL = [0] * self.cols
		self.content = []
		self.addRow( header )
	def addRow( self, rowContent ):
		self.content.append( rowContent )
		for i in range( self.cols ):
			if len(rowContent[i]) + 2 > self.maxL[i]:
				self.maxL[i] = len(rowContent[i]) + 2
	def display( self ):
		for row in self.content:
			if row == "sep":
				for n in range( self.cols ):
					print( "+", end="" )
					print( "-" * self.maxL[n], end ="" )
				print("+")
			else:
				j = 0
				for cell in row:
					print( "|" + cell.center( self.maxL[j], " "), end="" )
					j += 1
				print("|")
	def addSep( self ):
		self.content.append( "sep" )

myT = Table( ["First Header", "Second"] )
myT.addSep()
myT.addRow(["Content", "Some more content"])
myT.addRow(["Consecutive", "Separators are optional"])
myT.display()