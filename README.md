# Social Media API

 ---
 This Django REST framework-based API serves as a RESTful interface for a social media platform.

 ## How to run

 ---
 ```python
 git clone https: https://github.com/anastasiiashchoholieva/social-media-API.git
 cd social_media_api
 python -m venv venv
 source venv/bin/activate (for linux or macOS)
 venv\Scripts\activate (for Windows)
 pip install -r requirements.txt
 python manage.py migrate
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
