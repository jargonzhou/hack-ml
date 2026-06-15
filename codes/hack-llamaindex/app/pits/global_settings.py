"""
This contains application settings, configurations, and eventually Streamlit’s secrets for deployment. 
It centralizes parameters for easy management and updates
"""

from pathlib import Path


PITS_ROOT = ".pits/"


LOG_FILE = PITS_ROOT + "session_data/user_actions.log"
SESSION_FILE = PITS_ROOT + "session_data/user_session_state.yaml"  # pyyaml
CACHE_FILE = PITS_ROOT + "cache/pipeline_cache.json"
CONVERSATION_FILE = PITS_ROOT + "cache/chat_history.json"
QUIZ_FILE = PITS_ROOT + "cache/quiz.csv"
SLIDES_FILE = PITS_ROOT + "cache/slides.json"
STORAGE_PATH = PITS_ROOT + "ingestion_storage"
INDEX_STORAGE = PITS_ROOT + "index_storage"


QUIZ_SIZE = 5
ITEMS_ON_SLIDE = 4


def touch_storage():
  def touch_file(p):
    if not p.exists():
      p.parent.mkdir(parents=True, exist_ok=True)
      p.touch(exist_ok=True)

  def mkdir_p(p):
    if not p.exists():
      p.mkdir(parents=True, exist_ok=True)

  log_file = Path(LOG_FILE)
  session_file = Path(SESSION_FILE)
  cache_file = Path(CACHE_FILE)
  converstaion_file = Path(CONVERSATION_FILE)
  quiz_file = Path(QUIZ_FILE)
  slides_file = Path(SLIDES_FILE)
  storage_path = Path(STORAGE_PATH)
  index_storage = Path(INDEX_STORAGE)

  touch_file(log_file)
  touch_file(session_file)
  touch_file(cache_file)
  touch_file(converstaion_file)
  touch_file(quiz_file)
  touch_file(slides_file)
  mkdir_p(storage_path)
  mkdir_p(index_storage)
