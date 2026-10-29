# Automated CI/CD Pipeline with GitHub Actions

[![Python CI-CD Pipeline](https://github.com/vinitha0173-droid/github_actions_cicd/actions/workflows/ci-cd.yml/badge.svg?branch=main)](https://github.com/vinitha0173-droid/github_actions_cicd/actions/workflows/ci-cd.yml)

## Project Overview

This project implements an automated Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub Actions. It automates code linting, unit testing, Docker image building, and secure image publishing.

## Technologies Used

- Python 3.12
- GitHub Actions
- Flake8
- Pytest
- Docker
- GitHub Container Registry (GHCR)

## Features

- Automated Python code linting.
- Automated unit testing.
- Docker image building.
- Secure Docker image publishing.
- Automatic workflow execution on pushes and pull requests targeting the main branch.
- Workflow status monitoring through GitHub Actions.

## Project Structure

```text
.github/
└── workflows/
    └── ci-cd.yml
app.py
test_app.py
requirements.txt
Dockerfile
README.md
```

## CI/CD Workflow

1. **Linting:** Checks Python code using Flake8.
2. **Testing:** Executes automated unit tests using Pytest.
3. **Docker Build:** Builds a Docker image after linting and testing succeed.
4. **Docker Push:** Publishes the image to GitHub Container Registry when code is pushed to the main branch.

## Run Locally

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Run unit tests:

```bash
python -m pytest -v
```

Build the Docker image:

```bash
docker build -t trustlens-cicd:latest .
```

## Security

The pipeline uses GitHub Actions permissions and the automatically generated `GITHUB_TOKEN` to authenticate with GitHub Container Registry. Credentials are not hardcoded in the source code.

## Results

The workflow automatically checks code quality, runs unit tests, and builds the Docker image. Successful push-triggered runs publish the image to GHCR.

Workflow results and execution logs are available in the GitHub Actions tab.
