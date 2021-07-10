class Spot:
	def __init__(self, piece, x, y):
		self.piece = piece
		self.x = x
		self.y = y

	def spot(piece, x, y):
		self.set_piece(piece)
		self.set_x(x)
		self.set_y(y)


	def get_piece(self):
		return self.piece

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def set_x(self, x):
		self.x = x

	def set_y(self, y):
		self.y = y

	def set_piece(self, p):
		self.piece = p 



class Piece:
	def __init__(self):
		self.killed = False
		self.white = False

	def set_piece(self, white):
		self.white = white
	
	def isWhite(self):
		return self.white

	def piece(self, white):
		self.set_piece(white)

	def isKilled(self):
		return self.killed

	def set_killed(self, kill):
		self.killed = kill

	def canMove(self, board, start, end)

class Player():
	def __init__(self, whiteside, humanplayer):
		self.whiteside= whiteside
		self.humanplayer= humanplayer

	def isWhite(self):
		return self.whiteside

	def ishumanplayer(self):
		return self.humanplayer

	self.canMove(self, board, start, end)

class King(Player):
	def __init__(self, castlingDone=False):
		super().__init__()
		











