from PIL import Image, ImageTk
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io


def latex_to_photoimage(latex: str, fontsize: int = 20, dpi: int = 150):
    def _render(latex_str):
        fig = plt.figure(figsize=(0.01, 0.01))
        fig.text(0.01, 0.01, f"${latex_str}$", fontsize=fontsize)
        buf = io.BytesIO()
        plt.axis('off')
        plt.savefig(buf, format='png', dpi=dpi, bbox_inches='tight', pad_inches=0.1)
        plt.close(fig)
        buf.seek(0)
        pil_img = Image.open(buf)
        return ImageTk.PhotoImage(pil_img)

    try:
        return _render(latex)
    except Exception as e:
        fallback = latex.replace('\\arcsin', '\\sin^{-1}')
        fallback = fallback.replace('\\arccos', '\\cos^{-1}')
        fallback = fallback.replace('\\arctan', '\\tan^{-1}')
        fallback = fallback.replace('\\arcsec', '\\sec^{-1}')
        fallback = fallback.replace('\\arccsc', '\\csc^{-1}')
        fallback = fallback.replace('\\arccot', '\\cot^{-1}')
        try:
            return _render(fallback)
        except Exception as e2:
            print(f"LaTeX render failed for: {latex}\nAttempted fallback: {fallback}\nErrors: {e} | {e2}")
            raise
