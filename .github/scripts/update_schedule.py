from pathlib import Path

p = Path("index.html")
s = p.read_text()
start_marker = "    <!-- ================= SCHEDULE ================= -->"
end_marker = "    <!-- ================= ATTIRE ================= -->"

start = s.index(start_marker)
end = s.index(end_marker, start)

replacement = '''    <!-- ================= SCHEDULE ================= -->
    <section class="view" id="schedule" data-title="Schedule" aria-labelledby="h-schedule">
      <div class="wrap">
        <h2 id="h-schedule" tabindex="-1">A little about Indian weddings</h2>
        <p class="lead">Indian weddings are often celebrated over several events, with each one carrying its own meaning and traditions. Here’s a quick overview of a few traditions you’ll experience during our wedding weekend.</p>

        <h3 class="sub">Haldi</h3>
        <p>Haldi is a pre-wedding tradition where turmeric paste is applied to the bride and groom. It symbolizes blessings, good luck, and the start of the wedding celebrations.</p>

        <h3 class="sub">Sangeet</h3>
        <p>Sangeet is a celebration centered around music and dance. It brings both families and friends together before the wedding for performances, dancing, and celebration.</p>

        <h3 class="sub">Wedding ceremony</h3>
        <p>The wedding ceremony includes a series of traditional rituals that represent the couple’s commitment to one another and the joining of two families. We’ll be incorporating several Indian traditions throughout the ceremony, and we’ll make sure guests can follow along and understand what’s happening.</p>

        <div class="viewnav"><a class="btn btn--ghost" href="#home">Back to home</a></div>
      </div>
    </section>

'''

p.write_text(s[:start] + replacement + s[end:])
