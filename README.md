# Sample React App

## Dependencies
- Node.js (https://nodejs.org/en/download/)
- Yarn (```npm install --global yarn```)
- Assignment 1 (Placed in folder **api**)
- Libraries
  ```
  npm install @material-ui/core
  npm install material-table
  npm install @material-ui/icons
  ```

## Run App
### Run Backend Flask REST API App
```
cd api
set FLASK_APP=api.py
set FLASK_ENV=development
flask run
```
Backend server will be running on port **5000**

## Run Frontend React App
```
yarn start
```
Frontend client will be running on port **3000**

## References
### REST API in Flask
- https://www.youtube.com/watch?v=qbLc5a9jdXo
- https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
### React (+ Flask)
- https://blog.miguelgrinberg.com/post/how-to-create-a-react--flask-project
- https://stackoverflow.com/questions/63647493/react-material-table-is-not-displaying-table-icons
- https://blog.bitsrc.io/top-5-react-table-libraries-170505f75da7
- https://material-table.com/#/docs/features/editable
- https://jasonwatmore.com/post/2020/02/01/react-fetch-http-post-request-examples