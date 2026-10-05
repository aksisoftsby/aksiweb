#!/usr/bin/env python3
"""Downsample/recompress images inside a PDF to shrink file size.

Usage: py scripts/compress-pdf.py <input.pdf> <output.pdf> [max_side] [quality]

Keeps transparency by rendering alpha as an SMask if the source had one.
"""
import io
import sys

import pikepdf
from PIL import Image


def recompress(obj, max_side, quality):
    try:
        pdfimg = pikepdf.PdfImage(obj)
        pil = pdfimg.as_pil_image()
    except Exception:
        return 0

    had_alpha = pil.mode in ("RGBA", "LA") or (
        pil.mode == "P" and "transparency" in pil.info
    )
    if pil.mode == "P":
        pil = pil.convert("RGBA")
    if pil.mode not in ("RGB", "RGBA", "L"):
        pil = pil.convert("RGB")

    w, h = pil.size
    scale = max_side / max(w, h)
    if scale < 1:
        pil = pil.resize((max(1, round(w * scale)), max(1, round(h * scale))), Image.LANCZOS)

    smask_obj = None
    if had_alpha and pil.mode == "RGBA":
        alpha = pil.getchannel("A")
        abuf = io.BytesIO()
        alpha.save(abuf, format="JPEG", quality=min(quality, 60))
        smask_obj = pikepdf.Stream(
            obj.owner,
            abuf.getvalue(),
            Filter=pikepdf.Name("/DCTDecode"),
            Type=pikepdf.Name("/XObject"),
            Subtype=pikepdf.Name("/Image"),
            Width=alpha.width,
            Height=alpha.height,
            ColorSpace=pikepdf.Name("/DeviceGray"),
            BitsPerComponent=8,
        )
        pil = pil.convert("RGB")

    rgb = pil.convert("RGB")
    buf = io.BytesIO()
    rgb.save(buf, format="JPEG", quality=quality, optimize=True, progressive=True)
    if len(buf.getvalue()) >= len(obj.read_raw_bytes()):
        # not smaller; still try, but likely skip
        pass

    obj.write(buf.getvalue(), filter=pikepdf.Name("/DCTDecode"))
    obj.Type = pikepdf.Name("/XObject")
    obj.Subtype = pikepdf.Name("/Image")
    obj.Width = rgb.width
    obj.Height = rgb.height
    obj.ColorSpace = pikepdf.Name("/DeviceRGB")
    obj.BitsPerComponent = 8
    if "/Decode" in obj:
        del obj["/Decode"]
    if smask_obj is not None:
        obj.SMask = smask_obj
    return 1


def main():
    inp, outp = sys.argv[1], sys.argv[2]
    max_side = int(sys.argv[3]) if len(sys.argv) > 3 else 1100
    quality = int(sys.argv[4]) if len(sys.argv) > 4 else 72

    pdf = pikepdf.open(inp)
    seen = set()
    n = 0
    for page in pdf.pages:
        images = page.get_images()
        for name in list(images.keys()):
            obj = images[name]
            try:
                key = obj.objgen
            except Exception:
                key = id(obj)
            if key in seen:
                continue
            seen.add(key)
            try:
                n += recompress(obj, max_side, quality)
            except Exception as e:  # noqa: BLE001
                print("skip:", e, file=sys.stderr)
    pdf.save(
        outp,
        compress_streams=True,
        object_stream_mode=pikepdf.ObjectStreamMode.generate,
        recompress_flate=True,
    )
    print(f"recompressed {n} images -> {outp}")


if __name__ == "__main__":
    main()
