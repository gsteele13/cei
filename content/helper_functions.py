from IPython.display import display,HTML

def display_schematic(d):
    svg_data = d.get_imagedata('svg').decode('utf-8')
    
    # 3. Force center-alignment inside an HTML container
    display(HTML(f"""
    <div style="display: flex; justify-content: center; width: 100%;">
        {svg_data}
    </div>
    """))

import matplotlib as mpl
import matplotlib.pyplot as plt
from IPython.display import display, HTML
import io
import re

def show_plot(fig, scale=1): 
    buf = io.StringIO()
    fig.savefig(buf, format='svg', bbox_inches='tight')
    plt.close(fig)
    svg = buf.getvalue()

    def _scale_dim(match):
        attr, value, unit = match.group(1), float(match.group(2)), match.group(3)
        return f'{attr}="{value * scale:g}{unit}"'

    # Only touch the width/height on the opening <svg ...> tag
    def _scale_svg_tag(match):
        return re.sub(r'(width|height)="([\d.]+)([a-z%]*)"', _scale_dim, match.group(0), count=2)

    svg = re.sub(r'<svg\b[^>]*>', _scale_svg_tag, svg, count=1)

    display(HTML(f'<div style="display: flex; justify-content: center;">{svg}</div>'))

def show_svg(file, scale=1.0):
    with open(file, "r") as f:
        buf = f.read()

    html = f"""
    <div style="display: flex; justify-content: center;">
        <div style="width: {scale * 100}%;">
            <style>
                .svg-scaled svg {{ width: 100%; height: auto; }}
            </style>
            <div class="svg-scaled">{buf}</div>
        </div>
    </div>
    """
    display(HTML(html))        

from matplotlib_inline.backend_inline import set_matplotlib_formats
set_matplotlib_formats("svg")        # or "pdf", or both: set_matplotlib_formats("svg", "pdf")
