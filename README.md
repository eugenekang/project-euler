src/
	- euler/
		- euler_problems.py
		# Should be a file that sets up the values necessary to print the output in main.py. Main.py should import this function and run it. Should call a Euler Problem function if necessary that is tested elsewhere.
	- support/
		- custom_functions.py
		# For resuable functions. Not for specific Euler-problem solving functions
		- math.py
		# For specific mathematical operations not covered by python's math package (ie. find primes)
	- main.py
	# Main function that runs and produces output.
tests/unit/src
	- euler/test_euler_problems.py
	# Can probably be deprecated. The euler_problems.py already functions as a type of test itself.
	- support/
		- test_custom_functions.py
		- test_math.py
