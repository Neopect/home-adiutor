# Folder structure

## Root
- `main.py` *Main handler for init program*
- `/SR_TTS`
  - `/Scheduler`
    - `clock.py` *Handles the schedulers timers*
    - `queue.py` *Handles queues of notifications*
  - `/Voice`
    - `recognition.py`
    - `coms.py`
    - `speech.py`
    - `lang.json`
- `/Modules` *Folder holding user installed modules*
  - List of extensions
- `/SysMod` *Folder containing system modules*
  - `/Habits`
    - Routines
    - `habits.py` *Handles the init & communication of habits*
- `/Server`
  - `server.py` *Handles the remote server processing*
- `/Config`
  - `Config.yml` *Basic Config file*

## Progress
Use external API's until able to process locally