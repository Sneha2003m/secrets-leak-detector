# Secrets Leak Detection Pipeline

![CI](https://github.com/Sneha2003m/secrets-leak-detector/actions/workflows/secret-scan.yml/badge.svg)

DevSecOps CI/CD pipeline that automatically scans every push and Pull Request for leaked secrets and blocks the merge before they reach production.

## Tools Used
- GitHub Actions - CI/CD automation
- gitleaks v8.18.2 - secret scanning engine
- Slack Webhook - real-time alerts
- Custom regex rules - detect DB passwords, JWT secrets, Django keys

## What gets detected
- AWS Access Keys
- GitHub Personal Access Tokens
- Hardcoded database passwords
- JWT secrets
- Django/Flask SECRET_KEY
- Firebase API keys
- 100+ more patterns

## Project Structure
- .github/workflows/secret-scan.yml - main CI/CD pipeline
- .gitleaks.toml - custom scanning rules
- sample-app/app.py - secure vs insecure code demo
- .env.example - environment variables template
