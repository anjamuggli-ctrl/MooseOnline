// Vorlagen-Bibliothek: Filter, Vorschau, Drucken und PDF-Download.
(function () {
  const daten = JSON.parse(document.getElementById('vorlagen-daten').textContent);
  const $ = (id) => document.getElementById(id);
  let aktuell = 0, sichtbar = daten.map((_, i) => i);

  function liste(filter) {
    sichtbar = daten.map((_, i) => i).filter((i) => filter === 'alle' || daten[i].kategorie === filter);
    $('lib').innerHTML = sichtbar.map((i) => {
      const v = daten[i];
      return `<button class="tpl" type="button" data-i="${i}" aria-label="${v.titel} ansehen">
        <img src="vorlagen/vorschau/${v.datei}-klein.jpg" alt="Vorschau ${v.titel}" loading="lazy" width="300" height="426">
        <b>${v.titel}</b><span>${v.kategorie}</span></button>`;
    }).join('');
  }

  function zeigen(i) {
    aktuell = i; const v = daten[i];
    $('m-bild').src = `vorlagen/vorschau/${v.datei}.jpg`;
    $('m-bild').alt = `Vorlage ${v.titel}`;
    $('m-titel').textContent = v.titel;
    $('m-kat').textContent = `${v.kategorie} · A5 · PDF`;
    $('m-pdf').href = `vorlagen/${v.datei}.pdf`;
    $('m-pdf').setAttribute('download', `${v.datei}.pdf`);
    $('pv-print').innerHTML = `<img src="vorlagen/vorschau/${v.datei}.jpg" alt="">`;
    $('modal').classList.add('open');
  }
  function schliessen() { $('modal').classList.remove('open'); }
  function blaettern(d) { const k = sichtbar.indexOf(aktuell); zeigen(sichtbar[(k + d + sichtbar.length) % sichtbar.length]); }

  document.addEventListener('DOMContentLoaded', () => {
    liste('alle');
    $('filter').addEventListener('click', (e) => {
      const b = e.target.closest('button'); if (!b) return;
      [...$('filter').children].forEach((x) => x.classList.toggle('on', x === b));
      liste(b.dataset.f);
    });
    $('lib').addEventListener('click', (e) => { const b = e.target.closest('.tpl'); if (b) zeigen(+b.dataset.i); });
    $('modal').addEventListener('click', (e) => { if (e.target.id === 'modal') schliessen(); });
    $('m-x').addEventListener('click', schliessen);
    $('m-vor').addEventListener('click', () => blaettern(1));
    $('m-zur').addEventListener('click', () => blaettern(-1));
    document.addEventListener('keydown', (e) => {
      if (!$('modal').classList.contains('open')) return;
      if (e.key === 'Escape') schliessen();
      if (e.key === 'ArrowRight') blaettern(1);
      if (e.key === 'ArrowLeft') blaettern(-1);
    });
    $('m-drucken').addEventListener('click', () => {
      // Hochaufgelöste Seite für den Druck laden, dann drucken
      const v = daten[aktuell], img = $('pv-print').querySelector('img');
      document.body.classList.add('druck-vorlage');
      const los = () => { try { window.print(); } catch (err) { /* Druck nicht verfügbar */ } document.body.classList.remove('druck-vorlage'); };
      img.complete ? los() : (img.onload = los);
    });
  });
})();
