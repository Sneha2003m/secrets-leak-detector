
# Secrets Leak Detection Pipeline

DevSecOps CI/CD pipeline that automatically scans every push and Pull Request for leaked secrets — API keys, passwords, tokens — and blocks the merge before they reach production.

## Tools Used
- GitHub Actions — CI/CD automation
- gitleaks — secret scanning engine
- Slack Webhook — real-time alerts
- Custom regex rules — company-specific patterns

## How it works
1. Developer pushes code
2. GitHub Actions triggers automatically
3. gitleaks scans all files and git history
4. If secrets found → pipeline fails + Slack alert sent
5. If clean → pipeline passes, safe to merge

## Project Structure
- `.github/workflows/secret-scan.yml` — main pipeline
- `.gitleaks.toml` — custom scanning rules
- `sample-app/app.py` — demo showing good practices
- `.env.example` — environment variables template
