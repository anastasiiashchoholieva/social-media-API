# Social Media API

 ---
 This Django REST framework-based API serves as a RESTful interface for a social media platform.

## Installation

 ---

Create venv and install requirements
```
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

## Configuration

 ---

### Environment Variables

This project uses environment variables for configuration. To set up the required variables, follow these steps:

1. Create a new `.env` file in the root directory of the project.

2. Copy the contents of the `.env_sample` file into `.env`.

3. Replace the placeholder values in the `.env` file with the actual values specific to your environment.


## Usage

 ---

- To apply migrations to the database use command:
```
python manage.py migrate
```
- Use the following command to load prepared data from fixture:
```
python manage.py loaddata social_media_data.json
```
- After loading data from fixture you can use following test user for login:

Email: `admin@admin.com`
Password: `1qazcde3`

or create one yourself using command:

```
python manage.py createsuperuser
```

- To run server use command:
```
python manage.py runserver
```

 ## Features available

 ---
 * Authentication: Implement a secure method of accessing API endpoints by utilizing JWT token-based authentication.
 * Post management: Enable comprehensive CRUD functionality to handle posts, including their creation, retrieval, 
 updating, deletion and media attachment. In addition, provide users the ability to filter posts based on their hashtags
 * User management: Allow users to register, modify their profile details.
 * API documentation: Utilize Swagger UI to automatically generate interactive API documentation, which facilitates developers in effortlessly exploring and testing the API's endpoints.

 ## API Endpoints

 ---
 The following endpoints are available:

 #### User Registration, Authentication and Following
 * api/user/register: Register a new user by providing an email and password.
 * api/user/token: Receive a token
 * api/user/token/refresh/: Refresh token
 * api/user/token/verify/: Verify token
 * api/user/me/: User information

 ## Documentation

 ---

 * api/doc/swagger/: Documentation using Swagger

![social_api.png](documentation_images%2Fsocial_api.png)
![user_api.png](documentation_images%2Fuser_api.png)
