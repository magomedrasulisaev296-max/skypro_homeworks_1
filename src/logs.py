import logging
from pathlib import Path
import os

log_dir = Path("logs_output")
log_dir.mkdir(parents=True, exist_ok=True)

# 2. Потом создаем логгер
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

log_file = log_dir / f"{__name__}.log"
file_handler = logging.FileHandler(log_file)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)
