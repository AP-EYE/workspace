$ErrorActionPreference = 'Stop'
$image = 'wger/server@sha256:1c5789b93bfe5eed0b7287255782d9177027b255de2b22b59f511a693a48db04'
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$packageDir = Split-Path -Parent $scriptDir
$logPath = Join-Path $packageDir 'evidence/wger-2.7-template-tests.log'

docker run --rm --network none --name ap-eye-public-normal-eval `
  --entrypoint sh `
  -e DJANGO_DB_ENGINE=django.db.backends.sqlite3 `
  -e DJANGO_DB_DATABASE=/tmp/ap-eye-public-normal.sqlite3 `
  -e DJANGO_DEBUG=True `
  $image `
  -c 'python3 manage.py test wger.manager.tests.test_templates --verbosity 1' 2>&1 |
  Tee-Object -FilePath $logPath

if ($LASTEXITCODE -ne 0) {
  throw "wger template test failed with exit code $LASTEXITCODE; see $logPath"
}
