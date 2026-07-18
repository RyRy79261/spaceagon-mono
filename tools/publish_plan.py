#!/usr/bin/env python3
"""Resolve the requested app into a GitHub Actions publish matrix.

Publishing is manual only (workflow_dispatch): the matrix contains exactly the
requested app, whether it's a first publish or an update.

Target repo resolution: --repo input > [publish].repo in tildagon.toml >
<owner>/spaceagon-<app-with-dashes>.

Env: INPUT_APP, INPUT_REPO, OWNER, GITHUB_OUTPUT.
"""

import json
import os
import sys
from pathlib import Path

import tomllib

ROOT = Path(__file__).resolve().parent.parent


def load(app):
    return tomllib.loads((ROOT / "apps" / app / "tildagon.toml").read_text())


def target_repo(app, data, override=None):
    return (
        override
        or data.get("publish", {}).get("repo")
        or f"{os.environ['OWNER']}/spaceagon-{app.replace('_', '-')}"
    )


def main():
    app = os.environ["INPUT_APP"].strip()
    if not (ROOT / "apps" / app).is_dir():
        sys.exit(f"no such app: {app}")
    data = load(app)
    repo = target_repo(app, data, os.environ.get("INPUT_REPO", "").strip() or None)
    entries = [{"app": app, "repo": repo, "version": data["metadata"]["version"]}]

    print("matrix:", json.dumps(entries, indent=2))
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a") as handle:
            handle.write(f"matrix={json.dumps(entries)}\n")


if __name__ == "__main__":
    main()
