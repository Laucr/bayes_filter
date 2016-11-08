class Logger:

	def __init__(self):
		pass

	OKBLUE = '\033[94m' + '[-] '
	OKGREEN = '\033[92m' + '[-] '
	WARNING = '\033[93m' + '[*] '
	ERROR = '\033[91m' + '[#] '
	ENDC = '\033[0m'

	@staticmethod
	def log(msg, code=1):
		if code is 1:
			print Logger.OKBLUE, msg, Logger.ENDC
		elif code is 2:
			for iter_ in msg:
				print Logger.OKGREEN, iter_, Logger.ENDC
		else:
			print Logger.OKGREEN, msg, code, Logger.ENDC

