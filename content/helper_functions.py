from IPython.display import display,HTML

def display_schematic(d):
    svg_data = d.get_imagedata('svg').decode('utf-8')
    
    # 3. Force center-alignment inside an HTML container
    display(HTML(f"""
    <div style="display: flex; justify-content: center; width: 100%;">
        {svg_data}
    </div>
    """))