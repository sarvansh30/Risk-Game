# Risk Game Implementation

A Python implementation of the classic Risk board game with both CLI and GUI interfaces, featuring AI opponents using minimax algorithm.

## Project Structure

This repository contains two implementations:

- **Root Directory**: Command-Line Interface (CLI) implementation
- **Risk-Game-Final/**: Graphical User Interface (GUI) prototype implementation

## Features

### CLI Version (Root Directory)
✅ **Completed Features**
- Text-based interface
- Player setup and configuration
- Map with territory connections
- Troop deployment mechanics
- Dice-based combat system
- Turn phase management (Reinforce/Attack/Fortify)
- Continent bonus system

### GUI Version (Risk-Game-Final/)
✅ **Completed Features**
- Graphical User Interface using CustomTkinter
- Interactive map with clickable territories
- Visual representation of armies and ownership
- Player vs AI gameplay
- Real-time territory updates
- Dice roll animations
- AI opponent with minimax algorithm

🤖 **AI Implementation**
- Minimax algorithm with configurable depth
- Strategy evaluation based on:
  - Territory control
  - Continent ownership
  - Army distribution
  - Strategic positioning
- Automated decision-making for:
  - Territory claiming
  - Troop placement
  - Attack moves
  - Fortification

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Running the CLI Version

1. **Navigate to root directory:**
```bash
cd Risk-Game
```

2. **Create virtual environment:**
```bash
python -m venv venv
```

3. **Activate virtual environment:**

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Run the game:**
```bash
python riskProto.py
```

### Running the GUI Version

1. **Navigate to GUI directory:**
```bash
cd Risk-Game-Final
```

2. **Install dependencies (if not already installed):**
```bash
pip install customtkinter pillow
```

3. **Run the game:**
```bash
python gameBoard.py
```

## How to Play

### CLI Version
- Follow the text prompts to make decisions
- Enter commands as instructed
- View territory status through text output

### GUI Version
1. **Initial Setup**: Roll dice to determine who goes first
2. **Territory Claiming**: Click territories to claim them
3. **Game Phases**:
   - **Place Troops**: Click a territory you own and specify troop count (1-3)
   - **Attack**: Select attacking territory, then target, and specify army count
   - **End Turn**: Pass control to the next player
4. **AI Turns**: Watch as the AI automatically makes strategic decisions
5. **Victory**: Game ends when one player controls all territories

## Game Rules

- Players take turns in phases: Reinforce → Attack → Fortify
- Combat is resolved using dice rolls
- Continent control provides bonus armies
- Must leave at least 1 army in each territory
- Can attack with up to 3 armies at once
- Defender rolls up to 2 dice

## Project Files

### Root Directory (CLI)
- `riskProto.py` - Main CLI game file
- `requirements.txt` - Python dependencies
- Supporting game logic files

### Risk-Game-Final/ (GUI)
- `gameBoard.py` - Main entry point
- `mainGame.py` - Game window and UI logic
- `AIPlayer.py` - AI implementation with minimax
- `Player.py` - Player class
- `Game.py` - Game state manager
- `Territory.py` - Territory class
- `Continent.py` - Continent class
- `map.png` - Game board image

## Development Status

### ✅ Working
- Both CLI and GUI implementations functional
- AI opponent with strategic decision-making
- Complete game mechanics (attack, fortify, reinforce)
- Win condition detection

### 🚧 In Progress
- GUI refinements and polish
- Enhanced AI strategies
- Additional visual feedback
- Performance optimizations

### 📋 Planned Features
- Multiple AI difficulty levels
- Save/Load game functionality
- Network multiplayer support
- Custom map editor
- Statistics and game history

## Known Issues

- GUI prototype may require additional testing for edge cases
- AI decision-making can be slow with deep minimax searches
- Some territory adjacencies may need verification

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available for educational purposes.

## Credits

- Original Risk game concept by Albert Lamorisse
- Implementation by Sarvansh
- GUI built with CustomTkinter

## Contact

For questions or suggestions, please open an issue on GitHub.

---

**Note**: The GUI version is a prototype and may undergo significant changes. The CLI version provides a stable alternative for gameplay.