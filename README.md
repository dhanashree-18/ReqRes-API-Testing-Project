## ReqRes API Testing Project



API Testing project built with Python, Pytest and Requests library using ReqRes.in as the practice API.



## 

###### Tools \& Technologies

* Python 3.12
* Pytest
* Requests library
* Postman (manual testing)
* GitHub Actions (CI/CD)

\------------------------------------------------------------------------------------------------------------------------------------------------------------



Project Structure


ReqRes API Testing Project/
│
├── api/
│   ├── \_\_init\_\_.py
│   └── users\_api.py         ← POM style API class
│
├── tests/
│   ├── test\_users.py        ← Direct style tests
│   └── test\_pom\_users.py    ← POM style tests
│
├── .github/
│   └── workflows/
│       └── api-tests.yml    ← CI/CD workflow
│
├── conftest.py              ← Fixtures
├── pytest.ini               ← Markers
└── requirements.txt         ← Dependencies


\------------------------------------------------------------------------------------------------------------------------------------------------------------

###### 

###### Test Coverage

|Test|Method|Status Code|
|-|-|-|
|Get all users|GET|200|
|Get single user|GET|200|
|Create user|POST|201|
|Update user|PUT|200|
|Delete user|DELETE|204|
|Get invalid user|GET|404|

\------------------------------------------------------------------------------------------------------------------------------------------------------------

###### How To Run Tests

**Run all tests:**


py -m pytest -v


**Run by marker:**


py -m pytest -m get -v
py -m pytest -m post -v
py -m pytest -m put -v
py -m pytest -m delete -v


**Run with HTML report:**


py -m pytest -v --html=reports/api\_report.html


**Run only POM tests:**


py -m pytest tests/test\_pom\_users.py -v


\------------------------------------------------------------------------------------------------------------------------------------------------------------

###### Fixtures

* `api\_setup` → base URL and headers
* `users\_api` → UsersAPI class instance

\------------------------------------------------------------------------------------------------------------------------------------------------------------

###### Markers

* `get` → GET request tests
* `post` → POST request tests
* `put` → PUT request tests
* `delete` → DELETE request tests

\------------------------------------------------------------------------------------------------------------------------------------------------------------

###### CI/CD

* GitHub Actions workflow runs on every push to main
* All 12 tests run automatically on ubuntu-latest

