# Online Search Engine with Soccer Players (+ team-builder)

# https://fs-1920.herokuapp.com/


## Checklist 

1. [UML](https://github.com/romankondratiev/fs_1920/#1-uml)
2. [Metrics](https://github.com/romankondratiev/fs_1920/#2-metrics)
3. [Clean Code Development](https://github.com/romankondratiev/fs_1920/#3-clean-code-development)
4. [Build Management](https://github.com/romankondratiev/fs_1920/#4-build-management)
5. [Unit tests](https://github.com/romankondratiev/fs_1920/#5-unit-tests)
6. [Continous Integration and delivery](https://github.com/romankondratiev/fs_1920/#6-continuous-integration)
7. [IDE](https://github.com/romankondratiev/fs_1920/#7-ide)
8. [DSL](https://github.com/romankondratiev/fs_1920/#8-dsl)
9. [Functional Programming](https://github.com/romankondratiev/fs_1920/#9-functional-programming)

### Screenshots
<p align="center">
  <img src="/homepage.png">
</p>

<p align="center">
  <img src="/results.png">
</p>


Sonarcloud:

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=romankondratiev_fs_1920&metric=alert_status)](https://sonarcloud.io/dashboard?id=romankondratiev_fs_1920) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=romankondratiev_fs_1920&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=romankondratiev_fs_1920) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=romankondratiev_fs_1920&metric=security_rating)](https://sonarcloud.io/dashboard?id=romankondratiev_fs_1920) [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=romankondratiev_fs_1920&metric=ncloc)](https://sonarcloud.io/dashboard?id=romankondratiev_fs_1920) [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=romankondratiev_fs_1920&metric=sqale_index)](https://sonarcloud.io/dashboard?id=romankondratiev_fs_1920) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=romankondratiev_fs_1920&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=romankondratiev_fs_1920)


CodeClimate::

[![Maintainability](https://api.codeclimate.com/v1/badges/d03ed1bc12b0e6789bae/maintainability)](https://codeclimate.com/github/romankondratiev/fs_1920/maintainability)


## This webapp allows to search for soccer players and build perfect team with specific budgets. 

The database for this project was exported from the FIFA 2019 players database:
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

It was built with Python web-framework Django for backend, JavaScript/HTML/CSS for frontend, PostgreSQL as a database and deployed on Heroku. 

## 1. UML
To create UML diagrams I used 'creately' tool
### 1.1. Class Diagram
<p align="center">
  <img src="/uml-class-diagram-2.png">
</p>

### 1.2. Use Case diagram
<p align="center">
  <img src="/uml-use-cases.jpg">
</p>

### 1.3. Activity diagram
<p align="center">
  <img src="/uml-activity.jpg" style='width: 75%'>
</p>


## 2. Metrics

Besides the badges at the beginning of the page,
you can find additional information about used metrics
on the following pages:
* [sonarcloud.io](https://sonarcloud.io/dashboard?id=romankondratiev_fs_1920) 
* [codeclimate.com](https://codeclimate.com/github/romankondratiev/fs_1920) 

## 3. Clean Code Development

I Implemented most of the **Clean Code Development** principles and PEP Conventions with the help of Sublime Text Plugin 'Linter'.


[10 point Clean Code Development Cheatsheet](https://user-images.githubusercontent.com/35653122/51113192-86f8d880-1801-11e9-90ad-88dd58854a18.png)

1. Function rules: Small, Do one thing, Prefer fewer arguments, Use descriptive names, No side effects:
```python
	def form_valid(self, form):
		self.request.session['budget'] = form.cleaned_data.get('budget') #saving user input in current session
		return super(HomeView, self).form_valid(form)
	def read_table(sometable, function): # To populate database with data from .csv file
		df = pd.read_csv(sometable, sep=',', usecols = ['Name', 'Age', 'Photo', 'Nationality', 'Overall','Club', 'Value','Position'])
		for index, row in df.iterrows():
			Player.objects.get_or_create(
				name=row['Name'], 
				age=row['Age'],
				photo=row['Photo'],
				nationality=row['Nationality'],
				overall=row['Overall'],
				club=row['Club'],
				value=row['Value'],
				position=row['Position'],
				value_int=function(row['Value']),
				)
		return df
```

2. Understandability tips:
    Be consistent, use explanotary variables
```python
	def get_queryset(self, *args, **kwargs):
		query=self.request.GET.get('q', None)
		if query is not None:
			queryset = Player.objects.search(query)
			return Player.objects.search(query)
		queryset = Player.objects.all()
		return queryset
	def get_queryset(self, *args, **kwargs):
		user_input=self.request.session['budget']
		if user_input is not None:
			queryset = Player.objects.build_team(user_input)
			return queryset
		queryset = None
		return queryset
```

3. [Method Names and Instance Variables](https://pep8.org/#method-names-and-instance-variables):
    Proper function naming rules: lowercase with words separated by underscores to improve readability.
```python
	def get_context_data(self, *args, **kwargs): 
		context = super(TeamView, self).get_context_data(*args, **kwargs)  
		context['budget'] = self.request.session['budget']
		qs = self.get_queryset()
		if qs is not None:
			context['avg'] = qs.aggregate(Avg('overall'))
		return context
```

4. [Class Names](https://pep8.org/#class-names):
    Class names with the CapWords convention.
```python
    class TeamView(ListView): 
        ...
	class HomeView(FormView):
        ...
	class SearchView(ListView):
        ...
```

5. Source code structure: declare variables close to their usage, similar function should be close
```python
	class HomeView(FormView): 
		template_name = "players/home.html"
		form_class = TeamForm
		success_url = '/team'

		def form_valid(self, form):
			self.request.session['budget'] = form.cleaned_data.get('budget') #saving user input in current session
			return super(HomeView, self).form_valid(form)
```

6. [Maximum Line Length](https://pep8.org/#maximum-line-length):
    Maximum length of a single line should be around 80 chars.
```python
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

## 4. Build Management

I used [Heroku's automated build system](https://www.heroku.com/dynos/build) for the build process of my webapp:

To deploy an app, Heroku needs only three things from the developer: source code, a list of dependencies, and a [Procfile](/Procfile) (a text file that indicates which command should be used to start the code running). The build system takes the application, its dependencies, and the language runtime and produces a “slug.” A slug contains everything needed to run the app, except for the operating system.

<p align="center">
  <img src="/heroku_build.png">
</p>


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

I used [Circle CI](https://circleci.com/build-insights/gh/romankondratiev) for continuous integration and and [Heroku](https://www.heroku.com/continuous-delivery) for delivery


<p align="center">
  <img src="/heroku-cd.png">
</p>


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
* Show errors & dirty code with Linter (**⌘⇧AB**)


## 8. DSL

Since my project is an interactive webapp and the user interacts with my webapp through the input field, inserting queries with different parameters, there is no need for an explicit DSL-commands other than the input field for search queries. 

<p align="center">
  <img src="/dsl.png">
</p>

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




