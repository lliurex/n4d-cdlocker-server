#!/usr/bin/python3

import copy
import n4d.server.core as n4dcore
import n4d.responses

class CDLockerManager:
	

	def __init__(self):
		
		self.core=n4dcore.Core.get_core()
		
		pass
		
	#def init

	
	def startup(self,options):
		
		#Old n4d: self.internal_variable=copy.deepcopy(objects["VariablesManager"].get_variable("CDLOCKER"))
		self.internal_variable=self.core.get_variable("CDLOCKER").get('return',None)
		if self.internal_variable==None:
			try:
				self.initialize_variable()
				#Old n4d: objects["VariablesManager"].add_variable("CDLOCKER",copy.deepcopy(self.internal_variable),"","CDLocker internal variable","lliurex-cdlocker")
				self.core.set_variable('CDLOCKER',copy.deepcopy(self.internal_variable))
			except Exception as e:
				print(str(e))
	
	#def startup


	def initialize_variable(self):
		
		self.internal_variable={}
		self.internal_variable["enabled"]=False
		
	#def initialize_variable

	
	def is_enabled(self):
		
		try:
			#Old n4d: return self.internal_variable['enabled']
			return n4d.responses.build_successful_call_response(self.internal_variable["enabled"])

		except:
			#Old n4d: return False
			return n4d.responses.build_failed_call_response()
			
	#def is_enabled

	
	def set_lock_status(self,status):
		
		if type(status)==bool:
			self.internal_variable["enabled"]=status
			ret=self.save_variable()
			#Old n4d: return True
			return n4d.responses.build_successful_call_response(ret['status'])
			
		#returnreturn False
		return n4d.responses_build_failed_call_response()
		
	#def set_lock_status
	
	def save_variable(self,variable=None):

		if variable==None:
			variable=copy.deepcopy(self.internal_variable)
		else:
			self.internal_variable=copy.deepcopy(variable)
		
		#Old n4d:objects["VariablesManager"].set_variable("CDLOCKER",variable)
		self.core.set_variable('CDLOCKER',variable)
	
		return {"status":True,"msg":""}
		
	#def save_variable
	
#class CDLockerManager	
