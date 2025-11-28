def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)


def darken_hex(hex_color, amount=0.12):
    
    r, g, b = hex_to_rgb(hex_color)
    r = max(0, int(r * (1 - amount)))
    g = max(0, int(g * (1 - amount)))
    b = max(0, int(b * (1 - amount)))
    return rgb_to_hex((r, g, b))


def luminance(hex_color):
    r, g, b = hex_to_rgb(hex_color)
    
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_color(hex_color):
    
    return '#000000' if luminance(hex_color) > 128 else '#FFFFFF'


def apply_click_effect(btn, swap=False, press_bg=None, press_fg=None, textOnPress=False):
    try:
        orig_bg = btn.cget('bg')
        orig_fg = btn.cget('fg')
        orig_relief = btn.cget('relief')
        orig_bd = btn.cget('bd')
        orig_highlight = btn.cget('highlightthickness')
        orig_highlight_bg = btn.cget('highlightbackground')
    except Exception:
        config = btn.configure()
        orig_bg = config.get('bg')[-1] if 'bg' in config else None
        orig_fg = config.get('fg')[-1] if 'fg' in config else None
        orig_relief = config.get('relief')[-1] if 'relief' in config else None
        orig_bd = config.get('bd')[-1] if 'bd' in config else None
        orig_highlight = config.get('highlightthickness')[-1] if 'highlightthickness' in config else None
        orig_highlight_bg = config.get('highlightbackground')[-1] if 'highlightbackground' in config else None

    
    if orig_bg is None:
        orig_bg = '#FFFFFF'
    if orig_fg is None:
        orig_fg = '#000000'

    if swap:
        press_bg = press_bg or orig_fg
        press_fg = press_fg or orig_bg
    else:
        press_bg = press_bg or darken_hex(orig_bg, 0.16)
        press_fg = press_fg or contrast_color(press_bg)

    try:
        if abs(luminance(orig_bg) - luminance(press_bg)) < 8:
            
            press_bg = contrast_color(orig_bg)
            press_fg = orig_bg or contrast_color(press_bg)
    except Exception:
        pass

    
    def _on_press(event=None):
        try:
            btn.config(bg=press_bg, fg=press_fg)
            try:
                base_bd = int(orig_bd) if orig_bd is not None and str(orig_bd).isdigit() else 0
                new_bd = max(2, base_bd + 2)
                new_highlight = max(2, int(orig_highlight or 0) + 2)
                hb = contrast_color(press_bg or orig_bg)
                btn.config(relief='sunken', bd=new_bd, highlightthickness=new_highlight, highlightbackground=hb)
            except Exception:
                pass
            try:
                if btn.winfo_manager() == 'place':
                    info = btn.place_info()
                    # store original place info for restore
                    if not hasattr(btn, '_orig_place_info'):
                        btn._orig_place_info = info
                    x = int(info.get('x', 0))
                    y = int(info.get('y', 0))
                    w = int(info.get('width', 0)) if info.get('width') else None
                    h = int(info.get('height', 0)) if info.get('height') else None
                    new_kwargs = {'x': x + 1, 'y': y + 1}
                    if w:
                        new_kwargs['width'] = max(1, w - 2)
                    if h:
                        new_kwargs['height'] = max(1, h - 2)
                    btn.place_configure(**new_kwargs)
            except Exception:
                pass
            try:
                if textOnPress:
                    try:
                        if not hasattr(btn, '_orig_text'):
                            btn._orig_text = btn.cget('text')
                        btn.config(text=str(btn._orig_text) + ' ·')
                    except Exception:
                        pass
            except Exception:
                pass
        except Exception:
            pass

    def _on_release(event=None):
        try:
            btn.config(bg=orig_bg, fg=orig_fg)
            try:
                btn.config(relief=orig_relief, bd=orig_bd)
                try:
                    btn.config(highlightthickness=orig_highlight, highlightbackground=orig_highlight_bg)
                except Exception:
                    pass
            except Exception:
                pass
            try:
                if hasattr(btn, '_orig_place_info') and btn.winfo_manager() == 'place':
                    info = btn._orig_place_info
                    restore_kwargs = {}
                    if 'x' in info:
                        restore_kwargs['x'] = int(info['x'])
                    if 'y' in info:
                        restore_kwargs['y'] = int(info['y'])
                    if 'width' in info and info['width']:
                        restore_kwargs['width'] = int(info['width'])
                    if 'height' in info and info['height']:
                        restore_kwargs['height'] = int(info['height'])
                    if restore_kwargs:
                        btn.place_configure(**restore_kwargs)
                    delattr(btn, '_orig_place_info')
            except Exception:
                pass
            try:
                if textOnPress and hasattr(btn, '_orig_text'):
                    btn.config(text=btn._orig_text)
                    delattr(btn, '_orig_text')
            except Exception:
                pass
        except Exception:
            pass

    # Bind events
    btn.bind('<ButtonPress-1>', _on_press)
    btn.bind('<ButtonRelease-1>', _on_release)
    btn.bind('<Leave>', _on_release)

    try:
        btn.config(activebackground=press_bg, activeforeground=press_fg)
    except Exception:
        pass

    try:
        setattr(btn, '_click_effect_applied', True)
    except Exception:
        pass

    return btn
