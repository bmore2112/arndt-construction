"""Generate the Storm Damage Checklist PDF for lead-gen download."""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

OUT = "arndt-storm-checklist.pdf"

ACCENT = HexColor("#e8451f")
ACCENT_DARK = HexColor("#c4471c")
INK = HexColor("#111111")
MUTE = HexColor("#444444")
DIM = HexColor("#777777")
LIGHT_BG = HexColor("#fafafa")
RULE = HexColor("#dddddd")

PHASE1 = [
    ("Check the Downspouts",
     "Inspect base grading zones where metal gutters discharge. Scan for dense piles of loose asphalt shingle granules.",
     "Close-up of loose granules piled at the downspout exit."),
    ("Inspect Exterior Siding and Trim",
     "Scan window metallic wraps, vinyl cladding, and garage doors for fresh wind dents, splitting, or debris impact scars.",
     "Wide shot of dented framing, plus a close-up alongside a coin for physical scale."),
    ("Scan for Missing Shingle Teeth",
     "Observe roof valleys from lawn positions. Identify dark backing underlayment showing exposed deck profiles.",
     "High-zoom focus snapshot pinpointing detached shingle slots."),
]
PHASE2 = [
    ("The Daylight Beam Check",
     "Enter the attic during full peak brightness hours. Keep panels dark and trace wood patterns upward.",
     "Image capturing exterior light pinpricks shining through roof timber panels."),
    ("Inspect Underlying Structural Rafters",
     "Guide your flashlight directly across main support rafters. Inspect lumber for damp tracking, active wet beads, or mold spores.",
     "Sharp photo logging water trace marks tracking down support rafters."),
    ("Track Interior Wall-to-Ceiling Plaster",
     "Trace top sheetrock joints near second-story frame levels. Spot swelling paint, texturing separations, or dark moisture stains.",
     "Close-up of internal wall moisture tracks or blistering drywall paint."),
]
PHASE3 = [
    ("Record the Storm Event Details",
     "Write down the exact date, time, and type of weather event. Pull the NOAA or local news report confirming wind speeds, hail size, or gust duration in your zip code.",
     "Screenshot of the NOAA Storm Events Database entry for your county on the event date."),
    ("Pull Your Homeowner Policy and Deductible",
     "Locate your declarations page. Note your deductible, wind/hail deductible (often higher and separate), and the claims-reporting window required by your carrier.",
     "Photo of the policy declarations page and the wind/hail deductible section."),
    ("Log Estimates, Calls, and Adjuster Visits",
     "Start a single-page timeline. Every call, every emailed estimate, every adjuster visit date — written in one place. Wins supplements when scope disputes happen.",
     "Photograph of the running claim timeline before each adjuster visit."),
]


def draw_wrapped(c, text, x, y, max_w, font, size, leading, color=INK):
    """Draw text wrapping to max_w. Returns the y position below last line."""
    c.setFont(font, size)
    c.setFillColor(color)
    words = text.split()
    line, lines = "", []
    for w in words:
        test = (line + " " + w).strip()
        if c.stringWidth(test, font, size) > max_w and line:
            lines.append(line)
            line = w
        else:
            line = test
    if line:
        lines.append(line)
    for ln in lines:
        c.drawString(x, y, ln)
        y -= leading
    return y


def draw_header(c, w, h):
    """Top brand band + header."""
    # Orange accent bar
    c.setFillColor(ACCENT)
    c.rect(0, h - 0.18 * inch, w, 0.18 * inch, fill=1, stroke=0)
    # Eyebrow
    y = h - 0.55 * inch
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(0.6 * inch, y, "● SOUTHERN MARYLAND STORM RESOURCE")
    # Title
    y -= 0.32 * inch
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(0.6 * inch, y, "ARNDT CONSTRUCTION")
    # Subtitle
    y -= 0.2 * inch
    c.setFillColor(MUTE)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(0.6 * inch, y, "ROOFING & SIDING  |  MHIC #115973")
    # Right-side contact card
    box_x, box_y, box_w, box_h = w - 2.9 * inch, h - 1.2 * inch, 2.3 * inch, 0.85 * inch
    c.setStrokeColor(INK)
    c.setLineWidth(1)
    c.rect(box_x, box_y, box_w, box_h, stroke=1, fill=0)
    c.setFillColor(DIM)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(box_x + 0.15 * inch, box_y + box_h - 0.2 * inch, "NEED IMMEDIATE HELP?")
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(box_x + 0.15 * inch, box_y + box_h - 0.45 * inch, "(443) 624-7508")
    c.setFillColor(DIM)
    c.setFont("Helvetica", 8)
    c.drawString(box_x + 0.15 * inch, box_y + 0.12 * inch, "Free Digital Damage Assessments")
    # Divider under header
    c.setStrokeColor(RULE)
    c.setLineWidth(1)
    c.line(0.6 * inch, h - 1.4 * inch, w - 0.6 * inch, h - 1.4 * inch)


def draw_intro(c, w, h, y):
    # Intro card with left orange border
    pad = 0.18 * inch
    card_x = 0.6 * inch
    card_w = w - 1.2 * inch
    # Heading
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(card_x + pad, y - 0.05 * inch, "Storm Damage & Insurance Checklist")
    y -= 0.28 * inch
    # Body
    body = "A step-by-step guide to documenting residential roof conditions before initiating a regional insurance claim."
    y = draw_wrapped(c, body, card_x + pad, y, card_w - 2 * pad, "Helvetica", 10, 13, MUTE)
    y -= 0.05 * inch
    # Warning
    warn_y = y - 0.05 * inch
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(card_x + pad, warn_y, "SAFETY WARNING:")
    c.setFillColor(INK)
    c.setFont("Helvetica", 9)
    warn = "Never walk directly on a damaged or wet roof. Conduct all inspections from ground level, balconies, or windows."
    end_y = draw_wrapped(c, warn, card_x + pad + 1.05 * inch, warn_y, card_w - 2 * pad - 1.05 * inch, "Helvetica", 9, 12, INK)
    # Left orange accent
    border_top = y + 0.5 * inch
    border_bottom = end_y - 0.05 * inch
    c.setFillColor(ACCENT)
    c.rect(card_x - 0.04 * inch, border_bottom, 0.05 * inch, border_top - border_bottom, fill=1, stroke=0)
    return end_y - 0.25 * inch


def draw_phase(c, w, num, title, items, y):
    """Draw a phase block. Returns new y."""
    left = 0.6 * inch
    right_max = w - 0.6 * inch
    # Numbered circle
    cx, cy, r = left + 0.15 * inch, y - 0.13 * inch, 0.13 * inch
    c.setFillColor(ACCENT)
    c.circle(cx, cy, r, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(cx, cy - 0.05 * inch, str(num))
    # Phase title
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(left + 0.45 * inch, y - 0.16 * inch, title.upper())
    y -= 0.32 * inch
    # Divider
    c.setStrokeColor(RULE)
    c.line(left, y, right_max, y)
    y -= 0.22 * inch
    # Items
    for title_, desc, photo in items:
        # checkbox
        box_x, box_y = left, y - 0.14 * inch
        c.setStrokeColor(INK)
        c.setLineWidth(1.2)
        c.rect(box_x, box_y, 0.16 * inch, 0.16 * inch, stroke=1, fill=0)
        # title
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(left + 0.32 * inch, y - 0.04 * inch, title_.upper())
        y -= 0.2 * inch
        # description
        y = draw_wrapped(c, desc, left + 0.32 * inch, y, right_max - left - 0.32 * inch, "Helvetica", 9.5, 12.5, MUTE)
        y -= 0.04 * inch
        # photo required
        photo_text = "PHOTO REQUIRED: " + photo
        c.setFillColor(ACCENT_DARK)
        c.setFont("Helvetica-Bold", 8)
        y = draw_wrapped(c, photo_text, left + 0.32 * inch, y, right_max - left - 0.32 * inch, "Helvetica-Bold", 8, 11, ACCENT_DARK)
        y -= 0.22 * inch
    return y


def draw_footer(c, w, h):
    """Bottom of page: contact + meta line."""
    y = 0.6 * inch
    c.setStrokeColor(RULE)
    c.line(0.6 * inch, y + 0.55 * inch, w - 0.6 * inch, y + 0.55 * inch)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(0.6 * inch, y + 0.35 * inch, "Next step: call us at (443) 624-7508 or book a free inspection at arndtconstructionmd.com")
    c.setFillColor(DIM)
    c.setFont("Helvetica", 8)
    c.drawString(0.6 * inch, y + 0.18 * inch, "We meet your adjuster on the roof and supplement the scope when damage is missed.")
    c.setFillColor(DIM)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(0.6 * inch, y, "ARNDT CONSTRUCTION  ·  MHIC #115973  ·  11410 RAWHIDE ROAD, LUSBY, MD 20657  ·  ARNDTCONSTRUCTIONMD.COM")


def page_continue_header(c, w, h, page_num):
    """Smaller header for continuation pages."""
    c.setFillColor(ACCENT)
    c.rect(0, h - 0.12 * inch, w, 0.12 * inch, fill=1, stroke=0)
    c.setFillColor(DIM)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(0.6 * inch, h - 0.38 * inch, "ARNDT CONSTRUCTION  ·  STORM CHECKLIST")
    c.drawRightString(w - 0.6 * inch, h - 0.38 * inch, f"PAGE {page_num}  ·  (443) 624-7508")
    c.setStrokeColor(RULE)
    c.line(0.6 * inch, h - 0.55 * inch, w - 0.6 * inch, h - 0.55 * inch)


def build_pdf():
    c = canvas.Canvas(OUT, pagesize=LETTER)
    c.setTitle("Arndt Construction Storm Damage & Insurance Checklist")
    c.setAuthor("Arndt Construction")
    c.setSubject("Storm damage roof inspection and insurance claim checklist for Maryland homeowners")
    c.setKeywords("storm damage, roof inspection, insurance claim, Maryland, Calvert County, Arndt Construction")

    w, h = LETTER

    # PAGE 1: Header + Intro + Phase 1
    draw_header(c, w, h)
    y = h - 1.55 * inch
    y = draw_intro(c, w, h, y)
    y -= 0.05 * inch
    y = draw_phase(c, w, 1, "Phase 1: Immediate Ground Inspection", PHASE1, y)
    draw_footer(c, w, h)
    c.showPage()

    # PAGE 2: Phase 2 + Phase 3
    page_continue_header(c, w, h, 2)
    y = h - 0.85 * inch
    y = draw_phase(c, w, 2, "Phase 2: Interior Attic & Ceiling Audit", PHASE2, y)
    y -= 0.1 * inch
    y = draw_phase(c, w, 3, "Phase 3: Adjuster Case Record", PHASE3, y)
    draw_footer(c, w, h)
    c.showPage()

    c.save()
    print(f"Built {OUT} ({os.path.getsize(OUT)} bytes, {os.path.getsize(OUT)//1024} KB)")


if __name__ == "__main__":
    build_pdf()
