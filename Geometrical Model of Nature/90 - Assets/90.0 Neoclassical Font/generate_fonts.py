# generate_fonts.py
import os
import json
import html
import numpy as np
from fontTools import ttLib
from fontTools.ttLib import TTFont
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib.tables._c_m_a_p import cmap_format_4, table__c_m_a_p
from fontTools.ttLib.tables._g_l_y_f import Glyph, table__g_l_y_f
from fontTools.ttLib.tables._h_m_t_x import table__h_m_t_x
from fontTools.ttLib.tables._h_e_a_d import table__h_e_a_d
from fontTools.ttLib.tables._h_h_e_a import table__h_h_e_a
from fontTools.ttLib.tables.O_S_2f_2 import table_O_S_2f_2, Panose
from fontTools.ttLib.tables._n_a_m_e import table__n_a_m_e
from fontTools.ttLib.tables._p_o_s_t import table__p_o_s_t
from fontTools.ttLib.tables._m_a_x_p import table__m_a_x_p
from fontTools.ttLib.tables._l_o_c_a import table__l_o_c_a

# --- Configuration ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = SCRIPT_DIR
# UNITS_PER_EM_VALUES = [1000, 2048]
UNITS_PER_EM_VALUES = [1024]
CIRCLE_RADII = [64, 128, 256]  # In font units
FONT_SIZES_PT = [24, 36, 48, 60]  # For HTML report
HEX_RADIUS = 400
CIRCLE_IN_HEX_RADIUS = 80
GLYPH_THICKNESS = 32
THIN_GLYPH_THICKNESS = 24

# --- Helper Functions ---

def polygon_to_glyph(points, glyph_set):
    """Creates a glyph from a list of polygon points."""
    pen = TTGlyphPen(glyph_set)
    if not points:
        return pen.glyph()

    pen.moveTo(points[0])
    for point in points[1:]:
        pen.lineTo(point)
    pen.closePath()
    return pen.glyph()

def build_glyph_from_definition(definition, glyph_set, em_height, center_y, glyph_width):
    """Builds a glyph by assembling a list of declarative components from a definition."""
    pen = TTGlyphPen(glyph_set)
    background = definition.get('background')
    components = definition.get('components', [])
    is_inverted = (background is not None)

    # --- 1. Draw Background (if any) ---
    if is_inverted:
        if background['shape'] == 'square':
            square_dim = em_height - 2 * 0 # square_margin is 0
            x = (glyph_width - square_dim) / 2
            y = (em_height - square_dim) / 2 + (center_y - em_height / 2)
            # Draw CW for solid fill
            points = [(x, y), (x, y + square_dim), (x + square_dim, y + square_dim), (x + square_dim, y)]
            pen.moveTo(points[0]); [pen.lineTo(p) for p in points[1:]]; pen.closePath()
        elif background['shape'] == 'circle':
            radius = background['radius']
            # Draw CW for solid fill
            points = arc_poly(glyph_width / 2, center_y, radius, radius, 2 * np.pi, 0, num_segments=64)
            pen.moveTo(points[0]); [pen.lineTo(p) for p in points[1:]]; pen.closePath()

    # --- 2. Draw Components ---
    for comp in components:
        comp_type = comp['type']

        if comp_type == 'square':
            thickness = GLYPH_THICKNESS
            square_dim = em_height - 2 * 0
            x = (glyph_width - square_dim) / 2
            y = (em_height - square_dim) / 2 + (center_y - em_height / 2)
            # Outer contour: CW for draw, CCW for cutout
            outer_points = [(x, y), (x, y + square_dim), (x + square_dim, y + square_dim), (x + square_dim, y)] # CW
            if is_inverted: outer_points.reverse() # Becomes CCW
            pen.moveTo(outer_points[0]); [pen.lineTo(p) for p in outer_points[1:]]; pen.closePath()
            # Inner contour: CCW for draw, CW for cutout
            inner_x, inner_y = x + thickness, y + thickness
            inner_width, inner_height = square_dim - 2 * thickness, square_dim - 2 * thickness
            inner_points = [(inner_x, inner_y), (inner_x + inner_width, inner_y), (inner_x + inner_width, inner_y + inner_height), (inner_x, inner_y + inner_height)] # CW
            if not is_inverted: inner_points.reverse() # Becomes CCW
            pen.moveTo(inner_points[0]); [pen.lineTo(p) for p in inner_points[1:]]; pen.closePath()

        elif comp_type == 'concentric_circles':
            radii = comp['radii']
            thickness = GLYPH_THICKNESS
            for r in sorted(radii, reverse=True):
                # Outer contour: CW for draw, CCW for cutout
                outer_points = arc_poly(glyph_width / 2, center_y, r, r, 2 * np.pi if not is_inverted else 0, 0 if not is_inverted else 2 * np.pi, num_segments=64)
                pen.moveTo(outer_points[0]); [pen.lineTo(p) for p in outer_points[1:]]; pen.closePath()
                # Inner contour: CCW for draw, CW for cutout
                inner_r = r - thickness
                if inner_r > 0:
                    inner_points = arc_poly(glyph_width / 2, center_y, inner_r, inner_r, 0 if not is_inverted else 2 * np.pi, 2 * np.pi if not is_inverted else 0, num_segments=64)
                    pen.moveTo(inner_points[0]); [pen.lineTo(p) for p in inner_points[1:]]; pen.closePath()

        elif comp_type == 'hexagon_circles':
            fill_pattern = comp['fill_pattern']
            rotation_rad = np.deg2rad(comp.get('rotation', 0))
            thickness = GLYPH_THICKNESS
            for i in range(6):
                angle = i * np.pi / 3 + rotation_rad
                ccx = glyph_width / 2 + HEX_RADIUS * np.cos(angle)
                ccy = center_y + HEX_RADIUS * np.sin(angle)
                
                is_filled = (fill_pattern[i] == '0')

                if is_filled:
                    # Filled circle is always drawn on top, so it's always CW.
                    points = arc_poly(ccx, ccy, CIRCLE_IN_HEX_RADIUS, CIRCLE_IN_HEX_RADIUS, 2 * np.pi, 0, num_segments=32)
                    pen.moveTo(points[0]); [pen.lineTo(p) for p in points[1:]]; pen.closePath()
                else: # Hollow
                    # Outer contour: CW for draw, CCW for cutout
                    outer_points = arc_poly(ccx, ccy, CIRCLE_IN_HEX_RADIUS, CIRCLE_IN_HEX_RADIUS, 2 * np.pi if not is_inverted else 0, 0 if not is_inverted else 2 * np.pi, num_segments=32)
                    pen.moveTo(outer_points[0]); [pen.lineTo(p) for p in outer_points[1:]]; pen.closePath()
                    # Inner contour: CCW for draw, CW for cutout
                    inner_r = CIRCLE_IN_HEX_RADIUS - thickness
                    if inner_r > 0:
                        inner_points = arc_poly(ccx, ccy, inner_r, inner_r, 0 if not is_inverted else 2 * np.pi, 2 * np.pi if not is_inverted else 0, num_segments=32)
                        pen.moveTo(inner_points[0]); [pen.lineTo(p) for p in inner_points[1:]]; pen.closePath()

    return pen.glyph()

def arc_poly(cx, cy, rx, ry, start_angle, end_angle, num_segments=16):
    """Generates points for a polygonal approximation of an elliptical arc."""
    theta = np.linspace(start_angle, end_angle, num_segments + 1)
    points = [(cx + rx * np.cos(angle), cy + ry * np.sin(angle)) for angle in theta]
    return points

def shift_points(points, y_shift):
    """Shifts the y-coordinate of all points in a list."""
    return [(x, y + y_shift) for x, y in points]

# --- Core Font Generation ---

def create_font(font_name, units_per_em, glyphs_data, output_path):
    """Creates and saves a TTF font file from provided glyph data."""
    font = TTFont()
    glyph_order = ['.notdef'] + sorted(glyphs_data.keys())
    font.setGlyphOrder(glyph_order)

    # --- Glyf and Hmtx Tables ---
    font['glyf'] = glyf_table = table__g_l_y_f()
    glyf_table.glyphs = {}
    font['hmtx'] = hmtx_table = table__h_m_t_x()
    hmtx_table.metrics = {}

    glyf_table.glyphs['.notdef'] = Glyph()
    hmtx_table.metrics['.notdef'] = (int(units_per_em / 2), 0)

    ascent = int(units_per_em * 0.8)
    descent = -(units_per_em - ascent)
    center_y = (ascent + descent) / 2.0

    for char, data in glyphs_data.items():
        if data.get('type') == 'json_defined':
            glyph = build_glyph_from_definition(data, glyf_table.glyphs, units_per_em, center_y, data['width'])
        elif data.get('type') == 'polygon':
            glyph = polygon_to_glyph(data['points'], glyf_table.glyphs)
        else:
            continue  # Skip unknown glyph types

        glyph.recalcBounds(glyf_table)

        glyf_table.glyphs[char] = glyph
        lsb = glyph.xMin if hasattr(glyph, 'xMin') else 0
        hmtx_table.metrics[char] = (data['width'], lsb)

    # --- Cmap Table ---
    cmap = cmap_format_4(4)
    cmap.platformID = 3
    cmap.platEncID = 1
    cmap.language = 0
    cmap.cmap = {ord(c): c for c in glyphs_data.keys()}
    cmap_table = table__c_m_a_p()
    cmap_table.tableVersion = 0
    cmap_table.tables = [cmap]
    font['cmap'] = cmap_table

    # --- Font Header Tables ---
    font['head'] = head = table__h_e_a_d()
    head.tableVersion = 1.0
    head.fontRevision = 1.0
    head.checkSumAdjustment = 0
    head.magicNumber = 0x5F0F3CF5
    head.flags = 3  # Set default flags
    head.unitsPerEm = units_per_em
    head.created = 0
    head.modified = 0

    # Calculate font bounding box from all glyphs
    all_glyphs = [glyf_table.glyphs[name] for name in glyphs_data.keys()]

    xMins = [g.xMin for g in all_glyphs if hasattr(g, 'xMin')]
    yMins = [g.yMin for g in all_glyphs if hasattr(g, 'yMin')]
    xMaxs = [g.xMax for g in all_glyphs if hasattr(g, 'xMax')]
    yMaxs = [g.yMax for g in all_glyphs if hasattr(g, 'yMax')]

    if xMins:
        head.xMin = min(xMins)
        head.yMin = min(yMins)
        head.xMax = max(xMaxs)
        head.yMax = max(yMaxs)
    else:
        head.xMin, head.yMin, head.xMax, head.yMax = (0, 0, 0, 0)

    head.macStyle = 0
    head.lowestRecPPEM = 0
    head.fontDirectionHint = 2
    head.indexToLocFormat = 0
    head.glyphDataFormat = 0

    font['hhea'] = hhea = table__h_h_e_a()
    hhea.tableVersion = 0x00010000
    # Use an 80/20 split for ascent/descent for better vertical alignment
    hhea.ascent = int(units_per_em * 0.8)
    hhea.descent = -(units_per_em - hhea.ascent)
    hhea.lineGap = 0
    hhea.advanceWidthMax = 0  # Will be recalculated
    hhea.minLeftSideBearing = 0  # Will be recalculated
    hhea.minRightSideBearing = 0  # Will be recalculated
    hhea.xMaxExtent = 0  # Will be recalculated
    hhea.caretSlopeRise = 1
    hhea.caretSlopeRun = 0
    hhea.caretOffset = 0
    hhea.reserved0 = 0
    hhea.reserved1 = 0
    hhea.reserved2 = 0
    hhea.reserved3 = 0
    hhea.metricDataFormat = 0
    hhea.numberOfHMetrics = len(hmtx_table.metrics)

    font['OS/2'] = os2 = table_O_S_2f_2()
    os2.version = 4
    os2.xAvgCharWidth = units_per_em
    os2.usWeightClass = 400
    os2.usWidthClass = 5
    os2.fsType = 0
    os2.ySubscriptXSize, os2.ySubscriptYSize, os2.ySubscriptXOffset, os2.ySubscriptYOffset = (650, 700, 0, 140)
    os2.ySuperscriptXSize, os2.ySuperscriptYSize, os2.ySuperscriptXOffset, os2.ySuperscriptYOffset = (650, 700, 0, 480)
    os2.yStrikeoutSize, os2.yStrikeoutPosition = (50, 258)
    os2.sFamilyClass = 0
    os2.panose = Panose()
    os2.ulUnicodeRange1, os2.ulCodePageRange1 = (1, 1)
    os2.ulUnicodeRange2 = 0
    os2.ulUnicodeRange3 = 0
    os2.ulUnicodeRange4 = 0
    os2.ulCodePageRange2 = 0
    os2.achVendID = 'TEST'
    os2.fsSelection = 1 << 6
    os2.usFirstCharIndex = min(ord(c) for c in glyphs_data.keys())
    os2.usLastCharIndex = max(ord(c) for c in glyphs_data.keys())
    os2.sTypoAscender, os2.sTypoDescender, os2.sTypoLineGap = (hhea.ascent, hhea.descent, 0)
    os2.usWinAscent, os2.usWinDescent = (hhea.ascent, abs(hhea.descent))
    os2.sxHeight = int(units_per_em * 0.7)
    os2.sCapHeight = int(units_per_em * 0.7)
    os2.usDefaultChar = 0
    os2.usBreakChar = 0
    os2.usMaxContext = 0

    font['name'] = name = table__n_a_m_e()
    name.setName(font_name, 1, 3, 1, 0x409)
    name.setName("Regular", 2, 3, 1, 0x409)
    name.setName(font_name, 4, 3, 1, 0x409)
    name.setName(font_name.replace(" ", ""), 6, 3, 1, 0x409)

    font['post'] = post = table__p_o_s_t()
    post.formatType = 2.0
    post.italicAngle = 0.0
    post.underlinePosition = -100
    post.underlineThickness = 50
    post.isFixedPitch = 0
    post.minMemType42 = 0
    post.maxMemType42 = 0
    post.minMemType1 = 0
    post.maxMemType1 = 0
    post.extraNames = []
    post.mapping = {}
    post.glyphOrder = glyph_order

    # fontTools will compute maxp and loca tables on save
    font['maxp'] = maxp = table__m_a_x_p()
    maxp.tableVersion = 0x00010000
    maxp.numGlyphs = 0  # Will be recalculated
    maxp.maxPoints = 0  # Will be recalculated
    maxp.maxContours = 0  # Will be recalculated
    maxp.maxCompositePoints = 0  # Will be recalculated
    maxp.maxCompositeContours = 0  # Will be recalculated
    maxp.maxZones = 1  # Default for non-hinted fonts
    maxp.maxTwilightPoints = 0  # Default
    maxp.maxStorage = 0  # Default
    maxp.maxFunctionDefs = 0  # Default
    maxp.maxInstructionDefs = 0  # Default
    maxp.maxStackElements = 0  # Default
    maxp.maxSizeOfInstructions = 0  # Default
    maxp.maxComponentElements = 0  # Will be recalculated
    maxp.maxComponentDepth = 0  # Will be recalculated
    font['loca'] = table__l_o_c_a()

    font.save(output_path)
    print(f"Successfully created {output_path}")

# --- Visual Report Generation ---
def generate_html_report(font_files, output_dir):
    """Generates an HTML file to display the fonts."""
    sample_text = "DUE<hH|hH>(dud)e(udu)"
    escaped_sample_text = html.escape(sample_text)

    style_rules = ""
    for font_file in font_files:
        font_name = os.path.splitext(font_file)[0]
        style_rules += f"""
        @font-face {{
            font-family: '{font_name}';
            src: url('{font_file}') format('truetype');
        }}"""

    body_content = ""
    for font_file in font_files:
        font_name = os.path.splitext(font_file)[0]
        body_content += f"""
    <div class="font-showcase">
        <h2>Font: <span class="font-spec">{font_name}</span></h2>
"""
        for size in FONT_SIZES_PT:
            body_content += f"""        <p style="font-family: '{font_name}'; font-size: {size}pt;">{size}: {escaped_sample_text}</p>
"""
        body_content += "    </div>"

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Font Test Report</title>
    <style>
        body {{ font-family: sans-serif; padding: 2em; color: #333; background-color: #fdfdfd; }}
        .font-showcase {{ border: 1px solid #ddd; padding: 1.5em; margin-bottom: 2em; border-radius: 8px; background-color: #fff; }}
        h1 {{ text-align: center; }}
        h2 {{ border-bottom: 2px solid #eee; padding-bottom: 0.5em; margin-top: 0; }}
        .font-spec {{ font-family: monospace; background-color: #f0f0f0; padding: 2px 6px; border-radius: 4px; }}
{style_rules}
    </style>
</head>
<body>
    <h1>Font Generation Test Report</h1>{body_content}
</body>
</html>"""

    report_path = os.path.join(output_dir, "index.html")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Successfully created HTML report at {report_path}")

# --- Main Execution ---
def main():
    """Main script to generate fonts and the report."""
    # Load glyph definitions from JSON
    json_path = os.path.join(SCRIPT_DIR, 'glyphs.json')
    with open(json_path, 'r') as f:
        json_definitions = json.load(f)

    generated_fonts = []
    for em_size in UNITS_PER_EM_VALUES:
        font_name = "neoclassical"
        glyphs = {}

        # Adjust vertical alignment by setting a baseline and shifting glyphs
        ascent = int(em_size * 0.8)
        descent = -(em_size - ascent)
        center_y = (ascent + descent) / 2.0
        y_shift = center_y - (em_size / 2.0)
        narrow_width = int(em_size / 4)


        # --- Define symbol glyphs (still using polygon method) ---
        bar_thickness = THIN_GLYPH_THICKNESS
        bar_height = em_size * 0.7
        x_center = narrow_width / 2
        y_bottom = (em_size - bar_height) / 2
        points_bar = [
            (x_center - bar_thickness / 2, y_bottom),
            (x_center + bar_thickness / 2, y_bottom),
            (x_center + bar_thickness / 2, y_bottom + bar_height),
            (x_center - bar_thickness / 2, y_bottom + bar_height),
        ]
        glyphs['|'] = {'type': 'polygon', 'points': shift_points(points_bar, y_shift), 'width': narrow_width}

        # Glyph '<'
        chevron_thickness = THIN_GLYPH_THICKNESS
        side_bearing_x = narrow_width * 0.2
        x_left_point = 2 * side_bearing_x
        x_right_base = narrow_width
        x1, y1 = x_right_base, em_size * 0.9
        x2, y2 = x_right_base, em_size * 0.9 - chevron_thickness
        x3, y3 = x_left_point + chevron_thickness, em_size * 0.5
        x4, y4 = x_right_base, em_size * 0.1 + chevron_thickness
        x5, y5 = x_right_base, em_size * 0.1
        x6, y6 = x_left_point, em_size * 0.5
        points_lt = [(x1,y1), (x2,y2), (x3,y3), (x4,y4), (x5,y5), (x6,y6)]
        glyphs['<'] = {'type': 'polygon', 'points': shift_points(points_lt, y_shift), 'width': narrow_width}

        # Glyph '>'
        points_gt = [(narrow_width - x, y) for x, y in points_lt]
        glyphs['>'] = {'type': 'polygon', 'points': shift_points(points_gt, y_shift), 'width': narrow_width}

        # Glyphs for '(' and ')'
        paren_thickness = THIN_GLYPH_THICKNESS
        paren_ry = em_size * 0.45
        paren_rx = em_size * 0.1  # Keep this relative to em_size for a 'bowed' appearance
        paren_cy = center_y
        side_bearing_x = narrow_width * 0.2 # Using a side bearing to position parentheses

        # Glyph '(' - left parenthesis
        paren_l_cx = narrow_width - side_bearing_x
        outer_arc_l = arc_poly(paren_l_cx, paren_cy, paren_rx, paren_ry, np.pi / 2, 3 * np.pi / 2)
        inner_arc_l = arc_poly(paren_l_cx, paren_cy, paren_rx - paren_thickness, paren_ry, 3 * np.pi / 2, np.pi / 2)
        points_l_paren = outer_arc_l + inner_arc_l
        glyphs['('] = {'type': 'polygon', 'points': points_l_paren, 'width': narrow_width}

        # Glyph ')' - right parenthesis
        paren_r_cx = side_bearing_x
        outer_arc_r = arc_poly(paren_r_cx, paren_cy, paren_rx, paren_ry, -np.pi / 2, np.pi / 2)
        inner_arc_r = arc_poly(paren_r_cx, paren_cy, paren_rx - paren_thickness, paren_ry, np.pi / 2, -np.pi / 2)
        points_r_paren = outer_arc_r + inner_arc_r
        glyphs[')'] = {'type': 'polygon', 'points': points_r_paren, 'width': narrow_width}

        # Add JSON-defined glyphs
        for char, definition in json_definitions.items():
            glyphs[char] = definition
            glyphs[char]['type'] = 'json_defined'

        output_file = os.path.join(OUTPUT_DIR, f"{font_name}.ttf")
        create_font(font_name, em_size, glyphs, output_file)
        generated_fonts.append(os.path.basename(output_file))

    generate_html_report(generated_fonts, OUTPUT_DIR)

if __name__ == "__main__":
    main()
