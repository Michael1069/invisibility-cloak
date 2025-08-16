# invisibility-cloak
Sometimes coding feels like casting spells 🪄✨
## 🪄 Invisibility Cloak with Python & OpenCV

---
### Ever wanted your own **Harry Potter–style invisibility cloak**?  
This project uses **Python + OpenCV** to create a fun computer vision illusion where a specific colored cloak (in this case, **maroon**) makes you disappear from the camera feed.

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
```
---
## ▶️ Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/Michael1069/invisibility-cloak.git
   cd invisibility-cloak
   ```
2. Run the script:
   ```bash
   python invisibility_cloak.py
   ```
3. Stay out of frame for a few seconds while the background is captured.
4. Step in with your maroon cloak — and vanish!
5. Press `q` or `ESC` to quit.
---
## 🎨 Customization

Want to try different cloak colors?
Adjust the HSV ranges in `invisibility_cloak.py`:

Red: `0–10` & `170–180`
Green: `35–85`
Blue: `90–130`

Tip: lighting can affect detection, so tweak `S` (saturation) and `V` (value) ranges if needed.


---
## 📸 Demo
Here’s a sample of the cloak in action:

➡ (wait ra i'll upload my video lololol)

---
## 💡 Inspiration

Inspired by the legendary Harry Potter invisibility cloak 🧙‍♂️,
this project is a playful way to learn about:

* Background subtraction
* Color detection using HSV
* Image masking & bitwise operations
---
