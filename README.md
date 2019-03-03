# pybookstore
A book store written in Python as RESTful application.

## How to test
```bash
	$ git clone https://github.com/Cledersonbc/pybookstore.git
	$ cd pybookstore
	$ python3 -m venv env
	$ source env/bin/activate
	$ pip install -r requirements.txt
	$ python3 run.py
```

Visit [http://localhost:5000](http://localhost:5000).


The swagger-ui is available at [http://localhost/api/ui](http://localhost/api/ui).

# TODO list

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
* [X] Add footer
* [ ] Add relevant actions on navbar
* [ ] Add some widgets on sidebar
* [ ] Uploud of images on book
* [X] Compatible input with database columns
* [ ] Beautiful layout of CRUD pages (book)
* [ ] Logo
* [ ] Add some logo on header
* [X] Navigation between CRUD pages
* [ ] Uploud of images


**Database**
* [X] Use of ORM
* [X] Create DAO of book
* [ ] Create DAO of account


**Page User Preferences**
* on future


**Widgets**
* [ ] Navigator
* [ ] Comments
* [ ] Top books
* [ ] Smart search of book images using webscrapping
* [ ] Internationalization


**API Books**
* [X] Create new book (endpoint)
* [X] See a book (endpoint)
* [X] Update a book (endpoint)
* [X] Delete a book (endpoint)
* [X] See a list of books (endpoint)
* [X] Create new book (functional)
* [X] See a book (functional)
* [X] Update a book (functional)
* [X] Delete a book (functional)
* [X] See a list of books (functional)


**Security**
* [ ] Access to API
* [ ] Access to CRUD operations (without API, only with user's account)
* [ ] All CRUD operations need to be relative to each account
