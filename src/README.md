# FastAPI for Python Coders (Quarto Book)

This repository is ready for GitHub-hosted Quarto publishing.

## What is included

- Quarto book config: `_quarto.yml`
- Home page: `index.qmd`
- Chapters: `part-01.qmd` to `part-04.qmd`
- GitHub Actions publish workflow: `.github/workflows/publish.yml`

## How to publish on GitHub (no local Quarto install)

1. Create a new GitHub repository.
2. Push this folder to the `main` branch.
3. In GitHub, open `Settings -> Pages`.
4. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
5. Select branch `gh-pages` and folder `/ (root)`.
6. Push to `main` (or run workflow manually from **Actions**) to publish.

GitHub Actions will build and deploy the Quarto book automatically.
