#!/usr/bin/env python3
"""Validate PR diffs using a trusted BASE checkout, with no third-party dependencies.

Security: the workflow runs this script from the base SHA (never from the PR);
all head content is treated as data. GitHub metadata identifies the PR author.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE = re.compile(r"contributors/([a-z0-9](?:[a-z0-9-]{0,37}[a-z0-9])?)\.md\Z")
SHA = re.compile(r"[0-9a-fA-F]{40}\Z")


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT, stderr=subprocess.STDOUT)


def fail(reason: str) -> None:
    print(f"\n❌ {reason}", file=sys.stderr)
    sys.exit(1)


def show_changes(changes: list[tuple[str, str]]) -> None:
    print("📂 Files changed in this PR (compared with main):", flush=True)
    for status, path in changes:
        print(f"   {status:2} {path}", flush=True)


def main() -> None:
    base = os.environ.get("BASE_SHA", "")
    head = os.environ.get("HEAD_SHA", "")
    author = os.environ.get("PR_AUTHOR", "").lower()
    owner = os.environ.get("REPO_OWNER", "").lower()
    if not SHA.fullmatch(base) or not SHA.fullmatch(head):
        fail("Configuration error: missing valid BASE_SHA / HEAD_SHA. Contact the maintainer.")
    if not author or not owner:
        fail("Configuration error: missing PR_AUTHOR / REPO_OWNER. Contact the maintainer.")
    try:
        data = git("diff", "--no-renames", "--name-status", "-z", base, head)
    except subprocess.CalledProcessError:
        fail("Cannot compare PR changes. Re-run the job or contact the maintainer.")
    tokens = [x.decode("utf-8", "replace") for x in data.split(b"\0") if x]
    if len(tokens) % 2:
        fail("Cannot read the PR diff. Contact the maintainer.")
    changes = [(tokens[i], tokens[i + 1]) for i in range(0, len(tokens), 2)]
    show_changes(changes)
    if not changes:
        print("✅ No file changes to validate.")
        return

    # GitHub owns PR author metadata. This exception is ONLY for the repository owner.
    # It is not an authorization to merge: branch protections + manual review remain essential.
    if author == owner:
        print("✅ Repository owner PR: beginner-only restrictions do not apply. Manual review still required.")
        return

    if any(not status.startswith(("A", "M", "D")) for status, _ in changes):
        fail("Unsupported file change type. Please open an Issue for help. / Tipo de cambio no admitido.")

    profile_path = f"contributors/{author}.md"
    legacy_path = f"contributors/{author}"
    if not PROFILE.fullmatch(profile_path):
        fail("Your GitHub username cannot be used in the filename by this validator. Open an Issue. / Abre un Issue.")

    statuses = {(status, path) for status, path in changes}
    # For safety we never accept edits to another person's profile, workflows, or code.
    # The legacy rename is allowed only if the old path belongs to this PR author.
    permitted = [
        {("A", profile_path)},
        {("M", profile_path)},  # Author correcting their own existing profile
        {("D", legacy_path), ("A", profile_path)},  # Fix missing .md in an existing merged profile
    ]
    if statuses not in permitted or len(changes) != len(statuses):
        # Specific onboarding hints are easier to understand than a generic diff error.
        bare_added = ("A", legacy_path) in statuses
        if bare_added:
            fail(
                f"Your file is missing the .md extension: {legacy_path}\n"
                f"Rename it to {profile_path} in THE SAME pull request and push your change.\n"
                f"ES: Falta la extensión .md. Renombra el archivo a {profile_path} "
                "en LA MISMA Pull Request. ¡No necesitas abrir otra!"
            )
        if any(p.startswith("contributors/") and not p.endswith(".md") for _, p in changes):
            fail(
                f"Please use {profile_path} (including .md). Only your own profile can be changed.\n"
                f"ES: Usa {profile_path} (con .md). No modifiques perfiles de otros usuarios."
            )
        fail(
            "This beginner PR must add or update ONLY your own Markdown profile, "
            f"{profile_path}. Do not change README, scripts, workflows or other profiles.\n"
            "If you are fixing a filename, make the change in the SAME PR; "
            "check the changed files tab for extras.\n"
            "ES: Esta PR solo puede agregar o actualizar TU perfil .md. "
            "Corrige el archivo en la MISMA PR y revisa 'Files changed'. "
            "Para mantenimiento, contacta al dueño del repositorio."
        )

    try:
        body = git("show", f"{head}:{profile_path}").decode("utf-8")
    except (subprocess.CalledProcessError, UnicodeDecodeError):
        fail(f"Cannot read {profile_path} as UTF-8 Markdown. / No se pudo leer el archivo.")

    if not 80 <= len(body) <= 6000:
        fail("Your introduction needs 80–6,000 characters. / Tu presentación debe tener 80–6000 caracteres.")
    if not re.search(r"(?m)^#\s+\S", body):
        fail("Add a Markdown title starting with '# '. / Agrega un título que comience con '# '.")
    # Username matching is based on the authenticated GitHub PR author, not arbitrary PR content.
    url = re.compile(r"https://github\.com/" + re.escape(author) + r"(?=[/\s)\]#?]|$)", re.IGNORECASE)
    if not url.search(body):
        fail(f"Add your GitHub URL https://github.com/{author} / Agrega el enlace a tu perfil.")
    if "github.com/example" in body.lower() or "sample profile" in body.lower():
        fail("Replace example placeholder values. / Reemplaza los datos de ejemplo.")

    print(f"✅ Profile validated: {profile_path}. Ready for maintainer review / Listo para revisión.")


if __name__ == "__main__":
    main()
