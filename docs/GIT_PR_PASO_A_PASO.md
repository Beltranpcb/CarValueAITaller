# Git y GitHub: evidencia de colaboración obligatoria

**Todos los miembros deben figurar como autores de commits propios y autores de PRs.** Repartir trabajo en carpetas comunes sin ramas ni PRs no cuenta.

## Flujo de un alumno

```bash
git switch main
git pull --ff-only
git switch -c feature/vision-web   # ejemplo
# editar archivos de su responsabilidad
git status
git add app/vision.py templates/index.html templates/resultado.html
git commit -m "Conectar análisis visual con Cohere"
# realizar al menos otro commit significativo
git push -u origin feature/vision-web
```

En GitHub: **Pull requests → New pull request → base main / compare feature/vision-web → Create**. Poned un título descriptivo y un texto con: archivos, qué funciona, cómo lo habéis probado y qué necesita revisión.

El **revisor es otro integrante**. Lee el diff, comenta al menos una observación concreta y, si la plataforma permite esa acción, aprueba. Después hacer *merge* desde GitHub. En grupos de dos, cada cual revisa el PR de su compañero. En grupos de tres, A revisa B, B revisa C y C revisa A.

**No borrar el histórico de PRs:** hay que dejar visibles los PRs fusionados. No publicar `.env` ni `COHERE_API_KEY`.

## Si hay conflicto de merge

Desde la rama de la funcionalidad:

```bash
git fetch origin
git merge origin/main
# Resolver los marcadores <<<<<<< / ======= / >>>>>>> en el fichero
git add RUTA_DEL_ARCHIVO
git commit -m "Resolver conflicto al integrar main"
git push
```

Revisad el PR antes de fusionar. No utilicéis `--force` ni descartéis cambios de un compañero por accidente.

## Criterios Git (obligatorios)

- Una rama de funcionalidad por integrante (no `main`).
- Al menos **dos commits significativos** propios por integrante.
- Un PR **propio** por integrante (mínimo 2 o 3 PRs según el equipo).
- Revisión cruzada verificable en GitHub.
- PRs fusionados en `main`.
- `ENTREGA_GRUPO.md` con URLs de esos PRs.
