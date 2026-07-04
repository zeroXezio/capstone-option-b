Write-Output "=== VALIDANDO ENTREGABLES DEL PROYECTO ==="
$status = 0

# Validación de Fase 0 & Documentación Base
if (-not (Test-Path "session-log.md")) {
    Write-Output "❌ Error: session-log.md no ha sido creado."
    $status = 1
} else {
    Write-Output "✅ session-log.md detectado."
}

if (-not (Test-Path "analysis-report.md")) {
    Write-Output "⚠️ Alerta: analysis-report.md aún no se ha inicializado."
}

if ($status -eq 0) {
    Write-Output "🎉 Todo en orden para la fase actual."
} else {
    Write-Output "🛑 Corrige los elementos faltantes antes de continuar."
}

exit $status
