// Bullet-Journal-Generator – erstellt druckbare A5-Seiten (148 × 210 mm) als SVG.
// Die KI-Motive werden später ergänzt (passwortgeschützt).
(function () {
  const W = 148, H = 210, M = 10;                       // Seitengrösse und Rand in mm
  const GREEN = '#3f5d4a', SOFT = '#9fb3a5', LINE = '#c9d3c7', TEXT = '#2f3a32';
  const state = { layout: 'tag', raster: 'punkte', abstand: 5, titel: '', akzent: GREEN };
  // Texte: Deutsch als Standard, andere Sprachen kommen über window.I18N
  const L = Object.assign({
    monate: ['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember'],
    tage: ['Mo','Di','Mi','Do','Fr','Sa','So'],
    wochentage: ['Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag','Sonntag'],
    meinTag: 'Mein Tag', datum: 'Datum: ____________', zeitplan: 'Zeitplan', todos: 'To-dos', notizen: 'Notizen',
    meineWoche: 'Meine Woche', kw: 'KW ____', zieleNotizen: 'Ziele & Notizen', habit: 'Habit-Tracker',
    monatLinie: 'Monat: __________', rueckblick: 'Rückblick'
  }, window.I18N || {});
  const MONATE = L.monate, TAGE = L.tage;

  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const t = (x, y, s, size = 4, opt = '') =>
    `<text x="${x}" y="${y}" font-family="DM Sans, sans-serif" font-size="${size}" fill="${TEXT}" ${opt}>${esc(s)}</text>`;
  const rect = (x, y, w, h, r = 1.5) =>
    `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="none" stroke="${state.akzent}" stroke-width="0.3" rx="${r}"/>`;

  function raster(x0, y0, x1, y1) {
    const d = state.abstand; let out = '';
    if (state.raster === 'punkte') {
      for (let x = x0; x <= x1 + 0.01; x += d) for (let y = y0; y <= y1 + 0.01; y += d)
        out += `<circle cx="${x.toFixed(2)}" cy="${y.toFixed(2)}" r="0.32" fill="${SOFT}"/>`;
    } else if (state.raster === 'kaestchen') {
      for (let x = x0; x <= x1 + 0.01; x += d) out += `<line x1="${x}" y1="${y0}" x2="${x}" y2="${y1}" stroke="${LINE}" stroke-width="0.15"/>`;
      for (let y = y0; y <= y1 + 0.01; y += d) out += `<line x1="${x0}" y1="${y}" x2="${x1}" y2="${y}" stroke="${LINE}" stroke-width="0.15"/>`;
    } else if (state.raster === 'linien') {
      for (let y = y0 + d * 1.4; y <= y1 + 0.01; y += d * 1.4) out += `<line x1="${x0}" y1="${y}" x2="${x1}" y2="${y}" stroke="${LINE}" stroke-width="0.2"/>`;
    }
    return out;
  }

  function kopf(standard) {
    const titel = state.titel.trim() || standard;
    return t(M, M + 8, titel, 8, `font-family="Fraunces, serif" font-weight="600" fill="${state.akzent}"`) +
      `<line x1="${M}" y1="${M + 12}" x2="${W - M}" y2="${M + 12}" stroke="${state.akzent}" stroke-width="0.4"/>`;
  }

  function tagesplaner() {
    let s = kopf(L.meinTag) + t(W - M, M + 8, L.datum, 3.4, 'text-anchor="end"');
    const top = M + 18, colW = 62;
    s += t(M, top + 3, L.zeitplan, 3.6, 'font-weight="700"');
    for (let h = 6; h <= 21; h++) {
      const y = top + 8 + (h - 6) * 10.2;
      s += t(M, y + 3.2, String(h).padStart(2, '0') + ':00', 3) +
        `<line x1="${M + 13}" y1="${y + 4}" x2="${M + colW}" y2="${y + 4}" stroke="${LINE}" stroke-width="0.25"/>`;
    }
    const rx = M + colW + 8, rw = W - M - rx;
    s += t(rx, top + 3, L.todos, 3.6, 'font-weight="700"');
    for (let i = 0; i < 9; i++) {
      const y = top + 8 + i * 8;
      s += rect(rx, y, 3.4, 3.4, 0.6) + `<line x1="${rx + 6}" y1="${y + 3.4}" x2="${rx + rw}" y2="${y + 3.4}" stroke="${LINE}" stroke-width="0.25"/>`;
    }
    const ny = top + 84;
    s += t(rx, ny, L.notizen, 3.6, 'font-weight="700"') + raster(rx + 1, ny + 5, rx + rw - 1, H - M - 1) ;
    return s;
  }

  function woche() {
    let s = kopf(L.meineWoche) + t(W - M, M + 8, L.kw, 3.4, 'text-anchor="end"');
    const top = M + 17, gap = 3, bw = (W - 2 * M - gap) / 2, bh = (H - M - top - 3 * gap) / 4;
    const felder = [...L.wochentage, L.notizen];
    felder.forEach((name, i) => {
      const x = M + (i % 2) * (bw + gap), y = top + Math.floor(i / 2) * (bh + gap);
      s += rect(x, y, bw, bh) + t(x + 3, y + 5.5, name, 3.6, `font-weight="700" fill="${state.akzent}"`) + raster(x + 3, y + 9, x + bw - 3, y + bh - 3);
    });
    return s;
  }

  function monat() {
    const m = +$('bj-monat').value, j = +$('bj-jahr').value;
    let s = kopf(`${MONATE[m]} ${j}`);
    const top = M + 18, cw = (W - 2 * M) / 7, ch = 22;
    TAGE.forEach((d, i) => { s += t(M + i * cw + cw / 2, top + 3, d, 3.4, `text-anchor="middle" font-weight="700" fill="${state.akzent}"`); });
    const erster = (new Date(j, m, 1).getDay() + 6) % 7, tage = new Date(j, m + 1, 0).getDate();
    for (let i = 0; i < 42; i++) {
      const x = M + (i % 7) * cw, y = top + 6 + Math.floor(i / 7) * ch, nr = i - erster + 1;
      s += `<rect x="${x}" y="${y}" width="${cw}" height="${ch}" fill="none" stroke="${LINE}" stroke-width="0.25"/>`;
      if (nr >= 1 && nr <= tage) s += t(x + 1.6, y + 4.2, nr, 3.2);
    }
    const ny = top + 6 + 6 * ch + 6;
    s += t(M, ny, L.zieleNotizen, 3.6, 'font-weight="700"') + raster(M + 1, ny + 5, W - M - 1, H - M - 1);
    return s;
  }

  function habits() {
    let s = kopf(L.habit) + t(W - M, M + 8, L.monatLinie, 3.4, 'text-anchor="end"');
    const top = M + 18, nameW = 30, cell = (W - 2 * M - nameW) / 31, rows = 14, rh = 7.4;
    for (let d = 1; d <= 31; d++) s += t(M + nameW + (d - 0.5) * cell, top + 3, d, 2.2, 'text-anchor="middle"');
    for (let r = 0; r < rows; r++) {
      const y = top + 6 + r * rh;
      s += `<line x1="${M}" y1="${y + rh}" x2="${M + nameW - 2}" y2="${y + rh}" stroke="${LINE}" stroke-width="0.25"/>`;
      for (let d = 0; d < 31; d++)
        s += `<rect x="${(M + nameW + d * cell + 0.3).toFixed(2)}" y="${y + 1.6}" width="${(cell - 0.6).toFixed(2)}" height="${(rh - 2.6).toFixed(2)}" fill="none" stroke="${LINE}" stroke-width="0.2" rx="0.5"/>`;
    }
    const ny = top + 6 + rows * rh + 8;
    s += t(M, ny, L.rueckblick, 3.6, 'font-weight="700"') + raster(M + 1, ny + 5, W - M - 1, H - M - 1);
    return s;
  }

  function leer() {
    return (state.titel.trim() ? kopf('') : '') + raster(M, state.titel.trim() ? M + 18 : M, W - M, H - M);
  }

  function zeichnen() {
    const inhalt = { tag: tagesplaner, woche, monat, habits, leer }[state.layout]();
    $('sheet').innerHTML = `<rect width="${W}" height="${H}" fill="#fff"/>` + inhalt;
    $('bj-monatwahl').style.display = state.layout === 'monat' ? '' : 'none';
  }

  function segment(id, key, wert = (v) => v) {
    $(id).addEventListener('click', (e) => {
      const b = e.target.closest('button'); if (!b) return;
      [...$(id).children].forEach((x) => x.classList.toggle('on', x === b));
      state[key] = wert(b.dataset.v); zeichnen();
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    const jetzt = new Date();
    $('bj-monat').innerHTML = MONATE.map((n, i) => `<option value="${i}">${n}</option>`).join('');
    $('bj-monat').value = jetzt.getMonth();
    $('bj-jahr').value = jetzt.getFullYear();
    segment('bj-layout', 'layout');
    segment('bj-raster', 'raster');
    segment('bj-farbe', 'akzent');
    $('bj-abstand').addEventListener('change', (e) => { state.abstand = +e.target.value; zeichnen(); });
    $('bj-titel').addEventListener('input', (e) => { state.titel = e.target.value; zeichnen(); });
    $('bj-monat').addEventListener('change', zeichnen);
    $('bj-jahr').addEventListener('input', zeichnen);
    $('bj-drucken').addEventListener('click', () => { try { window.print(); } catch (e) { /* Druck in Vorschau nicht verfügbar */ } });
    zeichnen();
  });
})();
