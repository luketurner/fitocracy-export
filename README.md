## I Just Want My Damn Data, Is That Too Much To Ask?

Apparently, yes. I'm working on it though, man. 

Current state: Working but hacky. No exceptions, only basic error checking. No threads, so getting all data takes minutes. 

## Documentation

There isn't any, sorry. Examples below give a very general overview. If you want to know what functions the API session supports, you gotta look at the code.

## Example

	import api
	sesh = api.APISession()
	if sesh.login("user", "pass"):
		sesh.get_all_activity_data()
		sesh.save_activity_data("data.json")
	else:
		... login failed ...

alternatively:

	import api
	sesh = api.APISession()
	if sesh.login("user", "pass")
		data = sesh.get_all_activity_data()

	... do something with data ...

or:

	import api
	sesh = api.APISession()
	if sesh.login("user", "pass")
		squat_data = sesh.get_activity_data('Barbell Squat')

	... do something with data ...
