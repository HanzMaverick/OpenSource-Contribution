# Install OpenSource-Contribution / Instalar

## Recommended method / Método recomendado (Windows / PowerShell)

1. Clone the original repository: / Clona el repositorio original:

   ```powershell
   git clone https://github.com/HanzMaverick/OpenSource-Contribution.git
   cd OpenSource-Contribution
   git switch -c feat/v2-community-onboarding
   ```

2. Extract the ZIP and **copy its contents** (including hidden `.github` and `.gitignore`) into this clone's root. Do not copy the enclosing `OpenSource-Contribution-V2` folder as a subfolder. / Extrae el ZIP y **copia el contenido** (incluyendo `.github` y `.gitignore`) a la raíz del clon. No copies la carpeta contenedora.

3. Inspect the changes: / Revisa los cambios:

   ```powershell
   git status
   git diff -- README.md
   ```

4. Commit and push: / Guarda y publica:

   ```powershell
   git add .
   git commit -m "feat: launch beginner-friendly open source V2"
   git push -u origin feat/v2-community-onboarding
   ```

5. Open a PR from `feat/v2-community-onboarding` into `main`, review and merge. / Abre la PR y haz merge tras revisarla.

## GitHub configuration after merge / Configuración después del merge

- In **Settings → General → Features**, enable **Issues** if disabled. / Activa Issues.
- Optionally add labels `question`, `good first issue`, `documentation`. / Agrega las etiquetas si las necesitas. **Important:** the issue form references `question`; create that label or remove the label line in the template to avoid issues creating the form.
- Add repository topics such as `first-contribution`, `first-pull-request`, `good-first-issue`, `git`, `github`, `markdown`, `open-source`.
- Consider adding branch protection to `main` and requiring a review. **Do not require this validation workflow as a universal status check**: its path filter means it doesn't run for unrelated docs-only PRs.
- Test with a new branch/fork that only adds `contributors/your-username.md`.

## Important limits / Límites importantes

- The validator is scoped to beginner PRs touching `contributors/`; it does not auto-merge or certify identities.
- A successful check is **not** an endorsement or promise of GitHub achievements.
- First PRs that edit `contributors/example.md`, change extra files or modify existing profiles will fail intentionally.
- Maintainers should keep workflow/security changes in PRs that do not also add profiles.
