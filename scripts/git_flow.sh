#!/usr/bin/env bash
set -euo pipefail

# Verifica git instalado
command -v git >/dev/null 2>&1 || { echo "Se requiere git instalado."; exit 1; }

# Config por si falta
git config --global init.defaultBranch main >/dev/null 2>&1 || true
git config user.name >/dev/null 2>&1 || git config user.name "Demo User"
git config user.email >/dev/null 2>&1 || git config user.email "demo@example.com"

echo "Inicializando repo..."
rm -rf .git || true
git init

echo "Creando ramas base..."
git checkout -b develop
git checkout -b qa
git checkout -b release.s.agosto
git checkout -b release.1.0.0
git checkout -b main

echo "Volviendo a develop..."
git checkout develop

echo "Añadiendo archivos iniciales (HU-1)..."
git add .
git commit -m "HU-1: versión inicial de comprobación de palíndromos (básica)"

echo "Merge develop -> qa (HU-1)"
git checkout qa
git merge --no-ff develop -m "Merge HU-1: develop -> qa"

echo "Merge qa -> release.s.agosto (HU-1)"
git checkout release.s.agosto
git merge --no-ff qa -m "Merge HU-1: qa -> release.s.agosto"

echo "Merge release.s.agosto -> release.1.0.0 (HU-1)"
git checkout release.1.0.0
git merge --no-ff release.s.agosto -m "Merge HU-1: release.s.agosto -> release.1.0.0"

echo "Tag v1.0.0"
git tag -a v1.0.0 -m "Release 1.0.0 (HU-1)"

echo "Merge release.1.0.0 -> main (HU-1)"
git checkout main
git merge --no-ff release.1.0.0 -m "Merge HU-1: release.1.0.0 -> main"

echo "Aplicando HU-2 en develop..."
git checkout develop

# Simular cambios HU-2 (editar archivo para asegurar nuevo commit)
echo "# HU-2 applied at $(date -u +"%Y-%m-%dT%H:%M:%SZ")" >> CHANGELOG.md
git add CHANGELOG.md
git commit -m "HU-2: mejoras Unicode, stripping de acentos y CLI"

echo "Merge develop -> qa (HU-2)"
git checkout qa
git merge --no-ff develop -m "Merge HU-2: develop -> qa"

echo "Merge qa -> release.s.agosto (HU-2)"
git checkout release.s.agosto
git merge --no-ff qa -m "Merge HU-2: qa -> release.s.agosto"

echo "Merge release.s.agosto -> release.1.0.0 (HU-2)"
git checkout release.1.0.0
git merge --no-ff release.s.agosto -m "Merge HU-2: release.s.agosto -> release.1.0.0"

echo "Tag v1.0.1"
git tag -a v1.0.1 -m "Release 1.0.1 (HU-2)"

echo "Merge release.1.0.0 -> main (HU-2)"
git checkout main
git merge --no-ff release.1.0.0 -m "Merge HU-2: release.1.0.0 -> main"

cat <<'EOF'

✅ Flujo completo ejecutado localmente.
Sugerido para MRs/PRs en remoto (GitHub/GitLab):
1) develop → qa
2) qa → release.s.agosto
3) release.s.agosto → release.1.0.0
4) release.1.0.0 → main

Use:
git remote add origin <URL-DEL-REPO>
git push -u origin --all
git push origin --tags

Luego cree los MRs/PRs en el proveedor remoto.
EOF
