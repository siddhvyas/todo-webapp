# ToDo-webapp
To-Do list based web app, needs you to login with id and password and stores the list.

# Templates 
<dl>
  <dt>index.html</dt>
  <dd>- Home page; takes current user and and displays all tasks based on that user</dd>
  <dt>login.html</dt>
  <dd>- login page takes ussername and password; initializes and passes current user to home page</dd>
  <dt>signup.html</dt>
  <dd>- signup page takes username and password and creates a user based on the inputs</dd>
</dl>

# Languages used
Python, CSS, HTML

# Dependencies
<ul>
  <li>Flask</li>
  <li>Jinja2</li>
  <li>sqlite3</li>
</ul>

# Bugs
<ul>
  <li>sqlite3 OperationalError: Not able to access tables in database; Throws error while accessing database tables for all pages</li>
  <li>Signup page redirecting to login page instead of index after submiting</li>
</ul>
