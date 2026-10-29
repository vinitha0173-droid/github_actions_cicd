# Automated CI/CD Pipeline with GitHub Actions

![CI/CD Pipeline](https://github.com/OWNER/REPOSITORY/actions/workflows/ci-cd.yml/badge.svg)

An automated Continuous Integration and Continuous Deployment (CI/CD) pipeline for a Python application using GitHub Actions, Flake8, Pytest, Docker, and GitHub Container Registry (GHCR).

The pipeline automatically checks code quality, runs unit tests, builds a Docker image, and publishes the image securely to GHCR when changes are pushed to the main branch.

## Table of Contents

- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [CI/CD Workflow](#cicd-workflow)
- [Workflow Triggers](#workflow-triggers)
- [Running the Application Locally](#running-the-application-locally)
- [Running Unit Tests](#running-unit-tests)
- [Building the Docker Image](#building-the-docker-image)
- [Container Registry](#container-registry)
- [Security Practices](#security-practices)
- [Expected Results](#expected-results)
- [Future Enhancements](#future-enhancements)
- [Author](#author)

## Project Overview

Continuous Integration and Continuous Deployment help automate software testing, packaging, and delivery.

This project demonstrates a complete automated workflow for a Python application. Whenever code is pushed to the main branch or a pull request is created for main, GitHub Actions executes the configured pipeline.

The pipeline validates the Python source code, checks application behavior through automated tests, and builds a Docker image. For pushes to the main branch, the image is also published to GitHub Container Registry.

## Objectives

- Automate Python code quality checks.
- Execute unit tests on every relevant code change.
- Build a portable Docker image.
- Publish container images securely using GitHub Actions.
- Identify errors early in the development process.
- Maintain visible workflow logs and status checks.

## Key Features

### 1. Automated Code Linting

Flake8 checks Python files for common style violations and potential code-quality issues.

### 2. Automated Unit Testing

Pytest executes automated tests to verify the behavior of application functions.

### 3. Docker Image Build

Docker packages the application and its dependencies into a container image.

### 4. Secure Image Publishing

GitHub Actions uses the automatically provided `GITHUB_TOKEN` to authenticate with GHCR. The workflow has the required package permission.

### 5. Conditional Deployment

The image is published when the workflow runs on a push event. Pull requests run validation and build the image without publishing it.

### 6. Workflow Status Badge

The README displays the GitHub Actions workflow status so repository visitors can quickly check the latest workflow status.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Application development |
| Flake8 | Code linting |
| Pytest | Automated unit testing |
| Docker | Containerization |
| GitHub Actions | CI/CD automation |
| GitHub Container Registry | Container image storage |
| Git and GitHub | Version control and collaboration |

## Project Structure

```text
github-actions-cicd/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

### File Description

- `app.py` — contains the Python application functions.
- `test_app.py` — contains automated unit tests.
- `requirements.txt` — lists the Python packages required for linting and testing.
- `Dockerfile` — defines the environment and instructions to package the application.
- `.github/workflows/ci-cd.yml` — defines the automated pipeline.
- `README.md` — documents the project and its usage.

## CI/CD Workflow

The pipeline consists of three jobs.

### Stage 1: Lint Python Code

- Checks out the repository.
- Sets up Python 3.12.
- Installs Flake8.
- Runs lint checks on `app.py` and `test_app.py`.

Command:

```bash
python -m flake8 app.py test_app.py
```

### Stage 2: Run Unit Tests

- Checks out the repository.
- Sets up Python 3.12.
- Installs the packages listed in `requirements.txt`.
- Executes the automated tests using Pytest.

Command:

```bash
python -m pytest -v
```

### Stage 3: Build and Push Docker Image

- Runs after the lint and test jobs succeed.
- Sets up Docker Buildx.
- Builds the application image.
- Authenticates with GHCR for push events.
- Publishes the image to GHCR when triggered by a push to the main branch.

The image is tagged using the following format:

```text
ghcr.io/OWNER/REPOSITORY:latest
```

The workflow converts the repository name to lowercase to comply with container registry naming requirements.

## Workflow Triggers

The workflow runs on these events:

- **Push:** When changes are pushed to the `main` branch.
- **Pull request:** When a pull request targets the `main` branch.

Pull requests run linting, unit testing, and Docker image building. They do not publish the image.

## Running the Application Locally

### Prerequisites

Install Python 3.12 or a compatible version and Git.

Clone the repository:

```bash
git clone https://github.com/OWNER/REPOSITORY.git
cd REPOSITORY
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Expected output:

```text
Hello, TrustLens!
Sum: 30
Is 8 even? True
```

## Running Unit Tests

Execute the following command from the repository root:

```bash
python -m pytest -v
```

The tests validate the number addition function, even-number checking function, and greeting function.

A successful test run reports three passing test functions.

## Building the Docker Image

Ensure Docker Desktop or Docker Engine is installed and running.

Build the image locally:

```bash
docker build -t trustlens-cicd:latest .
```

Run the container:

```bash
docker run --rm trustlens-cicd:latest
```

The container executes the Python application and prints its output.

## Container Registry

The workflow publishes images to GitHub Container Registry (GHCR).

After a successful push-triggered workflow, the image can be accessed using:

```bash
docker pull ghcr.io/OWNER/REPOSITORY:latest
```

Replace `OWNER/REPOSITORY` with the lowercase GitHub owner and repository name.

The package may initially be private. Adjust its visibility in the GitHub package settings if public access is required.

## Security Practices

- Uses the automatically generated `GITHUB_TOKEN` instead of a manually embedded registry password.
- Limits workflow permissions to repository read access and package publishing.
- Does not store credentials directly in the source code.
- Does not publish Docker images from pull request runs.
- Keeps workflow execution logs available for troubleshooting and verification.

## Expected Results

A successful workflow should demonstrate:

- Flake8 lint checks passing.
- Pytest unit tests passing.
- Docker image building successfully.
- Docker image publishing successfully on eligible push events.
- A green GitHub Actions workflow status badge.

Workflow results and detailed execution logs are available in the repository's **Actions** tab.

## Future Enhancements

- Add code coverage reports.
- Introduce dependency vulnerability scanning.
- Add Docker image vulnerability scanning.
- Add versioned Docker image tags.
- Deploy the application to a cloud environment.
- Add branch protection and required status checks.

## Author

**Project:** Automated CI/CD Pipeline with GitHub Actions

**Repository:** [View Source Code](https://github.com/OWNER/REPOSITORY)
