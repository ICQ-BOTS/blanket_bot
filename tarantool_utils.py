import tarantool

#space - ../scheme/blanket.lua

connection = tarantool.connect("localhost", 3301)

space_user = connection.space('user')

space_photo = connection.space('photo')

space_message = connection.space('message')


class User:
	def __init__(self, user_id):
		self.user = space_user.select(user_id)
		if not self.user:
			self.user = space_user.insert((user_id, True, '', False, [], 0, 0))

	def save(self):
		space_user.replace(self.user[0])   