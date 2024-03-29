# A Crypto app using Flask, React, and Postgres

I decided to make this project so that I can learn more about Postgres. I wanted to learn a real backend language and was tired of Firebase so I went to YouTube. While scrolling, I found this kind (same age as me) but he wasn't like your average kid, he was a programming genius, and he basically taught me how to connect the Postgres database to my Flask project and then connect my Flask project to my React frontend. He has tons of videos on full-stack programming, [click this link to go to his channel.](https://www.youtube.com/@ArpanNeupaneProductions/videos)

Here's how I used each component: 
### Flask:
- Get the crypto API and send the data to a route --> ReactJS frontend would connect to the link and collect the data from the JSON
- Creating and Deleting rows from the database --> I used Flask to create the function and then used Axios in ReactJS to delete data from the database

### ReactJS:
- Get the data being sent from Flask --> then display it in the frontend
- Run the functions for adding and deleting data to the Postgres database

### Postgres: 
- To save certain coins to the database

## Future of this Project: 
The more that I learn about Postgres the more features that I add. I plan to add user authentication next so that I can have my own system. I think that the idea of having your own authentication is super cool in the sense that you can always deviate from it and add more to the authentication features.
