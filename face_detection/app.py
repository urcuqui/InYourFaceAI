from flask import Flask, render_template, request, redirect, url_for
#import cv2
import numpy as np
from PIL import Image
import os
import timm
import torch
from torchvision import transforms

app = Flask(__name__)
UPLOAD_FOLDER = "static"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
import os
model_filename = os.path.join(os.path.dirname(__file__), 'weights/vit_teacher.pth')
model = timm.create_model('vit_base_patch16_224.augreg_in21k_ft_in1k', pretrained=True)
model.head = torch.nn.Linear(model.head.in_features, 2)
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)
model.load_state_dict(
    torch.load(
        model_filename,
    )
)
model.eval()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        if not file:
            return "No images uploaded", 400
        img = Image.open(file.stream).convert("RGB")
        transform_original = transforms.Compose([
            transforms.Resize(224),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        img_tensor = transform_original(img).unsqueeze(0)
        with torch.no_grad():
            current_index = model(img_tensor.to(device))[0].argmax().unsqueeze(0)
            print("index is", current_index)
            if current_index == 1:
                return render_template("index.html", face_count="It's real!", result_img="output.jpg")
            else:
                return render_template("index.html", face_count="It's fake!", result_img="output.jpg")
        

    return render_template("index.html", face_count=None, result_img="output.jpg")

if __name__ == "__main__":
    app.run(debug=True)