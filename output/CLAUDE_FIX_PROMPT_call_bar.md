One fix for the master template, then re-deploy all 100 homepage concepts.

I tested all 100 live concepts on an iPhone-size screen (390 px). Everything passes (loads in about 1 second, phone links
match each Google number, no broken images, no horizontal scroll, one H1) except one thing:

**The bottom Call / Book bar never appears on phones on any of the 100 sites.** The CSS for it exists, but the bar
element is missing from the page HTML (or it is never switched on). Please:

1. Add the bar to the template's HTML, just before `</body>`: two equal buttons, "Call" as a `tel:` link with the
   site's phone number from the content file, and "Book a free consultation" (or that site's own CTA label) linking
   to the estimate form.
2. Show it only below 768 px wide, fixed to the bottom, appearing after the visitor scrolls past the hero, and keep it
   visible while scrolling. Use `padding-bottom: env(safe-area-inset-bottom)` and add bottom padding to the page
   equal to its height, so it never covers the footer or form fields. Hide it while the mobile menu is open.
3. Use the site's own tokens (dark background, accent button), 48 px tall buttons, AA contrast.
4. Rebuild and redeploy all 100 sites, then check five of them on a phone-size screen and confirm the bar shows and
   both buttons work.
