# invisibility-cloak
Sometimes coding feels like casting spells 🪄✨
# 🪄 Invisibility Cloak with Python & OpenCV

## Ever wanted your own **Harry Potter–style invisibility cloak**?  
This project uses **Python + OpenCV** to create a fun computer vision illusion where a specific colored cloak (in this case, **maroon**) makes you disappear from the camera feed. 🎥✨

---

## 🚀 How It Works
1. **Capture Background** – Record the static background scene without the person.  
2. **Color Detection** – Detect cloak color (HSV range tuned for maroon).  
3. **Masking & Replacement** – Replace cloak region with background pixels.  
4. **Result** – The person appears invisible where the cloak is present.  

---

## 🛠️ Requirements
- Python 3.x  
- OpenCV  
- NumPy  

Install dependencies with:
```bash
pip install opencv-python numpy
