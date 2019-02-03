# pybookstore
A book store written in Python as RESTful application.

## How to test
```bash
	$ git clone https://github.com/Cledersonbc/pybookstore.git
	$ cd pybookstore
	$ python3 -m venv env
	$ source env/bin/activate
	$ pip install -r requirements.txt
	$ python3 server.py
```

Visit [http://localhost:5000](http://localhost:5000).


The swagger-ui is available at [http://localhost/api/ui](http://localhost/api/ui).

**TODO** list

**Simple Pages, CRUD book**
* [X] Home
* [ ] Error 404
* [X] Create new book
* [X] See a book
* [X] Update a book (same as creation)
* [X] Delete a book (same as visualization)


**DAO Page of Accounts**
* [ ] Create new user account
* [ ] See a user account
* [ ] Update a user account (same as creation)
* [ ] Delete a user account (same as visualization)


**Adjusts on CRUD pages**
* [ ] Validate inputs and ranges (it depends on the database)
* [ ] Add footer
* [ ] Add some logo on header
* [ ] Add relevant actions on navbar
* [ ] Add some widgets on sidebar
* [ ] Uploud of images on book


**Database**
* [ ] Use of ORM
* [X] Create DAO of book
* [X] Create DAO of account


**Page User Preferences**
* on future


**Widgets**
* [ ] Navigator
* [ ] Comments
* [ ] Top books
* [ ] Smart search of book images using webscrapping


**API Books**
* [X] Create new book (endpoint)
* [X] See a book (endpoint)
* [ ] Update a book (endpoint)
* [ ] Delete a book (endpoint)
* [ ] Create new book (functional)
* [ ] See a book (functional)
* [ ] Update a book (functional)
* [ ] Delete a book (functional)


**Security**
* Access to API
* Acess to CRUD operations (without API, only with user's account)
