from flask import Flask

# current module (__name__) as argument.
app = Flask(__name__)

def test_add_rule():
	return 'This message try add url rule 1 :>'

def test_add_rule_1():
	return 'This message try add url rule 2 :>'

"""
'/' : mean url route
'demo_rule' : is unique name to identify the view funtion, here explicitly specified it as 'demo_rule'
test_add_rule: the function that should be called when this URL is requested
"""
app.add_url_rule('/','demo_rule',test_add_rule)

# main driver function
if __name__ == '__main__':
	app.run()
