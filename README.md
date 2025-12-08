<div align="center">

## 🎙️ VibeVoice: Open-Source Frontier Voice AI
[![Project Page](https://img.shields.io/badge/Project-Page-blue?logo=microsoft)](https://microsoft.github.io/VibeVoice)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Collection-orange?logo=huggingface)](https://huggingface.co/collections/microsoft/vibevoice-68a2ef24a875c44be47b034f)
[![Technical Report](https://img.shields.io/badge/Technical-Report-red?logo=adobeacrobatreader)](https://arxiv.org/pdf/2508.19205)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="Figures/VibeVoice_logo_white.png">
  <img src="Figures/VibeVoice_logo.png" alt="VibeVoice Logo" width="300">
</picture>

</div>

### Overview
VibeVoice is a novel open-source framework for generating **expressive, long-form, multi-speaker** conversational audio (e.g., podcasts) from text. It utilizes continuous speech tokenizers at an ultra-low frame rate (7.5 Hz) and a [next-token diffusion](https://arxiv.org/abs/2412.08635) architecture to achieve high efficiency and audio fidelity.

**Key Capabilities:**
- **Long-form Multi-speaker:** Synthesizes up to **90 minutes** of speech with **4 distinct speakers**.
- **Realtime Streaming:** Delivers initial audio in ~**300 ms** with support for streaming text input ([Realtime Model Docs](docs/vibevoice-realtime-0.5b.md)).

<div align="left">

<h3>📰 Latest News</h3>

<img src="https://img.shields.io/badge/Status-New-brightgreen?style=flat" alt="New" />
<img src="https://img.shields.io/badge/Feature-Realtime_TTS-blue?style=flat&logo=soundcharts" alt="Realtime TTS" />

* **2025-12-09:** Added experimental speakers in 9 languages (DE, FR, IT, JP, KR, NL, PL, PT, ES).
* **2025-12-03:** Open-sourced **VibeVoice‑Realtime‑0.5B**. Try it on [Colab](https://colab.research.google.com/github/microsoft/VibeVoice/blob/main/demo/vibevoice_realtime_colab.ipynb).

</div>

---

### 💻 Installation & Usage

Follow these steps to set up VibeVoice locally.

#### 1. Prerequisites
Ensure you have **Anaconda** or **Miniconda** installed on your system.
* [Download Anaconda here](https://www.anaconda.com/download)

#### 2. Clone the Repository
```bash
git clone [https://github.com/microsoft/VibeVoice.git](https://github.com/microsoft/VibeVoice.git)
cd VibeVoice
````

#### 3\. Configuration (Hugging Face Token)

You must configure your environment with a Hugging Face User Access Token.

1.  **Generate Token:**
      * Log in to your [Hugging Face account](https://huggingface.co/).
      * Navigate to **Settings** \> **Access Tokens**.
      * Click **Create New Token**.
      * Select **Write** permissions (or ensure it has access to the VibeVoice gated models).
      * Copy the token string (starts with `hf_...`).
2.  **Update Environment File:**
      * Open `.env.example` in a text editor.
      * Paste your token into the appropriate variable field.
      * Save and rename the file to `.env`:
        ```bash
        mv .env.example .env
        ```

#### 4\. Environment Setup

Create and activate the Conda environment, then install dependencies.

```bash
# Create the environment (adjust python version if specified in requirements, usually 3.10+)
conda create -n vibevoice python=3.10 -y

# Activate the environment
conda activate vibevoice

# Install dependencies
pip install -r requirements.txt
```

#### 5\. Running VibeVoice

To launch the demo or inference scripts:

```bash
# Example: Launch the Web UI (check repository for exact script name)
python app.py

# Or launch the realtime websocket demo
python demo/realtime_websocket.py
```

-----

### ⚠️ Risks and Limitations

  * **Deepfakes:** High-quality synthesis can be misused. Users must ensure transcripts are reliable and disclose the use of AI.
  * **Language Support:** Primarily optimized for English and Chinese. Other languages may yield unexpected results.
  * **Audio Scope:** Focuses solely on speech; does not generate background noise or music.
  * **License:** This model is intended for **research and development purposes only**.

*For more examples and details, visit the [Project Page](https://microsoft.github.io/VibeVoice).*

```
```
