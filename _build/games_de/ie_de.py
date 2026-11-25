# Deutsche Fassung von Island Escape. Codes und Reihenfolgen bleiben identisch.
HEAD_DE = r'''var FACTS = '<div class="ie-fact"><b>Steckbrief: Insel Mira</b><ul><li>4000 Einwohnerinnen und Einwohner; im Sommer kommen etwa 4000 Touristinnen und Touristen dazu.</li><li>Etwa 2500 Sonnenstunden pro Jahr, vor allem im Sommer.</li><li>Starke Winde an der Westküste, besonders im Herbst und Winter.</li><li>Der Unterschied zwischen Ebbe und Flut beträgt nur etwa 1 Meter. Ein kleiner Fluss, keine Berge.</li><li>Ein Vogelschutzgebiet auf den Hügeln der Westküste.</li></ul></div>';
var RULES = '<b>Regeln:</b> Jeder falsche Code kostet <b>1 Minute</b>. In jedem Raum gibt es einen Hinweis, der <b>2 Minuten</b> kostet. Besprecht euch im Team!';
var HOWTO = '<h3 style="margin-top:0">So wird gespielt</h3><ul><li>Ihr geht durch <b>vier Räume</b>. In jedem Raum löst ihr das Rätsel, findet den Code und gebt ihn im Schloss ein.</li><li>Raum 1: Bringt die Karten mit ▲ und ▼ in die richtige Reihenfolge. Raum 4: Schaltet die richtigen Aussagen EIN und zieht den Hebel.</li><li>Jeder falsche Code kostet <b>1 Minute</b>. In jedem Raum gibt es einen Hinweis, der <b>2 Minuten</b> kostet.</li><li>Die Lampen oben zeigen, wie viele Räume ihr gelöst habt. Euer Spiel wird in diesem Browser gespeichert.</li><li>Besprecht euch im Team!</li></ul>'+FACTS;

/* ================= RÄUME ================= */
var ROOMS = [
 {id:"weather", img:"ie-room1-weather.jpg", kick:"Raum 1 · Die Wetterstation", title:"Warum wird es auf der Insel wärmer?",
  story:"Die Tür der Wetterstation steht offen. Drinnen trommelt der Regen ans Fenster. Auf dem Pult hat die Meteorologin fünf Karten zum Treibhauseffekt liegen lassen, doch der Wind hat sie durcheinandergewirbelt. Auf jeder Karte ist eine Zahl gestempelt. Bringt die Karten in die richtige Reihenfolge: Die Zahlen ergeben dann den Code für die nächste Tür.",
  hint:"Beginnt mit der Sonne. Das Licht muss zuerst den Boden erreichen, bevor der Boden Wärme abgeben kann. Der Mensch kommt ganz am Schluss.",
  type:"order",
  items:[["Sonnenlicht durchquert die Atmosphäre und erreicht die Erde.","7"],["Land und Meere nehmen den grössten Teil des Sonnenlichts auf und erwärmen sich.","2"],["Die warme Oberfläche gibt Wärme als Infrarotstrahlung ab.","9"],["Treibhausgase halten einen Teil dieser Wärme zurück und senden sie zur Oberfläche zurück.","4"],["Der Mensch bringt zusätzliche Treibhausgase in die Luft, der Treibhauseffekt wird stärker und die Erde wärmer.","6"]],
  lock:{t:"Türcode", p:"Gebt die fünf gestempelten Zahlen in der richtigen Reihenfolge des Treibhauseffekts ein.", labels:["1.","2.","3.","4.","5."]},
  code:"72946", done:"Die Tür springt auf. Ein Windstoss weht euch zum Hafen."},
 {id:"harbour", img:"ie-room2-harbour.jpg", kick:"Raum 2 · Der Hafen", title:"Wie hoch muss der Damm sein?",
  story:"Wellen schlagen über den alten Steindamm. Der Schaltkasten der Hafenmeisterin ist verschlossen. Daneben hängt eine Liste mit sieben nummerierten Vorgängen. Der Code besteht aus den Nummern aller Vorgänge, die den Meeresspiegel wirklich steigen lassen, von der kleinsten zur grössten Nummer.",
  hint:"Nur Eis, das auf dem Land liegt, bringt neues Wasser ins Meer. Eis, das schon im Wasser schwimmt, ist wie ein Eiswürfel im Glas. Und denkt daran: Warmes Wasser braucht mehr Platz.",
  type:"list",
  items:["Schwimmendes Meereis in der Arktis schmilzt.","Meerwasser dehnt sich aus, wenn es wärmer wird.","Es fällt mehr Regen über dem Meer.","Der Eisschild auf Grönland schmilzt.","Eisberge, die schon im Meer treiben, schmelzen.","Gletscher in den Alpen schmelzen.","Der Eisschild der Antarktis schmilzt."],
  lock:{t:"Schaltkasten", p:"Die Nummern der Vorgänge, die den Meeresspiegel steigen lassen, von der kleinsten zur grössten.", labels:["","","",""]},
  code:"2467", done:"Der Schaltkasten öffnet sich, und die Pumpen laufen an. Das Wasser im Hafen sinkt langsam. Jetzt: ins Kraftwerkshaus!"},
 {id:"power", img:"ie-room3-powerhouse.jpg", kick:"Raum 3 · Das Kraftwerkshaus", title:"Jede Maschine wandelt Energie um",
  story:"Im Kraftwerkshaus hängt ein altes Plakat mit sechs Energieumwandlungen. Die Maschinen im Raum sind noch ausgeschaltet. Um sie wieder zu starten, fragt das Bedienfeld, welche Umwandlung jede Maschine ausführt. Findet für jede Maschine die passende Nummer.",
  hint:"Eine Solarzelle macht direkt aus Licht Strom (nicht aus Wärme). Ein Motor und ein Generator tun das Gegenteil voneinander: Der eine macht aus Strom Bewegung, der andere aus Bewegung Strom.",
  type:"poster",
  items:[["1","Bewegungsenergie → elektrische Energie"],["2","Lichtenergie → Wärme"],["3","chemische Energie → elektrische Energie"],["4","elektrische Energie → Bewegungsenergie"],["5","Lichtenergie → elektrische Energie"],["6","chemische Energie → Wärme und Licht"]],
  lock:{t:"Bedienfeld", p:"Welche Umwandlung führt jede Maschine aus? Gebt die Nummer vom Plakat ein.", labels:["Solarzelle","Elektromotor","Batterie (im Einsatz)","Generator"]},
  code:"5431", done:"Die Maschinen summen. Solaranlage, kleine Windturbine und Wasserrad sind wieder angeschlossen. Nur noch der Kontrollraum fehlt."},
 {id:"control", img:"ie-room4-control.jpg", kick:"Raum 4 · Der Kontrollraum", title:"Schaltet die Insel ein",
  story:"Der letzte Raum. Acht Schalter steuern das Energiesystem der Insel, und jeder trägt eine Aussage. Schaltet jede richtige Aussage EIN und lasst die falschen AUS. Dann zieht den Haupthebel. Ist die Einstellung falsch, zeigen die Lampen, wie viele Schalter richtig stehen.",
  hint:"Genau fünf Aussagen sind richtig. Die weisse Wolke über einem Kühlturm ist Wasserdampf, kein Rauch. Und Uran wird abgebaut: Es geht eines Tages aus.",
  type:"switch",
  items:[["Steuerstäbe fangen Neutronen ein und können die Kettenreaktion verlangsamen.",true],["Die weisse Wolke über einem Kühlturm ist Rauch voller CO₂.",false],["Kernenergie ist eine erneuerbare Energie.",false],["Die Insel Mira sollte kein Gezeitenkraftwerk bauen, weil der Tidenhub nur etwa 1 Meter beträgt.",true],["Batterien können Solarstrom vom Tag für die Nacht speichern.",true],["Eine Windturbine erzeugt bei jeder Windgeschwindigkeit Strom.",false],["Radioaktiver Abfall bleibt während Tausenden von Jahren gefährlich.",true],["Windturbinen in der Nähe des Vogelschutzgebiets können während des Vogelzugs abgeschaltet werden.",true]],
  done:"Der Haupthebel rastet ein. Eine Strassenlampe nach der anderen geht an …"}
];

'''

REPL = [
 ('var KEY = "mo_islandescape_v1", BEST = "mo_islandescape_best_v1";','var KEY = "mo_islandescape_de_v1", BEST = "mo_islandescape_de_best_v1";'),
 ('img("ie-intro.jpg","A small island after a storm, with dark houses and a wind turbine standing still")+\'<div class="cap"><small>Escape game · Unit 9</small><b>Island Escape: Power for Mira Island</b>',
  'img("ie-intro.jpg","Eine kleine Insel nach einem Sturm, mit dunklen Häusern und einer stillstehenden Windturbine")+\'<div class="cap"><small>Escape-Game · Energie und Umwelt</small><b>Island Escape: Strom für die Insel Mira</b>'),
 ("<p>Last night, a heavy storm hit <b>Mira Island</b>. The old diesel power plant is broken, the houses are dark, and the island’s new clean energy system is locked. You are the energy team that came by ship to help. Find your way through <b>four rooms</b>, solve the puzzles and switch the island back on before night falls.</p>'",
  "<p>🇬🇧 <a href=\"pome24b-island-escape.html\" style=\"text-decoration:underline\">English version of the game</a></p><p>Letzte Nacht hat ein heftiger Sturm die <b>Insel Mira</b> getroffen. Das alte Dieselkraftwerk ist kaputt, die Häuser sind dunkel, und das neue, saubere Energiesystem der Insel ist verriegelt. Ihr seid das Energieteam, das mit dem Schiff zu Hilfe gekommen ist. Findet euren Weg durch <b>vier Räume</b>, löst die Rätsel und schaltet die Insel wieder ein, bevor die Nacht hereinbricht.</p>'"),
 ("Continue the saved game (room '","Gespeichertes Spiel fortsetzen (Raum '"),
 ('<b>Team name</b></label><input class="ie-input" id="ie-name" maxlength="28" value="The Energy Team">','<b>Teamname</b></label><input class="ie-input" id="ie-name" maxlength="28" value="Das Energieteam">'),
 ('<b>Time</b></p>','<b>Zeit</b></p>'),('20 minutes · experts','20 Minuten · für Profis'),('>30 minutes<','>30 Minuten<'),('>45 minutes<','>45 Minuten<'),('no time limit</button>','ohne Zeitlimit</button>'),
 ('Start the escape</button>','Escape starten</button>'),('||"The Energy Team")','||"Das Energieteam")'),
 ('Best teams on this device</h3><table class="ie-best"><tr><th>Team</th><th>Time</th><th>Hints</th><th>Wrong codes</th>','Beste Teams auf diesem Gerät</h3><table class="ie-best"><tr><th>Team</th><th>Zeit</th><th>Hinweise</th><th>Falsche Codes</th>'),
 ('<button class="ie-btn">Back to the game</button>','<button class="ie-btn">Zurück zum Spiel</button>'),
 ('>📖 Rules</button>','>📖 Regeln</button>'),('border-color:#8aa0ad">Restart</button>','border-color:#8aa0ad">Neu starten</button>'),
 ("'<div class=\"ie-hint\"><b>Hint:</b> '","'<div class=\"ie-hint\"><b>Hinweis:</b> '"),
 ('aria-label="Poster with six energy conversions"','aria-label="Plakat mit sechs Energieumwandlungen"'),
 ('<h4>Main lever</h4><p>Set the switches, then pull the lever. Wrong setting: −1 minute.</p><div class="ie-lever"><button id="ie-pull">⏻ PULL THE LEVER</button>','<h4>Haupthebel</h4><p>Stellt die Schalter ein, dann zieht den Hebel. Falsche Einstellung: −1 Minute.</p><div class="ie-lever"><button id="ie-pull">⏻ HEBEL ZIEHEN</button>'),
 ("aria-label=\"Digit '","aria-label=\"Ziffer '"),('margin-left:6px">Open</button>','margin-left:6px">Öffnen</button>'),
 ('>💡 Hint (−2 minutes)</button>','>💡 Hinweis (−2 Minuten)</button>'),("Wrong codes so far: '","Falsche Codes bisher: '"),
 ('confirm("Restart the escape game? Your progress will be lost.")','confirm("Escape-Game neu starten? Euer Fortschritt geht verloren.")'),
 ('title="stamped number"','title="gestempelte Zahl"'),('aria-label="Move up"','aria-label="Nach oben"'),('aria-label="Move down"','aria-label="Nach unten"'),
 ('"Please fill in all "+ins.length+" digits."','"Bitte alle "+ins.length+" Ziffern ausfüllen."'),
 ('"Wrong code! −1 minute. Check the puzzle again."','"Falscher Code! −1 Minute. Prüft das Rätsel nochmals."'),
 ('msg.textContent = right+" of "+R.items.length+" switches are correct. −1 minute. Which statements are you not sure about?";','msg.textContent = right+" von "+R.items.length+" Schaltern stehen richtig. −1 Minute. Bei welchen Aussagen seid ihr unsicher?";'),
 ('"✔ Correct!"','"✔ Richtig!"'),
 ("id=\"ie-next\">Go to room '","id=\"ie-next\">Weiter zu Raum '"),
 ('img("ie-success.jpg","The island at night with all lights on")+\'<div class="cap"><small>Mission complete</small><b>Mira Island is shining again!</b>','img("ie-success.jpg","Die Insel bei Nacht, alle Lichter brennen")+\'<div class="cap"><small>Mission erfüllt</small><b>Die Insel Mira leuchtet wieder!</b>'),
 ("'<p>Well done, <b>'+esc(S.team)+'</b>! The solar panels, the wind turbines and the batteries supply the island with clean electricity, and the old diesel plant can stay switched off.</p>'",
  "'<p>Gut gemacht, <b>'+esc(S.team)+'</b>! Solaranlagen, Windturbinen und Batterien versorgen die Insel mit sauberem Strom, und das alte Dieselkraftwerk bleibt ausgeschaltet.</p>'"),
 ("</b>time (incl. penalties)</div>","</b>Zeit (inkl. Strafminuten)</div>"),("</b>hints used</div>","</b>Hinweise genutzt</div>"),("</b>wrong codes</div>","</b>falsche Codes</div>"),
 ("<b>What you used in this game</b><ul><li>Room 1: the greenhouse effect (book p. 119)</li><li>Room 2: rising sea levels (pp. 122–123)</li><li>Room 3: converting energy (pp. 124–126)</li><li>Room 4: nuclear power, wind power and the island project (pp. 129–131)</li></ul>",
  "<b>Was ihr in diesem Spiel gebraucht habt</b><ul><li>Raum 1: der Treibhauseffekt</li><li>Raum 2: der steigende Meeresspiegel</li><li>Raum 3: Energieumwandlung</li><li>Raum 4: Kernenergie, Windkraft und die Energieversorgung einer Insel</li></ul>"),
 ("<p><b>Talk about it:</b> Which energy mix would you recommend for Mira Island, and why? Practise your answer in English with your team.</p>",
  "<p><b>Darüber sprechen:</b> Welchen Energiemix würdet ihr der Insel Mira empfehlen, und warum? Begründet eure Antwort im Team.</p>"),
 ('id="ie-again">Play again</button>','id="ie-again">Nochmals spielen</button>'),
 ('img("ie-timeup.jpg","The dark island at night")+\'<div class="cap"><small>Time is up</small><b>Night has fallen on Mira Island</b>','img("ie-timeup.jpg","Die dunkle Insel bei Nacht")+\'<div class="cap"><small>Die Zeit ist um</small><b>Auf der Insel Mira ist es Nacht geworden</b>'),
 ("'<p>The island is still dark, but you got far: <b>'+S.room+' of 4 rooms</b> are solved. You can continue without a time limit to finish the mission, or start again.</p>'",
  "'<p>Die Insel ist noch dunkel, aber ihr seid weit gekommen: <b>'+S.room+' von 4 Räumen</b> sind gelöst. Ihr könnt ohne Zeitlimit weiterspielen und die Mission beenden oder neu beginnen.</p>'"),
 ('id="ie-cont">Continue without time limit</button><button class="ie-btn alt" id="ie-again">Start again</button>','id="ie-cont">Ohne Zeitlimit weiterspielen</button><button class="ie-btn alt" id="ie-again">Neu beginnen</button>'),
 ("<noscript><p>Please turn on JavaScript to play the game.</p></noscript>","<noscript><p>Bitte JavaScript aktivieren, um das Spiel zu spielen.</p></noscript>"),
]


def build(src):
    s = src
    a = s.index("var FACTS = "); b = s.index("/* ================= STATE")
    s = s[:a] + HEAD_DE + s[b:]
    miss = []
    for x, y in REPL:
        if x not in s: miss.append(x[:80]); continue
        s = s.replace(x, y)
    return s, miss
