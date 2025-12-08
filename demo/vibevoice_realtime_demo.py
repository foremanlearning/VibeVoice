import argparse
import os
from pathlib import Path

import uvicorn
from dotenv import load_dotenv


def main():
    # Load environment variables from .env at project root and package subdir
    project_root = Path(__file__).resolve().parents[1]
    root_env = project_root / ".env"
    pkg_env = project_root / "vibevoice" / ".env"
    load_dotenv(dotenv_path=root_env)
    load_dotenv(dotenv_path=pkg_env)

    # Map custom hugging_face_token to standard Hugging Face token env vars
    custom_token = os.environ.get("hugging_face_token")
    if custom_token:
        os.environ.setdefault("HUGGINGFACE_HUB_TOKEN", custom_token)
        os.environ.setdefault("HF_TOKEN", custom_token)

    p = argparse.ArgumentParser()
    p.add_argument("--port", type=int, default=3000)
    p.add_argument("--model_path", type=str, default=None)
    p.add_argument("--device", type=str, default=None, choices=["cpu", "cuda", "mpx", "mps"])
    p.add_argument("--reload", action="store_true", help="Reload the model or not")
    args = p.parse_args()

    # Resolve model path and device with precedence: CLI > ENV > fallback
    # Fallback to the realtime model repo used in the official docs
    default_repo = "microsoft/VibeVoice-Realtime-0.5B"
    model_path = args.model_path or os.environ.get("MODEL_PATH") or default_repo
    device = args.device or os.environ.get("MODEL_DEVICE", "cuda")

    os.environ["MODEL_PATH"] = model_path
    os.environ["MODEL_DEVICE"] = device

    print(f"[demo] Using MODEL_PATH={model_path!r}, MODEL_DEVICE={device!r}")

    uvicorn.run("web.app:app", host="0.0.0.0", port=args.port, reload=args.reload)

if __name__ == "__main__":
    main()
