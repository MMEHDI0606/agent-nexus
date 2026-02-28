[CmdletBinding()]
param(
  [string]$TargetPath = ".agents/skills",
  [switch]$Preview,
  [switch]$ForceGithubFallback
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$ProjectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $ProjectRoot

function Invoke-InstallCommand {
  param(
    [Parameter(Mandatory = $true)][string]$Command
  )

  Write-Host "Trying: $Command"
  if ($Preview) {
    return $true
  }

  $global:LASTEXITCODE = 0
  Invoke-Expression $Command
  if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed: $Command" -ForegroundColor Yellow
    return $false
  }

  Write-Host "Success: $Command"
  return $true
}

$resolvedTarget = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($TargetPath)
if (-not (Test-Path $resolvedTarget)) {
  New-Item -ItemType Directory -Force -Path $resolvedTarget | Out-Null
}

Write-Host "Installing Antigravity Awesome Skills into: $resolvedTarget"

$installed = $false
if (-not $ForceGithubFallback) {
  $installed = Invoke-InstallCommand -Command "npx -y antigravity-awesome-skills --path `"$resolvedTarget`""
}

if (-not $installed) {
  $installed = Invoke-InstallCommand -Command "npx -y github:sickn33/antigravity-awesome-skills --path `"$resolvedTarget`""
}

if (-not $installed) {
  throw "Antigravity installation failed for all installer paths."
}

Write-Host "Antigravity installation complete."
