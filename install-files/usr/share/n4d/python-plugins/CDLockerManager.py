import copy

class CDLockerManager:
	

	def __init__(self):
		
		pass
		
	#def init

	
	def startup(self,options):
		
		self.internal_variable=copy.deepcopy(objects["VariablesManager"].get_variable("CDLOCKER"))
		if self.internal_variable==None:
			try:
				self.initialize_variable()
				objects["VariablesManager"].add_variable("CDLOCKER",copy.deepcopy(self.internal_variable),"","CDLocker internal variable","lliurex-cdlocker")
			except Exception as e:
				print e
	
	#def startup


	def initialize_variable(self):
		
		self.internal_variable={}
		self.internal_variable["enabled"]=False
		
	#def initialize_variable

	
	def is_enabled(self):
		
		try:
			return self.internal_variable["enabled"]
		except:
			return False
			
	#def is_enabled

	
	def set_lock_status(self,status):
		
		if type(status)==bool:
			self.internal_variable["enabled"]=status
			self.save_variable()
			return True
			
		return False
		
	#def set_lock_status
	
	def save_variable(self,variable=None):

		if variable==None:
			variable=copy.deepcopy(self.internal_variable)
		else:
			self.internal_variable=copy.deepcopy(variable)
		
		objects["VariablesManager"].set_variable("CDLOCKER",variable)
	
		return {"status":True,"msg":""}
		
	#def save_variable
	
#class CDLockerManager	
