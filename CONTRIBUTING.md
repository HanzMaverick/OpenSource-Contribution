# 🤝 Contributing / Cómo contribuir

Welcome! / ¡Bienvenido!

## First-time contribution / Primera contribución

Create **one new Markdown file** inside `contributors/` named after your GitHub username in **lowercase**: `your-username.md`.

Crea **un archivo Markdown nuevo** en `contributors/` con tu usuario de GitHub en **minúsculas**: `tu-usuario.md`.

1. Fork this repository / Haz fork del repositorio.
2. Copy [`contributors/example.md`](contributors/example.md) into `contributors/your-username.md` in your fork (do not change `example.md`).
3. Replace the sample text with your own information; include your GitHub profile URL.
4. Commit your file and open a PR to `HanzMaverick/OpenSource-Contribution:main`.
5. Respond to review comments and wait for a maintainer to merge.

## Format / Formato

Your file must / Tu archivo debe:

- Be a new `.md` file in `contributors/` (one file per PR). / Ser un nuevo `.md` en `contributors/` (uno por PR).
- Use a lowercase GitHub username as filename (`a-z`, `0-9`, `-`; 2–39 chars, no leading/trailing hyphens). / Usar el usuario de GitHub en minúsculas como nombre de archivo.
- Contain `# ` as a Markdown heading and `https://github.com/` followed by your profile username. / Contener un encabezado `# ` y un enlace a tu perfil de GitHub.
- Contain between 80 and 6,000 characters. / Tener entre 80 y 6,000 caracteres.
- Be respectful, original, and free of personal contact details you do not want public. / Ser respetuoso, original y sin datos personales que no quieras publicar.

For beginner PRs, the validator rejects changes to existing files or files outside `contributors/`. Maintainers may make other changes in separate PRs that don't touch `contributors/`.

Para las PR de principiantes, el validador rechaza cambios a archivos existentes o fuera de `contributors/`. Los mantenedores pueden hacer cambios de mantenimiento en PR separadas que no modifiquen `contributors/`.

## Suggested template / Plantilla

```md
# Your display name

- **GitHub:** https://github.com/your-username
- **Country / País:** Optional / Opcional
- **Learning / Aprendiendo:** Git, GitHub, Markdown

## About me / Sobre mí

I'm practicing my first open-source Pull Request! / ¡Estoy practicando mi primera Pull Request!
```

## What happens after opening a PR? / ¿Qué sucede después?

The GitHub Action checks the format. A green check means the automated format rules passed — **not** that the PR is automatically approved. A maintainer reviews and decides whether to merge.

La GitHub Action verifica el formato. Una marca verde solo indica que la validación automática pasó; **no** significa aprobación automática. Un mantenedor revisará la PR y decidirá si se integra.

## Safe collaboration / Colaboración segura

No spam, advertising, impersonation, harassment, credentials or sensitive personal data. See [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

No spam, publicidad, suplantación, acoso, credenciales ni información personal sensible. Consulta [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## Profile credits / Créditos del perfil

GitHub's contribution graph and achievements are based on GitHub's rules, including whether activity is attributed to your account. Participation does not guarantee a badge or green square.

La gráfica de contribuciones y los logros de GitHub dependen de sus reglas. Participar no garantiza un badge ni un cuadro verde.

## 🛠️ Fixing a failed check / Corregir un error

**You do not need to close your PR or create a new one. / No necesitas cerrar tu PR ni crear otra.**

### ❌ Missing `.md` / Falta `.md`

If you created `contributors/your-username` (without the extension), rename it to `contributors/your-username.md` **on the same PR branch** and commit/push the change. GitHub will check the **full difference against `main`** again. If the file was already merged without `.md`, the validator also permits a one-to-one correction of *your own* profile.

Si creaste `contributors/tu-usuario` sin extensión, renómbralo a `contributors/tu-usuario.md` **en la misma rama de la PR**; guarda el cambio con commit y push. GitHub volverá a revisar la diferencia total contra `main`. Si el archivo sin extensión ya había sido integrado, también puedes corregir **tu propio** perfil con un renombre.

> In GitHub web: open your file on your fork and PR branch → click Edit (pencil) → change the name to end in `.md` → Commit changes to the **same branch**. If GitHub cannot rename it, add the corrected file and delete only your original file in the same branch.
>
> En la web de GitHub: abre el archivo de tu fork en la rama de la PR → Editar (lápiz) → agrega `.md` al nombre → **Commit changes** en la misma rama. Si no puedes renombrarlo, crea el archivo correcto y elimina solo tu archivo original en esa misma rama.

### ❌ "Only your own profile" / "Solo tu perfil"

Open the PR's **Files changed / Archivos cambiados** tab. For a first PR, it should show only `contributors/your-github-username.md`. Revert unrelated changes in the same branch. Files must match **your exact GitHub username**, written in lowercase.

Revisa **Files changed / Archivos cambiados** en la PR. Solo debe aparecer `contributors/tu-usuario-de-github.md`. Revierte cambios a otros archivos en la misma rama. Tu nombre de archivo debe coincidir con **tu usuario real de GitHub**, en minúsculas.

### ❌ Too short / missing title / wrong profile link

Keep 80–6,000 characters, add a heading `# My name` and include `https://github.com/your-username`. Replace placeholders in the example. After each commit/push on the PR branch, Actions runs again. A green check means *format accepted*, not *automatically merged*.

Usa 80–6000 caracteres, un título `# Mi nombre` y tu enlace `https://github.com/tu-usuario`. Reemplaza los ejemplos. Después de cada commit/push a la rama de tu PR, Actions se ejecuta nuevamente. Una marca verde valida el *formato*, no aprueba la PR automáticamente.
