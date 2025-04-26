# Vue3 Docker Template

This project provides a preconfigured Docker container that hosts a Vue 3 app using Vite.

## Getting Started

### Prerequisites

- [Docker Desktop](https://docs.docker.com/desktop/) installed and running on your machine.
- [Git](https://git-scm.com/) (optional) if you want to clone the repository.

### How to Host Locally

1. **Clone the Repository (if needed):**

   ```bash
   git clone https://github.com/your-username/vue3-docker-template.git
   cd vue3-docker-template
   ```

2. **Start the Docker Container:**

   Open a terminal on your Windows machine and run:

   ```bash
   docker-compose up
   ```

   This command uses the `docker-compose.yml` file which builds and runs the frontend service with the Vue 3 app.

3. **Open the Website in Your Browser:**

   Once the container is up and running, open your browser and navigate to:

   ```
   http://localhost:3000
   ```

   This URL maps port 3000 on the host machine to port 8080 in the container where the Vue 3 app is served.

### Additional Information

- Changes made in the `frontend/src` directory are synchronized with the running Docker container automatically.
- For more details on Docker Desktop and troubleshooting, please refer to the [Docker Desktop Documentation](https://docs.docker.com/desktop/).

Happy coding!
