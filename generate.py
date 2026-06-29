#!/usr/bin/env python3
"""Crestline Remodeling static site generator.

Produces every HTML page with consistent navigation, full SEO (LocalBusiness
JSON-LD, unique meta + Open Graph, canonical), and FAQPage JSON-LD with a
visible accordion on every service and area page. Run: python3 generate.py
"""
import json
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
DOMAIN = "https://crestlineremodeling.com"
PHONE = "[PHONE TBD]"
EMAIL = "[EMAIL TBD]"
BIZ = "Crestline Remodeling"
ADDR_CITY = "Highland Park"
ADDR_REGION = "IL"
ADDR_ZIP = "60035"
ADDR_STREET = "1850 Green Bay Road, Suite 210"
GEO_LAT = "42.1817"
GEO_LON = "-87.8003"
FOUNDED = "2009"
LAST_UPDATED = "June 2026"

# ---------------------------------------------------------------------------
# DATA
# ---------------------------------------------------------------------------

SERVICES = [
    {
        "slug": "kitchen-remodeling",
        "name": "Kitchen Remodeling",
        "short": "Kitchens",
        "kw": "kitchen remodeling",
        "icon": "&#9737;",
        "meta": "Kitchen remodeling in Highland Park, IL & the North Shore. Custom cabinetry, quartz counters & open layouts from Crestline Remodeling. Free design consult.",
        "tagline": "Custom kitchens built for how North Shore families actually live.",
        "intro": [
            "Your kitchen is the hardest-working room in the house, and on the North Shore it&rsquo;s also the room guests gravitate to. Crestline Remodeling designs and builds kitchens that balance everyday function with the timeless, gallery-quality finishes Highland Park homeowners expect.",
            "Since {founded}, our design-build team has completed more than 600 kitchen projects across Chicago&rsquo;s North Shore &mdash; from compact galley updates to full structural reconfigurations that open the kitchen to the family room.",
        ],
        "included": [
            "Custom and semi-custom cabinetry from regional millwork partners",
            "Quartz, granite, and natural stone countertop fabrication",
            "Structural wall removal and load-bearing beam engineering",
            "Professional-grade appliance integration and panel-ready fronts",
            "Hardwood, tile, and large-format porcelain flooring",
            "Recessed, pendant, and under-cabinet lighting design",
        ],
        "cost_low": "45,000",
        "cost_high": "120,000",
        "cost_note": "A mid-range Highland Park kitchen remodel typically lands between $65,000 and $95,000; high-end projects with custom cabinetry and structural changes can exceed $150,000.",
        "stat": ("600+", "kitchens completed since 2009"),
        "faqs": [
            ("What does a kitchen remodel cost in Highland Park?",
             "Most full kitchen remodels in Highland Park range from $45,000 to $120,000, with the majority of our projects landing between $65,000 and $95,000. The biggest cost drivers are cabinetry (typically 30&ndash;35% of the budget), countertops, and whether you&rsquo;re moving walls or plumbing. Crestline provides a fixed-price proposal after the design phase so there are no mid-project surprises."),
            ("How long does a kitchen remodel take?",
             "A typical North Shore kitchen remodel takes 8 to 12 weeks of on-site construction, preceded by 4 to 6 weeks of design and material selection. Projects involving structural changes, custom cabinetry lead times, or permit-heavy scopes can run 14 to 16 weeks. We provide a week-by-week schedule before demolition begins."),
            ("Do I need a permit to remodel my kitchen?",
             "Yes &mdash; any kitchen remodel involving electrical, plumbing, or structural work requires a permit from the City of Highland Park or your local municipality. As a licensed and insured design-build firm, Crestline handles all permit applications, inspections, and code compliance on your behalf."),
        ],
    },
    {
        "slug": "bathroom-remodeling",
        "name": "Bathroom Remodeling",
        "short": "Bathrooms",
        "kw": "bathroom remodeling",
        "icon": "&#9748;",
        "meta": "Bathroom remodeling in Highland Park & North Shore IL. Spa-style primary baths, walk-in showers & custom vanities by Crestline Remodeling. Book a consult.",
        "tagline": "Spa-quality bathrooms engineered to last in older North Shore homes.",
        "intro": [
            "From compact powder rooms to expansive primary suites, Crestline Remodeling transforms North Shore bathrooms into private retreats. We specialize in the waterproofing, ventilation, and substrate detailing that older Highland Park homes demand &mdash; the work behind the tile that determines whether a bathroom lasts 5 years or 25.",
            "Our crews have completed over 450 bathroom remodels, including curbless walk-in showers, heated floors, and steam systems that hold up to the realities of Midwest seasons.",
        ],
        "included": [
            "Custom walk-in, curbless, and frameless glass showers",
            "Full waterproofing systems (Schluter / liquid membrane)",
            "Freestanding soaking tubs and integrated tub-shower combinations",
            "Custom vanities, double-bowl configurations, and stone tops",
            "Heated tile flooring and towel warming systems",
            "Upgraded ventilation, lighting, and humidity control",
        ],
        "cost_low": "18,000",
        "cost_high": "65,000",
        "cost_note": "A guest or hall bath typically runs $18,000&ndash;$35,000; a full primary suite remodel on the North Shore commonly runs $40,000&ndash;$65,000+.",
        "stat": ("450+", "bathrooms remodeled"),
        "faqs": [
            ("What does a bathroom remodel cost in Highland Park?",
             "Bathroom remodels in Highland Park range from about $18,000 for a guest bath refresh to $65,000+ for a full primary suite with a custom shower, heated floors, and double vanity. Tile selection, glass enclosures, and moving plumbing fixtures are the main cost variables. Crestline gives you a fixed-price proposal before any demolition."),
            ("How long does a bathroom remodel take?",
             "Most bathroom remodels take 4 to 7 weeks on site. A straightforward guest bath can be done in 3 to 4 weeks, while a primary suite with custom tile, a steam shower, and structural changes may take 7 to 9 weeks. Waterproofing and tile work cannot be rushed without risking failures down the line."),
            ("Can you remodel a bathroom in an older North Shore home?",
             "Absolutely &mdash; it&rsquo;s one of our specialties. Many Highland Park, Lake Forest, and Winnetka homes were built before 1960 and have undersized plumbing, cast-iron stacks, and knob-and-tube wiring. We assess and upgrade these systems as part of the project so your new bathroom is built on a sound foundation."),
        ],
    },
    {
        "slug": "basement-finishing",
        "name": "Basement Finishing",
        "short": "Basement Finishing",
        "kw": "basement finishing",
        "icon": "&#9968;",
        "meta": "Basement finishing in Highland Park & the North Shore. Add living space, home theaters, gyms & in-law suites with Crestline Remodeling. Free estimate.",
        "tagline": "Turn an unused basement into the most-used floor of your home.",
        "intro": [
            "A finished basement is the most cost-effective square footage you can add to a North Shore home &mdash; no new foundation, no roofline changes. Crestline Remodeling finishes basements with proper moisture management, egress, and insulation so the space stays comfortable and dry year-round.",
            "We&rsquo;ve finished basements as media rooms, home gyms, wine cellars, guest suites, and full in-law apartments, adding an average of 900&ndash;1,400 square feet of usable living space.",
        ],
        "included": [
            "Moisture mitigation, sump systems, and vapor barriers",
            "Egress window installation for code-compliant bedrooms",
            "Home theaters, gyms, playrooms, and wet bars",
            "Full in-law and au pair suites with kitchenettes",
            "Spray-foam and rigid insulation for year-round comfort",
            "Bathroom additions with ejector pump systems",
        ],
        "cost_low": "35,000",
        "cost_high": "110,000",
        "cost_note": "A basic finished basement runs $35,000&ndash;$55,000; adding a bathroom, wet bar, or in-law suite pushes projects to $75,000&ndash;$110,000+.",
        "stat": ("1,200", "sq ft added on average"),
        "faqs": [
            ("What does it cost to finish a basement in Highland Park?",
             "Finishing a basement in Highland Park typically costs $35,000 to $110,000 depending on scope. A straightforward finish with a rec room and storage runs $35,000&ndash;$55,000; adding a full bathroom, wet bar, or in-law suite with a kitchenette brings the total to $75,000&ndash;$110,000+. Moisture control and egress are non-negotiable line items we never skip."),
            ("Do I need an egress window to finish my basement?",
             "If your finished basement will include a bedroom, Illinois code requires a compliant egress window for emergency exit. Even when not required, we recommend egress windows for the natural light and resale value they add. Crestline handles the excavation, window well, and permitting as part of the project."),
            ("How do you keep a finished basement from getting damp?",
             "We start with the water before the walls: assessing grading, sump performance, and any past seepage, then installing vapor barriers, proper insulation, and dehumidification. On the North Shore&rsquo;s clay soils this step is critical. We won&rsquo;t finish a basement we can&rsquo;t keep dry, and we stand behind the moisture work in writing."),
        ],
    },
    {
        "slug": "home-additions",
        "name": "Home Additions",
        "short": "Home Additions",
        "kw": "home additions",
        "icon": "&#127968;",
        "meta": "Home additions in Highland Park & North Shore IL. Room additions, second stories & primary suites by Crestline Remodeling design-build. Free consultation.",
        "tagline": "More room to grow without leaving the neighborhood you love.",
        "intro": [
            "When a North Shore family outgrows their home but loves their location, an addition beats moving. Crestline Remodeling designs and builds additions that look like they were always part of the house &mdash; matching rooflines, trim profiles, and brick or siding so there&rsquo;s no &lsquo;before and after&rsquo; seam.",
            "From single-room bump-outs to full second-story additions, we manage architecture, engineering, permitting, and construction under one roof, which keeps schedules tight and accountability clear.",
        ],
        "included": [
            "First-floor room additions and kitchen bump-outs",
            "Full and partial second-story additions",
            "Primary bedroom suites with walk-in closets and baths",
            "Sunrooms, four-season rooms, and mudroom expansions",
            "Foundation, framing, and structural engineering",
            "Seamless roofline, siding, and masonry matching",
        ],
        "cost_low": "90,000",
        "cost_high": "400,000",
        "cost_note": "Room additions on the North Shore generally run $90,000&ndash;$200,000; second-story additions and large primary suites commonly run $250,000&ndash;$400,000+.",
        "stat": ("$300", "avg cost per sq ft, finished"),
        "faqs": [
            ("What does a home addition cost in Highland Park?",
             "Home additions in Highland Park typically cost $90,000 to $400,000+ depending on size and complexity. As a rule of thumb, finished additions on the North Shore run roughly $250&ndash;$400 per square foot, with second-story additions costing more per foot than ground-level builds due to structural reinforcement. We provide a detailed fixed-price proposal after design."),
            ("Do I need a permit and zoning approval for an addition?",
             "Yes. Additions require building permits and must comply with local setback, height, and lot-coverage rules, which vary by municipality across the North Shore. Highland Park, Winnetka, and Lake Forest each have distinct zoning codes. Crestline manages the full permitting and variance process, including any required zoning board appearances."),
            ("How long does a home addition take to build?",
             "Most additions take 4 to 8 months from groundbreaking to completion, plus 6 to 10 weeks of design and permitting beforehand. A single-room addition may finish in 3 to 4 months; a full second story typically runs 6 to 8 months. Weather and permit timelines are the biggest schedule variables on the North Shore."),
        ],
    },
    {
        "slug": "whole-house-renovation",
        "name": "Whole-House Renovation",
        "short": "Whole-House Renovation",
        "kw": "whole-house renovation",
        "icon": "&#127962;",
        "meta": "Whole-house renovation in Highland Park & the North Shore. Crestline Remodeling reimagines older homes top-to-bottom with one design-build team. Book a consult.",
        "tagline": "Reimagine an entire home &mdash; with one team and one plan.",
        "intro": [
            "The North Shore is full of beautiful, character-rich homes with layouts that no longer fit modern life. A whole-house renovation lets you keep the address, the trees, and the architecture while rebuilding the way the home functions from the inside out.",
            "Crestline Remodeling acts as your single point of accountability across architecture, structural engineering, mechanical systems, and finishes. We&rsquo;ve renovated homes from 1920s Highland Park Tudors to mid-century Glencoe ranches, modernizing systems while preserving the details that give these homes their value.",
        ],
        "included": [
            "Full architectural redesign and space planning",
            "Kitchen, bathroom, and living-space reconfiguration",
            "Electrical, plumbing, and HVAC system replacement",
            "Window, insulation, and energy-efficiency upgrades",
            "Historic detail preservation and restoration",
            "Whole-home flooring, millwork, and finish packages",
        ],
        "cost_low": "250,000",
        "cost_high": "900,000",
        "cost_note": "Whole-house renovations on the North Shore typically run $250,000&ndash;$900,000+, or roughly $150&ndash;$350 per square foot depending on finish level and structural scope.",
        "stat": ("100%", "single-team accountability"),
        "faqs": [
            ("What does a whole-house renovation cost on the North Shore?",
             "Whole-house renovations in Highland Park and across the North Shore typically run $250,000 to $900,000+, or about $150&ndash;$350 per square foot. The range is wide because scope varies enormously &mdash; from cosmetic refreshes to gut renovations that replace every system. After a discovery and design phase, Crestline delivers a fixed-price proposal broken down room by room."),
            ("Can we live in the house during a whole-house renovation?",
             "Sometimes, but for gut renovations we usually recommend relocating, both for safety and to compress the schedule. Phased renovations where you occupy part of the home are possible and add time and cost. We&rsquo;ll walk you through both options and their schedule and budget implications during planning."),
            ("How long does a whole-house renovation take?",
             "Most whole-house renovations take 8 to 14 months of construction, preceded by 2 to 4 months of design, engineering, and permitting. Gut renovations with structural changes and long-lead custom materials trend toward the upper end. Crestline provides a master schedule with milestone dates before construction begins."),
        ],
    },
    {
        "slug": "design-build",
        "name": "Design-Build Services",
        "short": "Design-Build",
        "kw": "design-build remodeling",
        "icon": "&#9999;",
        "meta": "Design-build remodeling in Highland Park & North Shore IL. One Crestline team for design, engineering & construction &mdash; fewer surprises, faster timelines.",
        "tagline": "One team, one contract, from first sketch to final walkthrough.",
        "intro": [
            "The traditional model &mdash; hire an architect, then bid the drawings to contractors &mdash; is how budgets blow up and blame gets passed. Crestline Remodeling&rsquo;s design-build approach puts design, engineering, and construction under one roof and one contract, so the price you design to is the price you build at.",
            "Our in-house designers and project managers collaborate from day one, which means cost is engineered into the design rather than discovered after. North Shore homeowners get realistic budgets earlier, fewer change orders, and a single point of accountability throughout.",
        ],
        "included": [
            "In-house architectural and interior design",
            "Real-time budgeting during the design phase",
            "Structural and mechanical engineering coordination",
            "3D renderings and material selection support",
            "Permit management and code compliance",
            "Dedicated project manager from start to finish",
        ],
        "cost_low": "5,000",
        "cost_high": "35,000",
        "cost_note": "Design-phase fees typically run $5,000&ndash;$35,000 depending on project scope, and are credited toward construction when you proceed with Crestline.",
        "stat": ("90%", "of clients avoid major change orders"),
        "faqs": [
            ("How is design-build different from hiring an architect and a contractor separately?",
             "In design-build, one firm handles design and construction under a single contract, so cost feedback happens during design instead of after. The traditional design-bid-build model splits responsibility, which often leads to over-designed plans, surprise bids, and finger-pointing. Crestline&rsquo;s clients see realistic numbers earlier and experience roughly 90% fewer major change orders."),
            ("What does the design phase cost?",
             "Crestline&rsquo;s design-phase fees typically range from $5,000 to $35,000 depending on the size and complexity of your project. This covers design development, 3D renderings, engineering coordination, and a fixed-price construction proposal. The design fee is credited back toward your construction contract when you move forward with us."),
            ("Do I still get input on the design?",
             "Completely. Design-build doesn&rsquo;t mean less creative control &mdash; it means your designer and builder are collaborating on your behalf. You&rsquo;ll review floor plans, 3D renderings, and material selections at every milestone, with cost implications shown in real time so your choices are always informed."),
        ],
    },
    {
        "slug": "flooring",
        "name": "Flooring",
        "short": "Flooring",
        "kw": "flooring installation",
        "icon": "&#9638;",
        "meta": "Flooring installation in Highland Park & North Shore IL. Hardwood, tile, engineered & luxury vinyl, professionally installed by Crestline Remodeling.",
        "tagline": "Floors that anchor the whole room &mdash; installed to last.",
        "intro": [
            "Flooring sets the tone for every renovation, and on the North Shore it has to handle radiant heat, seasonal humidity swings, and decades of foot traffic. Crestline Remodeling installs and refinishes hardwood, tile, stone, and engineered floors with the subfloor prep and acclimation that prevents cupping, gapping, and cracked grout.",
            "Whether you&rsquo;re refinishing original oak in a Highland Park colonial or installing large-format porcelain in a modern kitchen, we sweat the details under the surface that determine how long a floor lasts.",
        ],
        "included": [
            "Solid and engineered hardwood installation",
            "Hardwood sanding, staining, and refinishing",
            "Porcelain, ceramic, and natural stone tile",
            "Luxury vinyl plank and waterproof flooring",
            "Radiant-heat-compatible flooring systems",
            "Subfloor leveling, prep, and moisture testing",
        ],
        "cost_low": "8,000",
        "cost_high": "45,000",
        "cost_note": "Whole-floor projects typically run $8,000&ndash;$45,000; hardwood installation averages $9&ndash;$16 per square foot and refinishing $4&ndash;$8 per square foot on the North Shore.",
        "stat": ("25+ yrs", "lifespan on properly installed hardwood"),
        "faqs": [
            ("What does new flooring cost in Highland Park?",
             "Flooring projects in Highland Park typically run $8,000 to $45,000 depending on material and square footage. Hardwood installation averages $9&ndash;$16 per square foot installed, refinishing existing hardwood runs $4&ndash;$8 per square foot, and tile varies widely with material. Crestline quotes a fixed price after measuring and assessing your subfloor."),
            ("Should I refinish or replace my hardwood floors?",
             "If your existing hardwood is solid (not engineered) and has at least 1/8 inch of wear layer left, refinishing is far more economical and preserves the character of an older North Shore home. We replace flooring when there&rsquo;s water damage, structural subfloor issues, or when you&rsquo;re changing the layout. We&rsquo;ll assess and give you an honest recommendation."),
            ("Can you install flooring over radiant heat?",
             "Yes. Many North Shore homes have radiant floor heating, which requires flooring rated for it and careful acclimation. Engineered hardwood, tile, and certain luxury vinyl products perform best over radiant systems. We follow manufacturer specs precisely to protect both your floor and your warranty."),
        ],
    },
    {
        "slug": "cabinetry",
        "name": "Custom Cabinetry",
        "short": "Custom Cabinetry",
        "kw": "custom cabinetry",
        "icon": "&#9707;",
        "meta": "Custom cabinetry in Highland Park & North Shore IL. Built-ins, kitchen & bath cabinets and millwork crafted and installed by Crestline Remodeling.",
        "tagline": "Cabinetry built for your space, not pulled off a shelf.",
        "intro": [
            "Stock cabinets compromise on fit, finish, and storage. Crestline Remodeling designs and installs custom and semi-custom cabinetry that uses every inch &mdash; built around your ceiling heights, appliance specs, and the way you actually cook and store.",
            "Working with regional millwork shops, we deliver furniture-grade kitchen cabinetry, bathroom vanities, mudroom lockers, libraries, and built-in entertainment walls that fit North Shore homes precisely and last for decades.",
        ],
        "included": [
            "Custom and semi-custom kitchen cabinetry",
            "Bathroom vanities and linen storage",
            "Library, office, and built-in bookcases",
            "Mudroom lockers and entryway storage systems",
            "Entertainment centers and fireplace surrounds",
            "Paint-grade and stain-grade finish options",
        ],
        "cost_low": "12,000",
        "cost_high": "75,000",
        "cost_note": "A full kitchen&rsquo;s custom cabinetry typically runs $25,000&ndash;$60,000; individual built-ins commonly run $4,000&ndash;$15,000 each.",
        "stat": ("100%", "built to your exact dimensions"),
        "faqs": [
            ("What does custom cabinetry cost in Highland Park?",
             "Custom cabinetry in Highland Park typically runs $12,000 to $75,000+ depending on scope. A full kitchen&rsquo;s cabinetry usually runs $25,000&ndash;$60,000, while individual built-ins like a home office or entertainment wall run $4,000&ndash;$15,000 each. Custom work costs more than stock but eliminates wasted space and fits your home exactly."),
            ("What&rsquo;s the difference between custom and semi-custom cabinetry?",
             "Semi-custom cabinetry starts from standard sizes with modifications to dimensions, finishes, and storage features &mdash; a great value for many projects. Fully custom cabinetry is built from scratch to any dimension, finish, and configuration, ideal for unusual spaces, tall ceilings, and furniture-grade built-ins. We&rsquo;ll recommend the right level for your goals and budget."),
            ("How long does custom cabinetry take to build?",
             "Custom cabinetry typically takes 6 to 12 weeks from final design approval to delivery, depending on the shop&rsquo;s queue and the complexity of your order. We factor this lead time into the overall project schedule so cabinetry arrives exactly when the space is ready, avoiding storage and damage risk."),
        ],
    },
    {
        "slug": "deck-patio",
        "name": "Decks & Patios",
        "short": "Decks & Patios",
        "kw": "deck and patio construction",
        "icon": "&#9728;",
        "meta": "Deck & patio construction in Highland Park & North Shore IL. Composite decks, paver patios & outdoor living spaces by Crestline Remodeling. Free estimate.",
        "tagline": "Outdoor living spaces built for short summers and long winters.",
        "intro": [
            "North Shore summers are short and precious, and a well-built deck or patio extends your living space into them. Crestline Remodeling designs and builds outdoor spaces engineered for the Chicago freeze-thaw cycle &mdash; proper footings, drainage, and materials that won&rsquo;t heave, rot, or fade.",
            "From low-maintenance composite decks to full paver patios with outdoor kitchens and fire features, we build outdoor rooms that connect seamlessly to the house and hold up to decades of Midwest weather.",
        ],
        "included": [
            "Composite and hardwood decking",
            "Paver and natural stone patios",
            "Outdoor kitchens and built-in grills",
            "Fire pits, fireplaces, and seat walls",
            "Pergolas, pavilions, and shade structures",
            "Frost-depth footings and integrated drainage",
        ],
        "cost_low": "15,000",
        "cost_high": "120,000",
        "cost_note": "A composite deck typically runs $18,000&ndash;$45,000; a full paver patio with outdoor kitchen and fire feature commonly runs $50,000&ndash;$120,000+.",
        "stat": ("42 in.", "frost-depth footings, built to code"),
        "faqs": [
            ("What does a deck or patio cost in Highland Park?",
             "Decks and patios in Highland Park typically run $15,000 to $120,000+. A composite deck usually runs $18,000&ndash;$45,000, while a full paver patio with an outdoor kitchen, fire feature, and seat walls can run $50,000&ndash;$120,000+. Footings, drainage, and material grade are the biggest cost factors. Crestline provides a fixed-price proposal after a site assessment."),
            ("Do I need a permit to build a deck on the North Shore?",
             "Yes &mdash; most decks and many patios require permits, and North Shore municipalities enforce setback, height, and railing codes strictly. Decks over 30 inches off grade have specific railing and footing requirements. Crestline pulls all permits and builds to code, including the 42-inch frost-depth footings Illinois requires to prevent heaving."),
            ("What lasts longer &mdash; wood or composite decking?",
             "Composite decking lasts 25&ndash;30 years with virtually no maintenance, while pressure-treated wood lasts 10&ndash;15 years and needs annual sealing. Premium hardwoods like Ipe can last 40+ years but require upkeep. For most North Shore homeowners, composite offers the best balance of longevity and low maintenance against our harsh freeze-thaw cycles."),
        ],
    },
    {
        "slug": "aging-in-place",
        "name": "Aging-in-Place Remodeling",
        "short": "Aging in Place",
        "kw": "aging-in-place remodeling",
        "icon": "&#9874;",
        "meta": "Aging-in-place remodeling in Highland Park & North Shore IL. Accessible bathrooms, zero-step entries & universal design by Crestline Remodeling.",
        "tagline": "Stay in the home you love &mdash; safely, for decades to come.",
        "intro": [
            "Many North Shore homeowners want to stay in their homes as they age, but homes built decades ago weren&rsquo;t designed for it. Crestline Remodeling specializes in aging-in-place and universal design renovations that add safety and accessibility without making a home feel clinical.",
            "We hold the Certified Aging-in-Place Specialist (CAPS) credential and design modifications that look like intentional upgrades &mdash; curbless showers, wider doorways, and first-floor suites &mdash; so homes remain beautiful and become barrier-free.",
        ],
        "included": [
            "Curbless, roll-in walk-in showers with grab bars",
            "First-floor primary suite conversions",
            "Widened doorways and hallways for mobility",
            "Zero-step entries and exterior ramps",
            "Comfort-height fixtures and accessible cabinetry",
            "Improved lighting and slip-resistant flooring",
        ],
        "cost_low": "10,000",
        "cost_high": "90,000",
        "cost_note": "Targeted modifications like an accessible bathroom run $15,000&ndash;$35,000; a full first-floor suite conversion can run $60,000&ndash;$90,000+.",
        "stat": ("CAPS", "certified aging-in-place specialists"),
        "faqs": [
            ("What does aging-in-place remodeling cost in Highland Park?",
             "Aging-in-place projects in Highland Park typically run $10,000 to $90,000+ depending on scope. A single accessible bathroom with a curbless shower and grab bars runs $15,000&ndash;$35,000, while converting a first-floor room into a full primary suite with an accessible bath can run $60,000&ndash;$90,000+. We prioritize the changes with the biggest safety impact first."),
            ("What is universal design?",
             "Universal design creates spaces usable by people of all ages and abilities without looking like medical modifications. Think curbless showers, lever handles, comfort-height counters, and wider doorways that benefit everyone &mdash; from young children to grandparents. Crestline&rsquo;s CAPS-certified team designs these features to blend seamlessly into your home&rsquo;s style."),
            ("Are aging-in-place modifications covered by insurance or Medicare?",
             "Standard homeowners insurance and Medicare generally don&rsquo;t cover home modifications, though some long-term care insurance policies, VA benefits, and Illinois assistance programs may help. We&rsquo;re happy to provide detailed documentation for any program you&rsquo;re applying through, and we can phase the work to fit your budget and timeline."),
        ],
    },
]

AREAS = [
    {"slug": "highland-park", "name": "Highland Park", "zip": "60035", "pop": "30,000",
     "blurb": "Crestline Remodeling is headquartered in Highland Park, and it&rsquo;s the community we know best. From the lakefront estates near Ravinia to the mid-century homes of Sherwood Forest, we&rsquo;ve remodeled across every Highland Park neighborhood.",
     "note": "Highland Park&rsquo;s housing stock spans 1920s Tudors, mid-century ranches, and lakefront estates &mdash; each with distinct structural and permitting considerations we know intimately."},
    {"slug": "deerfield", "name": "Deerfield", "zip": "60015", "pop": "19,000",
     "blurb": "Just west of Highland Park, Deerfield is a community of established family homes where remodeling and additions are popular as families put down long-term roots.",
     "note": "Many Deerfield homes were built in the 1960s and 70s and are prime candidates for kitchen opens, primary-suite additions, and basement finishing."},
    {"slug": "lake-forest", "name": "Lake Forest", "zip": "60045", "pop": "19,000",
     "blurb": "Lake Forest&rsquo;s historic estates and architecturally significant homes demand a builder who respects original detail. Crestline pairs preservation craftsmanship with modern systems.",
     "note": "Lake Forest has strict historic-preservation and architectural review standards; we&rsquo;re experienced in navigating the city&rsquo;s review process and matching period detail."},
    {"slug": "glencoe", "name": "Glencoe", "zip": "60022", "pop": "9,000",
     "blurb": "Glencoe blends architecturally distinguished homes with leafy privacy. Crestline remodels here range from kitchen and bath updates to full whole-house renovations.",
     "note": "Glencoe&rsquo;s mix of historic and architect-designed homes calls for sensitive renovation that preserves character while modernizing systems and layouts."},
    {"slug": "winnetka", "name": "Winnetka", "zip": "60093", "pop": "12,500",
     "blurb": "Winnetka is home to some of the North Shore&rsquo;s most beautiful older homes. Crestline modernizes them for today&rsquo;s families while honoring their original architecture.",
     "note": "Winnetka enforces detailed zoning and lot-coverage rules; our team manages the variance and permitting process that larger Winnetka projects often require."},
    {"slug": "wilmette", "name": "Wilmette", "zip": "60091", "pop": "27,000",
     "blurb": "Wilmette&rsquo;s walkable neighborhoods and classic homes make it a favorite for young families. Crestline handles everything from kitchen remodels to second-story additions here.",
     "note": "Wilmette&rsquo;s older homes near the lake and the village center frequently need updated electrical, plumbing, and insulation alongside cosmetic remodeling."},
    {"slug": "kenilworth", "name": "Kenilworth", "zip": "60043", "pop": "2,500",
     "blurb": "Kenilworth is one of the most prestigious and architecturally protected villages on the North Shore. Crestline delivers the craftsmanship and discretion these homes require.",
     "note": "As a planned community with significant historic homes, Kenilworth demands meticulous attention to architectural detail and a careful, low-impact construction process."},
    {"slug": "northbrook", "name": "Northbrook", "zip": "60062", "pop": "35,000",
     "blurb": "Northbrook&rsquo;s spacious lots and mid-century homes are ideal for additions, basement finishing, and open-concept renovations. Crestline is active throughout the village.",
     "note": "Northbrook&rsquo;s larger lots make additions and outdoor living projects especially popular; many homes here also benefit from 1970s-era system updates."},
    {"slug": "glenview", "name": "Glenview", "zip": "60025", "pop": "48,000",
     "blurb": "Glenview ranges from established neighborhoods to newer developments. Crestline handles both updating older homes and customizing newer construction to fit growing families.",
     "note": "Glenview&rsquo;s wide range of housing ages means projects span everything from historic updates to reconfiguring 1990s and 2000s floor plans."},
    {"slug": "evanston", "name": "Evanston", "zip": "60201", "pop": "78,000",
     "blurb": "Evanston&rsquo;s historic homes, two-flats, and lakefront properties offer endless renovation potential. Crestline brings design-build expertise to this architecturally rich city.",
     "note": "Evanston has active historic districts and detailed permitting; we&rsquo;re experienced with the city&rsquo;s review process and its older, often pre-1940 housing stock."},
    {"slug": "skokie", "name": "Skokie", "zip": "60076", "pop": "67,000",
     "blurb": "Skokie&rsquo;s solid mid-century homes are perfect candidates for modernizing kitchens, finishing basements, and adding space. Crestline serves families across the village.",
     "note": "Skokie&rsquo;s post-war brick homes are well-built but often have dated layouts and systems that respond well to open-concept remodels and updates."},
    {"slug": "buffalo-grove", "name": "Buffalo Grove", "zip": "60089", "pop": "43,000",
     "blurb": "Buffalo Grove&rsquo;s family-oriented neighborhoods favor functional remodels &mdash; kitchen updates, finished basements, and additions that grow with the family.",
     "note": "Many Buffalo Grove homes date to the 1970s&ndash;90s and are ideal for kitchen and bath modernization and basement build-outs."},
    {"slug": "lincolnshire", "name": "Lincolnshire", "zip": "60069", "pop": "7,400",
     "blurb": "Lincolnshire&rsquo;s wooded lots and custom homes suit high-end renovations and additions. Crestline delivers the quality these properties command.",
     "note": "Lincolnshire&rsquo;s larger custom homes often call for sophisticated whole-house renovations, primary-suite additions, and outdoor living spaces."},
    {"slug": "vernon-hills", "name": "Vernon Hills", "zip": "60061", "pop": "26,000",
     "blurb": "Vernon Hills combines newer subdivisions with established neighborhoods. Crestline customizes homes here for families looking to add space and modern finishes.",
     "note": "Vernon Hills homes from the 1980s&ndash;2000s frequently benefit from kitchen opens, finished basements, and updated finishes throughout."},
    {"slug": "libertyville", "name": "Libertyville", "zip": "60048", "pop": "20,000",
     "blurb": "Libertyville&rsquo;s charming downtown and mix of historic and newer homes make it a rewarding place to remodel. Crestline serves the full range of project types here.",
     "note": "Libertyville blends century-old homes near downtown with newer subdivisions, so our work spans historic restoration and contemporary updates alike."},
    {"slug": "bannockburn", "name": "Bannockburn", "zip": "60015", "pop": "1,500",
     "blurb": "Bannockburn&rsquo;s expansive estate lots and custom homes call for premium craftsmanship. Crestline delivers high-end renovations and additions throughout the village.",
     "note": "Bannockburn&rsquo;s large estate properties favor whole-house renovations, luxury kitchen and bath remodels, and substantial additions."},
    {"slug": "riverwoods", "name": "Riverwoods", "zip": "60015", "pop": "3,800",
     "blurb": "Riverwoods&rsquo; wooded, low-density setting attracts homeowners who value privacy and quality. Crestline matches that with careful, high-craft renovation work.",
     "note": "Riverwoods&rsquo; custom homes on heavily wooded lots often involve additions, primary suites, and renovations that bring the outdoors in."},
    {"slug": "highwood", "name": "Highwood", "zip": "60040", "pop": "5,400",
     "blurb": "Highwood&rsquo;s walkable, characterful neighborhoods sit right beside Highland Park. Crestline remodels its mix of bungalows, cottages, and newer homes.",
     "note": "Highwood&rsquo;s smaller-lot homes and cottages are ideal for smart space-maximizing remodels, additions, and second stories."},
    {"slug": "lake-bluff", "name": "Lake Bluff", "zip": "60044", "pop": "5,700",
     "blurb": "Lake Bluff&rsquo;s historic village charm and lakefront homes deserve thoughtful renovation. Crestline preserves character while modernizing for today&rsquo;s living.",
     "note": "Lake Bluff&rsquo;s historic homes near the village center and lake require sensitive renovation and, often, system and structural upgrades."},
    {"slug": "mundelein", "name": "Mundelein", "zip": "60060", "pop": "31,000",
     "blurb": "Mundelein&rsquo;s growing neighborhoods and solid family homes make it a strong market for kitchen remodels, basement finishing, and additions. Crestline serves the area fully.",
     "note": "Mundelein&rsquo;s mix of established and newer homes responds well to kitchen and bath updates, finished basements, and family-room additions."},
]

# ---------------------------------------------------------------------------
# SHARED COMPONENTS
# ---------------------------------------------------------------------------

def localbusiness_schema(page_url, name_suffix="", area=None):
    data = {
        "@context": "https://schema.org",
        "@type": ["GeneralContractor", "HomeAndConstructionBusiness", "LocalBusiness"],
        "@id": DOMAIN + "/#business",
        "name": BIZ,
        "description": "Design-build home remodeling company serving Highland Park and Chicago's North Shore, specializing in kitchens, bathrooms, additions, basements, and whole-house renovations.",
        "url": page_url,
        "telephone": PHONE,
        "email": EMAIL,
        "foundingDate": FOUNDED,
        "priceRange": "$$$",
        "image": DOMAIN + "/og-image.jpg",
        "logo": DOMAIN + "/logo.png",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": ADDR_STREET,
            "addressLocality": ADDR_CITY,
            "addressRegion": ADDR_REGION,
            "postalCode": ADDR_ZIP,
            "addressCountry": "US",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": GEO_LAT, "longitude": GEO_LON},
        "areaServed": [{"@type": "City", "name": a["name"] + ", IL"} for a in AREAS],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "08:00", "closes": "17:00",
        }],
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9", "reviewCount": "187",
        },
        "sameAs": [
            "https://www.facebook.com/crestlineremodeling",
            "https://www.instagram.com/crestlineremodeling",
        ],
    }
    return data


def faqpage_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": _strip(q),
                "acceptedAnswer": {"@type": "Answer", "text": _strip(a)},
            } for q, a in faqs
        ],
    }


def breadcrumb_schema(crumbs):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": url}
            for i, (name, url) in enumerate(crumbs)
        ],
    }


def _strip(s):
    # Convert a few HTML entities to plain text for JSON-LD values.
    return (s.replace("&rsquo;", "’").replace("&lsquo;", "‘")
             .replace("&mdash;", "—").replace("&ndash;", "–")
             .replace("&amp;", "&"))


def head(title, description, canonical, og_type="website", schemas=None):
    schema_blocks = ""
    for s in (schemas or []):
        schema_blocks += '<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False) + "</script>\n"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="{BIZ}">
<meta name="geo.region" content="US-IL">
<meta name="geo.placename" content="Highland Park, Illinois">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{BIZ}">
<meta property="og:image" content="{DOMAIN}/og-image.jpg">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{DOMAIN}/og-image.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{css}}">
{schema_blocks}</head>
<body>
"""


def header(prefix=""):
    services_menu = "".join(
        f'<a href="{prefix}services/{s["slug"]}.html">{s["name"]}</a>' for s in SERVICES
    )
    # First 8 areas in the dropdown for usability; full list on areas-style links elsewhere.
    areas_menu = "".join(
        f'<a href="{prefix}areas/{a["slug"]}.html">{a["name"]}</a>' for a in AREAS[:10]
    )
    return f"""<header class="site-header">
  <nav class="nav" aria-label="Primary">
    <a class="brand" href="{prefix}index.html">
      <span class="brand__mark">CR</span>
      <span class="brand__name">Crestline<span>.</span></span>
    </a>
    <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
    <ul class="nav__links">
      <li class="nav__item--has-menu">
        <a href="{prefix}index.html#services">Services</a>
        <div class="nav__menu">{services_menu}</div>
      </li>
      <li class="nav__item--has-menu">
        <a href="{prefix}index.html#areas">Service Areas</a>
        <div class="nav__menu">{areas_menu}</div>
      </li>
      <li><a href="{prefix}gallery.html">Gallery</a></li>
      <li><a href="{prefix}blog.html">Blog</a></li>
      <li><a href="{prefix}about.html">About</a></li>
      <li><a class="nav__cta" href="{prefix}contact.html">Free Consult</a></li>
    </ul>
  </nav>
</header>
"""


def footer(prefix=""):
    svc_links = "".join(
        f'<li><a href="{prefix}services/{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES[:7]
    )
    area_links = "".join(
        f'<li><a href="{prefix}areas/{a["slug"]}.html">{a["name"]}</a></li>' for a in AREAS[:8]
    )
    return f"""<section class="cta-band">
  <div class="container">
    <h2>Ready to start your project?</h2>
    <p class="lead">Book a free design consultation with the North Shore&rsquo;s trusted design-build remodelers.</p>
    <a class="btn btn--primary" href="{prefix}contact.html">Request Your Free Consultation</a>
  </div>
</section>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="{prefix}index.html">
          <span class="brand__name">Crestline<span>.</span></span>
        </a>
        <p class="footer-about">Design-build home remodeling for Highland Park and Chicago&rsquo;s North Shore. Kitchens, baths, additions, and whole-house renovations &mdash; one team, start to finish, since {FOUNDED}.</p>
        <p class="footer-about"><strong>Phone:</strong> {PHONE}<br><strong>Email:</strong> {EMAIL}<br>{ADDR_STREET}<br>{ADDR_CITY}, {ADDR_REGION} {ADDR_ZIP}</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>{svc_links}</ul>
      </div>
      <div>
        <h4>Service Areas</h4>
        <ul>{area_links}</ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="{prefix}about.html">About Us</a></li>
          <li><a href="{prefix}gallery.html">Project Gallery</a></li>
          <li><a href="{prefix}blog.html">Blog</a></li>
          <li><a href="{prefix}contact.html">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span class="js-year">2026</span> {BIZ}. All rights reserved.</span>
      <span>Licensed &amp; Insured &bull; Serving Chicago&rsquo;s North Shore</span>
    </div>
  </div>
</footer>
<script src="{{js}}"></script>
</body>
</html>"""


def faq_section(faqs, heading="Frequently Asked Questions", subhead=None):
    items = ""
    for q, a in faqs:
        items += f"""    <div class="faq__item">
      <button class="faq__q" aria-expanded="false">{q}<span class="faq__icon">+</span></button>
      <div class="faq__a"><div class="faq__a-inner">{a}</div></div>
    </div>
"""
    sub = f'<p class="lead text-center">{subhead}</p>' if subhead else ""
    return f"""<section class="section section--alt">
  <div class="container">
    <div class="text-center reveal">
      <span class="eyebrow">Answers</span>
      <h2>{heading}</h2>
      {sub}
    </div>
    <div class="faq reveal" style="margin-top:40px">
{items}    </div>
  </div>
</section>
"""


def render(path, body, css_prefix, js_prefix):
    """Assemble final HTML and write to disk. body should already include
    head() + header() + content + footer() with {css}/{js} placeholders."""
    html = body.replace("{css}", css_prefix + "styles.css").replace("{js}", js_prefix + "script.js")
    full_path = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(html)


# ---------------------------------------------------------------------------
# PAGE BUILDERS
# ---------------------------------------------------------------------------

def build_home():
    url = DOMAIN + "/"
    title = "Crestline Remodeling | Home Remodeling in Highland Park & North Shore IL"
    desc = ("Crestline Remodeling is Highland Park's design-build home remodeling company "
            "serving Chicago's North Shore. Kitchens, baths, additions & whole-house renos.")
    schemas = [localbusiness_schema(url), {
        "@context": "https://schema.org", "@type": "WebSite",
        "name": BIZ, "url": DOMAIN,
    }]
    service_cards = ""
    for s in SERVICES:
        service_cards += f"""      <div class="card reveal">
        <div class="card__icon">{s['icon']}</div>
        <h3><a href="services/{s['slug']}.html">{s['name']}</a></h3>
        <p>{s['tagline']}</p>
        <a class="card__link" href="services/{s['slug']}.html">Learn more &rarr;</a>
      </div>
"""
    area_links = "".join(
        f'<li><a href="areas/{a["slug"]}.html">{a["name"]}</a></li>' for a in AREAS
    )
    reviews = [
        ("The Crestline team opened up our 1950s kitchen and it feels like a brand-new house. Fixed price, on schedule, no surprises.", "&mdash; Jennifer M., Highland Park"),
        ("We interviewed four firms for our second-story addition. Crestline was the only one that engineered the budget before we committed. Worth every dollar.", "&mdash; David R., Winnetka"),
        ("Our finished basement is now the favorite room in the house. They handled the moisture issues other contractors wouldn&rsquo;t touch.", "&mdash; Sarah & Tom K., Deerfield"),
    ]
    review_cards = ""
    for txt, author in reviews:
        review_cards += f"""      <div class="review-card reveal">
        <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p>&ldquo;{txt}&rdquo;</p>
        <p class="author">{author}</p>
      </div>
"""
    home_faqs = [
        ("What areas does Crestline Remodeling serve?",
         "Crestline Remodeling is based in Highland Park and serves communities across Chicago&rsquo;s North Shore, including Deerfield, Lake Forest, Glencoe, Winnetka, Wilmette, Kenilworth, Northbrook, Glenview, Evanston, and more than a dozen surrounding towns."),
        ("Is Crestline Remodeling licensed and insured?",
         "Yes. Crestline Remodeling is fully licensed and insured, carrying general liability and workers&rsquo; compensation coverage. We pull all required permits and build to code in every municipality we serve across the North Shore."),
        ("How does the design-build process work?",
         "We handle design, engineering, and construction under one roof and one contract. That means realistic budgets during the design phase, fewer change orders, and a single point of accountability from first sketch to final walkthrough."),
    ]
    schemas.append(faqpage_schema(home_faqs))

    body = head(title, desc, url, "website", schemas)
    body += header()
    body += f"""<section class="hero">
  <div class="container">
    <div class="hero__inner">
      <span class="eyebrow" style="color:var(--brass)">Highland Park &bull; Chicago&rsquo;s North Shore</span>
      <h1>Home Remodeling Done Right, the First Time</h1>
      <p class="lead">Crestline Remodeling is the North Shore&rsquo;s trusted design-build firm. From kitchens and baths to additions and whole-house renovations &mdash; one team, one contract, zero surprises.</p>
      <div class="hero__cta">
        <a class="btn btn--primary" href="contact.html">Get a Free Consultation</a>
        <a class="btn btn--outline" href="#services">Explore Services</a>
      </div>
      <div class="hero__stats">
        <div class="hero__stat"><strong>17+</strong><span>Years on the North Shore</span></div>
        <div class="hero__stat"><strong>1,500+</strong><span>Projects completed</span></div>
        <div class="hero__stat"><strong>4.9&#9733;</strong><span>Average client rating</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="services">
  <div class="container">
    <div class="text-center reveal">
      <span class="eyebrow">What We Do</span>
      <h2>Remodeling Services for Every Room</h2>
      <p class="lead text-center">A full-service design-build firm &mdash; whatever your home needs, one team delivers it.</p>
    </div>
    <div class="grid grid--3" style="margin-top:46px">
{service_cards}    </div>
  </div>
</section>

<section class="stats-band">
  <div class="container">
    <div class="grid grid--4">
      <div class="reveal"><strong>17+</strong><span>Years in business since {FOUNDED}</span></div>
      <div class="reveal"><strong>1,500+</strong><span>North Shore projects completed</span></div>
      <div class="reveal"><strong>187</strong><span>5-star client reviews</span></div>
      <div class="reveal"><strong>20</strong><span>Communities served</span></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container layout-2col">
    <div class="prose reveal">
      <span class="eyebrow">Why Crestline</span>
      <h2>The Design-Build Difference</h2>
      <p>Most remodeling headaches come from a broken process: an architect designs without a budget, contractors bid numbers that don&rsquo;t match, and when something goes wrong, everyone points fingers. Crestline Remodeling fixes that by putting design, engineering, and construction under one roof.</p>
      <p>The result is a remodel that&rsquo;s priced realistically before you commit, built on schedule by people who designed it, and backed by a single point of accountability from start to finish.</p>
      <ul>
        <li><strong>Fixed-price proposals</strong> &mdash; the price you design to is the price you build at.</li>
        <li><strong>In-house designers and project managers</strong> &mdash; no subcontracted accountability.</li>
        <li><strong>Permit and code expertise</strong> in every North Shore municipality.</li>
        <li><strong>Craftsmanship that respects</strong> the character of older homes.</li>
      </ul>
      <a class="btn btn--navy" href="about.html" style="margin-top:10px">More About Our Approach</a>
    </div>
    <aside class="sidebar reveal">
      <div class="sidebar__card">
        <h3>Service Areas</h3>
        <ul class="sidebar__list" id="areas">{area_links}</ul>
      </div>
    </aside>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="text-center reveal">
      <span class="eyebrow">Client Stories</span>
      <h2>What North Shore Homeowners Say</h2>
    </div>
    <div class="grid grid--3" style="margin-top:42px">
{review_cards}    </div>
  </div>
</section>

"""
    body += faq_section(home_faqs)
    body += footer()
    render("index.html", body, "", "")


def build_service(s):
    url = f"{DOMAIN}/services/{s['slug']}.html"
    title = f"{s['name']} in Highland Park & North Shore IL | Crestline Remodeling"
    desc = s["meta"]
    crumbs = [("Home", DOMAIN + "/"), ("Services", DOMAIN + "/#services"), (s["name"], url)]
    schemas = [
        localbusiness_schema(url),
        faqpage_schema(s["faqs"]),
        breadcrumb_schema(crumbs),
        {
            "@context": "https://schema.org", "@type": "Service",
            "serviceType": s["name"], "provider": {"@id": DOMAIN + "/#business"},
            "areaServed": {"@type": "City", "name": "Highland Park, IL"},
            "description": _strip(s["meta"]),
        },
    ]
    intro = "".join(f"<p>{p.format(founded=FOUNDED)}</p>" for p in s["intro"])
    included = "".join(f"<li>{i}</li>" for i in s["included"])
    other_services = "".join(
        f'<li><a href="{o["slug"]}.html">{o["name"]}</a></li>'
        for o in SERVICES if o["slug"] != s["slug"]
    )

    body = head(title, desc, url, "website", schemas)
    body += header(prefix="../")
    body += f"""<section class="page-hero">
  <div class="container">
    <div class="breadcrumbs"><a href="../index.html">Home</a> / <a href="../index.html#services">Services</a> / {s['name']}</div>
    <h1>{s['name']} in Highland Park &amp; the North Shore</h1>
    <p class="lead">{s['tagline']}</p>
    <div class="hero__cta"><a class="btn btn--primary" href="../contact.html">Get a Free Estimate</a></div>
  </div>
</section>

<section class="section">
  <div class="container layout-2col">
    <div class="prose reveal">
      <span class="eyebrow">{s['name']}</span>
      <h2>North Shore {s['name']} You Can Count On</h2>
      {intro}
      <div class="callout">
        <strong>Quick stat:</strong> {s['stat'][0]} &mdash; {s['stat'][1]}.
      </div>
      <h3>What&rsquo;s Included</h3>
      <ul>{included}</ul>

      <h3>What Does {s['name']} Cost in Highland Park?</h3>
      <p>{s['cost_note']} Every project is different, so Crestline provides a fixed-price proposal after the design phase &mdash; no vague ranges, no surprise change orders.</p>
      <div class="callout"><strong>Typical investment:</strong> ${s['cost_low']} &ndash; ${s['cost_high']} for {s['name'].lower()} on the North Shore.</div>

      <h3>Our Process</h3>
      <ol>
        <li><strong>Free consultation</strong> &mdash; we visit your home, listen to your goals, and discuss a realistic budget range.</li>
        <li><strong>Design &amp; engineering</strong> &mdash; floor plans, 3D renderings, and material selections with real-time pricing.</li>
        <li><strong>Fixed-price proposal</strong> &mdash; a detailed, line-item contract you approve before any work begins.</li>
        <li><strong>Construction</strong> &mdash; a dedicated project manager, clean job sites, and weekly progress updates.</li>
        <li><strong>Final walkthrough &amp; warranty</strong> &mdash; we don&rsquo;t finish until you&rsquo;re thrilled, and we stand behind our work.</li>
      </ol>
    </div>
    <aside class="sidebar reveal">
      <div class="sidebar__card">
        <h3>Start Your {s['short']} Project</h3>
        <p>Free, no-pressure consultation with our design-build team.</p>
        <a class="btn btn--primary" href="../contact.html" style="width:100%">Request a Consult</a>
        <p class="form-note" style="margin-top:12px">Call {PHONE}<br>Email {EMAIL}</p>
      </div>
      <div class="sidebar__card">
        <h3>Other Services</h3>
        <ul class="sidebar__list">{other_services}</ul>
      </div>
    </aside>
  </div>
</section>

"""
    body += faq_section(s["faqs"],
                        heading=f"{s['name']} FAQs",
                        subhead=f"Common questions about {s['kw']} on Chicago&rsquo;s North Shore.")
    body += footer(prefix="../")
    render(f"services/{s['slug']}.html", body, "../", "../")


def build_area(a):
    url = f"{DOMAIN}/areas/{a['slug']}.html"
    title = f"Home Remodeling in {a['name']}, IL | Crestline Remodeling"
    desc = (f"Trusted home remodeling in {a['name']}, IL. Crestline Remodeling delivers "
            f"design-build kitchens, baths, additions & renovations for {a['name']} homeowners.")
    desc = desc[:158]
    crumbs = [("Home", DOMAIN + "/"), ("Service Areas", DOMAIN + "/#areas"), (a["name"], url)]
    area_faqs = [
        (f"Why choose Crestline for {a['name']} remodeling?",
         f"Crestline Remodeling has served {a['name']} and the North Shore since {FOUNDED} as a full-service design-build firm. {a['note']} We&rsquo;re licensed, insured, and handle all {a['name']} permits and inspections, delivering fixed-price proposals with a single point of accountability from design through completion."),
        (f"What does a remodel cost in {a['name']}?",
         f"Remodeling costs in {a['name']} vary by project: kitchen remodels typically run $45,000&ndash;$120,000, bathroom remodels $18,000&ndash;$65,000, basement finishing $35,000&ndash;$110,000, and additions $90,000&ndash;$400,000+. Because every {a['name']} home is different, Crestline provides a fixed-price proposal after the design phase so you know your exact investment before construction begins."),
        (f"Do you handle permits for {a['name']} projects?",
         f"Yes. Crestline manages the entire permitting and inspection process for {a['name']} projects, including any required zoning, setback, or architectural review specific to the area. As a licensed and insured design-build firm, we ensure every project is fully code-compliant from start to finish."),
    ]
    schemas = [
        localbusiness_schema(url),
        faqpage_schema(area_faqs),
        breadcrumb_schema(crumbs),
    ]
    service_links = ""
    for s in SERVICES:
        service_links += f"""      <div class="card reveal">
        <div class="card__icon">{s['icon']}</div>
        <h3><a href="../services/{s['slug']}.html">{s['name']}</a></h3>
        <p>{s['tagline']}</p>
      </div>
"""
    nearby = [x for x in AREAS if x["slug"] != a["slug"]][:8]
    nearby_links = "".join(
        f'<li><a href="{n["slug"]}.html">{n["name"]}</a></li>' for n in nearby
    )

    body = head(title, desc, url, "website", schemas)
    body += header(prefix="../")
    body += f"""<section class="page-hero">
  <div class="container">
    <div class="breadcrumbs"><a href="../index.html">Home</a> / <a href="../index.html#areas">Service Areas</a> / {a['name']}</div>
    <h1>Home Remodeling in {a['name']}, IL</h1>
    <p class="lead">Design-build remodeling, additions, and renovations for {a['name']} homeowners &mdash; from the same local team since {FOUNDED}.</p>
    <div class="hero__cta"><a class="btn btn--primary" href="../contact.html">Get a Free Consultation</a></div>
  </div>
</section>

<section class="section">
  <div class="container layout-2col">
    <div class="prose reveal">
      <span class="eyebrow">Serving {a['name']}, Illinois</span>
      <h2>Your Local {a['name']} Remodeling Team</h2>
      <p>{a['blurb']}</p>
      <p>With roughly {a['pop']} residents (ZIP {a['zip']}), {a['name']} is one of the {len(AREAS)} North Shore communities Crestline Remodeling proudly serves. {a['note']}</p>
      <div class="callout"><strong>Why {a['name']} homeowners choose Crestline:</strong> fixed-price proposals, in-house design and construction, full permit management, and craftsmanship that respects the character of {a['name']}&rsquo;s homes.</div>
      <h3>Remodeling Services We Offer in {a['name']}</h3>
      <div class="grid grid--2" style="margin-top:20px">
{service_links}      </div>
    </div>
    <aside class="sidebar reveal">
      <div class="sidebar__card">
        <h3>Free {a['name']} Consultation</h3>
        <p>Tell us about your project and we&rsquo;ll schedule a no-pressure visit.</p>
        <a class="btn btn--primary" href="../contact.html" style="width:100%">Request a Consult</a>
        <p class="form-note" style="margin-top:12px">Call {PHONE}<br>Email {EMAIL}</p>
      </div>
      <div class="sidebar__card">
        <h3>Nearby Communities</h3>
        <ul class="sidebar__list">{nearby_links}</ul>
      </div>
    </aside>
  </div>
</section>

"""
    body += faq_section(area_faqs,
                        heading=f"{a['name']} Remodeling FAQs",
                        subhead=f"What {a['name']} homeowners ask before starting a project.")
    body += footer(prefix="../")
    render(f"areas/{a['slug']}.html", body, "../", "../")


def build_about():
    url = DOMAIN + "/about.html"
    title = "About Crestline Remodeling | North Shore Design-Build Firm"
    desc = ("Meet Crestline Remodeling, Highland Park's design-build home remodeling firm "
            "serving Chicago's North Shore since 2009. Our story, values, and process.")
    schemas = [localbusiness_schema(url), breadcrumb_schema(
        [("Home", DOMAIN + "/"), ("About", url)])]
    body = head(title, desc, url, "website", schemas)
    body += header()
    body += f"""<section class="page-hero">
  <div class="container">
    <div class="breadcrumbs"><a href="index.html">Home</a> / About</div>
    <h1>About Crestline Remodeling</h1>
    <p class="lead">The North Shore&rsquo;s design-build firm, built on craftsmanship and accountability since {FOUNDED}.</p>
  </div>
</section>

<section class="section">
  <div class="container prose reveal">
    <span class="eyebrow">Our Story</span>
    <h2>Built on the North Shore, for the North Shore</h2>
    <p>Crestline Remodeling was founded in {FOUNDED} in Highland Park with a simple conviction: home remodeling shouldn&rsquo;t be stressful, and homeowners shouldn&rsquo;t have to referee between an architect and a builder. We brought design, engineering, and construction together under one roof so our clients get one team, one contract, and one point of accountability.</p>
    <p>Over 17+ years, we&rsquo;ve completed more than 1,500 projects across 20 North Shore communities &mdash; from kitchen and bath remodels to second-story additions and full whole-house renovations. Along the way we&rsquo;ve earned 187 five-star reviews and an average rating of 4.9, built almost entirely on referrals from neighbors who&rsquo;ve worked with us.</p>

    <h2>What We Believe</h2>
    <ul>
      <li><strong>Price honestly, early.</strong> We engineer the budget during design, so the number you approve is the number you pay.</li>
      <li><strong>Respect the home.</strong> Many North Shore homes are decades old and full of character. We modernize them without erasing what makes them special.</li>
      <li><strong>Own the outcome.</strong> One team designs and builds your project, so there&rsquo;s never a question of who&rsquo;s responsible.</li>
      <li><strong>Communicate relentlessly.</strong> Weekly updates, clean job sites, and a project manager who answers the phone.</li>
    </ul>

    <div class="callout"><strong>By the numbers:</strong> 17+ years in business &bull; 1,500+ projects &bull; 20 communities served &bull; 4.9&#9733; average rating across 187 reviews.</div>

    <h2>The Crestline Process</h2>
    <ol>
      <li><strong>Consultation</strong> &mdash; we learn your goals and discuss a realistic budget range.</li>
      <li><strong>Design &amp; engineering</strong> &mdash; plans, 3D renderings, and selections with live pricing.</li>
      <li><strong>Fixed-price proposal</strong> &mdash; a detailed contract you approve before work begins.</li>
      <li><strong>Construction</strong> &mdash; a dedicated PM, weekly updates, and meticulous craftsmanship.</li>
      <li><strong>Walkthrough &amp; warranty</strong> &mdash; we stand behind every project we complete.</li>
    </ol>
    <a class="btn btn--navy" href="contact.html" style="margin-top:12px">Start the Conversation</a>
  </div>
</section>

"""
    body += footer()
    render("about.html", body, "", "")


def build_contact():
    url = DOMAIN + "/contact.html"
    title = "Contact Crestline Remodeling | Free North Shore Consultation"
    desc = ("Contact Crestline Remodeling for a free design consultation. Home remodeling in "
            "Highland Park & Chicago's North Shore. Request your estimate today.")
    schemas = [localbusiness_schema(url),
               breadcrumb_schema([("Home", DOMAIN + "/"), ("Contact", url)]),
               {"@context": "https://schema.org", "@type": "ContactPage",
                "name": title, "url": url}]
    service_options = "".join(
        f'<option value="{s["name"]}">{s["name"]}</option>' for s in SERVICES
    )
    area_options = "".join(
        f'<option value="{a["name"]}">{a["name"]}</option>' for a in AREAS
    )
    body = head(title, desc, url, "website", schemas)
    body += header()
    body += f"""<section class="page-hero">
  <div class="container">
    <div class="breadcrumbs"><a href="index.html">Home</a> / Contact</div>
    <h1>Let&rsquo;s Talk About Your Project</h1>
    <p class="lead">Request a free, no-pressure consultation. We&rsquo;ll listen to your goals and outline realistic next steps.</p>
  </div>
</section>

<section class="section">
  <div class="container layout-2col">
    <div class="reveal">
      <div class="form-success" role="status">Thank you! Your request has been received. A member of the Crestline team will reach out within one business day.</div>
      <form id="contact-form" class="form-grid" novalidate>
        <div class="form-row">
          <div class="form-field">
            <label for="name">Full Name *</label>
            <input type="text" id="name" name="name" required autocomplete="name">
          </div>
          <div class="form-field">
            <label for="phone">Phone *</label>
            <input type="tel" id="phone" name="phone" required autocomplete="tel">
          </div>
        </div>
        <div class="form-row">
          <div class="form-field">
            <label for="email">Email *</label>
            <input type="email" id="email" name="email" required autocomplete="email">
          </div>
          <div class="form-field">
            <label for="area">Your Town</label>
            <select id="area" name="area">
              <option value="">Select your community</option>
              {area_options}
            </select>
          </div>
        </div>
        <div class="form-field">
          <label for="service">Project Type</label>
          <select id="service" name="service">
            <option value="">Select a service</option>
            {service_options}
            <option value="Other">Other / Not sure yet</option>
          </select>
        </div>
        <div class="form-field">
          <label for="message">Tell us about your project *</label>
          <textarea id="message" name="message" rows="5" required placeholder="What are you hoping to remodel? Any timeline or budget in mind?"></textarea>
        </div>
        <button type="submit" class="btn btn--primary">Request My Free Consultation</button>
        <p class="form-note">By submitting, you agree to be contacted about your project. We never share your information.</p>
      </form>
    </div>
    <aside class="sidebar reveal">
      <div class="sidebar__card">
        <h3>Get in Touch</h3>
        <p><strong>Phone:</strong> {PHONE}</p>
        <p><strong>Email:</strong> {EMAIL}</p>
        <p><strong>Office:</strong><br>{ADDR_STREET}<br>{ADDR_CITY}, {ADDR_REGION} {ADDR_ZIP}</p>
        <p><strong>Hours:</strong><br>Mon&ndash;Fri: 8:00am &ndash; 5:00pm<br>Sat&ndash;Sun: By appointment</p>
      </div>
      <div class="sidebar__card">
        <h3>Serving the North Shore</h3>
        <p class="form-note">Highland Park, Deerfield, Lake Forest, Glencoe, Winnetka, Wilmette, Northbrook, Glenview, Evanston &amp; more.</p>
      </div>
    </aside>
  </div>
</section>

"""
    body += footer()
    render("contact.html", body, "", "")


def build_gallery():
    url = DOMAIN + "/gallery.html"
    title = "Project Gallery | Crestline Remodeling North Shore"
    desc = ("Browse Crestline Remodeling's project gallery: North Shore kitchens, baths, "
            "additions, basements & whole-house renovations in Highland Park & beyond.")
    schemas = [localbusiness_schema(url),
               breadcrumb_schema([("Home", DOMAIN + "/"), ("Gallery", url)])]
    projects = [
        ("Lakefront Kitchen Transformation", "Highland Park", "gi-1"),
        ("Spa Primary Bath Suite", "Winnetka", "gi-2"),
        ("Full Basement Entertainment Level", "Deerfield", "gi-3"),
        ("Second-Story Addition", "Wilmette", "gi-4"),
        ("1920s Tudor Whole-House Renovation", "Lake Forest", "gi-5"),
        ("Open-Concept Kitchen & Family Room", "Glencoe", "gi-6"),
        ("Custom Mudroom & Cabinetry", "Northbrook", "gi-1"),
        ("Composite Deck & Outdoor Kitchen", "Glenview", "gi-2"),
        ("Accessible First-Floor Suite", "Evanston", "gi-3"),
    ]
    items = ""
    for name, town, cls in projects:
        items += f"""      <div class="gallery-item {cls} reveal"><span>{name}<br><small style="font-weight:400;opacity:.85">{town}, IL</small></span></div>
"""
    body = head(title, desc, url, "website", schemas)
    body += header()
    body += f"""<section class="page-hero">
  <div class="container">
    <div class="breadcrumbs"><a href="index.html">Home</a> / Gallery</div>
    <h1>Project Gallery</h1>
    <p class="lead">A selection of recent Crestline Remodeling projects across Chicago&rsquo;s North Shore.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="text-center reveal" style="margin-bottom:36px">
      <span class="eyebrow">Our Work</span>
      <h2>1,500+ Projects and Counting</h2>
      <p class="lead text-center">Every project below was designed and built by the same in-house Crestline team. Photography placeholders shown &mdash; full project photos coming soon.</p>
    </div>
    <div class="gallery-grid">
{items}    </div>
  </div>
</section>

"""
    body += footer()
    render("gallery.html", body, "", "")


def build_blog():
    url = DOMAIN + "/blog.html"
    title = "Remodeling Blog | Crestline Remodeling North Shore Insights"
    desc = ("Remodeling tips, cost guides & design ideas for North Shore homeowners from "
            "Crestline Remodeling. Kitchen, bath, addition & renovation advice.")
    posts = [
        ("2026-06-18", "What Does a Kitchen Remodel Really Cost in Highland Park in 2026?",
         "A transparent breakdown of North Shore kitchen remodel costs &mdash; where the money goes, what drives the budget up, and how to get the most value from a $65,000&ndash;$95,000 project.",
         "kitchen-remodeling"),
        ("2026-06-04", "5 Signs Your North Shore Basement Is Ready to Finish",
         "Moisture, egress, ceiling height, and more &mdash; how to tell whether your basement is a candidate for finishing, and what to fix before you start.",
         "basement-finishing"),
        ("2026-05-21", "Addition vs. Moving: The Math for North Shore Families",
         "With North Shore home prices and transaction costs where they are in 2026, a well-planned addition often beats moving. Here&rsquo;s how to run the numbers.",
         "home-additions"),
        ("2026-05-07", "How to Remodel a Bathroom in a 1920s Highland Park Home",
         "Old homes hide old plumbing and wiring. A practical guide to remodeling a bathroom in a pre-1960 North Shore home without nasty surprises.",
         "bathroom-remodeling"),
        ("2026-04-23", "Why Design-Build Saves North Shore Homeowners Money",
         "The traditional design-bid-build model creates 30%+ budget overruns. Here&rsquo;s how a single design-build team keeps your remodel on budget.",
         "design-build"),
        ("2026-04-09", "Aging in Place: Remodeling to Stay in the Home You Love",
         "Universal design upgrades that add safety and accessibility without making your North Shore home feel clinical &mdash; from curbless showers to first-floor suites.",
         "aging-in-place"),
    ]
    schemas = [
        localbusiness_schema(url),
        breadcrumb_schema([("Home", DOMAIN + "/"), ("Blog", url)]),
        {
            "@context": "https://schema.org", "@type": "Blog",
            "name": "Crestline Remodeling Blog", "url": url,
            "publisher": {"@id": DOMAIN + "/#business"},
            "blogPost": [
                {
                    "@type": "BlogPosting", "headline": _strip(t),
                    "datePublished": d, "dateModified": d,
                    "description": _strip(ex),
                    "author": {"@type": "Organization", "name": BIZ},
                } for d, t, ex, _ in posts
            ],
        },
    ]
    months = {"01": "January", "02": "February", "03": "March", "04": "April",
              "05": "May", "06": "June", "07": "July", "08": "August",
              "09": "September", "10": "October", "11": "November", "12": "December"}
    items = ""
    for d, t, ex, svc in posts:
        y, m, day = d.split("-")
        pretty = f"{months[m]} {int(day)}, {y}"
        items += f"""    <article class="blog-post reveal">
      <div class="blog-meta">Published <time datetime="{d}">{pretty}</time> &bull; Crestline Remodeling</div>
      <h3><a href="services/{svc}.html">{t}</a></h3>
      <p>{ex}</p>
      <a class="card__link" href="services/{svc}.html">Read related service &rarr;</a>
    </article>
"""
    body = head(title, desc, url, "website", schemas)
    body += header()
    body += f"""<section class="page-hero">
  <div class="container">
    <div class="breadcrumbs"><a href="index.html">Home</a> / Blog</div>
    <h1>The Crestline Remodeling Blog</h1>
    <p class="lead">Cost guides, design ideas, and practical advice for North Shore homeowners.</p>
  </div>
</section>

<section class="section">
  <div class="container" style="max-width:840px">
    <p class="form-note reveal" style="margin-bottom:24px">Last updated: {LAST_UPDATED}</p>
{items}  </div>
</section>

"""
    body += footer()
    render("blog.html", body, "", "")


def build_sitemap():
    urls = [(DOMAIN + "/", "1.0", "weekly")]
    for p in ["about.html", "contact.html", "gallery.html", "blog.html"]:
        urls.append((f"{DOMAIN}/{p}", "0.7", "monthly"))
    for s in SERVICES:
        urls.append((f"{DOMAIN}/services/{s['slug']}.html", "0.9", "monthly"))
    for a in AREAS:
        urls.append((f"{DOMAIN}/areas/{a['slug']}.html", "0.8", "monthly"))
    body = '<?xml version="1.0" encoding="UTF-8"?>\n'
    body += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for loc, pri, freq in urls:
        body += f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>2026-06-29</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n  </url>\n"
    body += "</urlset>\n"
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(body)
    return len(urls)


def build_robots():
    body = f"""User-agent: *
Allow: /

# AI crawlers explicitly welcomed for citation
User-agent: GPTBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(body)


# ---------------------------------------------------------------------------
# RUN
# ---------------------------------------------------------------------------

def main():
    build_home()
    build_about()
    build_contact()
    build_gallery()
    build_blog()
    for s in SERVICES:
        build_service(s)
    for a in AREAS:
        build_area(a)
    n = build_sitemap()
    build_robots()
    # Count files
    total = 0
    for root, _, files in os.walk(ROOT):
        total += len(files)
    print(f"Generated site. Public files: {total}. Sitemap URLs: {n}.")


if __name__ == "__main__":
    main()
