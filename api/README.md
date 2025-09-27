## Generating the API client

```shell
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

## Publish

```shell
python -m build
twine upload dist/*
```