# spaceagon-mono

A monorepo of apps for the **EMF Camp Spaceagon badge** (the 2026 front-board upgrade of
the hexagonal Tildagon badge), plus shared libraries — notably a generic input-abstraction
layer for assigning functionality to buttons/joystick/touch and composing apps from reusable
parts.

> **Status: research phase complete; awaiting architecture sign-off.**
> Read [`docs/PROPOSAL.md`](docs/PROPOSAL.md) — that's the decision document.

## What is this badge?

- Hexagonal ESP32-S3 badge running **Tildagon OS** (MicroPython 1.28). Apps are plain
  Python — subclass `App`, implement `update(delta)` / `draw(ctx)`, export `__app_export__`.
- The 2026 **Spaceagon** front board adds: 6 buttons (A–F), a 5-way joystick, a 12-pad
  capacitive touch ring, 2 proximity sensors, and a compass — all on top of the 2024 base
  board (round 240×240 display, 18 usable RGB LEDs, IMU, WiFi/BLE/ESP-NOW, dual USB-C).
- Apps publish to the [official app directory](https://apps.badge.emfcamp.org/) via GitHub
  repos with the `tildagon-app` topic (one repo per app — see the publishing research for
  how this monorepo deals with that).

## Research docs (start here)

| Doc | Contents |
|---|---|
| [docs/PROPOSAL.md](docs/PROPOSAL.md) | Proposed architecture & stack (decision doc) |
| [docs/PROPOSAL-2-template-devkit-cat-app.md](docs/PROPOSAL-2-template-devkit-cat-app.md) | **Template repo, dev kit, CI/CD, theming, flags + the Cat & Yarn example app** |
| [docs/research/09-cat-app-feasibility.md](docs/research/09-cat-app-feasibility.md) | Feasibility research behind Proposal 2 |
| [docs/research/01-hardware.md](docs/research/01-hardware.md) | The hardware, chip by chip |
| [docs/research/02-app-model.md](docs/research/02-app-model.md) | How apps are written (App class, ctx, UI, eventbus) |
| [docs/research/03-input.md](docs/research/03-input.md) | Buttons/joystick/touch — full input API |
| [docs/research/04-sensors-and-peripherals.md](docs/research/04-sensors-and-peripherals.md) | IMU, compass, LEDs, power, radio |
| [docs/research/05-toolchain.md](docs/research/05-toolchain.md) | Simulate, sideload, debug, flash |
| [docs/research/06-publishing.md](docs/research/06-publishing.md) | App store mechanics + the monorepo verdict |
| [docs/research/07-ecosystem.md](docs/research/07-ecosystem.md) | Repos to learn from, community channels |
| [docs/research/08-verification-log.md](docs/research/08-verification-log.md) | How claims were adversarially verified + tooling recency audit |

## Upstream links

- Docs: <https://tildagon.badge.emfcamp.org/> · App directory: <https://apps.badge.emfcamp.org/>
- Firmware + simulator: <https://github.com/emfcamp/badge-2024-software>
- Official 2026 input example: <https://github.com/emfcamp/badge-2026-apps-spaceagon-test>
- Community: Matrix `#badge:emfcamp.org` · IRC `#emfcamp-badge` (libera) · badge@emfcamp.org
