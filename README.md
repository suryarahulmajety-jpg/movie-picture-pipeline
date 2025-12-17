# Movie Picture Pipeline

CI/CD pipeline project for a movie catalog application.

## What's This?

This is a full-stack movie app with automated deployment:
- **Frontend**: React app that shows a list of movies
- **Backend**: Flask API that serves movie data
- **CI/CD**: GitHub Actions workflows handle testing, building, and deploying everything

## Running Apps

- Frontend: http://a3d74404a250c4f2391153cf36e010f9-627109615.us-east-1.elb.amazonaws.com
- Backend API: http://aab9837dffb4d4761bd5f01ff57b026b-1033079496.us-east-1.elb.amazonaws.com/movies

## How It Works

Push code to `main` → GitHub Actions builds Docker images → Pushes to ECR → Deploys to EKS cluster

Pull requests trigger CI checks (lint + test) before merging.

## Workflows

- `frontend-ci.yaml` - Tests frontend on PRs
- `frontend-cd.yaml` - Deploys frontend on merge
- `backend-ci.yaml` - Tests backend on PRs  
- `backend-cd.yaml` - Deploys backend on merge

## Local Development

**Frontend:**
```bash
cd starter/frontend
npm install
REACT_APP_MOVIE_API_URL=http://localhost:5000 npm start
```

**Backend:**
```bash
cd starter/backend
pipenv install
pipenv run serve
```

## Tech Stack

- React + TypeScript
- Flask + Python
- Docker
- Kubernetes (EKS)
- GitHub Actions
- AWS ECR

## Setup

Used Terraform in `setup/terraform` to create the AWS infrastructure. See project docs for details.

## Notes

Remember to tear down AWS resources after project review:
```bash
cd setup/terraform
terraform destroy
```
