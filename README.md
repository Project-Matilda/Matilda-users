the workflow
1) username,Gmail, password and confirm password
2) validation check for username,gmail, password
3) registered successfully in db and access key generated
4) username,pwd, access key asked as input 
5) after cross checking in db, a message is displayed (as of now) denoting a successful login.
Points to note:
1) no duplication of registration data
2) access key validity= 7 days
3) common passwords, wrong format gmails, pwd mismatch, register and login data mismatch all checked
4) works in both rest framework HTML and raw data form as well as postman
5) only after giving the access token in postman the admin can do crud operations
6) diff users,diff keys, use them alone
how to access:
create a superuser and go to postman in authorization click basic auth and give those credentials to perform CRUD operations on Registered data.
as a normal user, give the token in both input field and in postman authorization click bearer token and give the token generated.
links for access:
http://127.0.0.1:8000/api/api/login/
http://127.0.0.1:8000/api/api/register/
http://127.0.0.1:8000/api/api/users/ (use in postman)
http://127.0.0.1:8000/api/api/users/<id> (use in postman)
