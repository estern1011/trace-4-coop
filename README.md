# Review Your Co-op

## Video
Here's what the project looks like when it's running!
- https://vimeo.com/390266154

## Inspiration
- It's very hard to get information about co-op interview processes and what it is like to co-op in a certian role at a specific company. 
    - Glassdoor is a thing, but there are barriers, and at large companies it can be hard to see specifics regarding certain roles and locations. 

## Features
- Add companies that aren't in the list
    - The backend will hit clearbit's API in order to get the domain address and logo for the company. 
- Add positions for companies
- Add reviews for positions at companies
    - The forms have auto-completion for looking up specific companies and roles
- All stored in MongoDB

## How to run
- Run MongoDB (default port 27017)
- In /backend
    - Set up a python3 virtual environment: python3 -m venv venv
    - Enter the virtual environment: source venv/bin/activate
        - To leave the virtual environment, "deactivate"
    - Install the requirements: pip install -r requirements.txt
    - Run the backend server: python3 app/app.py
- In /frontend
    - Make sure you have all of the dependencies installed:
        - Install npm
        - Install the rest: npm install
    - Run the frontend server: npm run serve
- You should now be able to access the app at http://localhost:8080
