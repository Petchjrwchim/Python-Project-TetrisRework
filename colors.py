class Colors:
	dark_grey = (26, 31, 40)
	green = (114, 203, 59)
	red = (255, 50, 19)
	orange = (255, 151, 28)
	yellow = (255, 213, 0)
	purple = (166, 0, 247)
	cyan = (21, 204, 209)
	blue = (3, 65, 174)
	white = (255, 255, 255)
	dark_blue = (44, 44, 127)
	light_blue = (59, 85, 162)
	pink = (255, 105, 180)
	

	@classmethod
	def get_cell_colors(cls):
		return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue, cls.pink]
