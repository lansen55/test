# test
This repository contains a small example project.

## Dodgeball Game

`dodgeball.py` is a short Pygame script where you move a blue square to
avoid falling red balls. Each ball that passes adds to your score. The
game ends when your square collides with any ball.

### Running the Game

1. (Optional) Run `./setup_env.sh` to create a virtual environment and
   install dependencies listed in `requirements.txt`.
2. If you prefer manual installation, make sure the `pygame` package is
   installed (`pip install pygame`).
3. Execute the script:

   ```bash
   python dodgeball.py
   ```

If `pygame` isn't installed, the game will exit immediately with a brief
message explaining how to install it or use the provided `setup_env.sh`
script.

Use the arrow keys to dodge the balls. A score counter appears in the
top-left corner. When the game ends, a short message is shown before the
window closes.
