import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mathapp.latex_renderer import latex_to_photoimage

expr = r"\int \frac{6}{\sqrt{4-9x^2}} \, dx"
img = latex_to_photoimage(expr, fontsize=120, dpi=150, math_fontset='cm', return_pil=True)
img.save('test_user_integral.png')
print('Saved test_user_integral.png')
