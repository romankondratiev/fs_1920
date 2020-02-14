# https://fs-1920.herokuapp.com/

# Online Search Engine with Soccer Players (+ team-builder)


Sonarcloud:

[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=romankondratiev_fs_1920)](https://sonarcloud.io/dashboard?id=romankondratiev_fs_1920)

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=romankondratiev_fs_1920&metric=ncloc)](https://sonarcloud.io/dashboard?id=romankondratiev_fs_1920) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=romankondratiev_fs_1920&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=romankondratiev_fs_1920) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=romankondratiev_fs_1920&metric=alert_status)](https://sonarcloud.io/dashboard?id=romankondratiev_fs_1920) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=romankondratiev_fs_1920&metric=security_rating)](https://sonarcloud.io/dashboard?id=romankondratiev_fs_1920) [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=romankondratiev_fs_1920&metric=sqale_index)](https://sonarcloud.io/dashboard?id=romankondratiev_fs_1920) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=romankondratiev_fs_1920&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=romankondratiev_fs_1920)


CodeClimate::

[![Maintainability](https://api.codeclimate.com/v1/badges/d03ed1bc12b0e6789bae/maintainability)](https://codeclimate.com/github/romankondratiev/fs_1920/maintainability)


The database was exported from the FIFA 2019 players database:
https://www.kaggle.com/karangadiya/fifa19


The webapp has 2 main features: 
1. Search engine 
	- search within the database with a text query
	- display the players that match the search criteria ( the “searchable" attributes are: name, club & nationality)
	- the displayed attributes for a search result are the following
		- name
		- age
		- nationality
		- club
		- photo
		- overall score
2. Team-builder
	- takes input a specific budget (e.g: $200,000,000)
	- Once the budget defined, the tool shows  a list of 11 players that constitute the best team I can have for this specific budget. Best player is defined from their overall score. (You can also decide to use other attributes to define the best player if you wish).
	-There is some logic behing the team building: 
		-As you know, you can’t have a team with only attackers; you’ll see there is a position attribute in the DB.
		- Every 11 player team will need 1 goalkeeper, 2 fullback, 3 halfback and 5 forward playing


## 1. UML
To create UML diagrams I used a UML plagin in Sublime Text Editor.
### 1.1. Class Diagram
<p align="center">
  <img src="/uml-class-diagram-2.png">
</p>

### 1.2. Use Case diagram
<p align="center">
  <img src="/uml-class-diagram-2.png">
</p>

### 1.3. Activity diagram
<p align="center">
  <img src="/uml-class-diagram-2.png">
</p>


## 2. Metrics

Besides the badges at the beginning of the page,
you can find additional information about used metrics
on the following pages:
* [sonarcloud.io](https://sonarcloud.io/dashboard?id=romankondratiev_fs_1920) 
* [codeclimate.com](https://codeclimate.com/github/romankondratiev/fs_1920) 

## 3. Clean Code Development

## 4. Build Management with PyGradle and Gradle

## 5. Unit-Tests

The player model was covered by the unit tests
[tests.py](players/tests.py):

```python
from django.test import TestCase
from .models import Player

class PlayerTestCase(TestCase): #Test Case for object creation

    def setUp(self):
		Player.objects.create(
			name="test", 
			age=100,
			photo="test", 
			nationality="test", 
			overall=100, 
			club="test", 
			value="test", 
			position="test", 
			value_int=100 )

        Player.objects.create(
			name="test_second",
			age=200,
			photo="test_second",
			nationality="test_second", 
			overall=200,
			club="test_second", 
			value="test_second",
			position="test_second", 
			value_int=200 )

    def test_players(self):
        first = Player.objects.get(age=100)
        second = Player.objects.get(age=200)
        self.assertEqual(first, 'test')
        self.assertEqual(second, 'test_second')
  ```





## 6. Continuous Integration

## 7. IDE 

I have used Sublime Text as my IDE.

I used such packages as:
* Alignment 
* Django Starter 
* Emmet 
* SublimeGit
* SublimeLinter

My favorite shortcuts in the Sublime are:
* Open terminal (**⌘⇧T**) 
* Allign code (**⌘⇧A**) 
* Find All (**⌘⇧F**)
* Show errors & dirty code with Lintner (**⌘⇧AB**)


## 8. DSL

## 9. Functional Programming

* Final data structures

Within the whole codebase I used such data structures as lists, dictionaries, tuples

* Side effect free functions

    Example:
    ```python
	def get_queryset(self, *args, **kwargs):
		query=self.request.GET.get('q', None)
		if query is not None:
			queryset = Player.objects.search(query)
			return queryset
		return Player.objects.all()
    ```

 * The use of higher order functions

	Example:
     ```python
    	def form_valid(self, form):
			self.request.session['budget'] = form.cleaned_data.get('budget') #saving user input in current session
			return self.validate(form)
     ```

* Functions as parameters and return values/anonymous functions

    Simple example using anonymous function
    ```python
		# Program to double each item in a list using map()
		my_list = [1, 5, 4, 6, 8, 11, 3, 12]
		new_list = list(map(lambda x: x * 2 , my_list))
		# Output: [2, 10, 8, 12, 16, 22, 6, 24]
		print(new_list)
    ```

    Simple example using functions as parameters:
    ```python
	def myfunc(anotherfunc, extraArgs):
	    anotherfunc(*extraArgs)
    ```


* Use Closures
    
    Simple example using closures with Python
    ```python
	def print_msg(msg):
		# This is the outer enclosing function

		    def printer():
		# This is the nested function
		        print(msg)

		    printer()

	# We execute the function
	# Output: Hello
	print_msg("Hello")

    ```




