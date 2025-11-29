import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mathapp.latex_renderer import latex_to_photoimage

exprs = [
    r"\int \frac{6}{\sqrt{4-9x^2}} \, dx",
    r"\int_0^{\infty} e^{-x^2} \, dx",
    r"\int x^3 + x^2 \, dx",
    r"\int_{-1}^{1} \frac{1}{\sqrt{1-x^2}} \, dx",
]

for i, e in enumerate(exprs):
    img = latex_to_photoimage(e, fontsize=80, dpi=150, math_fontset='cm', return_pil=True, pad_inches=0.14)
    fname = f"test_spacing_{i}.png"
    img.save(fname)
    print('Saved', fname)
