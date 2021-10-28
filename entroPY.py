from cryptography.fernet import Fernet
import gzip
import sys


#takes a file and return a gziped string of it.
class cryptor:
	def __init__(self, inFile):
		self.fileName = inFile#this gets the filename
		self.imports = ['gzip']#thes are the moduals required for this class
		self.deCompressSudoCode = []

		#this gets the contents of the file
		with open(self.fileName) as filesname:
			self.fileData = filesname.read() 


	def compressMe(self, data):
		"""returns a gzip compressed utf8 string"""
		return gzip.compress(data.encode()).decode('cp437')

	def deCompressMe(self, data):
		"""returns a decompressed string"""
		return gzip.decompress(data.encode('cp437')).decode()

	def deCompresserCodeGenrator(self):
		pass


class polygram:
	def __init__(self, data):
		self.code = data.encode()#this is the string we want to encrypt
		self.stringKey = Fernet.generate_key()#this is a random key, it is only usd for the decryptCodeGenrator function
		self.key = Fernet(self.stringKey)# this is a class
		self.imports = ['from cryptography.fernet import Fernet']#thes are the moduals required for this class
		self.unEncryptSudoCode = []

	def encrpytS(self, text):
		"""this will return an encrypted string"""
		return self.key.encrypt(text)

	def decryptS(self, text):
		"""this will return  a decrypted string"""
		return self.key.decrypt(text).decode()

	def decryptCodeGenrator(self, mesage):
		"""the execution of thgis cod will give you ├Γéº┬░ya┬á+(Γò⌐Γòá+ΓòñP"""
		import random
		import string
		
		#random variables
		self.letters = string.ascii_letters
		self.eMessage = ''.join(random.choice(self.letters) for i in range(10))
		self.k = ''.join(random.choice(self.letters) for i in range(10))
		self.fKey = ''.join(random.choice(self.letters) for i in range(10))
		self.dMessage = ''.join(random.choice(self.letters) for i in range(10))
		self.randFileName = ''.join(random.choice(self.letters) for i in range(10))

		self.unEncryptSudoCode = [self.eMessage+' = b\''+mesage+'\'',
		self.k+' = '+str(self.stringKey),
		'from cryptography.fernet import Fernet',
		self.fKey+' = Fernet('+self.k+')',
		self.dMessage+' = '+self.fKey+'.decrypt('+self.eMessage+')',
		'a = '+self.dMessage+'.decode()',
		'exec(gzip.decompress(a.encode(\'cp437\')).decode())']
		
			





newFile = open('bomb.py','w')

file = str(sys.argv[-1])

c = cryptor(file)
newFile.write('import '+c.imports[0]+'\n')

compressed = c.compressMe(c.fileData)
poly = polygram(compressed)

#this works it returns
poly.decryptCodeGenrator(poly.encrpytS(compressed.encode()).decode('cp437'))
for x in poly.unEncryptSudoCode:
	newFile.write(x+'\n')
newFile.close()


