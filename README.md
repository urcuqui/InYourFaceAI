# InYourFaceAI
Web app for detecting fake faces in images and videos using deep learning. It analyzes media to flag synthetic content (e.g., deepfakes), helping users verify authenticity. Ideal for cybersecurity, forensics, and media validation tasks. Built with AI-first principles.


## Features

- **Deepfake Detection:** Utilizes AI models to distinguish between real and synthetic faces in both images and videos.
- **User-Friendly Interface:** Simple web interface for uploading and analyzing media files.
- **Real-Time Analysis:** Fast processing to deliver results quickly.
- **Security-Focused:** Ideal for cybersecurity, digital forensics, and media validation tasks.
- **Extensible Architecture:** Built with AI-first principles, allowing easy integration of new detection models and features.

## How It Works

1. **Upload Media:** Users can upload images or videos through the web interface.
2. **AI Analysis:** The system processes the media using a vision transformer-based model to detect signs of manipulation or synthetic generation.
3. **Results:** The app provides a clear indication of whether the faces in the media are likely real or fake, along with confidence scores.

## Use Cases

- **Cybersecurity:** Prevent the spread of deepfake content and protect digital identities.
- **Forensics:** Assist investigators in verifying the authenticity of visual evidence.
- **Media Verification:** Help journalists and content creators ensure the integrity of published media.

## Getting Started

1. Clone the repository.
2. Install the required dependencies.
3. Run the web app using the provided scripts.
4. Access the interface via your browser and start analyzing media files.

## Model

The system uses a vision transformer model, with pre-trained weights provided in the `weights/` directory (`vit_teacher.pth`).

---

For more details, see the [face_detection/app.py](face_detection/app.py) implementation and the [notebooks/AppSec Biometrics.ipynb](face_detection/notebooks/AppSec%20Biometrics.ipynb) notebook for model development insights.