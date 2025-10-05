# Copilot Instructions: Update Wise API Spec

This guide provides step-by-step instructions for updating the Wise API specification and regenerating the client library.

## Prerequisites

- Docker installed and running
- Python 3.9+ installed
- `build` and `twine` packages installed (`pip install build twine`)

## Update Process

### Step 1: Download the Latest API Spec

Download the latest OpenAPI specification from the source repository:

```bash
curl -o api/spec.yaml https://raw.githubusercontent.com/maxploter/wise-openapi/main/openapi/spec.yaml
```

### Step 2: Update Package Version

Update the version number in the file: **api/config.json** - Update `packageVersion` field

Follow semantic versioning (e.g., 0.3.0 → 0.4.0 for minor changes, 0.3.0 → 0.3.1 for patches).

### Step 3: Clean Old Generated Files

Delete the following directories to ensure a clean regeneration:

```bash
rm -rf docs test wise_api_client wise_api_client.egg-info dist
```

### Step 4: Generate the API Client

Run the OpenAPI generator using Docker:

```bash
docker run --rm \
  -v ${PWD}/api:/local/api \
  -v ${PWD}:/local \
  openapitools/openapi-generator-cli generate \
  -i /local/api/spec.yaml \
  -g python \
  -o /local \
  -c /local/api/config.json \
  --git-user-id "maxploter" \
  --git-repo-id "wise-python" \
  --ignore-file-override /local/.openapi-generator-ignore
```

This will regenerate:
- `docs/` - API documentation
- `test/` - Auto-generated tests
- `wise_api_client/` - Python client library
- pyproject.toml - Updated version
- setup.py - Updated version
- other related files

### Step 5: Build the Distribution

Build the package distribution files:

```bash
python -m build
```

This creates distribution files in the `dist/` directory.

### Step 6: Publish to PyPI

Upload the package to PyPI:

```bash
twine upload dist/*
```

You'll be prompted for your PyPI credentials unless you have them configured in `~/.pypirc`.

## Quick Reference Script

Here's a complete script to automate the entire process (except version bumping):

```bash
#!/bin/bash
set -e

# Step 1: Download latest spec
echo "Downloading latest API spec..."
curl -o api/spec.yaml https://raw.githubusercontent.com/maxploter/wise-openapi/main/openapi/spec.yaml

# Step 2: Manual version update required
echo "⚠️  IMPORTANT: Update version in api/config.json, pyproject.toml, and setup.py"
read -p "Press enter after updating the versions..."

# Step 3: Clean old files
echo "Cleaning old generated files..."
rm -rf docs test wise_api_client wise_api_client.egg-info dist

# Step 4: Generate client
echo "Generating API client..."
docker run --rm \
  -v ${PWD}/api:/local/api \
  -v ${PWD}:/local \
  openapitools/openapi-generator-cli generate \
  -i /local/api/spec.yaml \
  -g python \
  -o /local \
  -c /local/api/config.json \
  --git-user-id "maxploter" \
  --git-repo-id "wise-python" \
  --ignore-file-override /local/.openapi-generator-ignore

# Step 5: Build
echo "Building package..."
python -m build

# Step 6: Publish
echo "Publishing to PyPI..."
twine upload dist/*

echo "✅ Done!"
```

## Version Bump Helper

When updating versions, use this pattern:

- **Patch** (0.3.0 → 0.3.1): Bug fixes, minor updates
- **Minor** (0.3.0 → 0.4.0): New features, backward compatible
- **Major** (0.3.0 → 1.0.0): Breaking changes

Current version is tracked in:
- `api/config.json` → `packageVersion`

You don't need to change pyproject.toml and setup.py manually if you run the script:
- `pyproject.toml` → `version`
- `setup.py` → `VERSION`

## Troubleshooting

### Docker Issues
- Ensure Docker is running
- Check volume mount permissions
- Try with absolute paths if relative paths fail

### Build Issues
- Clean `dist/` folder before building
- Ensure all old `.egg-info` directories are removed
- Verify Python virtual environment is activated if using one

### PyPI Upload Issues
- Ensure version number hasn't been used before
- Check PyPI credentials
- Use `twine upload --repository testpypi dist/*` for testing

## Files Modified During Update

Generated/Updated:
- `docs/` (entire directory)
- `test/` (entire directory)  
- `wise_api_client/` (entire directory)
- `dist/` (build artifacts)

Manual Updates Required:
- `api/config.json`
- `pyproject.toml`
- `setup.py`
- `api/spec.yaml` (downloaded)

