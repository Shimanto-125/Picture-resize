# Image Resizer (Streamlit App)

Chobi upload koro, custom width/height dio, resize hoye download korte parbe.

## Files
- `app.py` – Main Streamlit application
- `requirements.txt` – Dependencies

## 1. Local e run korar niyom

```bash
# Virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# App run koro
streamlit run app.py
```

Run korar por browser e automatically `http://localhost:8501` open hoye jabe.

## 2. Kivabe use korবে (usage)
1. "Browse files" e click kore image upload koro (jpg/png/webp)
2. Notun Width & Height dio (jemon 1200 x 800)
3. Chaile "Aspect ratio maintain" checkbox on kore rakho (image stretch hobe na)
4. "Resize Image" button e click koro
5. "Download Resized Image" button diye chobi save koro

## 3. Streamlit Cloud e deploy korar niyom (Free)

1. Ei folder (`app.py` + `requirements.txt`) ekta GitHub repo e push koro
2. Jao: https://share.streamlit.io/
3. GitHub account diye login koro
4. "New app" click koro, tomar repo select koro
5. Main file path e likho: `app.py`
6. "Deploy" click koro — ekta live link pabe (jemon `https://your-app.streamlit.app`)

## 4. Alternative deploy option
- **Render.com** / **Railway.app**: GitHub repo connect kore, start command dite hobe:
  ```
  streamlit run app.py --server.port $PORT --server.address 0.0.0.0
  ```
- **Hugging Face Spaces**: Space type "Streamlit" select kore, ei duita file upload korle deploy hoye jabe.

## Note
- Chobi ke small theke large size e convert kora hocche "upscaling" — image ke stretch/interpolate kora hoy, tai bou beshi enlarge korle (jemon 420x250 → 4000x3000) image ta blur/pixelated dekhate pare. Best quality result er jonno "LANCZOS" option select koro (already default).
- Onek beshi enlarge korte hole AI-based upscaling tool (jemon Real-ESRGAN) lagbe, jeta ei simple version e nei. Bolo jodi eta lagbe, ami add kore dite pari.
