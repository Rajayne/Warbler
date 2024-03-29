# Warbler
Twitter clone to practice reading/understanding an existing application, as well as fixing bugs, writing tests, and extending it with new features.

# Setup
Create virtual environment and run seed file.

# Guidelines
1. Fix logout route
    - Should flash success and redirect to login
2. Fix user profile
    - Include location, bio and header image
3. Fix user card
    - Show bio for each user on followers, following, and list-users pages
4. Edit profile
    - Allow user to edit profile if logged in
    - Display form to edit username, email, image_url, header_image_url, bio
    - Form should require user to enter password to save changes
    - Check for correct password for current user then redirect to user details page
5. Fix homepage to show:
    - The last 100 recent messages
    - Only displays messages from the current user and users the current user is following 
6. Add likes function
    - Import Likes model
    - Add feature that allows user to 'like' a message
    - Profile page should display likes count and link to a page showing all liked messages
7. Add unit tests
    - Create new db warbler-test for testing
