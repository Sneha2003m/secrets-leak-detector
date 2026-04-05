#!/bin/bash
echo "Running secrets scan locally..."
if ./gitleaks.exe detect --source . --config .gitleaks.toml --verbose; then
  echo "PASSED: No secrets found!"
else
  echo "FAILED: Secrets detected! Fix before pushing."
  exit 1
fi
