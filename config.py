"""
Configuration settings for ClarityVault
"""

import os

# Optional: load environment variables from a local .env file for development.
# If python-dotenv isn't installed, the app still works with OS env vars.
try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:
    pass

# Flask settings
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")

# Upload folder: default to a writable temp directory on Render (ephemeral),
# otherwise use a local ./uploads folder.
_default_upload_folder = (
    "/tmp/clarityvault_uploads" if os.environ.get("RENDER_EXTERNAL_URL") else "uploads"
)
UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER", _default_upload_folder)
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {
    "pdf",
    "png",
    "jpg",
    "jpeg",
    "bmp",
    "tiff",
    "webp",
    "docx",
    "pptx",
    "txt",
}

# Groq AI settings
# Supports comma-separated keys via GROQ_API_KEYS env var for rotation,
# or a single key via GROQ_API_KEY env var.
_groq_keys_str = os.environ.get("GROQ_API_KEYS", "")
if _groq_keys_str:
    GROQ_API_KEYS = [k.strip() for k in _groq_keys_str.split(",") if k.strip()]
else:
    _single_key = os.environ.get("GROQ_API_KEY", "")
    GROQ_API_KEYS = [_single_key] if _single_key else []

GROQ_MODEL = "llama-3.3-70b-versatile"

# YouTube API settings
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", "")

# Supabase settings
SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "")

# JWT settings
JWT_SECRET = os.environ.get("JWT_SECRET", "change-this-secret-in-production")
JWT_ALGORITHM = "HS256"
JWT_EXPIRY_DAYS = 90
