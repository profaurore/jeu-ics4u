param (
    [switch]$r = $true # replace
)

$repertoire = Split-Path -Parent $MyInvocation.MyCommand.Definition
Push-Location $repertoire

ForEach ($rep in (Get-ChildItem -Directory)) {
    $pycache = Join-Path $rep "__pycache__"
    if (Test-Path $pycache) {
        Remove-Item $pycache -Recurse
    }

    $zip = $rep.Name + ".zip"
    if ($r -or (-not(Test-Path -Path $zip))) {
        $rep.Name
        Compress-Archive -Path $rep -DestinationPath $zip -Force
    }
}

Pop-Location
