import configparser, os

class DataManager(object):

	__instance = None
	
	config = configparser.ConfigParser()
	
	currOnOff = False
	currLevel = 0
	
	def __new__(cls):
		if cls.__instance is None:
			cls.__instance = super(DataManager,cls).__new__(cls)
			cls.__instance.__initialized = False
			return cls.__instance

	def __init__(self):
		if(self.__initialized): return
		self.__initialized = True
		self.initConfig()
		
	def initConfig(self):
		if not os.path.exists("config.ini"):
			print("creo ini")
			self.config["DEFAULTS"] = {"onoff" : "0", "level" : "0"}
			self.save()
		self.config.read("config.ini")
		if not self.config.has_section("DEFAULTS"):
			print("creo sezione defaults")
			self.config["DEFAULTS"] = {"onoff" : "0", "level" : "0"}
			self.save()
		self.config.read("config.ini")
		if self.config["DEFAULTS"]["onoff"] == "0":
			self.currOnOff = False
		else:
			self.currOnOff = True
		self.currLevel = int(self.config["DEFAULTS"]["level"])
		
	def setOnOff(self, val):
		print("da salvare ", val)
		newVal = "0"
		if val == "true":
			print("è true")
			newVal = "1"
		print("salvo" , newVal)
		self.config["DEFAULTS"]["onoff"] = newVal
		self.save()
		self.currOnOff = val
		
	def setLevel(self, val):
		print("nuovo valore ", str(val))
		self.config["DEFAULTS"]["level"] = str(val)
		self.save()
		self.currLevel = val
		
	
		
	def save(self):
		with open("config.ini" ,"w") as fileConf:
			self.config.write(fileConf)

