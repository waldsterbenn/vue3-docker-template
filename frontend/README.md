# Vue 3 Docker App

## Description
This project is a simple Vue 3 application that uses Bootstrap for UI elements and demonstrates routing with a few components. It is built and hosted using Vite.

## Project Structure
```
vue3-docker-app
├── src
│   ├── assets          # Static assets such as images, fonts, and stylesheets
│   ├── components      # Vue components
│   │   ├── Home.vue    # Home component
│   │   └── About.vue   # About component
│   ├── router          # Vue Router setup
│   │   └── index.ts    # Router configuration
│   ├── App.vue         # Root component
│   └── main.ts         # Entry point of the application
├── public
│   └── index.html      # Main HTML file
├── package.json        # Yarn configuration file
├── tsconfig.json       # TypeScript configuration file
├── vite.config.ts      # Vite configuration file
├── Dockerfile          # Dockerfile for building the application
└── .dockerignore       # Files to ignore when building the Docker image
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd vue3-docker-app
   ```

2. **Install dependencies:**
   ```
   yarn install
   ```

3. **Run the application in development mode:**
   ```
   yarn serve
   ```

4. **Build the application for production:**
   ```
   yarn build
   ```

5. **Run the application in Docker:**
   ```
   docker build -t vue3-docker-app .
   docker run -p 3000:3000 vue3-docker-app
   ```

## Usage
- Navigate to `http://localhost:3000` to view the application.
- Use the navigation to switch between the Home and About components. 

## License
This project is licensed under the MIT License.