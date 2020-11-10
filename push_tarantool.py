from tarantool_utils import space_photo, space_message

photo = [
	'0Vgym000BiXoouibgLjv4H5fa132831ai',
	'08g5j000Fs46rieYjeKYfr5fa132821ai'
]

message = [
	'Я скучаю ',
	'Возвращайся '
]

for c in photo:
	space_photo.insert((None, c))

for c in message:
	space_message.insert((None, c))
