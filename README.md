# Tower Defense

A desktop tower-defense game built with Python and Pygame. Place and upgrade
different towers, manage your resources, and defend the path across 13 waves of
zombies, ghosts, and wizards.

## Play on Replit

### [▶ Run Tower Defense on Replit](https://replit.com/@DanielWang75/Tower-Defense)

Open the project, click **Run**, and play the game in the **VNC** pane.

![Tower Defense title screen running on Replit](docs/tower-defense-demo.webp)

## Run locally

Python 3.10 or newer is recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 run.py
```

On Windows, activate the environment with `.venv\\Scripts\\activate` instead.

## How to play

- Select a tower from the sidebar, then click to place it away from the enemy path.
- Use the play/pause button to start or pause a wave.
- Click a placed tower to upgrade or sell it.
- Survive all 13 waves without losing all 10 lives.
