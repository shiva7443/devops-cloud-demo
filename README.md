# DevOps and Cloud Integration Demonstrator

An automated workflow demo using **Git/GitHub + Docker**.

## Flow
Developer -> `git push` -> GitHub Actions (test -> build Docker image -> push to GHCR -> deploy to cloud) -> Live app

## Run locally
```bash
docker build -t demo-app .
docker run -p 8080:8080 demo-app
# open http://localhost:8080
```

## Pipeline (.github/workflows/ci.yml)
1. **test** - runs pytest
2. **build-and-push** - builds the Docker image and pushes it to GitHub Container Registry
3. **deploy** - triggers a cloud deploy (Render deploy hook, optional)

## Demo steps
1. Edit `VERSION` in `app.py`
2. `git commit` and `git push`
3. Watch the **Actions** tab turn green
4. Refresh the live URL to see the change
