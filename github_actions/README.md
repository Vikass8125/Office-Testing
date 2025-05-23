# FastAPI Docker CI/CD Project

This is a simple FastAPI application with Docker and GitHub Actions CI/CD pipeline.

## Project Structure
- `main.py`: FastAPI application with a simple "Hello World" endpoint
- `requirements.txt`: Python dependencies
- `Dockerfile`: Container configuration
- `.github/workflows/docker-build.yml`: GitHub Actions workflow

## Local Development

1. Build the Docker image:
```bash
docker build -t fastapi-app .
```

2. Run the container:
```bash
docker run -p 8000:8000 fastapi-app
```

3. Access the API:
- Open your browser and go to `http://localhost:8000`
- Or use curl: `curl http://localhost:8000`

## CI/CD Pipeline

The project uses GitHub Actions to automatically:
1. Build the Docker image when code is pushed to the main branch
2. Push the image to GitHub Container Registry (ghcr.io)

To use the pipeline:
1. Push your code to GitHub
2. The workflow will automatically trigger on push to main branch
3. The Docker image will be built and pushed to ghcr.io

## API Endpoints

- `GET /`: Returns a "Hello World" message 