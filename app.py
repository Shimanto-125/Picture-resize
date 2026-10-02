import streamlit as st
from PIL import Image
import io
import re

st.set_page_config(page_title="Image Resizer", page_icon="🖼️", layout="centered")

st.title("🖼️ Image Resizer")
st.write(
    "Upload the picture. After uploading the custom resize option is showed below. "
)

# 1. Upload image 
uploaded_file = st.file_uploader(
    "Upload (jpg, jpeg, png, webp)",
    type=["jpg", "jpeg", "png", "webp"],
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    orig_width, orig_height = image.size

    st.image(image, caption=f"Original Image ({orig_width} x {orig_height} px)", use_container_width=True)

    st.subheader("Notun size dio")

    new_width = st.number_input("Width (px)", min_value=1, value=1280, step=1)
    new_height = st.number_input("Height (px)", min_value=1, value=720, step=1)

    keep_ratio = st.checkbox(" Maintain Aspect ratio (image stretch/distort hobe na)", value=False)

    # If aspect ratio is maintained, recalc height based on width
    if keep_ratio:
        aspect = 9 / 16
        new_height = int(new_width * aspect)
        st.info(f"Aspect ratio ontosare final size hobe: {new_width} x {new_height} px")

    #Resize quality option 
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

    #Custom file name (optional)
    custom_name = st.text_input(
        "Custom file name (optional)",
        placeholder=f"resized_{int(new_width)}x{int(new_height)}",
        help="Custom file name add kora jabe. Khali rakhle automatic naam hobe. Extension likhte hobe na, auto add hobe.",
    )

    if st.button("🔄 Resize Image"):
        resample_method = resample_map[resample_option]
        resized_image = image.resize((int(new_width), int(new_height)), resample=resample_method)

        img_format = image.format if image.format else "PNG"
        if img_format.upper() == "JPEG":
            resized_image = resized_image.convert("RGB")

        buf = io.BytesIO()
        resized_image.save(buf, format=img_format)

        ext = img_format.lower()

        # clean name of file
        clean_name = custom_name.strip()
        clean_name = re.sub(r"\.(jpg|jpeg|png|webp)$", "", clean_name, flags=re.IGNORECASE)
        # invalid character replace
        clean_name = re.sub(r'[\\/:*?"<>|]', "_", clean_name).strip()

        if not clean_name:
            clean_name = f"resized_{int(new_width)}x{int(new_height)}"

        st.session_state["result"] = {
            "source": uploaded_file.file_id,
            "image": resized_image,
            "bytes": buf.getvalue(),
            "ext": ext,
            "width": int(new_width),
            "height": int(new_height),
            "file_name": f"{clean_name}.{ext}",
        }

    #Show result + download
    result = st.session_state.get("result")
    if result and result["source"] == uploaded_file.file_id:
        st.success(f"Resize complete! New size: {result['width']} x {result['height']} px")
        st.image(result["image"], caption="Resized Image", use_container_width=True)
        st.caption(f"Custom file name: **{result['file_name']}**")

        st.download_button(
            label="⬇️ Download Resized Image",
            data=result["bytes"],
            file_name=result["file_name"],
            mime=f"image/{result['ext']}",
        )
else:
    st.session_state.pop("result", None)
    st.info("Upload an image first.")
