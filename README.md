<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VibeVoice Documentation</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
            line-height: 1.6;
            color: #24292f;
            max-width: 850px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        a { color: #0969da; text-decoration: none; }
        a:hover { text-decoration: underline; }
        h2, h3 { margin-top: 24px; margin-bottom: 16px; font-weight: 600; line-height: 1.25; }
        h2 { border-bottom: 1px solid #d0d7de; padding-bottom: 0.3em; font-size: 1.5em; }
        h3 { font-size: 1.25em; }
        p { margin-top: 0; margin-bottom: 16px; }
        code {
            padding: 0.2em 0.4em;
            margin: 0;
            font-size: 85%;
            background-color: #afb8c133;
            border-radius: 6px;
            font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
        }
        pre {
            padding: 16px;
            overflow: auto;
            font-size: 85%;
            line-height: 1.45;
            background-color: #f6f8fa;
            border-radius: 6px;
        }
        pre code { background-color: transparent; padding: 0; }
        ul { padding-left: 2em; margin-bottom: 16px; }
        .center { text-align: center; }
        .badges { margin-bottom: 20px; }
        .badges img { margin: 0 4px; vertical-align: middle; }
        .logo { max-width: 300px; display: block; margin: 20px auto; }
        blockquote {
            padding: 0 1em;
            color: #57606a;
            border-left: 0.25em solid #d0d7de;
            margin-left: 0;
        }
        hr {
            height: 0.25em;
            padding: 0;
            margin: 24px 0;
            background-color: #d0d7de;
            border: 0;
        }
    </style>
</head>
<body>

    <div class="center">
        <h2>🎙️ VibeVoice: Open-Source Frontier Voice AI</h2>
        
        <div class="badges">
            <a href="https://microsoft.github.io/VibeVoice"><img src="https://img.shields.io/badge/Project-Page-blue?logo=microsoft" alt="Project Page"></a>
            <a href="https://huggingface.co/collections/microsoft/vibevoice-68a2ef24a875c44be47b034f"><img src="https://img.shields.io/badge/HuggingFace-Collection-orange?logo=huggingface" alt="Hugging Face"></a>
            <a href="https://arxiv.org/pdf/2508.19205"><img src="https://img.shields.io/badge/Technical-Report-red?logo=adobeacrobatreader" alt="Technical Report"></a>
        </div>

        <picture>
            <source media="(prefers-color-scheme: dark)" srcset="Figures/VibeVoice_logo_white.png">
            <img src="Figures/VibeVoice_logo.png" alt="VibeVoice Logo" class="logo">
        </picture>
    </div>

    <h3>Overview</h3>
    <p>VibeVoice is a novel open-source framework for generating <strong>expressive, long-form, multi-speaker</strong> conversational audio (e.g., podcasts) from text. It utilizes continuous speech tokenizers at an ultra-low frame rate (7.5 Hz) and a <a href="https://arxiv.org/abs/2412.08635">next-token diffusion</a> architecture to achieve high efficiency and audio fidelity.</p>

    <p><strong>Key Capabilities:</strong></p>
    <ul>
        <li><strong>Long-form Multi-speaker:</strong> Synthesizes up to <strong>90 minutes</strong> of speech with <strong>4 distinct speakers</strong>.</li>
        <li><strong>Realtime Streaming:</strong> Delivers initial audio in ~<strong>300 ms</strong> with support for streaming text input (<a href="docs/vibevoice-realtime-0.5b.md">Realtime Model Docs</a>).</li>
    </ul>

    <hr>

    <h3>📰 Latest News</h3>
    <p>
        <img src="https://img.shields.io/badge/Status-New-brightgreen?style=flat" alt="New" />
        <img src="https://img.shields.io/badge/Feature-Realtime_TTS-blue?style=flat&logo=soundcharts" alt="Realtime TTS" />
    </p>
    <ul>
        <li><strong>2025-12-09:</strong> Added experimental speakers in 9 languages (DE, FR, IT, JP, KR, NL, PL, PT, ES).</li>
        <li><strong>2025-12-03:</strong> Open-sourced <strong>VibeVoice‑Realtime‑0.5B</strong>. Try it on <a href="https://colab.research.google.com/github/microsoft/VibeVoice/blob/main/demo/vibevoice_realtime_colab.ipynb">Colab</a>.</li>
    </ul>

    <hr>

    <h3>💻 Installation & Usage</h3>
    <p>Follow these steps to set up VibeVoice locally.</p>

    <h4>1. Prerequisites</h4>
    <p>Ensure you have <strong>Anaconda</strong> or <strong>Miniconda</strong> installed on your system.</p>
    <ul>
        <li><a href="https://www.anaconda.com/download">Download Anaconda here</a></li>
    </ul>

    <h4>2. Clone the Repository</h4>
    <pre><code>git clone https://github.com/microsoft/VibeVoice.git
cd VibeVoice</code></pre>

    <h4>3. Configuration (Hugging Face Token)</h4>
    <p>You must configure your environment with a Hugging Face User Access Token.</p>
    <ol>
        <li><strong>Generate Token:</strong>
            <ul>
                <li>Log in to your <a href="https://huggingface.co/">Hugging Face account</a>.</li>
                <li>Navigate to <strong>Settings</strong> > <strong>Access Tokens</strong>.</li>
                <li>Click <strong>Create New Token</strong>.</li>
                <li>Select <strong>Write</strong> permissions (or ensure it has access to the VibeVoice gated models).</li>
                <li>Copy the token string (starts with <code>hf_...</code>).</li>
            </ul>
        </li>
        <li><strong>Update Environment File:</strong>
            <ul>
                <li>Open <code>.env.example</code> in a text editor.</li>
                <li>Paste your token into the appropriate variable field.</li>
                <li>Save and rename the file to <code>.env</code>:</li>
            </ul>
            <pre><code>mv .env.example .env</code></pre>
        </li>
    </ol>

    <h4>4. Environment Setup</h4>
    <p>Create and activate the Conda environment, then install dependencies.</p>
    <pre><code># Create the environment (adjust python version if specified in requirements, usually 3.10+)
conda create -n vibevoice python=3.10 -y

# Activate the environment
conda activate vibevoice

# Install dependencies
pip install -r requirements.txt</code></pre>

    <h4>5. Running VibeVoice</h4>
    <p>To launch the demo or inference scripts:</p>
    <pre><code># Example: Launch the Web UI (check repository for exact script name)
python app.py

# Or launch the realtime websocket demo
python demo/realtime_websocket.py</code></pre>

    <hr>

    <h3>⚠️ Risks and Limitations</h3>
    <ul>
        <li><strong>Deepfakes:</strong> High-quality synthesis can be misused. Users must ensure transcripts are reliable and disclose the use of AI.</li>
        <li><strong>Language Support:</strong> Primarily optimized for English and Chinese. Other languages may yield unexpected results.</li>
        <li><strong>Audio Scope:</strong> Focuses solely on speech; does not generate background noise or music.</li>
        <li><strong>License:</strong> This model is intended for <strong>research and development purposes only</strong>.</li>
    </ul>

    <p><em>For more examples and details, visit the <a href="https://microsoft.github.io/VibeVoice">Project Page</a>.</em></p>

</body>
</html>
