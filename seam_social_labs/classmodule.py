class chat_response():
	english_ques = [
		"What is your zipcode?", 
		"How long have you lived in Miami?", 
		"What is your favorite thing about Miami?", 
		"If you could change one thing about Miami what would it be?", 
		"How do you feel about the current leadership?", 
		"Do you see yourself staying in Miami?"]

	spanish_ques = [
		"¿Cuál es su código postal?", 
		"¿Cuánto tiempo has vivido en Miami?",
		"¿Qué es lo que más te gusta de Miami?",
		"Si pudieras cambiar una cosa de Miami, ¿cuál sería?",
		"¿Cómo te sientes acerca del liderazgo actual?",
		"¿Te ves en Miami?"
	]

	creole_ques = [
		"Ki sa ki postal postal ou a?",
		"Depi konbyen tan ou rete nan Miami?",
		"Ki bagay ou pi renmen sou Miami?",
		"Si ou ta ka chanje yon sèl bagay sou Miami ki sa li ta dwe?",
		"Kijan ou santi ou sou lidèchip aktyèl la?",
		"Èske ou wè tèt ou rete nan Miami?"
	]

	def __init__(self, lang):
		self.responses = []
		self.lang = lang

	def print_response(self):
		for i in range(6):
			if (self.lang == "english"):
				print(self.english_ques[i])
			elif (self.lang == "spanish"):
				print(self.spanish_ques[i])
			else:
				print(self.creole_ques[i])
			print(str(i)+ "." + self.responses[i])
		print("\n")
		

	def questions(self):
		if self.lang == "invalid":
			return

		for i in range(6):
			if (self.lang == "english"):
				print(self.english_ques[i])
			elif (self.lang == "spanish"):
				print(self.spanish_ques[i])
			else:
				print(self.creole_ques[i])
			resp = input()
			print("\n")
			self.responses.append(resp)

		self.print_response()

