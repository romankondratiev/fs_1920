# https://fs-1920.herokuapp.com/

# Online Search Engine with Soccer Players (+ team-builder)

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
To create UML diagrams I used a PlantUML plugin in PyCharm.
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