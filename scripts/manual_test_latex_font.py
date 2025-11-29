import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mathapp.latex_renderer import latex_to_photoimage

# This will render a PIL Image and save to disk
img = latex_to_photoimage(r"x^2 + \frac{1}{2} + \sin(\theta)", fontsize=60, dpi=150, math_fontset='cm', return_pil=True)
img.save('test_latex_cm.png')
print('Saved test_latex_cm.png')

img2 = latex_to_photoimage(r"x^2 + \frac{1}{2} + \sin(\theta)", fontsize=60, dpi=150, math_fontset='stix', return_pil=True)
img2.save('test_latex_stix.png')
print('Saved test_latex_stix.png')

# Try using tex if a TeX engine is available (may fail if not installed): fallback is okay
try:
    img3 = latex_to_photoimage(r"x^2 + \frac{1}{2} + \sin(\theta)", fontsize=60, dpi=150, math_fontset='cm', return_pil=True, use_tex=True)
    img3.save('test_latex_usetex.png')
    print('Saved test_latex_usetex.png')
except Exception as e:
    print('Failed to render with use_tex (likely missing LaTeX):', e)
