# AirBnB_Clone

![image](https://imgur.com/8AFBO3N.png)

## Description

This project focuses of developing a clone of the AirBnb system.

In a total time of 4 months, we should have a complete web application composed by:
- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A website (the front-end) that shows the final product to everybody: static and dynamic
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Requirements

#### Enviroment
Ubuntu 20.04 LTS

#### Python version
3.8.5

#### Coding style
pycodestyle (v `2.8.*`)

#### Tests
Python unittest


*This particular project/repo focuses on the console of the web application*


## The Console

### Installation
Follow these steps to install the AirBnB_clone console
1. Clone this repo
```
$ cd ~
$ git clone https://github.com/iagmidif/AirBnB_clone.git
$ cd ~/AirBnb_clone
```
2. Now you can run the console.py
```
$ ./console.py
```

### Stuff that this console can do
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

In fewer words, this console can do:
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

### Examples

- Creating new models

```
$ ./console
(hbnb) create
** class name missing **
(hbnb) create BaseModel
b4d4d135-c2db-4145-9edf-263a380ca0f7
(hbnb) create User
3a6c168d-f1ab-4b36-9b28-7befa12f9c90
(hbnb) create State
fa3e81d0-ddfe-4fd4-8499-fadc7cd0e0ac
(hbnb) create City
6d6e4bcc-2b23-4e62-8318-37b94da5dfc3
(hbnb) create Review
b4452214-a039-4d41-8924-eae8baef72cd
(hbnb) create Amenity
40be8810-806d-4642-9b98-465050f0a3d4
(hbnb)
```

- The `all` command
    - use `all` to print all stored instances of every model
    - you can also use all `<model name>` it to print all stored instances of a specific model:
    - And you can use it as a method call:

```
(hbnb) all
["[BaseModel] (404c5725-1b55-4613-8465-b6eafaf79980) {'id': '404c5725-1b55-4613-8465-b6eafaf79980', 'created_at': datetime.datetime(2022, 8, 11, 15, 42, 3, 870030), 'updated_at': datetime.datetime(2022, 8, 11, 15, 42, 3, 870046)}", "[User] (2c378e51-02fe-4b99-b4a5-8f15d2a19341) {'id': '2c378e51-02fe-4b99-b4a5-8f15d2a19341', 'created_at': datetime.datetime(2022, 8, 11, 15, 42, 8, 344083), 'updated_at': datetime.datetime(2022, 8, 11, 15, 42, 8, 344095)}", "[State] (9991bd60-6909-484a-a39f-7f2351224d52) {'id': '9991bd60-6909-484a-a39f-7f2351224d52', 'created_at': datetime.datetime(2022, 8, 11, 15, 42, 13, 825929), 'updated_at': datetime.datetime(2022, 8, 11, 15, 42, 13, 825946)}", "[City] (930fbc35-103e-4982-b810-1837ff947d43) {'id': '930fbc35-103e-4982-b810-1837ff947d43', 'created_at': datetime.datetime(2022, 8, 11, 15, 42, 18, 368613), 'updated_at': datetime.datetime(2022, 8, 11, 15, 42, 18, 368625)}", "[Amenity] (eae5e9f1-be58-4114-9a84-5ad4298b979e) {'id': 'eae5e9f1-be58-4114-9a84-5ad4298b979e', 'created_at': datetime.datetime(2022, 8, 11, 15, 42, 24, 57277), 'updated_at': datetime.datetime(2022, 8, 11, 15, 42, 24, 57282)}", "[Place] (57b02da1-2ccd-47e2-8981-a9c1294f00f1) {'id': '57b02da1-2ccd-47e2-8981-a9c1294f00f1', 'created_at': datetime.datetime(2022, 8, 11, 15, 42, 27, 790399), 'updated_at': datetime.datetime(2022, 8, 11, 15, 42, 27, 790412)}", "[Review] (f5346d31-ec18-49e8-8ab3-a51fe5606b2e) {'id': 'f5346d31-ec18-49e8-8ab3-a51fe5606b2e', 'created_at': datetime.datetime(2022, 8, 11, 15, 42, 32, 404947), 'updated_at': datetime.datetime(2022, 8, 11, 15, 42, 32, 404957)}"]
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (404c5725-1b55-4613-8465-b6eafaf79980) {'id': '404c5725-1b55-4613-8465-b6eafaf79980', 'created_at': datetime.datetime(2022, 8, 11, 15, 42, 3, 870030), 'updated_at': datetime.datetime(2022, 8, 11, 15, 42, 3, 870046)}"]
(hbnb) all Place
["[Place] (57b02da1-2ccd-47e2-8981-a9c1294f00f1) {'id': '57b02da1-2ccd-47e2-8981-a9c1294f00f1', 'created_at': datetime.datetime(2022, 8, 11, 15, 42, 27, 790399), 'updated_at': datetime.datetime(2022, 8, 11, 15, 42, 27, 790412)}"]
(hbnb)
(hbnb) User.all()
["[User] (2c378e51-02fe-4b99-b4a5-8f15d2a19341) {'id': '2c378e51-02fe-4b99-b4a5-8f15d2a19341', 'created_at': datetime.datetime(2022, 8, 11, 15, 42, 8, 344083), 'updated_at': datetime.datetime(2022, 8, 11, 15, 42, 8, 344095)}"]
(hbnb)
```

The same applies to the rest commands:
- `show`
- `count` (available only as a method call)
- `destroy`
- `update`
