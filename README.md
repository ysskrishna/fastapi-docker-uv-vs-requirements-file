# FastAPI Docker UV vs Requirements File Comparison

[![License: MIT](https://img.shields.io/github/license/ysskrishna/fastapi-docker-uv-vs-requirements-file)](https://github.com/ysskrishna/fastapi-docker-uv-vs-requirements-file/blob/main/LICENSE) [![Author site](https://img.shields.io/badge/author-ysskrishna.space-informational)](https://ysskrishna.space)


A FastAPI starter project with user management features, containerized using Docker in two distinct setups. One version uses the traditional requirements.txt with pip, while the other leverages the modern uv package manager for faster and more reproducible Python dependency management. 


## Features

- FastAPI backend with user management endpoints
- SQLite database integration
- CORS middleware enabled
- Docker containerization
- Health checks for both services

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:
```bash
git clone <repository-url>
cd fastapi-docker-uv-vs-requirements-file
```

2. Create a `.env` file:
```bash
cp .env.sample .env
```
Then edit the `.env` file with your configuration values.

3. Start the services:
```bash
docker-compose up --build
```

The services will be available at:
- Requirements file version: http://localhost:8081
- UV version: http://localhost:8082


## Project Structure

```
.
├── core/                        # Core functionality
├── models/                      # Database models
├── routers/                     # API routes
├── Dockerfile.uv                # Dockerfile using uv
├── Dockerfile.requirementsfile  # Dockerfile using requirements.txt
├── docker-compose.yml           # Docker Compose configuration
├── main.py                      # FastAPI application entry point
├── requirements.txt             # Python dependencies
├── pyproject.toml               # Project metadata
├── .env.sample                 # Sample environment variables
└── .env                        # Environment variables (create from .env.sample)
```

## Comparison

The project demonstrates two different approaches to Python dependency management:

1. **Requirements File Approach**:
   - Uses traditional `requirements.txt`
   - Installs dependencies using pip
   - Port: 8081

2. **UV Approach**:
   - Uses modern `uv` package manager
   - Faster dependency resolution
   - Better caching
   - Port: 8082

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Built and maintained by

FastAPI Docker UV vs Requirements File Comparison is built and maintained by:

| | Name | GitHub | Role |
|---|------|--------|------|
| <img src="https://github.com/ysskrishna.png?size=120" width="60" height="60" alt="Y. Siva Sai Krishna"> | **Y. Siva Sai Krishna** | [@ysskrishna](https://github.com/ysskrishna) | Creator |

## Support

If you find this project helpful:

- ⭐ Star the repository
- 🐛 [Report issues](https://github.com/ysskrishna/fastapi-docker-uv-vs-requirements-file/issues)
- 🔀 Submit pull requests
- 💝 [Sponsor on GitHub](https://github.com/sponsors/ysskrishna)

## License

MIT © [Y. Siva Sai Krishna](https://github.com/ysskrishna) — see [LICENSE](LICENSE) for details.

---

<p align="left">
  <a href="https://github.com/ysskrishna">Author's GitHub</a> •
  <a href="https://linkedin.com/in/ysskrishna">Author's LinkedIn</a> •
  <a href="https://ysskrishna.space">Author's site</a> •
  <a href="https://github.com/ysskrishna/fastapi-docker-uv-vs-requirements-file/issues">Report Issues</a>
</p>
