## I Just Want My Damn Data, Is That Too Much To Ask?

Apparently, yes. I'm working on it though, man. 

Current state: Working but hacky. No exceptions, only basic error checking. No threads, so getting all data takes minutes. 

## Documentation

There isn't any, sorry. Examples below give a very general overview. If you want to know what functions the API session supports, you gotta look at the code.

## CLI Client

Intent: Provide simple method for people to back up their data without having
to use the API directly

Usage: 

    python cli.py [user] [pass]

## API Example

	import fitocracy_export
	sesh = fitocracy_export.APISession()
	if sesh.login("user", "pass"):
		sesh.get_all_activity_data()
		sesh.save_activity_data("data.json")
	else:
		... login failed ...

alternatively:

	import fitocracy_export
	sesh = fitocracy_export.APISession()
	if sesh.login("user", "pass")
		data = sesh.get_all_activity_data()

	... do something with data ...

or:

	import fitocracy_export
	sesh = fitocracy_export.APISession()
	if sesh.login("user", "pass")
		squat_data = sesh.get_activity_data('Barbell Squat')

	... do something with data ...
