import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="Image Resizer", page_icon="🖼️", layout="centered")

st.title("🖼️ Image Resizer")
st.write(
    "Upload the picture. After uploading the custom resize option is showed below. "
)

# ---- 1. Upload image ----
uploaded_file = st.file_uploader(
    "Upload (jpg, jpeg, png, webp)",
    type=["jpg", "jpeg", "png", "webp"],
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    orig_width, orig_height = image.size

    st.image(image, caption=f"Original Image ({orig_width} x {orig_height} px)", use_container_width=True)

    st.subheader("Notun size dio")

    new_width = st.number_input("Width (px)", min_value=1, value=1200, step=1)
    new_height = st.number_input("Height (px)", min_value=1, value=800, step=1)

    keep_ratio = st.checkbox(" Maintain Aspect ratio (image stretch/distort hobe na)", value=False)

    # If aspect ratio is maintained, recalc height based on width
    if keep_ratio:
        aspect = orig_height / orig_width
        new_height = int(new_width * aspect)
        st.info(f"Aspect ratio ontosare final size hobe: {new_width} x {new_height} px")

    # ---- 2. Resize quality option ----
    resample_option = st.selectbox(
        "Resize quality (LANCZOS best for enlarging)",
        ["LANCZOS (best quality)", "BICUBIC", "BILINEAR", "NEAREST (fastest, low quality)"],
    )

    resample_map = {
        "LANCZOS (best quality)": Image.LANCZOS,
        "BICUBIC": Image.BICUBIC,
        "BILINEAR": Image.BILINEAR,
        "NEAREST (fastest, low quality)": Image.NEAREST,
    }

    if st.button("🔄 Resize Image"):
        resample_method = resample_map[resample_option]
        resized_image = image.resize((int(new_width), int(new_height)), resample=resample_method)

        st.success(f"Resize complete! New size: {resized_image.size[0]} x {resized_image.size[1]} px")
        st.image(resized_image, caption="Resized Image", use_container_width=True)

        # ---- 3. Prepare download ----
        buf = io.BytesIO()
        img_format = image.format if image.format else "PNG"
        if img_format.upper() == "JPEG":
            resized_image = resized_image.convert("RGB")
        resized_image.save(buf, format=img_format)
        byte_data = buf.getvalue()

        st.download_button(
            label="⬇️ Download Resized Image",
            data=byte_data,
            file_name=f"resized_{new_width}x{new_height}.{img_format.lower()}",
            mime=f"image/{img_format.lower()}",
        )
else:
    st.info("Upload an image first.")