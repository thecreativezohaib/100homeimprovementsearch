// Download every generated image on a Gemini chat page with its FILE NAME (e.g. 004_ai_service_backsplash.jpg).
// Use: scroll to the top of the chat so every image has loaded, open DevTools (F12) > Console, paste this, press Enter.
// If Chrome asks "Download multiple files?", click Allow. A log file gemini_download_log.csv is saved at the end.
(async () => {
  const NAME = /\b\d{3}_ai_[a-z0-9_]+\.(?:jpe?g|png|webp)\b/gi;
  const events = [];
  const seen = new Set();
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_TEXT);
  for (let n = walker.currentNode; n; n = walker.nextNode()) {
    if (n.nodeType === 3) {
      for (const m of n.textContent.matchAll(NAME)) events.push({ t: "name", v: m[0].toLowerCase() });
    } else if (n.tagName === "IMG") {
      const r = n.getBoundingClientRect();
      const src = n.currentSrc || n.src;
      if (!src || src.startsWith("data:image/svg") || seen.has(src)) continue;
      if (Math.max(r.width, n.naturalWidth) < 200) continue; // icons, avatars
      seen.add(src);
      events.push({ t: "img", v: src });
    }
  }
  const imgs = events.filter(e => e.t === "img").length;
  const first = events.find(e => e.t === "name" || e.t === "img");
  const nameAfter = !first || first.t === "img"; // Gemini wrote the name under each image (else above it)
  console.log(`${imgs} images, ${events.filter(e => e.t === "name").length} file names found; names ${nameAfter ? "under" : "above"} images`);

  const jobs = [];
  const used = new Set();
  events.forEach((e, i) => {
    if (e.t !== "img") return;
    let name = null;
    const step = nameAfter ? 1 : -1;
    for (let j = i + step; j >= 0 && j < events.length && events[j].t !== "img"; j += step) {
      if (events[j].t === "name") { name = events[j].v; break; }
    }
    if (!name || used.has(name)) name = `unnamed_${String(jobs.length + 1).padStart(3, "0")}.jpg`;
    used.add(name);
    jobs.push({ name, src: e.v });
  });

  const full = s => /googleusercontent\.com/.test(s) ? s.replace(/=[a-z0-9-]+$/i, "") + "=s0" : s;
  const get = async s => { const r = await fetch(s); if (!r.ok) throw new Error(r.status); return r.blob(); };
  const save = (blob, name) => {
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = name;
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(a.href), 60000);
  };
  const log = [["n", "file_name", "status"]];
  let ok = 0;
  for (const [k, j] of jobs.entries()) {
    let blob = null;
    for (const s of [full(j.src), j.src]) {
      try { blob = await get(s); if (blob.size > 5000) break; } catch (err) { blob = null; }
    }
    if (blob) {
      const ext = blob.type.includes("png") ? "png" : blob.type.includes("webp") ? "webp" : "jpg";
      save(blob, j.name.replace(/\.(jpe?g|png|webp)$/i, "." + ext));
      ok++;
    }
    log.push([k + 1, j.name, blob ? "saved" : "FAILED"]);
    console.log(`${k + 1}/${jobs.length} ${j.name} ${blob ? "saved" : "FAILED"}`);
    await new Promise(r => setTimeout(r, 400));
  }
  save(new Blob([log.map(r => r.join(",")).join("\n")], { type: "text/csv" }), "gemini_download_log.csv");
  console.log(`Done: ${ok} of ${jobs.length} saved, ${jobs.length - ok} failed, ${jobs.filter(j => j.name.startsWith("unnamed")).length} without a name.`);
})();
