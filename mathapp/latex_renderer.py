from PIL import Image, ImageTk
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
from matplotlib import rc_context

def latex_to_photoimage(latex: str, fontsize: int = 20, dpi: int = 150, math_fontset: str = 'cm', return_pil: bool = False, use_tex: bool = False, pad_inches: float = 0.18):

    def _render(latex_str):
        rc = {
            'mathtext.fontset': math_fontset,
            'font.family': 'serif',
        }
        if use_tex:
            rc['text.usetex'] = True

        with rc_context(rc):

            fig = plt.figure(figsize=(1, 1), dpi=dpi)
            fig.text(0.5, 0.5, f"${latex_str}$", fontsize=fontsize, ha='center', va='center')
            plt.axis('off')
            fig.canvas.draw()
            renderer = fig.canvas.get_renderer()
            text_artist = fig.texts[0]
            bbox = text_artist.get_window_extent(renderer)
            width_in = max(bbox.width / dpi, 0.1)
            height_in = max(bbox.height / dpi, 0.1)
            pad_value = float(pad_inches)
            fig.set_size_inches(width_in + pad_value, height_in + pad_value)
            fig.canvas.draw()
            buf = io.BytesIO()
            plt.savefig(buf, format='png', dpi=dpi, bbox_inches='tight', pad_inches=pad_value)
            plt.close(fig)
            buf.seek(0)
            pil_img = Image.open(buf)
            if return_pil:
                return pil_img
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
