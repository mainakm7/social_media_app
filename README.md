# social_media_app (In development)

## Description
social_media_app is an application designed for users to blog their thoughts and post pictures. It utilizes a SQL database to store blogged items and incorporates user authentication features. Users can create a profile, log in securely, and then add, or delete their blogs within the app. Any user can currently read all blogs by anyone. Their is an admin superuser to regulate user activity. The application provides REST APIs for performing CRUD (Create, Read, Update, Delete) operations on the to-do items, making it easy to integrate with other systems or extend its functionality.

## Features
- User authentication system: Allows users to create accounts and securely log in.
- Blog management: Users can add, delete, and view their blogs.
- Users can read blogs by other users.
- REST APIs: Provides endpoints for performing CRUD operations on to-do items, facilitating integration with other systems.
- Relative module imports: Utilizes relative imports for compatibility with pytest, ensuring smooth testing procedures.

## Installation
1. Clone the repository: `https://github.com/mainakm7/social_media_app.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Python version used = 3.11.5

## Usage
1. Ensure you have SQLite3 and MySQL 5.6 installed and running on your system.
2. Run the application from the root folder outside the app package, e.g., `root_folder/social_media_app`.
3. Access the application through your preferred web browser or API client.
4. Create a user profile and log in to start managing your blogs.

## Database
- The application supports any SQL database options: SQLite3 and MySQL:5.6 were tested.
- Choose the appropriate database configuration in the application settings or environment variables.
- Ensure the database server is running and accessible before running the application.

## Development
- This application was developed using FastAPI for building REST APIs.
- Contributions and feedback are welcome. Feel free to submit pull requests or raise issues on the GitHub repository.

## Contributors
- Mainak Mustafi

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
